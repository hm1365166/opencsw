#!/usr/bin/env python2.6

import datetime
import difflib
import hachoir_parser as hp
import hashlib
import logging
import magic
import os
import re
import shutil
import subprocess
import tempfile
import time

import configuration as c
import opencsw
import overrides

# Suppress unhelpful warnings
# http://bitbucket.org/haypo/hachoir/issue/23
import hachoir_core.config
hachoir_core.config.quiet = True


ADMIN_FILE_CONTENT = """
basedir=default
runlevel=nocheck
conflict=nocheck
setuid=nocheck
action=nocheck
partial=nocheck
instance=unique
idepend=quit
rdepend=quit
space=quit
authentication=nocheck
networktimeout=10
networkretries=5
keystore=/var/sadm/security
proxy=
"""

class Error(Exception):
  pass


class PackageError(Error):
  pass


class ShellMixin(object):

  def ShellCommand(self, args, quiet=False):
    logging.debug("Calling: %s", repr(args))
    if quiet:
      process = subprocess.Popen(args,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
      stdout, stderr = process.communicate()
      retcode = process.wait()
    else:
      retcode = subprocess.call(args)
    if retcode:
      raise Error("Running %s has failed." % repr(args))
    return retcode


class CswSrv4File(ShellMixin, object):
  """Represents a package in the srv4 format (pkg)."""

  def __init__(self, pkg_path, debug=False):
    self.pkg_path = pkg_path
    self.workdir = None
    self.gunzipped_path = None
    self.transformed = False
    self.dir_format_pkg = None
    self.debug = debug
    self.pkgname = None
    self.md5sum = None
    self.mtime = None

  def __repr__(self):
    return u"CswSrv4File(%s)" % repr(self.pkg_path)

  def GetWorkDir(self):
    if not self.workdir:
      self.workdir = tempfile.mkdtemp(prefix="pkg_")
      fd = open(os.path.join(self.workdir, "admin"), "w")
      fd.write(ADMIN_FILE_CONTENT)
      fd.close()
    return self.workdir

  def GetAdminFilePath(self):
    return os.path.join(self.GetWorkDir(), "admin")

  def GetGunzippedPath(self):
    if not self.gunzipped_path:
      gzip_suffix = ".gz"
      pkg_suffix = ".pkg"
      if self.pkg_path.endswith("%s%s" % (pkg_suffix, gzip_suffix)):
        # Causing the class to stat the .gz file.  This call throws away the
        # result, but the result will be cached as a class instance member.
        self.GetMtime()
        base_name_gz = os.path.split(self.pkg_path)[1]
        shutil.copy(self.pkg_path, self.GetWorkDir())
        self.pkg_path = os.path.join(self.GetWorkDir(), base_name_gz)
        args = ["gunzip", "-f", self.pkg_path]
        unused_retcode = self.ShellCommand(args)
        self.gunzipped_path = self.pkg_path[:(-len(gzip_suffix))]
      elif self.pkg_path.endswith(pkg_suffix):
        self.gunzipped_path = self.pkg_path
      else:
        raise Error("The file name should end in either "
                    "%s or %s, but it's %s."
                    % (gzip_suffix, pkg_suffix, repr(self.pkg_path)))
    return self.gunzipped_path

  def Pkgtrans(self, src_file, destdir, pkgname):
    """A proxy for the pkgtrans command.

    This requires custom-pkgtrans to be available.
    """
    if not os.path.isdir(destdir):
      raise PackageError("%s doesn't exist or is not a directory" % destdir)
    args = [os.path.join(os.path.dirname(__file__), "custom-pkgtrans"),
            src_file,
            destdir,
            pkgname ]
    pkgtrans_proc = subprocess.Popen(args,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
    stdout, stderr = pkgtrans_proc.communicate()
    ret = pkgtrans_proc.wait()
    if ret:
      logging.error(stdout)
      logging.error(stderr)
      logging.error("% has failed" % args)

  def GetPkgname(self):
    """It's necessary to figure out the pkgname from the .pkg file.
    # nawk 'NR == 2 {print $1; exit;} $f
    """
    if not self.pkgname:
      gunzipped_path = self.GetGunzippedPath()
      args = ["nawk", "NR == 2 {print $1; exit;}", gunzipped_path]
      nawk_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
      stdout, stderr = nawk_proc.communicate()
      ret_code = nawk_proc.wait()
      self.pkgname = stdout.strip()
      logging.debug("GetPkgname(): %s", repr(self.pkgname))
    return self.pkgname

  def GetMtime(self):
    if not self.mtime:
      # This fails if the file is not there.
      s = os.stat(self.pkg_path)
      t = time.gmtime(s.st_mtime)
      self.mtime = datetime.datetime(*t[:6])
    return self.mtime

  def TransformToDir(self):
    """Transforms the file to the directory format.

    This uses the Pkgtrans function at the top, because pkgtrans behaves
    differently on Solaris 8 and 10.  Having our own implementation helps
    achieve consistent behavior.
    """
    if not self.transformed:
      gunzipped_path = self.GetGunzippedPath()
      pkgname = self.GetPkgname()
      args = [os.path.join(os.path.dirname(__file__),
                           "..", "..", "bin", "custom-pkgtrans"),
              gunzipped_path, self.GetWorkDir(), pkgname]
      logging.debug("transforming: %s", args)
      unused_retcode = self.ShellCommand(args, quiet=(not self.debug))
      dirs = self.GetDirs()
      if len(dirs) != 1:
        raise Error("Need exactly one package in the package stream: "
                    "%s." % (dirs))
      self.dir_format_pkg = DirectoryFormatPackage(dirs[0])
      self.transformed = True

  def GetDirFormatPkg(self):
    self.TransformToDir()
    return self.dir_format_pkg

  def GetDirs(self):
    paths = os.listdir(self.GetWorkDir())
    dirs = []
    for p in paths:
      abspath = os.path.join(self.GetWorkDir(), p)
      if os.path.isdir(abspath):
        dirs.append(abspath)
    return dirs

  def GetPkgmap(self, analyze_permissions, strip=None):
    dir_format_pkg = self.GetDirFormatPkg()
    return dir_format_pkg.GetPkgmap(analyze_permissions, strip)

  def GetMd5sum(self):
    if not self.md5sum:
      logging.debug("GetMd5sum() reading file %s", repr(self.pkg_path))
      fp = open(self.pkg_path)
      hash = hashlib.md5()
      hash.update(fp.read())
      fp.close()
      self.md5sum = hash.hexdigest()
    return self.md5sum

  def GetPkgchkOutput(self):
    """Returns: (exit code, stdout, stderr)."""
    args = ["pkgchk", "-d", self.GetGunzippedPath(), "all"]
    pkgchk_proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = pkgchk_proc.communicate()
    ret = pkgchk_proc.wait()
    return ret, stdout, stderr

  def GetFileMtime(self):
    if not self.mtime:
      self.mtime = os.stat(self.pkg_path).st_mtime
    return self.mtime

  def __del__(self):
    if self.workdir:
      logging.debug("Removing %s", repr(self.workdir))
      shutil.rmtree(self.workdir)


class DirectoryFormatPackage(ShellMixin, object):
  """Represents a package in the directory format.

  Allows some read-write operations.
  """
  def __init__(self, directory):
    self.directory = directory
    self.pkgname = os.path.basename(directory)
    self.pkgpath = self.directory
    self.pkginfo_dict = None
    self.binaries = None
    self.file_paths = None
    self.files_metadata = None

  def __repr__(self):
    return u"<DirectoryFormatPackage directory=%s>" % repr(self.directory)

  def GetCatalogname(self):
    """Returns the catalog name of the package.

    A bit hacky.  Looks for the first word of the NAME field in the package.
    """
    pkginfo = self.GetParsedPkginfo()
    words = re.split(c.WS_RE, pkginfo["NAME"])
    return words[0]

  def GetParsedPkginfo(self):
    if not self.pkginfo_dict:
      pkginfo_fd = open(self.GetPkginfoFilename(), "r")
      self.pkginfo_dict = opencsw.ParsePkginfo(pkginfo_fd)
      pkginfo_fd.close()
    return self.pkginfo_dict

  def GetSrv4FileName(self):
    """Guesses the Srv4FileName based on the package directory contents."""
    return opencsw.PkginfoToSrv4Name(self.GetParsedPkginfo())

  def ToSrv4(self, target_dir):
    target_file_name = self.GetSrv4FileName()
    target_path = os.path.join(target_dir, target_file_name)
    if os.path.exists(target_path):
      return target_path
    pkg_container_dir, pkg_dir = os.path.split(self.directory)
    if not os.path.isdir(target_dir):
      os.makedirs(target_dir)
    args = ["pkgtrans", "-s", pkg_container_dir, target_path, pkg_dir]
    self.ShellCommand(args, quiet=True)
    args = ["gzip", "-f", target_path]
    self.ShellCommand(args, quiet=True)
    return target_path

  def GetPkgmap(self, analyze_permissions=False, strip=None):
    fd = open(os.path.join(self.directory, "pkgmap"), "r")
    return opencsw.Pkgmap(fd, analyze_permissions, strip)

  def SetPkginfoEntry(self, key, value):
    pkginfo = self.GetParsedPkginfo()
    logging.debug("Setting %s to %s", repr(key), repr(value))
    pkginfo[key] = value
    self.WritePkginfo(pkginfo)
    pkgmap_path = os.path.join(self.directory, "pkgmap")
    pkgmap_fd = open(pkgmap_path, "r")
    new_pkgmap_lines = []
    pkginfo_re = re.compile("1 i pkginfo")
    ws_re = re.compile(r"\s+")
    for line in pkgmap_fd:
      if pkginfo_re.search(line):
        fields = ws_re.split(line)
        # 3: size
        # 4: sum
        pkginfo_path = os.path.join(self.directory, "pkginfo")
        args = ["cksum", pkginfo_path]
        cksum_process = subprocess.Popen(args, stdout=subprocess.PIPE)
        stdout, stderr = cksum_process.communicate()
        cksum_process.wait()
        size = ws_re.split(stdout)[1]
        args = ["sum", pkginfo_path]
        sum_process = subprocess.Popen(args, stdout=subprocess.PIPE)
        stdout, stderr = sum_process.communicate()
        sum_process.wait()
        sum_value = ws_re.split(stdout)[0]
        fields[3] = size
        fields[4] = sum_value
        logging.debug("New pkgmap line: %s", fields)
        line = " ".join(fields)
      new_pkgmap_lines.append(line.strip())
    pkgmap_fd.close()
    # Write that back
    pkgmap_path_new = pkgmap_path + ".new"
    logging.debug("Writing back to %s", pkgmap_path_new)
    pkgmap_fd = open(pkgmap_path_new, "w")
    pkgmap_fd.write("\n".join(new_pkgmap_lines))
    pkgmap_fd.close()
    shutil.move(pkgmap_path_new, pkgmap_path)

    # TODO(maciej): Need to update the relevant line on pkgmap too

  def GetPkginfoFilename(self):
    return os.path.join(self.directory, "pkginfo")

  def WritePkginfo(self, pkginfo_dict):
    # Some packages extract read-only. To be sure, change them to be
    # user-writable.
    args = ["chmod", "-R", "u+w", self.directory]
    self.ShellCommand(args)
    pkginfo_filename = self.GetPkginfoFilename()
    os.chmod(pkginfo_filename, 0644)
    pkginfo_fd = open(pkginfo_filename, "w")
    pkginfo_dict = self.GetParsedPkginfo()
    for k, v in pkginfo_dict.items():
      pkginfo_fd.write("%s=%s\n" % (k, pkginfo_dict[k]))
    pkginfo_fd.close()

  def ResetNameProperty(self):
    """Sometimes, NAME= contains useless data. This method resets them."""
    pkginfo_dict = self.GetParsedPkginfo()
    catalog_name = opencsw.PkgnameToCatName(pkginfo_dict["PKG"])
    description = pkginfo_dict["DESC"]
    pkginfo_name = "%s - %s" % (catalog_name, description)
    self.SetPkginfoEntry("NAME", pkginfo_name)

  def GetDependencies(self):
    depends = []
    depend_file_path = os.path.join(self.directory, "install", "depend")
    if not os.path.exists(depend_file_path):
      return depends
    fd = open(os.path.join(self.directory, "install", "depend"), "r")
    # It needs to be a list because there might be duplicates and it's
    # necessary to carry that information.
    for line in fd:
      fields = re.split(c.WS_RE, line)
      if fields[0] == "P":
        pkgname = fields[1]
        pkg_desc = " ".join(fields[1:])
        depends.append((pkgname, pkg_desc))
    fd.close()
    return depends

  def CheckPkgpathExists(self):
    if not os.path.isdir(self.directory):
      raise PackageError("%s does not exist or is not a directory"
                         % self.directory)

  def GetFilesMetadata(self):
    """Returns a data structure with all the files plus their metadata.

    [
      {
        "path": ...,
        "mime_type": ...,
      },
    ]
    """
    if not self.files_metadata:
      self.CheckPkgpathExists()
      self.files_metadata = []
      files_root = os.path.join(self.directory, "root")
      if not os.path.exists(files_root):
        return self.files_metadata
      all_files = self.GetAllFilePaths()
      def StripRe(x, strip_re):
        return re.sub(strip_re, "", x)
      root_re = re.compile(r"^root/")
      file_magic = FileMagic()
      for file_path in all_files:
        full_path = unicode(self.MakeAbsolutePath(file_path))
        file_info = {
            "path": StripRe(file_path, root_re),
            "mime_type": file_magic.GetFileMimeType(full_path)
        }
        if not file_info["mime_type"]:
          logging.error("Could not establish the mime type of %s",
                        full_path)
          # We really don't want that, as it misses binaries.
          raise PackageError("Could not establish the mime type of %s"
                             % full_path)
        if opencsw.IsBinary(file_info):
          parser = hp.createParser(full_path)
          if not parser:
            logging.warning("Can't parse file %s", file_path)
          else:
            file_info["mime_type_by_hachoir"] = parser.mime_type
            machine_id = parser["/header/machine"].value
            file_info["machine_id"] = machine_id
            file_info["endian"] = parser["/header/endian"].display
        self.files_metadata.append(file_info)
    return self.files_metadata

  def ListBinaries(self):
    """Lists all the binaries from a given package.

    Original checkpkg code:

    #########################################
    # find all executables and dynamic libs,and list their filenames.
    listbinaries() {
      if [ ! -d $1 ] ; then
        print errmsg $1 not a directory
        rm -rf $EXTRACTDIR
        exit 1
      fi
      find $1 -print | xargs file |grep ELF |nawk -F: '{print $1}'
    }

    Returns a list of absolute paths.

    Now that there are files_metadata, this function can safely go away, once
    all its callers are modified to use files_metadata instead.
    """
    if self.binaries is None:
      self.CheckPkgpathExists()
      files_metadata = self.GetFilesMetadata()
      self.binaries = []
      # The nested for-loop looks inefficient.
      for file_info in files_metadata:
        if opencsw.IsBinary(file_info):
          self.binaries.append(file_info["path"])
      self.binaries.sort()
    return self.binaries

  def GetAllFilePaths(self):
    """Returns a list of all paths from the package."""
    if not self.file_paths:
      self.CheckPkgpathExists()
      remove_prefix = "%s/" % self.pkgpath
      self.file_paths = []
      for root, dirs, files in os.walk(os.path.join(self.pkgpath, "root")):
        full_paths = [os.path.join(root, f) for f in files]
        self.file_paths.extend([f.replace(remove_prefix, "") for f in full_paths])
    return self.file_paths

  def _GetOverridesStream(self, file_path):
    # This might potentially cause a file descriptor leak, but I'm not going to
    # worry about that at this stage.
    # NB, the whole catalog run doesn't seem to be suffering. (~2500 packages)
    #
    # There is a race condition here, but it's executing sequentially, I don't
    # expect any concurrency problems.
    if os.path.isfile(file_path):
      logging.debug("Opening %s override file." % repr(file_path))
      return open(file_path, "r")
    else:
      logging.debug("Override file %s not found." % repr(file_path))
      return None

  def _ParseOverridesStream(self, stream):
    override_list = []
    for line in stream:
      if line.startswith("#"):
        continue
      override_list.append(overrides.ParseOverrideLine(line))
    return override_list

  def GetOverrides(self):
    """Returns overrides, a list of overrides.Override instances."""
    overrides = []
    catalogname = self.GetCatalogname()
    override_paths = (
        [self.directory,
         "root",
         "opt/csw/share/checkpkg/overrides", catalogname],
        [self.directory,
         "install",
         "checkpkg_override"],
    )
    for override_path in override_paths:
      file_path = os.path.join(*override_path)
      stream = self._GetOverridesStream(file_path)
      if stream:
        overrides.extend(self._ParseOverridesStream(stream))
    return overrides

  def GetFileContent(self, pkg_file_path):
    if pkg_file_path.startswith("/"):
      pkg_file_path = pkg_file_path[1:]
    # TODO: Write a unit test for the right path
    file_path = os.path.join(self.directory, "root", pkg_file_path)
    try:
      fd = open(file_path, "r")
      content = fd.read()
      fd.close()
      return content
    except IOError, e:
      raise PackageError(e)

  def GetFilesContaining(self, regex_list):
    full_paths = self.GetAllFilePaths()
    files_by_pattern = {}
    for full_path in full_paths:
      content = open(self.MakeAbsolutePath(full_path), "rb").read()
      for regex in regex_list:
        if re.search(regex, content):
          if regex not in files_by_pattern:
            files_by_pattern[regex] = []
          files_by_pattern[regex].append(full_path)
    return files_by_pattern

  def MakeAbsolutePath(self, p):
    return os.path.join(self.pkgpath, p)


class FileMagic(object):
  """Libmagic sometimes returns None, which I think is a bug.
  Trying to come up with a way to work around that.
  """

  def __init__(self):
    self.cookie_count = 0
    self.magic_cookie = None

  def _GetCookie(self):
    magic_cookie = magic.open(self.cookie_count)
    self.cookie_count += 1
    magic_cookie.load()
    magic_cookie.setflags(magic.MAGIC_MIME)
    return magic_cookie

  def _LazyInit(self):
    if not self.magic_cookie:
      self.magic_cookie = self._GetCookie()

  def GetFileMimeType(self, full_path):
    """Trying to run magic.file() a few times, not accepting None."""
    self._LazyInit()
    mime = None
    for i in xrange(10):
      mime = self.magic_cookie.file(full_path)
      if mime:
        break;
      else:
        # Returned mime is null. Re-initializing the cookie and trying again.
        logging.error("magic_cookie.file(%s) returned None. Retrying.",
                      full_path)
        self.magic_cookie = self._GetCookie()
    return mime


class PackageComparator(object):

  def __init__(self, file_name_a, file_name_b,
               permissions=False,
               strip_a=None,
               strip_b=None):
    self.analyze_permissions = permissions
    self.pkg_a = CswSrv4File(file_name_a)
    self.pkg_b = CswSrv4File(file_name_b)
    self.strip_a = strip_a
    self.strip_b = strip_b

  def Run(self):
    pkgmap_a = self.pkg_a.GetPkgmap(self.analyze_permissions, strip=self.strip_a)
    pkgmap_b = self.pkg_b.GetPkgmap(self.analyze_permissions, strip=self.strip_b)
    diff_ab = difflib.unified_diff(sorted(pkgmap_a.paths),
                                   sorted(pkgmap_b.paths),
                                   fromfile=self.pkg_a.pkg_path,
                                   tofile=self.pkg_b.pkg_path)
    diff_text = "\n".join(diff_ab)
    if diff_text:
      less_proc = subprocess.Popen(["less"], stdin=subprocess.PIPE)
      less_stdout, less_stderr = less_proc.communicate(input=diff_text)
      less_proc.wait()
    else:
      print "No differences found."


class PackageSurgeon(ShellMixin):
  """Takes an OpenCSW gzipped package and performs surgery on it.

  Sows it up, adjusts checksums, and puts it back together.
  """

  def __init__(self, pkg_path, debug):
    self.debug = debug
    self.pkg_path = pkg_path
    self.srv4 = CswSrv4File(pkg_path)
    self.dir_pkg = None
    self.exported_dir = None
    self.parsed_filename = opencsw.ParsePackageFileName(self.pkg_path)

  def Transform(self):
    if not self.dir_pkg:
      self.dir_pkg = self.srv4.GetDirFormatPkg()
      logging.debug(repr(self.dir_pkg))
      # subprocess.call(["tree", self.dir_pkg.directory])

  def Export(self, dest_dir):
    self.Transform()
    if not self.exported_dir:
      basedir, pkgname = os.path.split(self.dir_pkg.directory)
      self.exported_dir = os.path.join(dest_dir, pkgname)
      shutil.copytree(
          self.dir_pkg.directory,
          self.exported_dir)
      subprocess.call(["git", "init"], cwd=self.exported_dir)
      subprocess.call(["git", "add", "."], cwd=self.exported_dir)
      subprocess.call(["git", "commit", "-a", "-m", "Initial commit"],
                      cwd=self.exported_dir)
    else:
      logging.warn("The package was already exported to %s",
                   self.exported_dir)

  def Patch(self, patch_file):
    self.Transform()
    args = ["gpatch", "-p", "1", "-d", self.dir_pkg.directory, "-i", patch_file]
    logging.debug(args)
    subprocess.call(args)

  def ToSrv4(self, dest_dir):
    self.Transform()
    pkginfo = self.dir_pkg.GetParsedPkginfo()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    self.parsed_filename["revision_info"]["REV"] = date_str
    new_filename = opencsw.ComposePackageFileName(self.parsed_filename)
    # Plan:
    # - Update the version in the pkginfo
    # - Update the pkgmap file, setting the checksums
    # - Transform it back to the srv4 form
    # - gzip it.
