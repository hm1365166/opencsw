NAME = xfce4-session
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Session Manager
define BLURB
   Xfce Session Manager 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWxfcesession.depend CSWxfcesession.gspec CSWxfcesession.prototype
# DISTFILES += CSWlibxfcesession.depend CSWlibxfcesession.gspec CSWlibxfcesession.prototype
# DISTFILES += CSWxfcesessiondoc.depend CSWxfcesessiondoc.gspec CSWxfcesessiondoc.prototype
# DISTFILES += CSWlibxfcesessiondev.depend CSWlibxfcesessiondev.gspec CSWlibxfcesessiondev.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

DISTFILES += $(call admfiles,CSWxfcesession, depend)

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS += --enable-dbus
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

