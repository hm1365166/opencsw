NAME = keepassx
VERSION = 0.4.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Cross platform password manager
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

# This needs qmake from Qt >= 4.3

include gar/category.mk
