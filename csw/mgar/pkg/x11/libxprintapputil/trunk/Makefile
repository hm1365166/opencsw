NAME = libXprintAppUtil
VERSION = 1.0.1
CATEGORIES = x11
GARTYPE = v2

DESCRIPTION = Xprint job utility client library
define BLURB
  libxprintapputil provides utility Xpau APIs allowing client applications to access information about and control Xprint jobs from an Xprint server. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxprintapputil CSWlibxprintapputildevel

CATALOGNAME_CSWlibxprintapputil = libxprintapputil
CATALOGNAME_CSWlibxprintapputildevel = libxprintapputil_devel

SPKG_DESC_CSWlibxprintapputil = $(DESCRIPTION)
SPKG_DESC_CSWlibxprintapputildevel = $(DESCRIPTION) development files

BUILD_DEP_PKGS = CSWlibxprintutildevel
RUNTIME_DEP_PKGS_CSWlibxprintapputil = CSWlibice CSWlibx11 CSWlibxau CSWlibxp CSWlibxprintutil CSWlibxt
RUNTIME_DEP_PKGS_CSWlibxprintapputildevel = CSWlibxprintapputil

PKGFILES_CSWlibxprintapputildevel  = $(PKGFILES_DEVEL)

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

include gar/category.mk
