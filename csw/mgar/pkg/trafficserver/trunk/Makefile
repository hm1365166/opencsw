# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = trafficserver
VERSION = 3.2.4
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server.
define BLURB
  Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server
endef

MASTER_SITES = http://people.apache.org/~igalic/releases/
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-i386
BUILD64_ONLY = 1
ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/$(NAME)
CONFIGURE_ARGS += --libexecdir=$(libexecdir)/$(NAME)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-tcl=$(libdir)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-lzma=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --enable-hwloc
CONFIGURE_ARGS += --disable-silent-rules

PROTOTYPE_MODIFIERS += data
PROTOTYPE_FILES_data += $(sysconfdir)/?.*
PROTOTYPE_FILES_data += $(datadir)/?.*
PROTOTYPE_USER_data = nobody
PROTOTYPE_GROUP_data = nobody

STRIP_LIBTOOL = 1

GARCOMPILER = SOS12U3

RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibz1
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWstlport                                                                                                                                                                 
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibhwloc5
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibexpat1                                                                                                                                                                   
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWliblzma5

EXTRA_LINKER_FLAGS += -norunpath

REINPLACE_USRLOCAL += plugins/regex_remap/regex_remap.cc
CHECKPKG_OVERRIDES_CSWtrafficserver += file-with-bad-content|/usr/share|root/opt/csw/bin/amd64/traffic_shell
CHECKPKG_OVERRIDES_CSWtrafficserver += file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/trafficserver

# It's currently not useful to separate these:
CHECKPKG_OVERRIDES_CSWtrafficserver += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWtrafficserver += shared-lib-pkgname-mismatch

LICENSE = LICENSE

# Be careful with GNU tools. We only need it for ginstall
INSTALL_ENV_PATH = $(prefix)/gnu:$(PATH)

inclu