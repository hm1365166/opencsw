VERSION = 1.3.2
CATEGORIES = x11
PROTONAME = randrproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org Randr protocol headers
define BLURB
  Randr protocol headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11randrproto += catalogname-does-not-match-pkgname|pkgname=CSWx11randrproto|catalogname=x11_randrproto|expected-catalogname=x11randrproto
CHECKPKG_OVERRIDES_CSWx11randrproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

