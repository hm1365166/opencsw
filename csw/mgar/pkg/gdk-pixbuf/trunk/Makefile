# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gdk-pixbuf
VERSION = 2.28.2
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = GNOME tools for pixmap manupulation
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
DISTFILES += CSWgdkpixbuf.postinstall

EXPANDVARS = CSWgdkpixbuf.postinstall

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

REINPLACE_USRSHARE += docs/reference/gdk-pixbuf/html/*.html

PACKAGES += CSWgdkpixbuf
# To retain backwards compatibility with gdk pixbuf package 0.22
CATALOGNAME_CSWgdkpixbuf = gdk_pixbuf
SPKG_DESC_CSWgdkpixbuf = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdkpixbuf  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgdk-pixbuf-xlib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibintl8
# I assume if one installs CSWgdkpixbuf, one wants all the stuff
# except -dev
CHECKPKG_OVERRIDES_CSWgdkpixbuf += surplus-dependency|CSWlibgdk-pixbuf-xlib2-0-0
CHECKPKG_OVERRIDES_CSWgdkpixbuf += catalogname-does-not-match-pkgname|pkgname=CSWgdkpixbuf|catalogname=gdk_pixbuf|expected-catalogname=gdkpixbuf

PACKAGES += CSWgdkpixbuf-doc
# To retain backwards compatibility with gdk pixbuf package 0.22
CATALOGNAME_CSWgdkpixbuf-doc = gdk_pixbuf_doc
SPKG_DESC_CSWgdkpixbuf-doc = $(DESCRIPTION), Documentation
ARCHALL_CSWgdkpixbuf-doc = 1
PKGFILES_CSWgdkpixbuf-doc = .*/gtk-doc/.*
CHECKPKG_OVERRIDES_CSWgdkpixbuf-doc += catalogname-does-not-match-pkgname|pkgname=CSWgdkpixbuf-doc|catalogname=gdk_pixbuf_doc|expected-catalogname=gdkpixbuf_doc

PACKAGES += CSWlibgdk-pixbuf2-0-0
SPKG_DESC_CSWlibgdk-pixbuf2-0-0 = $(DESCRIPTION), libgdk_pixbuf-2.0.so.0
PKGFILES_CSWlibgdk-pixbuf2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0  = CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibintl8

PACKAGES += CSWlibgdk-pixbuf-xlib2-0-0
SPKG_DESC_CSWlibgdk-pixbuf-xlib2-0-0 = $(DESCRIPTION), libgdk_pixbuf_xlib-2.0.so.0
PKGFILES_CSWlibgdk-pixbuf-xlib2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf_xlib-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgdk-pixbuf-dev
SPKG_DESC_CSWlibgdk-pixbuf-dev = Developtment files $(DESCRIPTION)
PKGFILES_CSWlibgdk-pixbuf-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev = CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev += CSWlibgdk-pixbuf-xlib2-0-0

BUILD_DEP_PKGS  = CSWggettext-dev
BUILD_DEP_PKGS += CSWlibjbig-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibtiff-dev

BUILD64 = 1

# We need the binaries to query 64 bit modules
MERGE_DIRS_isa-extra = $(bindir) $(libdir)

CONFIGURE_ARGS-32 = 
# Fails on introspection build on 64bits
CONFIGURE_ARGS-64 = --enable-introspection=no

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix
CONFIGURE_ARGS += --with-libintl-prefix
CONFIGURE_ARGS += --with-x11
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

include gar/category.mk

