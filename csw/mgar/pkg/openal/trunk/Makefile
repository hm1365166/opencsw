NAME = openal
VERSION = 0.0.8
GARTYPE = v1
CATEGORIES = lib

DESCRIPTION = openal - A 3D positional spatialized sound library (gcc3)
define BLURB
endef

MASTER_SITES = http://www.openal.org/openal_webstf/downloads/

DISTFILES  =$(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWopenal,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = al_main.diff

GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-esd

include gar/category.mk

#pre-configure:
#	( cd $(WORKSRC) ; ./autogen.sh )
#	@$(MAKECOOKIE)
