NAME = xfprint
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Printing Helper
define BLURB
   Xfce Printing Helper 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWxfceprint.depend CSWxfceprint.gspec CSWxfceprint.prototype
# DISTFILES += CSWxfceprintdoc.depend CSWxfceprintdoc.gspec CSWxfceprintdoc.prototype
# DISTFILES += CSWlibxfceprint.depend CSWlibxfceprint.gspec CSWlibxfceprint.prototype
# DISTFILES += CSWlibxfceprintdev.depend CSWlibxfceprintdev.gspec CSWlibxfceprintdev.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

DISTFILES += $(call admfiles,CSWxfceprint, depend)

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS += --enable-bsdlpr --enable-cups

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

