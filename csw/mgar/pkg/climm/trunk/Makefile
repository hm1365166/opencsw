NAME = climm
VERSION = 0.6.1
GARTYPE = v1

DESCRIPTION = terminal-based ICQ client
define BLURB
  mICQ is a very portable text-mode ICQ clone - it is known to compile under
  Linux, Solaris, BSD, AIX, HPUX, Windows, AmigaOS and with restrictions BeOS.
endef

MASTER_SITES = http://www.climm.org/
DISTFILES  = $(NAME)-$(VERSION).tgz
DISTFILES += $(call admfiles,CSWclimm,prototype depend)
DISTFILES += climm.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

PATCHFILES = climm.patch

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS += --enable-tcl --enable-ssl --enable-autopackage
CONFIGURE_ARGS += --enable-binreloc --enable-binreloc-threads

# climm doesn't have a test target
TEST_TARGET =

include gar/category.mk

post-install:
	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/climm
	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/climm
