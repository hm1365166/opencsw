NAME = xfdesktop
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Desktop Manager
define BLURB
   Xfce Desktop Manager 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWxfcedesktop.depend CSWxfcedesktop.gspec CSWxfcedesktop.prototype
# DISTFILES += CSWxfcedesktopdoc.depend CSWxfcedesktopdoc.gspec CSWxfcedesktopdoc.prototype
DISTFILES += $(call admfiles,CSWxfcedesktop, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

CONFIGURE_ARGS +=   --enable-desktop-icons 
CONFIGURE_ARGS +=   --enable-file-icons
CONFIGURE_ARGS +=   --enable-thunarx 
CONFIGURE_ARGS +=   --enable-exo
CONFIGURE_ARGS +=   --enable-menueditor 
CONFIGURE_ARGS +=   --enable-desktop-menu
CONFIGURE_ARGS +=   --enable-panel-plugin

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/thunar-vfs-1
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/thunarx-1

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

