# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = muparser
VERSION = v2_2_3
# GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A fast math parser library
define BLURB
  Many applications require the parsing of mathematical expressions. The main objective of this library is to provide a fast and easy way of doing this. muParser is an extensible high performance math expression parser library written in C++. It works by transforming a mathematical expression into bytecode and precalculating constant parts of the expression. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(subst -,_,$(NAME)-$(VERSION))
DISTFILES  = $(DISTNAME).zip

LICENSE = License.txt

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

G# prefix = $(BUILD_PREFIX)/gxx

PACKAGES += CSWlibmuparser2
PKGFILES_CSWlibmuparser2Wlibmuparser2-gxx += $(call baseisadirs,$(libdir),libmuparser\.so\.2(\.\d+)*)
SPKG_DES += $(DESCRIPTION), libmuparser.so.2
RUNTIME_DEP_PKGS_CSWlibmuparser2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmuparser2 += CSWlibstdc++6Wlibmuparser2-gxx

PACKAGES += CSWmuparser-dev
CATALOGNAME_CSWmuparser-dev = muparser_dev
SPKG_DESC_CSWmuparser-dev += $(DESCRIPTION), development files
PKGFILES_CSWmuparser-dev += $RUNTIME_DEP_PKGS_CSWmuparser-dev += CSWlibmuparser2

# no target
SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

