VERSION = 2.6
CATEGORIES = x11
PROTONAME = dri2proto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org DRI2 prototype headers
define BLURB
  DRI2 prototype headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11dri2proto += catalogname-does-not-match-pkgname|pkgname=CSWx11dri2proto|catalogname=x11_dri2proto|expected-catalogname=x11dri2proto
CHECKPKG_OVERRIDES_CSWx11dri2proto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

