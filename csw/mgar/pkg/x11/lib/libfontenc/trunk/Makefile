NAME = libfontenc
VERSION = 1.0.5
CATEGORIES = x11

DESCRIPTION = X11 font encoding library
define BLURB
  libfontenc is a library which helps font libraries portably determine and deal with different encodings of fonts.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibfontenc CSWlibfontencdevel

CATALOGNAME_CSWlibfontenc = libfontenc
CATALOGNAME_CSWlibfontencdevel = libfontenc_devel

SPKG_DESC_CSWlibfontenc = $(DESCRIPTION)
SPKG_DESC_CSWlibfontencdevel = $(DESCRIPTION) development files

RUNTIME_DEP_PKGS_CSWlibfontencdevel = CSWlibfontenc
RUNTIME_DEP_PKGS_CSWlibfontenc      = CSWzlib

PKGFILES_CSWlibfontencdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
