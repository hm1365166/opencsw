GARNAME = GD
GARVERSION = 2.44
CATEGORIES = cpan
AUTHOR = LDS

DESCRIPTION = Interface to GD Graphics Library
define BLURB
  GD.pm is a Perl interface to Thomas Boutell\'s gd graphics library (version
  2.01 or higher; see below). GD allows you to create color drawings using a
  large number of graphics primitives, and emit the drawings as PNG files.
endef

PACKAGES = CSWpmgd
CATALOGNAME = pm_gd

RUNTIME_DEP_PKGS = CSWftype2 CSWgd CSWiconv CSWjpeg CSWpng
RUNTIME_DEP_PKGS += CSWxpm CSWzlib CSWfconfig
BUILD_DEP_PKGS = CSWgd

# if we build against libjpeg7, we need to patch one test
# PATCHFILES = diff-GD.t

CONFIGURE_ARGS  = lib_gd_path $(libdir)
CONFIGURE_ARGS += lib_ft_path $(libdir)
CONFIGURE_ARGS += lib_png_path $(libdir)
CONFIGURE_ARGS += lib_jpeg_path $(libdir)
CONFIGURE_ARGS += lib_xpm_path $(libdir)
CONFIGURE_ARGS += lib_zlib_path $(libdir)

# Don't use hardcoded -Wformat=0
BUILD_OVERRIDE_DIRS = CCFLAGS

include gar/category.mk
pre-build-modulated:
	gsed -i'' 's,-ljpeg,/opt/csw/lib/libjpeg.so.62,' $(WORKSRC)/Makefile
