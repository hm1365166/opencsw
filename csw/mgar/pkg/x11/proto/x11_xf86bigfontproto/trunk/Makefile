VERSION = 1.2.0
CATEGORIES = x11
PROTONAME = xf86bigfontproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = X.Org XF86BigFont protocol headers
define BLURB
  XF86BigFont protocol headersX protocol and ancillary headers from modular X.org
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11xf86bigftproto
CATALOGNAME_CSWx11xf86bigftproto = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11xf86bigftproto += catalogname-does-not-match-pkgname|pkgname=CSWx11xf86bigftproto|catalogname=x11_xf86bigfontproto|expected-catalogname=x11xf86bigftproto
CHECKPKG_OVERRIDES_CSWx11xf86bigftproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

