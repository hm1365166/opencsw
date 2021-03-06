# $Id$

NAME = scons
VERSION = 2.3.2
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A next-generation build tool
define BLURB
  SCons is an Open Source software construction tool - that is,
  a next-generation build tool. Think of SCons as an improved,
  cross-platform substitute for the classic Make utility with
  integrated functionality similar to autoconf/automake and compiler
  caches such as ccache. In short, SCons is an easier, more
  reliable and faster way to build software.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(NAME)-$(VERSION).tar.gz

# Linker patch for Solaris 9 only
PATCHFILES-5.9 += 0001-Solaris-9-ld-1-needs-h-for-soname.patch
PATCHFILES += $(PATCHFILES-$(GAROSREL))

# We have only one package and that is archall, choose sparc
# We need libserf on Solaris 9 for subversion and that requires a current scons
# Solaris 10 has different link options, so different packages for Solaris 9 and 10
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc

VENDOR_URL = http://www.scons.org/

PACKAGES += CSWscons
SPKG_DESC_CSWscons = A next-generation build tool
# PKGFILES is catchall
ARCHALL_CSWscons = 1
CHECKPKG_OVERRIDES_CSWscons += file-with-bad-content
# We definitely need Python 2.7
RUNTIME_DEP_PKGS_CSWscons += CSWpython27
CHECKPKG_OVERRIDES_CSWscons += surplus-dependency|CSWpython27

# scons needs Python 2.7
REINPLACEMENTS += python
REINPLACE_MATCH_python = \#!.*
REINPLACE_WITH_python = \#!/opt/csw/bin/python2.7
REINPLACE_FILES_python += script/scons

CONFIGURE_SCRIPTS =
TEST_SCRIPTS = 
EXTRA_PAX_ARGS = -s ",\./opt/csw/man,./opt/csw/share/man,"

EXTRA_MERGE_EXCLUDE_FILES = .*\.py[co]

include gar/category.mk
