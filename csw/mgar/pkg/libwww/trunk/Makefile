NAME = w3c-libwww
VERSION = 5.4.0
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

MASTER_SITES = http://www.w3.org/Library/Distribution
DISTFILES  = $(NAME)-$(VERSION).tgz

PACKAGES = CSWlibwww
CATALOGNAME_CSWlibwww = w3c_libwww
SPKG_DESC_CSWgd = $(DESCRIPTION)

#PATCHFILES = 

#RUNTIME_DEP_PKGS_CSWlibwww  = 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

#BUILD64 = 1
#NOISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk
