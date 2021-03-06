# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GSHHS_VERSION = 2.1.0

GARNAME = gmtcoast
GARVERSION = $(GSHHS_VERSION)
CATEGORIES = apps
DESCRIPTION = Coastline Definition Files for Generic Mapping Tools
define BLURB
  GMT is an open source collection of ~60 tools for manipulating geographic and Cartesian data sets (including filtering, trend fitting, gridding, projecting, etc.) and producing Encapsulated PostScript File (EPS) illustrations ranging from simple x-y plots via contour maps to artificially illuminated surfaces and 3-D perspective views. GMT supports ~30 map projections and transformations and comes with support data such as GSHHS coastlines, rivers, and political boundaries. GMT is developed and maintained by Paul Wessel and Walter H. F. Smith with help from a global set of volunteers, and is supported by the National Science Foundation. It is released under the GNU General Public License. 
endef

SPKG_SOURCEURL = http://gmt.soest.hawaii.edu/
MASTER_SITES = ftp://ftp.iris.washington.edu/pub/gmt/ ftp://ftp.soest.hawaii.edu/gmt/ ftp://gd.tuwien.ac.at/pub/gmt/

DISTFILES  = GSHHS$(GSHHS_VERSION)_coast.tar.bz2 \
	     GSHHS$(GSHHS_VERSION)_full.tar.bz2 \
	     GSHHS$(GSHHS_VERSION)_high.tar.bz2 

UFILES_REGEX = GSHHS(\d+(?:\.\d+)*)_(.*).tar.gz

ARCHALL = 1

LICENSE = LICENSE.TXT

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

## The tarball just dumps into the current directory, no archive name
WORKSRC = $(WORKDIR)

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(datadir)/coast
	@ginstall -d $(DESTDIR)$(datadir)/coast
	@cp -r $(WORKSRC)/share/coast/* $(DESTDIR)$(datadir)/coast/
	@$(MAKECOOKIE)
