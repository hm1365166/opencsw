VERSION = 1.0.4
CATEGORIES = x11
PROTONAME = windowswmproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION =  Windowswmproto headers for X.org
define BLURB
  Windowswmproto headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11windowswmproto += catalogname-does-not-match-pkgname|pkgname=CSWx11windowswmproto|catalogname=x11_windowswmproto|expected-catalogname=x11windowswmproto
CHECKPKG_OVERRIDES_CSWx11windowswmproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

