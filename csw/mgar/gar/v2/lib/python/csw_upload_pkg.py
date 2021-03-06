#!/opt/csw/bin/python2.6

"""csw_upload_pkg.py - uploads packages to the database.

POST using pycurl code example taken from:
http://pycurl.cvs.sourceforge.net/pycurl/pycurl/tests/test_post2.py?view=markup
"""

from StringIO import StringIO
import getpass
import hashlib
import json
import logging
import optparse
import os.path
import pycurl
import rest
import socket
import subprocess
import sys
import urllib2

import common_constants
import configuration
import errors
import file_set_checker
import opencsw
import struct_util

DEFAULT_CATREL = "unstable"
USAGE = """%prog [ options ] <file1.pkg.gz> [ <file2.pkg.gz> [ ... ] ]

Uploads a set of packages to the unstable catalog in opencsw-future.

- When an architecture-independent package is uploaded, it gets added to both
  sparc and i386 catalogs

- When a SunOS5.x package is sent, it's added to catalogs SunOS5.x,
  SunOS5.(x+1), up to SunOS5.11, but only if there are no packages specific to
  5.10 (and/or 5.11).

- If a package update is sent, the tool uses both the catalogname and the
  pkgname to identify the package it's updating. For example, you might upload
  foo_stub/CSWfoo and mean to replace foo/CSWfoo with it.

The --os-release flag makes %prog only insert the package to catalog with the
given OS release.

The --catalog-release flag allows to insert a package into a specific catalog,
instead of the default 'unstable'.

= General considerations =

This tool operates on a database of packages and a package file store. It
modifies a number of package catalogs, e.g.:

  {{dublin,unstable,kiel,bratislava}}x{{sparc,i386}}x{{5.8,5.9.5.10,5.11}}

For more information, see:
http://wiki.opencsw.org/automated-release-process#toc0
"""

class PackageCheckError(errors.Error):
  """A problem with a package."""


class DataError(errors.Error):
  """Unexpected data found."""


class WorkflowError(errors.Error):
  """Unexpected state of workflow, e.g. expected element not found."""


class OurInfrastructureSucksError(errors.Error):
  """Something that would work in a perfect world, but here it doesn't."""


