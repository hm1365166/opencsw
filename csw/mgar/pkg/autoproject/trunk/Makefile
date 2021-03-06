# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = autoproject
VERSION = 0.20

GARTYPE = v2
DESCRIPTION = A utility for automated configuration of GNU autotools
define BLURB

  autoproject interviews the user, then creates a source package for a new
  program which follows the GNU programming standards. The new package uses
  autoconf to configure itself, and automake to create the Makefile. `make
  distcheck' succeeds.

  The idea is that you execute autoproject just once when you start a new
  project. It will ask a few questions, then create a new directory and populate
  it with standard files, customized for the new project.

endef
SPKG_SOURCEURL = http://packages.debian.org/unstable/devel/autoproject
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/a/$(NAME)/
DISTFILES  = $(NAME)_$(VERSION).orig.tar.gz
PATCHFILES = 0001-gawk-and-ggrep.patch
ARCHALL = 1
RUNTIME_DEP_PKGS = CSWautomake CSWbash CSWgawk CSWggrep
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
AWK=gawk
GREP=ggrep
EXTRA_EXPORTS = AWK GREP

# checkpkg can't detect that gawk and ggrep are necessary
CHECKPKG_OVERRIDES_CSWautoproject += surplus-dependency
# /usr/local in the documentation.
CHECKPKG_OVERRIDES_CSWautoproject += file-with-bad-content

include gar/category.mk
