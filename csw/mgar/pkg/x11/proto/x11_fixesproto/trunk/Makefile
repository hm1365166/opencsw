VERSION = 5.0
CATEGORIES = x11
PROTONAME = fixesproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION =  X11 Fixes extension protocol specification 
define BLURB
   Fixes extension protocol specification modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11fixesproto += catalogname-does-not-match-pkgname|pkgname=CSWx11fixesproto|catalogname=x11_fixesproto|expected-catalogname=x11fixesproto
CHECKPKG_OVERRIDES_CSWx11fixesproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
