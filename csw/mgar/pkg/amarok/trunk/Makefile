NAME = amarok
VERSION = 1.4.8
GARTYPE = v1

DESCRIPTION = Amarok is the music player for Linux and Unix with an intuitive interface
define BLURB
  Amarok is the KDE media player, but it
  is also widely used on other desktop environments
endef

MASTER_SITES = ftp://ftp.kde.org/pub/kde/stable/amarok/$(VERSION)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += $(call admfiles,CSWamarok,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PATCHFILES = disable-broken-languages.diff
PATCHFILES += gpod-stdint.h.diff

GARCOMPILER = GNU
#GCC4 works, but Phil has requested GCC3 for now
GNU_CC_HOME = /opt/csw/gcc3

LIBDEPS += lib/libgpod

CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += --prefix=$(prefix)/kde-gcc
CONFIGURE_ARGS += --with-qt-dir=/opt/csw/kde-gcc
CONFIGURE_ARGS += --with-qt-libraries=/opt/csw/kde-gcc/lib
CONFIGURE_ARGS += --includedir=/opt/csw/include
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --with-libgpod

CONFIGURE_ARGS += LDFLAGS="-L/opt/csw/kde-gcc/lib -L/opt/csw/lib/$$ISALIST"

TEST_SCRIPTS =

include gar/category.mk

#I'm having all manner of issues with the final RUNPATH linking of amarok
#Setting LD_OPTIONS here explicitly, as kde-gcc/lib _MUST_ be first for qt to work
LD_OPTIONS := "-R/opt/csw/kde-gcc/lib:/opt/csw/\$$ISALIST:/opt/csw/lib"

post-install: remove-libtool-files

remove-libtool-files:
	(gfind $(DESTDIR)/opt/csw/kde-gcc/lib -name \*.la -exec rm {} \;)
	(gfind $(DESTDIR)/opt/csw/kde-gcc/lib -name \*.a -exec rm {} \;)
