NAME = xfwm4
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Window Manager 
define BLURB
   Xfce Window Manager
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += CSWxfcexfwm4.depend CSWxfcexfwm4.gspec CSWxfcexfwm4.prototype
DISTFILES += CSWxfcexfwm4doc.depend CSWxfcexfwm4doc.gspec CSWxfcexfwm4doc.prototype

# PATCHFILES = frame.c.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

LIBDEPS = xfce/mcs-mananager

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS +=  --enable-xsync --enable-render --enable-randr --enable-xinerama --enable-compositor

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

