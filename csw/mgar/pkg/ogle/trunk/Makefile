NAME = ogle
VERSION = 0.9.2
GARTYPE = v1
CATEGORIES = apps

DESCRIPTION = opensource DVD player with DVD menu support
define BLURB
  opensource DVD player with DVD menu support
endef

MASTER_SITES = http://www.dtek.chalmers.se/groups/dvd/dist/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWogle, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

#PATCHFILES = configure.in.diff

CONFIGURE_ARGS = $(DIRPATHS) --disable-mmx
CONFIGURE_ARGS += --with-libmlib=/export/home/jgoerzen/MediaLib

TEST_SCRIPTS =

include gar/category.mk

# Cannot do this yet (libtool problems)
#pre-configure:
#	( cd $(WORKSRC) ; ./autogen.sh )
#	@$(MAKECOOKIE)
