NAME = sox
VERSION = 14.4.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Swiss Army Knife of sound processing utilities
define BLURB
  SoX is the Swiss Army Knife of sound processing utilities. It can convert
  audio files to other popular audio file types and also apply sound effects
  and filters during the conversion.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES bz2$(GARCOMPILER = GCC4$(DISTNAME).tar.gz

# There is a hack in there to rewind pipes when detecting file formats.
# As the FILE struct is opaque in 64 bit we:
# I believe the behaviour should be consistent in both 32 and 64, and
# anyway, rewinding a *pipe*?!
PATCHFILES = 0001-Disable-stdio-hack-to-rewind-pipes.patch(?:\.\d+)*).tar.gz

VENDOR_URL = http://sox.BUILD_DEP_PKGS += CSWlibvorbis-dev
BUILD_DEP_PKGS += CSWlibogg-dev
BUILD_DEP_PKGS += CSWlibmad-dev
BUILD_DEP_PKGS += CSWlibflac-dev
BUILD_DEP_PKGS += CSWlibao-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibwavpack-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibmagic-dev
BUILD_DEP_PKGS += CSWlibmp3lame-dev
BUILD_DEP_PKGS += CSWlibsndfile-dev
BUILD_DEP_PKGS += CSWlibid3tagx.sourceforge.net/

PACKAGES += CSWsox
CATALOGNAME_CSWsox = sox
SPKG_DESC_CSWsox = $(DESCRIPTION)
RUNTIME_DEP_PKGS_C2

PACKAGES += CSWlibsox2
CATALOGNAME_CSWlibsox2 = libsox2
SPKG_DESC_CSWlibsox2 = SOX Library for audio processing, libsox.so.2
PKGFILES_CSWlibsox2 += $(call pkgfiles_lib,libsox.so.2)
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibmad0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibflac8
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibao4
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibwavpack1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibmagic1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibsndfile1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibid3tag0 += CSWlibmp3lame0

PACKAGES += CSWlibsox-dev
CATALOGNAME_CSWlibsox-dev = libsox_dev
SPKG_DESC_CSlibrary development files, libsox.so.2
PKGFILES_CSWlibsox-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsox-dev = CSWlibsox2x-dev = CSWlibsox1

OBSOLETED_BY_CSWlibsox-dev = CSWlibsoxdevel
CATALOGNAME_CSWlibsoxde_stub

+= CSWlame-devel

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS +=  --withou = 1
ISAEXEC = 1

include gar/category.mk
