# $Id$

NAME = clusterssh
VERSION = 3.28
GARTYPE = v2

DESCRIPTION = ClusterSSH controls a number of xterm windows via a single graphical console window
define BLURB
  ClusterSSH controls a number of xterm windows via a single graphical console
  window to allow commands to be interactively run on multiple servers over an
  ssh connection.
endef

SF_PROJECT = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Search-opt-csw-bin-instead-of-usr-local.patch

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=89139
UPSTREAM_USE_SF = 1

RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpmtk
RUNTIME_DEP_PKGS += CSWpm-x11-protocol

CHECKPKG_OVERRIDES_CSWclusterssh += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWclusterssh += surplus-dependency|CSWpmtk
CHECKPKG_OVERRIDES_CSWclusterssh += surplus-dependency|CSWpm-x11-protocol

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)

# Not gonna do it
TEST_SCRIPTS =

include gar/category.mk
