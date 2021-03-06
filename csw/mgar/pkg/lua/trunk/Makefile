# $Id$

# Open issues:
# - provide different C/C++ libs for liblua as discussed here:
#     http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=560139

NAME = lua
VERSION = 5.2.2
MAJOR = $(shell echo $(VERSION) | awk -F. '{print $$1"."$$2}') lang
GARTYPE = v2

DESCRIPTION = Light-weight language designed for extending applications
define BLURB
  Lua is a powerful light-weight programming language designed for extending
  applications. Lua is also frequently used as a general-purpose, stand-alone
  language.
endef

MASTER_SITES = http://www.lua.org/ftp/
DISTFILES += $DISTFILES += lua.pc
EXPANDVARS += lua.pc$(DISTNAME).tar.gz

PATCHFILES += 0001-Make-c solaris10-i386

VENDOR_URL = http://www.lua.org

LICENSE = doc/readme.html

PACKAGES += CSWlua
SPKG_DESC_CSWlua = Light-weight language designed for extending applications
# PKGFILES is catchall

PACKAGES += CSWliblua5-2
SPKG_DESC_CSWliblua5-2 = Library for the LUA langauge, liblua.so.5.2
PKGFILES_CSWliblua5-2 += $(call pkgfiles_lib,liblua.so.5.2)

PACKAGES += CSWlua-dev
SPKG_DESC_CSWlua-dev = Development files for liblua.so.5.2
PKGFILES_CSWlua-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlua-dev += CSWliblua5-2

REINPLACEMENTS += luaroot
REINPLACE_MATCH_luaroot = (\#define\s+LUA_ROOT\s+).*
REINPLACE_WITH_luaro/ot = $$1"$(prefix)"
REINPLACE_FILES_luaroot += src/luaconf.h

BUILD64 = 1
ISAEXEC = 1

# No configure
CONFIGURE_SCRIPTS =

EXTR# This is in the original Makefile, add here as we overwrite CFLAGS
EXTRA_CFLAGS += -DLUA_COMPAT_ALLRA_CFLAGS += -KPIC

BUILD_ARGS += solaris
BUILD_ARGS += CC=$(CC)
BUILD_ARGS += CFLAGS="$(CFLAGS)"
BUILD_ARGS += MYLIBS="-ldl"
BUILD_ARGS += LDFLAGS="$(LDFLAGS)"

TEST_TARGET = test

INSTALL_ARGS += INSTALL=ginstall
INSTALL_ARGS += INSTALL_TOP=$(DESTDIR)$(prefix)
INSTALL_ARGS += INSTALL_MAN=$(DESTDIR)$(mandir)/man1
INSTALL_ARGS += INSTALL_BIN=$(DESTDIR)$(bindir)
INSTALL_ARGS += INSTALL_LIB=$(DESTDIR)$(libdir)

includ
post-install-modulated:
	ginstall -d $(DESTDIR)$(libdir)/pkgconfig
	ginstall $(WORKDIR)/lua.pc $(DESTDIR)$(libdir)/pkgconfig/lua-$(MAJOR).pc
	gln -s lua-$(MAJOR).pc $(DESTDIR)$(libdir)/pkgconfig/lua$(MAJOR).pc
	gln -s lua-$(MAJOR).pc $(DESTDIR)$(libdir)/pkgconfig/lua.pc
	@$(MAKECOOKIE)
