NAME = libxkbfile
VERSION = 1.0.6
CATEGORIES = x11

DESCRIPTION = X11 keyboard file manipulation library
define BLURB
  Libxkbfile provides an interface to read and manipulate description
  files for XKB, the X11 keyboard configuration extension.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibxkbfile CSWlibxkbfiledevel

CATALOGNAME_CSWlibxkbfile = libxkbfile
CATALOGNAME_CSWlibxkbfiledevel = libxkbfile_devel

SPKG_DESC_CSWlibxkbfile = X11 keyboard file manipulation library
SPKG_DESC_CSWlibxkbfiledevel = X11 keyboard file manipulation library development files

RUNTIME_DEP_PKGS_CSWlibxkbfile = CSWlibx11
RUNTIME_DEP_PKGS_CSWlibxkbfiledevel = CSWlibxkbfile

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxkbfiledevel = $(PKGFILES_DEVEL)

include gar/category.mk
