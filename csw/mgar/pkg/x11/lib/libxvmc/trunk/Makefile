NAME = libXvMC
VERSION = 1.0.5
CATEGORIES = x11

DESCRIPTION = XVideo Motion Compensation Library
define BLURB
  X-Video Motion Compensation (XvMC) provides accelerated video playback by offloading video decoding to hardware. It is an extension of the X video extension for the X Window System.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxvmc CSWlibxvmcdevel

CATALOGNAME_CSWlibxvmc = libxvmc
CATALOGNAME_CSWlibxvmcdevel = libxvmc_devel

SPKG_DESC_CSWlibxvmc = $(DESCRIPTION)
SPKG_DESC_CSWlibxvmcdevel = $(DESCRIPTION) development files

BUILD_DEP_PKGS = CSWxv

RUNTIME_DEP_PKGS_CSWlibxvmc       = CSWlibx11 CSWlibxext CSWlibxv
RUNTIME_DEP_PKGS_CSWlibxvmcdevel += CSWlibxvmc

BUILD_DEP_PKGS_CSWlibxvmc 	 += CSWlibxv
BUILD_DEP_PKGS_CSWlibxvmc 	 += CSWlibxvdevel

PKGFILES_CSWlibxvmcdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
