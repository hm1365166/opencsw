NAME = libart_lgpl
VERSION = 2.3.20
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = libart - High performance 2D graphics library
define BLURB
  Libart is a library of functions for 2D graphics supporting a superset of
  the PostScript imaging model, designed to be integrated with graphics,
  artwork, and illustration programs. It is written in optimized C, and is
  fully compatible with C++. With a small footprint of 10,000 lines of code,
  it is especially suitable for embedded applications. Libart is currently
  being used in several free software applications, including Gill
  (the Gnome SVG editor), the Gnome Canvas, and several others under
  development.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWlibart

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

include gar/category.mk
