NAME = gtk-xfce-engine
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce GTK theme engine 
define BLURB
   Xfce GTK theme engine 
endef

VERSION = 2.4.2
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWgtkxfceengine.depend CSWgtkxfceengine.gspec CSWgtkxfceengine.prototype
DISTFILES += $(call admfiles,CSWgtkxfceengine, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

include gar/category.mk

CFLAGS   += -xlibmil
CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/xfce4
LDFLAGS  += -L/opt/csw/lib -R/opt/csw/lib

# DEPENDS += xfce/libxfce4util

CONFIGURE_ARGS = --prefix=/opt/csw --disable-debug --enable-final 

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( if [ -d $(DESTDIR)/opt/csw/lib/gtk-2.0/2.10.0/engines ] ; then  cp -frpv $(DESTDIR)/opt/csw/lib/gtk-2.0/2.10.0/engines $(DESTDIR)/opt/csw/lib/gtk-2.0 ; rm -fr $(DESTDIR)/opt/csw/lib/gtk-2.0/2.10.0 ; fi ; )
