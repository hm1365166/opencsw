PROTONAME = applewmproto
VERSION = 1.4.2
CATEGORIES = x11
NAME = x11_$(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = AppleWM extension headers from X.org
define BLURB
  AppleWM extension headers from modular X.org X11 project
endef

MASTER_SITES = $(X11_PROTO_MASTER_SITE)
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWx11applewmproto
CATALOGNAME_CSWx11applewmproto = x11_applewmproto

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

CHECKPKG_OVERRIDES_CSWx11applewmproto += catalogname-does-not-match-pkgname|pkgname=CSWx11applewmproto|catalogname=x11_applewmproto|expected-catalogname=x11applewmproto
CHECKPKG_OVERRIDES_CSWx11applewmproto += surplus-dependency|CSWx11common

include gar/category.mk

