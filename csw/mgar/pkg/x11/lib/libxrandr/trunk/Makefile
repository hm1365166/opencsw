NAME = libXrandr
VERSION = 1.3.0
CATEGORIES = x11

DESCRIPTION = X11 RandR extension library
define BLURB
  libXrandr provides an X Window System client interface to the RandR extension to the X protocol. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxrandr CSWlibxrandrdevel

CATALOGNAME_CSWlibxrandr = libxrandr
CATALOGNAME_CSWlibxrandrdevel = libxrandr_devel

SPKG_DESC_CSWlibxrandr = $(DESCRIPTION)
SPKG_DESC_CSWlibxrandrdevel = $(DESCRIPTION) development files

RUNTIME_DEP_PKGS_CSWlibxrandrdevel = CSWlibxrandr

# BUILD_DEP_PKGS = CSWrandrproto CSWlibxextdevel 

PKGFILES_CSWlibxrandrdevel  = $(PKGFILES_DEVEL)
# PKGFILES_CSWlibxrandr       = CSWlibx11 CSWlibxext CSWlibxrender

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
