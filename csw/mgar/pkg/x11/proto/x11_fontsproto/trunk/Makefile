VERSION = 2.1.2
CATEGORIES = x11
PROTONAME = fontsproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = Fonts extension headers
define BLURB
  Font-related prototype header files for X11
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11fontsproto += catalogname-does-not-match-pkgname|pkgname=CSWx11fontsproto|catalogname=x11_fontsproto|expected-catalogname=x11fontsproto
CHECKPKG_OVERRIDES_CSWx11fontsproto += surplus-dependency|CSWx11common


RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

