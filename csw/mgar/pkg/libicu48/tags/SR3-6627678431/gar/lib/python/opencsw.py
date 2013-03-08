#!/opt/csw/bin/python2.6
# coding=utf-8
#
# $Id$
#
# vim:set sw=2 ts=2 sts=2 expandtab:
#
# Copyright (c) 2009 OpenCSW
# Author: Maciej Bliziński
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation.

import copy
import datetime
import logging
import os
import os.path
import re
import shutil
import urllib2
from Cheetah import Template
import sharedlib_utils as su
import common_constants

MAJOR_VERSION = "major version"
MINOR_VERSION = "minor version"
PATCHLEVEL = "patchlevel"
REVISION = "revision"
OTHER_VERSION_INFO = "other version info"
NEW_PACKAGE = "new package"
NO_VERSION_CHANGE = "no version change"
REVISION_ADDED = "revision number added"
PKG_URL_TMPL = "http://www.opencsw.org/packages/%s"
CATALOG_URL = "http://mirror.opencsw.org/opencsw/current/i386/5.10/catalog"
KNOWN_PKGNAME_PREFIXES = ["SUNW", "FJSV", "CSW"]
SUBMITPKG_TMPL = """From: $from
To: $to
#if $cc
Cc: $cc
#end if
Subject: $subject

#for $pkg_group in $pkg_groups
#if $pkg_group.upgrade_type == $NEW_PACKAGE
* $pkg_group.name: new package
#elif $pkg_group.upgrade_type == $NO_VERSION_CHANGE
* WARNING: no version change of $pkg_group.name
#else
* $pkg_group.name: $pkg_group.upgrade_type upgrade
  - from: $pkg_group.versions[0]
  -   to: $pkg_group.versions[1]
#end if
#for pkg in $pkg_group.pkgs
  + $pkg.basename
#end for

#end for
-- 
Generated by submitpkg
"""


class Error(Exception):
  pass


class PackageError(Error):
  pass


def ParsePackageFileName(p):
  if p.endswith(".gz"):
    p = p[:-3]
  if p.endswith(".pkg"):
    p = p[:-4]
  bits = p.split("-")
  if len(bits) >= 6:
    catalogname = "-".join(bits[:len(bits) - 4])
    bits = [catalogname] + bits[len(bits) - 4:]
  else:
    catalogname = bits[0]
  if len(bits) < 2:
    version, version_info, revision_info = None, None, None
    full_version_string = None
  else:
    version, version_info, revision_info = ParseVersionString(bits[1])
    full_version_string = bits[1]
  if len(bits) == 5:
    osrel, arch, vendortag = bits[2:5]
  elif len(bits) == 4:
    arch, vendortag = bits[2:4]
    osrel = "unspecified"
  elif len(bits) == 3:
    arch = bits[2]
    vendortag = "UNKN"
    osrel = "unspecified"
  else:
    arch = "unknown"
    vendortag = "UNKN"
    osrel = "unspecified"
  data = {
      'catalogname': catalogname,
      'full_version_string': full_version_string,
      'version': version,
      'version_info': version_info,
      'revision_info': revision_info,
      'osrel': osrel,
      'arch': arch,
      'vendortag': vendortag,
  }
  return data


def ComposeVersionString(version, revision_info):
  if revision_info:
    version += ","
    rev_lst = []
    for key in sorted(revision_info.keys()):
      rev_lst.append("%s=%s" % (key, revision_info[key]))
    version += "_".join(rev_lst)
  return version


def ComposePackageFileName(parsed_filename):
  """Composes package name, based on a parsed filename data structure.

  Does not use the version_string property, but builds the version from
  the basic version plus revision info.
  """
  tmpl = "%(catalogname)s-%(new_version)s-%(osrel)s-%(arch)s-%(vendortag)s.pkg"
  version_string = parsed_filename["version"]
  revision_info = parsed_filename["revision_info"]
  version_string = ComposeVersionString(version_string, revision_info)
  new_data = copy.copy(parsed_filename)
  new_data["new_version"] = version_string
  return tmpl % new_data


def ParseVersionString(s):
  version_bits = re.split("_|,", s)
  version_str = version_bits[0]
  revision_bits = version_bits[1:]
  revision_info = {}
  version_info = {}
  version_number_bits = version_str.split(".")
  version_info[MAJOR_VERSION] = version_number_bits[0]
  if len(version_number_bits) >= 2:
    version_info[MINOR_VERSION] = version_number_bits[1]
  if len(version_number_bits) >= 3:
    version_info[PATCHLEVEL] = version_number_bits[2]
  for version_bit in revision_bits:
    if "=" in version_bit:
      (var_name, var_value) = version_bit.split("=")
      revision_info[var_name] = var_value
    else:
      if not "extra_strings" in revision_info:
        revision_info["extra_strings"] = []
      revision_info["extra_strings"].append(version_bit)
  # Bits of parsed version must be hashable; especially extra_strings in
  # revision_info.
  if "extra_strings" in revision_info:
    revision_info["extra_strings"] = tuple(revision_info["extra_strings"])
  return version_str, version_info, revision_info


