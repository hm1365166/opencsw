NAME = liboldX
VERSION = 1.0.1
CATEGORIES = x11
GARTYPE = v2

DESCRIPTION = The oldX Library
define BLURB
  The old X10 compatibility library
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWliboldx CSWliboldxdevel

CATALOGNAME_CSWliboldx = liboldx
CATALOGNAME_CSWliboldxdevel = liboldx_devel

SPKG_DESC_CSWliboldx = $(DESCRIPTION)
SPKG_DESC_CSWliboldxdevel = $(DESCRIPTION) development files

RUNTIME_DEP_PKGS_CSWliboldxdevel = CSWliboldx

PKGFILES_CSWliboldxdevel  = $(PKGFILES_DEVEL)

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

include gar/category.mk
