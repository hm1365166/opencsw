# $Id$
NAME = libemf
VERSION = 1.0.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library implementation of ECMA-234 API for the generation of enhanced metafiles
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = libEMF-$(VERSION)
DISTFILES  = $(DISTNAME).ta+= 0001-Use-__sparc-and-__i386-for-Solaris.patch
PATCHFILES += 0003-Keep-norunpath-during-libtool.patch

PACKAGES += CSWlibemf
SPKG_DESC_CSWlibemf = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibemf += CSWlibemf1

PACKAGES += CSWlibemf1
SPKG_DESC_CSWlibemf1 = Runtime library libEMF.so.1
PKGFILES_CSWlibemf1 += $(call pkgfiles_lib,libEMF.so.1)
# This is true for sparc as the library does not work for sparc64
CHECKPKG_OVERRIDES_CSWlibemf1 += 64-bit-binaries-missing

PACKAGES += CSWlibemf-dev
SPKG_DESC_CSWlibemf-dev = Development files for libEMF.so.1
PKGFILES_CSWlibemf-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibemf-dev = CSWlibemf1
OBSOLETED_BY_CSWlibemf-dev += CSWlibemf-develevel = CSWlibemf1

VENDOR_URL = http://libemf.sourceforge.net/

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:EXTRA_LINKER_FLAGS += -norunpath

BUILD64_LIBS_ONLY = 1

# 64 bit on Sparc is problematic as documented in include/libEMF/wine/winnt.h:
#    * This structure is valid only for 32-bit SPARC architectures, not for 64-bit SPARC.
SKIP_MODULATIONS += isa-$(ISA_DEFAULT64_sparc)

include gar/category.mk