def ParseRevisionInfo(revinfo):
  if "REV" in revinfo:
    rev = revinfo["REV"]
    m = re.match(r"(\d+)\.(\d+)\.(\d+)", rev)
    if m:
      return tuple([int(x) for x in m.groups()])
    else:
      return ()
  else:
    return ()


def CompareVersions(v1, v2):
  """Compares two package versions represented as strings.

  This function should eventually converge with what pkgutil is doing.
  """
  # ('1.8.1', {'minor version': '8', 'patchlevel': '1', 'major version': '1'},
  # {'REV': '2010.07.13'})
  logging.debug("CompareVersions(%s, %s)", repr(v1), repr(v2))
  bv1, sv1, ri1 = ParseVersionString(v1)
  bv2, sv2, ri2 = ParseVersionString(v2)
  vn1 = tuple([int(x) for x in re.findall(r"\d+", bv1)])
  vn2 = tuple([int(x) for x in re.findall(r"\d+", bv2)])
  pr1, pr2 = (), ()
  if "REV" in ri1:
    pr1 = ParseRevisionInfo(ri1)
  if "REV" in ri2:
    pr2 = ParseRevisionInfo(ri2)
  key1 = pr1 + vn1
  key2 = pr2 + vn2
  return cmp(key1, key2)


class CatalogBasedOpencswPackage(object):

  catalog_downloaded = False

  def __init__(self, catalogname):
    self.catalogname = catalogname

  def IsOnTheWeb(self):
    url = PKG_URL_TMPL % self.catalogname
    logging.debug("Opening %s", repr(url))
    package_page = urllib2.urlopen(url)
    html = package_page.read()
    # Since beautifulsoup is not installed on the buildfarm yet, a quirk in
    # package page display is going to be used.
    package_not_in_mantis_pattern = u"cannot find maintainer"
    return html.find(package_not_in_mantis_pattern) >= 0

  def IsNew(self):
    return not self.IsOnTheWeb()

  def UpgradeType(self, new_version_string):
    """What kind of upgrade would it be if the new version was X.

    This function contains ugly logic.  It has many unit tests to prove that it
    does the right thing.

    Args:
      New (candidate) version string

    Returns:
      Revision type, message, (old_data, new_data)
    """
    (new_version,
     new_version_info,
     new_revision_info) = ParseVersionString(new_version_string)
    catalog_data = self.GetCatalogPkgData()
    if not catalog_data:
      return (NEW_PACKAGE,
              "/dev/null -> %s" % new_version_string,
              (None, new_version_string))
    cat_version_info = catalog_data["version_info"]
    levels = (MAJOR_VERSION, MINOR_VERSION, PATCHLEVEL)
    for level in levels:
      if level in cat_version_info and level in new_version_info:
        if (cat_version_info[level] != new_version_info[level]):
          versions = (catalog_data["full_version_string"], new_version_string)
          msg = "%s --> %s" % versions
          return level, msg, versions
    cat_rev_info = catalog_data["revision_info"]
    for rev_kw in new_revision_info:
      if rev_kw in cat_rev_info:
        if cat_rev_info[rev_kw] != new_revision_info[rev_kw]:
          msg = "%s: %s --> %s" % (rev_kw,
                                   cat_rev_info[rev_kw],
                                   new_revision_info[rev_kw])
          versions = cat_rev_info[rev_kw], new_revision_info[rev_kw]
          return REVISION, msg, versions
      else:
        # This revision info is missing from the old package
        msg = "new tag %s: %s" % (repr(rev_kw),
                                  new_revision_info[rev_kw])
        return REVISION_ADDED, msg, (None, new_revision_info[rev_kw])
    if (catalog_data["version"] == new_version
            and
        catalog_data["revision_info"] == new_revision_info):
      return NO_VERSION_CHANGE, "no", (new_version, new_version)
    return OTHER_VERSION_INFO, "other", (None, None)

  @classmethod
  def LazyDownloadCatalogData(cls, catalog_source=None):
    if not cls.catalog_downloaded:
      cls.DownloadCatalogData(catalog_source)
      cls.catalog_downloaded = True

  @classmethod
  def DownloadCatalogData(cls, catalog_source):
    """Downloads catalog data."""
    logging.debug("Downloading catalog data from %s.", repr(CATALOG_URL))
    if not catalog_source:
      catalog_source = urllib2.urlopen(CATALOG_URL)
    cls.catalog = {}
    for line in catalog_source:
      # Working around the GPG signature
      if line.startswith("#"): continue
      if "BEGIN PGP SIGNED MESSAGE" in line: continue
      if line.startswith("Hash:"): continue
      if len(line.strip()) <= 0: continue 
      if "BEGIN PGP SIGNATURE" in line: break
      fields = re.split(r"\s+", line)
      try:
        cls.catalog[fields[0]] = ParsePackageFileName(fields[3])
      except IndexError, e:
        print repr(line)
        print fields
        print e
        raise

  @classmethod
  def _GetCatalogPkgData(cls, catalogname):
    cls.LazyDownloadCatalogData()
    if catalogname in cls.catalog:
      return cls.catalog[catalogname]
    else:
      return None

  def GetCatalogPkgData(self):
    """A wrapper for the classmethod _GetCatalogPkgData, supplying the catalogname."""
    return self._GetCatalogPkgData(self.catalogname)


