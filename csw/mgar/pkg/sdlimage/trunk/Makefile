NAME = SDL_image
VERSION = 1.2.12
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = SDL image file loading library
define BLURB
SDL image library loads images as SDL surfaces, and supports the following formats: BMP, PNM, XPM, LBM, PCX, GIF, JPEG, PNG, TGA.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_image/release/
DISTFILES  = $(NAME)-$(GARCOMPILER = SUN$(VERSION).+= CSWlibsdl-image1-2-0
CATALOGNAME_CSWlibsdl-image1-2-0 = libsdl_image1_2_0
PKGFILES_CSWlibsdl-image1-2-0 += $(call baseisadirs,$(libdir),libSDL_image-1\.2\.so\.0\.8\.4)
PKGFILES_CSWlibsdl-image1-2-0 += $(call baseisadirs,$(libdir),libSDL_image-1\.2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsdl-image1-2-0 += $(DESCRIPTION), libSDL_image-1.2.so.0

# This creates the stub package that older packages depend on.
OBSOLETED_BY_CSWlibsdl-image1-2-0 += CSWsdlimage

# Split development files into separate package. 
PACKAGES += CSWsdlimage-dev
CATALOGNAME_CSWsdlimage-dev = sdlimage_dev
SPKG_DESC_CSWsdlimage-dev += $(DESCRIPTION), development files
PKGFILES_CSWsdlimage-dev += /opt/csw/lib/libSDL_image.so
PKGFILES_CSWsdlimage-dev += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWsdlimage-dev += CSWlibsdl-image1-2-0
RUNTIME_DEP_PKGS_CSWlibsdl-image1-2-0 += CSWlibsdl1-2-0_RUNTIME_DEP_PKGS_CSWlibsdl-image1-2-0 += CSWlibwebp4_PKGS = CSWlibsdl

UFILES_REGEX = $(NAME)-(\d+(?:BUILD64_LIBS_ONLY = 1?:# lower build level for the 32-bit libs for backwords compatibilty.
ISA_DEFAULT_sparc-5.10 ?= sparcv8
ISA_DEFAULT_i386-5.10 ?= i386?:EXTRA_LINKER_FLAGS = -lwebp

CONFIGURE_ARGS = $(DIRPATHS) --disable-static

TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWlibsdl-image1-2-0 += surplus-dependency|CSWlibwebp4

include gar/category.mk