class Srv4Uploader(object):

  def __init__(self, filenames, os_release=None, debug=False,
      output_to_screen=True,
      username=None, password=None,
      catrel=DEFAULT_CATREL):
    super(Srv4Uploader, self).__init__()
    if filenames:
      filenames = self.SortFilenames(filenames)
    self.filenames = filenames
    self.md5_by_filename = {}
    self.debug = debug
    self.os_release = os_release
    config = configuration.GetConfig()
    self._rest_client = rest.RestClient(
        pkgdb_url=config.get('rest', 'pkgdb'),
        releases_url=config.get('rest', 'releases'),
        username=username,
        password=password)
    self.output_to_screen = output_to_screen
    self.username = username
    self.password = password
    self.catrel = catrel

  def _SetAuth(self, c):
    """Set basic HTTP auth options on given Curl object."""
    if self.username:
      logging.debug("Using basic AUTH for user %s", self.username)
      c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
      c.setopt(pycurl.USERPWD, "%s:%s" % (self.username, self.password))
    else:
      logging.debug("User and password not set, not using HTTP AUTH")
    return c

  def _ImportMetadata(self, filename):
    md5_sum = self._GetFileMd5sum(filename)
    metadata = self._rest_client.GetPkgByMd5(md5_sum)
    if metadata:
      # Metadata are already in the database.
      return
    logging.fatal("%s (%s) is not known to the database.", filename, md5_sum)
    raise OurInfrastructureSucksError(
        "The package database doesn't know about your package. "
        "Normally, packages are checked by GAR automatically right after "
        "being built. Did you build your package outside the buildfarm? "
        "Or was your package built a long time ago and not released (so it "
        "might have been garbage-collected)? If so, the easiest fix is "
        "to reroll your package on the buildfarm using 'mgar repackage' "
        "(on both sparc and intel) and submit the newly created package.")


  def Upload(self):
    do_upload = True
    planned_modifications = []
    metadata_by_md5 = {}
    if self.output_to_screen:
      print "Processing %s file(s). Please wait." % (len(self.filenames),)
    for filename in self.filenames:
      self._ImportMetadata(filename)
      md5_sum = self._GetFileMd5sum(filename)
      if not self._rest_client.IsRegisteredLevelTwo(md5_sum):
        self._rest_client.RegisterLevelTwo(md5_sum)
      file_in_allpkgs, file_metadata = self._GetSrv4FileMetadata(md5_sum)
      if file_in_allpkgs:
        logging.debug("File %s already uploaded.", filename)
      else:
        if do_upload:
          logging.debug("Uploading %s.", filename)
          self._rest_client.PostFile(filename, md5_sum)
          # Querying the database again, this time the data should be
          # there
          file_in_allpkgs, file_metadata = self._GetSrv4FileMetadata(md5_sum)
      logging.debug("file_metadata %s", repr(file_metadata))
      if not file_metadata:
        logging.error(
            "File metadata was not found in the database.  "
            "This happens when the package you're trying to upload was never "
            "unpacked and imported into the database.  "
            "To fix the problem, run checkpkg against your package and try "
            "importing again.")
        raise DataError("file_metadata is empty: %s" % repr(file_metadata))
      osrel = file_metadata['osrel']
      arch = file_metadata['arch']
      metadata_by_md5[md5_sum] = file_metadata
      # TODO(unassigned): The problem is that the assignment can (should) also
      # depend on other packages in the same batch. This function shouldn't
      # really take a single package as an argument, but a group of packages.
      # Or it should not return ready assignments, but weights instead.
      catalogs = self._MatchSrv4ToCatalogs(
          filename, self.catrel, arch, osrel, md5_sum)
      for unused_catrel, cat_arch, cat_osrel in catalogs:
        planned_modifications.append(
            (filename, md5_sum,
             arch, osrel, cat_arch, cat_osrel))
    # The plan:
    # - Create groups of files to be inserted into each of the catalogs
    # - Invoke checkpkg to check every target catalog
    checkpkg_sets = self._CheckpkgSets(planned_modifications)
    checks_successful = self._RunCheckpkg(checkpkg_sets)
    if checks_successful:
      if self.output_to_screen:
        print "All checks successful. Proceeding."
      for arch, osrel in sorted(checkpkg_sets):
        for filename, md5_sum in checkpkg_sets[(arch, osrel)]:
          file_metadata = metadata_by_md5[md5_sum]
          self._InsertIntoCatalog(filename, arch, osrel, file_metadata)

  def _GetFileMd5sum(self, filename):
    if filename not in self.md5_by_filename:
      logging.debug("_GetFileMd5sum(%s): Reading the file", filename)
      with open(filename, "rb") as fd:
        hash = hashlib.md5()
        hash.update(fd.read())
        md5_sum = hash.hexdigest()
        self.md5_by_filename[filename] = md5_sum
    return self.md5_by_filename[filename]

  def _MatchSrv4ToCatalogs(self, filename,
                           catrel, srv4_arch, srv4_osrel,
                           md5_sum):
    """Compile a list of catalogs affected by the given file.

    If it's a 5.9 package, it can be matched to 5.9, 5.10 and 5.11.  However,
    if there already are specific 5.10 and/or 5.11 versions of the package,
    don't overwrite them.

    Args:
      filename: string, base file name of the srv4 stream file
      catrel: string denoting catalog release, usually 'unstable'
      srv4_arch: string, denoting srv4 file architecture (sparc, i386 or all)
      srv4_osrel: string, OS release of the package, e.g. 'SunOS5.9'
      md5_sum: string, md5 sum of the srv4 file

    Returns:
      A tuple of tuples, where each tuple is: (catrel, arch, osrel)
    """
    basename = os.path.basename(filename)
    parsed_basename = opencsw.ParsePackageFileName(basename)
    osrels = None
    for idx, known_osrel in enumerate(common_constants.OS_RELS):
      if srv4_osrel == known_osrel:
        osrels = common_constants.OS_RELS[idx:]
    assert osrels, "OS releases not found"
    if srv4_arch == 'all':
      archs = ('sparc', 'i386')
    else:
      archs = (srv4_arch,)
    catalogname = parsed_basename["catalogname"]
    # This part of code quickly became complicated and should probably be
    # rewritten.  However, it is unit tested, so all the known cases are
    # handled as intended.
    catalogs = []
    first_cat_osrel_seen = None
    for arch in archs:
      for osrel in osrels:
        logging.debug("%s %s %s", catrel, arch, osrel)
        cat_key = (catrel, arch, osrel)
        try:
          srv4_in_catalog = self._rest_client.Srv4ByCatalogAndCatalogname(
              catrel, arch, osrel, catalogname)
        except urllib2.HTTPError:
          srv4_in_catalog = None
        if srv4_in_catalog:
          logging.debug("Catalog %s %s contains version %s of the %s package",
                        arch, osrel, srv4_in_catalog["osrel"], catalogname)
        else:
          logging.debug(
              "Catalog %s %s does not contain any version of the %s package.",
              arch, osrel, catalogname)
        if not first_cat_osrel_seen:
          if srv4_in_catalog:
            first_cat_osrel_seen = srv4_in_catalog["osrel"]
          else:
            first_cat_osrel_seen = srv4_osrel
          logging.debug("Considering %s the base OS to match",
                        first_cat_osrel_seen)
        if (not srv4_in_catalog
            or srv4_in_catalog["osrel"] == srv4_osrel
            or srv4_in_catalog["osrel"] == first_cat_osrel_seen):
          # The same architecture as our package, meaning that we can insert
          # the same architecture into the catalog.
          if (not self.os_release
              or (self.os_release and osrel == self.os_release)):
            catalogs.append(cat_key)
        else:
          if self.os_release and osrel == self.os_release:
            logging.debug("OS release specified and matches %s.", osrel)
            catalogs.append(cat_key)
          else:
            logging.debug(
                "Not matching %s %s package with %s containing a %s package",
                catalogname,
                srv4_osrel, osrel, srv4_in_catalog["osrel"])
          logging.debug(
              "Catalog %s %s %s has another version of %s.",
              catrel, arch, osrel, catalogname)
    return tuple(catalogs)

  def _InsertIntoCatalog(self, filename, arch, osrel, file_metadata):
    logging.debug(
        "_InsertIntoCatalog(%s, %s, %s)",
        repr(arch), repr(osrel), repr(filename))
    print("Inserting %s (%s %s) into catalog %s %s %s"
          % (file_metadata["catalogname"],
             file_metadata["arch"],
             file_metadata["osrel"],
             self.catrel, arch, osrel))
    md5_sum = self._GetFileMd5sum(filename)
    basename = os.path.basename(filename)
    parsed_basename = opencsw.ParsePackageFileName(basename)
    logging.debug("parsed_basename: %s", parsed_basename)
    return self._rest_client.AddSvr4ToCatalog(self.catrel, arch, osrel, md5_sum)

  def _GetSrv4FileMetadata(self, md5_sum):
    return self._rest_client.GetSrv4FileMetadataForReleases(md5_sum)

  def _CheckpkgSets(self, planned_modifications):
    """Groups packages according to catalogs.

    Used to determine groups of packages to check together, against
    a specific catalog.

    Args:
      A list of tuples

    Returns:
      A dictionary of tuples, indexed by (arch, osrel) tuples.
    """
    by_catalog = {}
    for fields in planned_modifications:
      filename, md5_sum, pkg_arch, pkg_osrel, cat_arch, cat_osrel = fields
      key = cat_arch, cat_osrel
      by_catalog.setdefault(key, [])
      by_catalog[key].append((filename, md5_sum))
    return by_catalog

  def SortFilenames(self, filenames):
    """Sorts filenames according to OS release.

    The idea is that in lexicographic sorting, SunOS5.9 is after
    SunOS5.10, while we want 5.9 to be first.
    """
    by_osrel = {}
    sorted_filenames = []
    for filename in filenames:
      basename = os.path.basename(filename)
      parsed_basename = opencsw.ParsePackageFileName(basename)
      by_osrel.setdefault(parsed_basename["osrel"], []).append(filename)
    for osrel in common_constants.OS_RELS:
      if osrel in by_osrel:
        for filename in by_osrel.pop(osrel):
          sorted_filenames.append(filename)
    if by_osrel:
      raise DataError("Unexpected architecture found in file list: %s."
                      % (repr(by_osrel),))
    return sorted_filenames

  def _PluralS(self, number):
    return 's' if number == 0 or number >= 2 else ''

  def _RunCheckpkg(self, checkpkg_sets):
    bin_dir = os.path.dirname(__file__)
    checkpkg_executable = os.path.join(bin_dir, "checkpkg2.py")
    assert os.path.exists(checkpkg_executable), (
        "Could not find %s. Make sure that the checkpkg executable is "
        "available \n"
        "from the same directory as csw-upload-pkg." % checkpkg_executable)
    checks_failed_for_catalogs = []
    args_by_cat = {}
    for arch, osrel in checkpkg_sets:
      number_checked = len(checkpkg_sets[(arch, osrel)])
      print ("Checking %s package%s against catalog %s %s %s"
             % (number_checked, self._PluralS(number_checked),
                self.catrel, arch, osrel))
      md5_sums = []
      basenames = []
      for filename, md5_sum in checkpkg_sets[(arch, osrel)]:
        md5_sums.append(md5_sum)
        basenames.append(os.path.basename(filename))
      # Not using the checkpkg Python API.  The reason is that checkpkg
      # requires the process calling its API to have an established
      # MySQL connection, while csw-upload-pkg does not, and it's better
      # if it stays that way.
      args_by_cat[(arch, osrel)] = [
          checkpkg_executable,
          "--catalog-release", self.catrel,
          "--os-release", osrel,
          "--catalog-architecture", arch,
      ] + md5_sums
      ret = subprocess.call(args_by_cat[(arch, osrel)] + ["--quiet"])
      if ret:
        checks_failed_for_catalogs.append(
            (arch, osrel, basenames)
        )
    if checks_failed_for_catalogs:
      print "Checks failed for the following catalogs:"
      for arch, osrel, basenames in checks_failed_for_catalogs:
        print "  - %s %s" % (arch, osrel)
        for basename in basenames:
          print "    %s" % basename
        print "To see the errors, run:"
        print " ", " ".join(args_by_cat[(arch, osrel)])
        print "Or check on the buildfarm:"
        for md5s in md5_sums:
          print "http://buildfarm.opencsw.org/pkgdb/srv4/%s/" % md5s
      print ("Your packages have not been submitted to the %s catalog."
             % self.catrel)
    return not checks_failed_for_catalogs


