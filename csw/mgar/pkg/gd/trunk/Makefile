NAME    = gd
VERSION = 2.1.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library used for dynamic image creation
define BLURB
	GD is an open source code library for the dynamic creation of 
	images by programmers. GD creates PNG, JPEG and GIF images, 
	among other formats. GD is commonly used to generate charts, 
	graphics, thumbnails, and most anything else, on the fly. 
	While not restricted to use on the web, the most common 
	applications of GD involve web site development.
endef

MAs://bitbucket.org/libgd/gd-libgd/downloads/
DISTNAME = lib$(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.xz

GARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWpkgconfig= COMPILER = GCC4

PACKAGES = CSWgd
CATALOGNAME_CSWgd = gd
SPKG_DESC_CSWgd = Utilities facilitating libgd for dynamic image creation
# PKGFILES is catcPKGS_CSWgd += CSWlibgd3

PACKAGES += CSWlibgd3
CATALOGNAME_CSWlibgd3 = libgd3
SPKG_DESC_CSWlibgd3 = A library used for dynamic image creation providing libgd.so.3
PKGFILES_CSWlibgd3 += $(call pkgfiles_lib,libgd.so.3)
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibxpm4
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgd3 += CSWlibtiff5libgd2 += CSWzlib

PACKAGES += CSWlibgd-dev
CATALOGNAME_CSWlibgd-dev = libgd_dev
SPKG_DESC_CSWlibgd-dev = Development f.3
PKGFILES_CSWlibgd-dev +LES_CSWlibgd-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlib3?:\.\d+)*).tar.gz

CSW_DEFAULT_FONTPATH = $(sharedstatedir)/fonts/truetype

# This is evaluated twice, quote properly
EXTRA_CPPFLAGS = -DDEFAULT_FONTPATH=\\\"$(CSW_DEFAUL# For the success of the test for iconv
EXTRA_LINKER_FLAGS = -liconv

BUILD64 = 1
ISAEXEC = 1
D64_LIBS_ONLY = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-freetype=$(prefix)
CONFIGURE_ARGS += --with-fontconfig=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-xpm=$(prefix)
CONFIGURE_ARGS += --disable-fast-install

# GD does not have a testsuite
TEST_SCRIPTS =
it comes from a default error message
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/amd64/annotate
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/pentium_pro/annotate
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/sparcv8plus/annotate
CHECKPKG_OVERRIDES_CSWgd += file-with-bad-content|/usr/share|root/opt/csw/bin/sparcv9/annotate/csw/include/gd.h

include gar/category.mk

# Make sure GDFONTPATH is set correctly
post-extract-modulated:
	perl -pi -e 's,/usr/share/fonts/truetype,$(CSW_DEFAULT_FONTPATH),' \
		$(WORKSRC)/gdtestft.c \
		$(WORKSRC)/annotate.c
	perl -pi -e 's,(DEFAULT_FONTPATH\s+"),\1$(CSW_DEFAULT_FONTPATH):,' \
		$(WORKSRC)/gd.h
