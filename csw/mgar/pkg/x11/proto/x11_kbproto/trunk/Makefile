VERSION = 1.0.6
PROTONAME = kbproto
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

CATEGORIES = x11

DESCRIPTION = KB extension headers from X.org
define BLURB
  This provides the KB extension headers from modular X.org X11 project.
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11$(PROTONAME)
CATALOGNAME_CSWx11$(PROTONAME) = x11_$(PROTONAME)

CHECKPKG_OVERRIDES_CSWx11kbproto += catalogname-does-not-match-pkgname|pkgname=CSWx11kbproto|catalogname=x11_kbproto|expected-catalogname=x11kbproto
CHECKPKG_OVERRIDES_CSWx11kbproto += surplus-dependency|CSWx11common

RUNTIME_DEP_PKGS = CSWx11common
INCOMPATIBLE_PKGS = CSWkbproto

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

