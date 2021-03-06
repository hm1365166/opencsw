# $Id$

NAME = gpgme
VERSION = 1.5.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = GPGME - GnuPG Made Easy
define BLURB
  GPGME (GnuPG Made Easy) is a C language library that allows to add support
  for cryptography to a program. It is designed to make access to public key
  crypto engines like GnuPG or GpgSM easier for applications. GPGME provides
  a high-level crypto API for encryption, decryption, signing, signature
  verification and key management.
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/gpgme/
DISTFILES  = $(NAME)-$mVENDOR_gme,)

SPKG_SOURCEURL = http://www.gnupg.org/related_software/libraries.e# this is necessary to have vasprintf which is available only with
# libc from SUNW_1.22.7 up; if the map file is not inhibited any user
# of the library which also uses the vasprintf() will get the private
# reference which core dumps in most of the cases.
LINKER_MAP_RELEASE	=	

GARCOMPILER		=	GNU
#GARFLAVOR		=	DBG

PATCHFILES += 0001-fix-tz-set-warning.patch
PATCHFILES += 0002-fix-trace-macros-in-non-void-return.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-fd-passing

BUILD64_LIBS_ONLY = 1

BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibpth-dev
BUILD_DEP_PKGS += CSWlibassuan-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWgnupg2

OBSOLETED_BY_CSWlibgpgme11 = CSWgpgme
OBSOLETED_BY_CSWlibgpgme-pthread11 = CSWgpgme

PACKAGES += CSWlibgpgme-pthread11
CATALOGNAME_CSWlibgpgme-pthread11 = libgpgme_pthread11
PKGFILES_CSWlibgpgme-pthread11 += $(call baseisadirs,$(libdir),libgpgme-pthread\.so\.11(\.\d+)*)
SPKG_DESC_CSWlibgpgme-pthread11 += $(DESCRIPTION), libgpgme-pthread.so.11
RUNTIME_DEP_PKGS_CSWlibgpgme-pthread11 += CSWlibassuan0
RUNTIME_DEP_PKGS_CSWlibgpgme-pthread11 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgpgme-pthread11 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibgpgme-pthread11	+=	forbidden-version-interface-dependencies|/opt/csw/lib/libgpgme-pthread.so.11.13.0|requires|forbidden|interface|version|SUNW_1.22.7|in|library|libc.so.1
CHECKPKG_OVERRIDES_CSWlibgpgme-pthread11	+=	forbidden-version-interface-dependencies|/opt/csw/lib/sparcv9/libgpgme-pthread.so.11.13.0|requires|forbidden|interface|version|SUNW_1.22.7|in|library|libc.so.1
CHECKPKG_OVERRIDES_CSWlibgpgme-pthread11	+=	forbidden-version-interface-dependencies|/opt/csw/lib/amd64/libgpgme-pthread.so.11.13.0|requires|forbidden|interface|version|SUNW_1.22.7|in|library|libc.so.1

PACKAGES += CSWlibgpgme11
CATALOGNAME_CSWlibgpgme11 = libgpgme11
PKGFILES_CSWlibgpgme11 += $(call baseisadirs,$(libdir),libgpgme\.so\.11(\.\d+)*)
SPKG_DESC_CSWlibgpgme11 += $(DESCRIPTION), libgpgme.so.11
RUNTIME_DEP_PKGS_CSWlibgpgme11 += CSWlibassuan0
RUNTIME_DEP_PKGS_CSWlibgpgme11 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgpgme11 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibgpgme11	+=	forbidden-version-interface-dependencies|/opt/csw/lib/libgpgme.so.11.13.0|requires|forbidden|interface|version|SUNW_1.22.7|in|library|libc.so.1
CHECKPKG_OVERRIDES_CSWlibgpgme11	+=	forbidden-version-interface-dependencies|/opt/csw/lib/sparcv9/libgpgme.so.11.13.0|requires|forbidden|interface|version|SUNW_1.22.7|in|library|libc.so.1
CHECKPKG_OVERRIDES_CSWlibgpgme11	+=	forbidden-version-interface-dependencies|/opt/csw/lib/amd64/libgpgme.so.11.13.0|requires|forbidden|interface|version|SUNW_1.22.7|in|library|libc.so.1

PACKAGES += CSWgpgme-dev
CATALOGNAME_CSWgpgme-dev = gpgme_dev
SPKG_DESC_CSWgpgme-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWgpgme-dev += CSWlibgpgme11
RUNTIME_DEP_PKGS_CSWgpgme-dev += CSWlibgpgme-pthread11

include gar/category.mk