if __name__ == '__main__':
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug",
      dest="debug",
      default=False, action="store_true")
  parser.add_option("--os-release",
      dest="os_release",
      help="If specified, only uploads to the specified OS release. "
           "Valid values: {0}".format(" ".join(common_constants.OS_RELS)))
  parser.add_option("--no-filename-check",
      dest="filename_check",
      default=True, action="store_false",
      help="Don't check the filename set (e.g. for a missing architecture)")
  parser.add_option("--catalog-release",
      dest="catrel",
      default=DEFAULT_CATREL,
      help=("Uploads to a specified named catalog. "
            "Note that the server side only allows to upload to a limited "
            "set of catalogs."))
  options, args = parser.parse_args()
  logging_level = logging.INFO
  if options.debug:
    logging_level = logging.DEBUG
  fmt = '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s'
  logging.basicConfig(format=fmt, level=logging_level)
  logging.debug("args: %s", args)
  hostname = socket.gethostname()
  if not hostname.startswith('login'):
    logging.warning("This script is meant to be run on the login host.")
  os_release = options.os_release
  if os_release:
    os_release = struct_util.OsReleaseToLong(os_release)

  if not args:
    parser.print_usage()
    sys.exit(1)

  # Check the file set.
  fc = file_set_checker.FileSetChecker()
  error_tags = fc.CheckFiles(args)
  if error_tags:
    print "There is a problem with the presented file list."
    for error_tag in error_tags:
      print "*", error_tag
    if options.filename_check:
      sys.exit(1)
    else:
      print "Continuing anyway."

  if os_release and os_release not in common_constants.OS_RELS:
    raise DataError(
        "OS release %r is not valid. The valid values are: %r"
        % (os_release, common_constants.OS_RELS))

  username, password = rest.GetUsernameAndPassword()
  uploader = Srv4Uploader(args,
                          os_release=os_release,
                          debug=options.debug,
                          username=username,
                          password=password,
                          catrel=options.catrel)
  uploader.Upload()