class StagingDir(object):
  """Represents a staging directory."""

  def __init__(self, dir_path):
    self.dir_path = dir_path

  def __repr__(self):
    return u"StagingDir(%s)" % repr(self.dir_path)

  def GetLatest(self,
                software,
                architectures=common_constants.ARCHITECTURES,
                os_rels=common_constants.OS_RELS):
    files = os.listdir(self.dir_path)
    package_files = []
    for os_rel in os_rels:
      for a in architectures:
        glob1 = "*-%s-%s-*.pkg.gz" % (os_rel, a)
        logging.debug("files: %s", files)
        logging.debug("glob1: %s", glob1)
        relevant_pkgs = sorted(
            shutil.fnmatch.filter(files, glob1))
        logging.debug("relevant_pkgs: %s", relevant_pkgs)
        glob2 = "%s-*.pkg.gz" % (software)
        logging.debug("glob2: %s", glob2)
        relevant_pkgs = sorted(
            shutil.fnmatch.filter(relevant_pkgs, glob2))
        logging.debug("relevant_pkgs: %s", relevant_pkgs)
        if relevant_pkgs:
          package_files.append(relevant_pkgs[-1])
    if not package_files:
      logging.warning(
          "Could not find any %s-* packages in %s",
          repr(software), repr(self.dir_path))
    logging.debug("The latest packages %s in %s are %s",
                  repr(software),
                  repr(self.dir_path),
                  repr(package_files))
    return [os.path.join(self.dir_path, x) for x in package_files]


class NewpkgMailer(object):

  def __init__(self, pkgnames, paths,
               release_mgr_name,
               release_mgr_email,
               sender_name,
               sender_email,
               release_cc):
    self.sender = u"%s <%s>" % (sender_name, sender_email)
    self.pkgnames = pkgnames
    self.paths = paths
    if release_mgr_name:
      self.release_mgr = u"%s <%s>" % (release_mgr_name, release_mgr_email)
    else:
      self.release_mgr = u"%s" % (release_mgr_email)
    self.release_cc = release_cc
    if self.release_cc:
      self.release_cc = unicode(release_cc)

  def FormatMail(self):
    return self._FormatMail(self.paths, self.pkgnames, self.sender,
                            self.release_mgr, self.release_cc)

  def _GetPkgsData(self, paths):
    """Gathering package info, grouping packages that are upgraded together."""
    pkgs_data = {}
    for p in paths:
      base_file_name = os.path.split(p)[1]
      catalogname = base_file_name.split("-")[0]
      pkg = CatalogBasedOpencswPackage(catalogname)
      new_data = ParsePackageFileName(base_file_name)
      new_version_str = new_data["full_version_string"]
      catalog_data = pkg.GetCatalogPkgData()
      if catalog_data:
        catalog_version_str = catalog_data["full_version_string"]
      else:
        catalog_version_str = "package not in the catalog"
      upgrade_type, upgrade_msg, versions = pkg.UpgradeType(new_version_str)
      pkgs_data_key = (upgrade_type, upgrade_msg, versions)
      if pkgs_data_key not in pkgs_data:
        pkgs_data[pkgs_data_key] = []
      pkg.srv4path = p
      pkg.cat_version_str = catalog_version_str
      pkg.new_version_str = new_version_str
      pkgs_data[pkgs_data_key].append(pkg)
    return pkgs_data

  def _FormatMail(self, paths, pkgnames, sender, release_mgr, release_cc):
    pkgs_data = self._GetPkgsData(paths)
    # Formatting grouped packages:
    pkg_groups = []
    for upgrade_type, upgrade_msg, versions in pkgs_data:
      pkg_group = {}
      pkg_group["upgrade_type"] = upgrade_type
      pkg_group["upgrade_msg"] = upgrade_msg
      pkg_group["versions"] = versions
      pkgs = pkgs_data[(upgrade_type, upgrade_msg, versions)]
      group_name = CatalogNameGroupName([pkg.catalogname for pkg in pkgs])
      pkg_group["name"] = group_name
      pkg_group["pkgs"] = [{'basename': os.path.basename(x.srv4path)} for x in pkgs]
      pkg_groups.append(pkg_group)
    subject = u"newpkgs %s" % (", ".join(pkgnames))
    if len(subject) > 50:
      subject = "%s(...)" % (subject[:45],)
    # Cheetah
    namespace = {
        'from': sender,
        'to': release_mgr,
        'cc': release_cc,
        'subject': subject,
        'date': datetime.datetime.now(),
        'pkg_groups': pkg_groups,
        'NEW_PACKAGE': NEW_PACKAGE,
        'NO_VERSION_CHANGE': NO_VERSION_CHANGE,
    }
    t = Template.Template(SUBMITPKG_TMPL, searchList=[namespace])
    return unicode(t)

  def GetEditorName(self, env):
    editor = "/opt/csw/bin/vim"
    if "EDITOR" in env:
      editor = env["EDITOR"]
    if "VISUAL" in env:
      editor = env["VISUAL"]
    return editor


