NAME = orage
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Orage Calendar
define BLURB
   Orage provides a calendar which integrates nicely into the Xfce desktop environment. It is highly configurable and supports alerts based on dates. It warns you with popup or audio alarm. As it is an application kind-of every day use it launches itself in the background as a daemon.
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfceorage, depend)
# DISTFILES += CSWxfceorage.depend CSWxfceorage.gspec CSWxfceorage.prototype
# DISTFILES += CSWxfceoragedoc.depend CSWxfceoragedoc.gspec CSWxfceoragedoc.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS += --enable-reentrant

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

