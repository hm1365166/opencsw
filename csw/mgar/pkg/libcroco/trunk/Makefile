NAME = libcroco
VERSION = 0.6.2
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = A CSS parsing and manipulation toolkit
define BLURB
  The Libcroco project is an effort to build a generic Cascading Style
  Sheet (CSS) parsing and manipulation toolkit that can be used by GNOME
  applications in need of CSS support.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWggettextrt CSWglib2 CSWlibxml2

BUILD64_LIBS_ONLY = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