def ParsePkginfo(lines):
  """Parses a pkginfo data."""
  d = {}
  for line in lines:
    try:
      # Can't use split, because there might be multiple '=' characters.
      line = line.strip()
      # Skip empty and commented lines
      if not line: continue
      if line.startswith("#"): continue
      var_name, var_value = line.split("=", 1)
      d[var_name] = var_value
    except ValueError, e:
      raise PackageError("Can't parse %s: %s" % (repr(line), e))
  return d


def PkgnameToCatName(pkgname):
  """Creates a catalog name based on the pkgname.

  SUNWbash  --> sunw_bash
  SUNWbashS --> sunw_bash_s
  SUNWPython --> sunw_python

  This function is incomprehensible, but unit tested!
  """
  for prefix in KNOWN_PKGNAME_PREFIXES:
    if pkgname.startswith(prefix):
      unused, tmp_prefix, the_rest = pkgname.partition(prefix)
      pkgname = tmp_prefix + "_" + the_rest
  return "_".join(SplitByCase(pkgname))


def SplitByCase(s):
  def CharType(c):
    if c.isalnum():
      if c.isupper():
        return 1
      else:
        return 2
    else:
      return 3
  chartype_list = [CharType(x) for x in s]
  neighbors = zip(chartype_list, chartype_list[1:])
  casechange = [False] + [x != y for x, y in neighbors]
  str_list = [(cc * "_") + l.lower() for l, cc in zip(s, casechange)]
  s2 = "".join(str_list)
  return re.findall(r"[a-z0-9]+", s2)


def CatalogNameGroupName(catalogname_list):
  """Uses heuristics to guess the common name of a group of packages."""
  catalogname_list = copy.copy(catalogname_list)
  if len(catalogname_list) == 1:
    return catalogname_list[0]
  current_substring = su.CollectionLongestCommonSubstring(catalogname_list)
  # If it's something like foo_, make it foo.
  while current_substring and not current_substring[-1].isalnum():
    current_substring = current_substring[:-1]
  if len(current_substring) >= 2:
    return current_substring
  return "various packages"


def PkginfoToSrv4Name(pkginfo_dict):
  SRV4_FN_TMPL = "%(catalog_name)s-%(version)s-%(osver)s-%(arch)s-%(tag)s.pkg"
  fn_data = {}
  fn_data["catalog_name"] = PkgnameToCatName(pkginfo_dict["PKG"])
  fn_data["version"] = pkginfo_dict["VERSION"]
  # os_version = pkginfo_dict["SUNW_PRODVERS"].split("/", 1)[0]
  # fn_data["osver"] = pkginfo_dict["SUNW_PRODNAME"] + os_version
  fn_data["osver"] = "SunOS5.10" # Hardcoded, because the original data contains
                                 # trash.
  fn_data["arch"] = pkginfo_dict["ARCH"]
  fn_data["tag"] = "SUNW"
  return SRV4_FN_TMPL % fn_data