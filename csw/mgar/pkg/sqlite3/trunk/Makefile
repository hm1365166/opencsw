NAME = sqlite3
VERSION = 3080300
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION  = An embeddable SQL engine in a C library
define BLURB
  SQLite is a in-process library that implements a self-contained, serverless,
  zero-configuration, transactional SQL database engine.
endef

# Download informations
MASTER_SITES = h2014http://sqlite.org/
DISTNAME = sqlite-autoconf-$(VERSION)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += copyrigVENDOR_URL = http://sqlite.orgight-release.html

LICENSE = copyright-relING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386ight-release.html

PACKAGES += CSWsqlite3
SPKG_DESC_CSWsqlite3 = An embeddable SQL engine in a C library
# PKGFILES_CSWsqlite3 = $(bindir)/.*
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWsqlite3 += CSWlibreadline6

PACKAGES += CSWlibsqlite3-0
SPKG_DESC_CSWlibsqlite3-0 = SQLite library providing libsqlite3.so.0
PKGFILES_CSWlibsqlite3-0 = $(call pkgfiles_lib,libsqlite3.so.0)
OBSOLETED_BY_CSWlibsqlite3-0 = CSWsqlite3rt
CATALOGNAME_CSWsqlite3rt = sqlite3_rt_stub

PACKAGES += CSWlibsqlite3-dev
SPKG_DESC_CSWlibsqlite3-dev = Development files for libsqlite3.so.0
PKGFILES_CSWlibsqlite3-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsqlite3-dev = CSWlibsqlite3-0
OBSOLETED_BY_CSWlibsqlite3-dev = CSWsqlite3devel
CATALOGNAME_CSWsqlite3devel = sqlite3_devel_stub

BUILD_DEP_PKGS += CSWreadline

# Enable sqlite3_unlock_notify() API as requested in #4837
EXTRA_CPPFLAGS += -DSQLITE_ENABLE_# FOr fchmod in stat.h
EXTRA_CPPFLAGS-5.9 += -D__EXTENSIONS__=1
EXTRA_CPPFLAGS += $(EXTRA_CPPFLAGS-$(GAROSREL))

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

