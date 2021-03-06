#####################################################################
# OpenCSW build recipe for cadaver
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = cadaver
VERSION = 0.23.3
GARTYPE = v2

DESCRIPTION = WebDAV commandline tool
define BLURB
 cadaver is a command-line WebDAV client. It supports resource upload/download/display, namespace 
 operations (copy/move), collection deletion/creation, property manipulation, and locking operations.
endef

PACKAGES = CSWcadaver
SPKG_DESC_CSWcadaver = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWcadaver = CSWlibintl8
RUNTIME_DEP_PKGS_CSWcadaver += CSWlibneon27
RUNTIME_DEP_PKGS_CSWcadaver += CSWlibreadline6

# Stub package that allow us to rename transparently the package
# from CSWcadav to CSWcadaver
OBSOLETED_BY_CSWcadaver = CSWcadav
CATALOGNAME_CSWcadav = cadaver_stub

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

###### Upstream and opencsw files information #######

MASTER_SITES = http://www.webdav.org/cadaver/

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += changelog.CSW

# cadaver wants to links with curses because of readline
# but it's not necessary as readline already depends on
# ncurses
PATCHFILES = 0001-no-curses-dependency.patch

##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat

TEST_SCRIPTS =

include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

post-merge:
	ginstall -D $(DOWNLOADDIR)/changelog.CSW $(PKGROOT)$(docdir)/$(NAME)/changelog.CSW


