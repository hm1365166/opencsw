NAME = mousepad
VERSION = 0.2.13
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Mousepad Text Editor
define BLURB
   Xfce Mousepad Text Editor 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWxfcemousepad.depend CSWxfcemousepad.gspec CSWxfcemousepad.prototype
DISTFILES += $(call admfiles,CSWxfcemousepad, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

