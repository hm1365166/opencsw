# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# Based on the following resources:
# - http://sources.gentoo.org/viewcvs.py/gentoo-x86/dev-libs/nss/nss-3.12.4-r1.ebuild?view=markup
# - https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Build_instructions
# - https://developer.mozilla.org/en/NSS_reference/NSS_environment_variables
# - https://developer.mozilla.org/en/NSS_reference/Building_and_installing_NSS/Installation_guide
#
# A discussion:
# - https://groups.google.com/group/mozilla.dev.tech.crypto/browse_thread/thread/709646e32fc4fad0#
#
# TODO: nss-config
# TODO: a better nss.pc
#
# there are a lot of other tools, which are not in the package at the moment,
# some of them was part of the 'Netscape/iPlanet Certificate Management System', see:
# http://docs.oracle.com/cd/E19850-01/816-6400-10/pkcsutil.html
# http://docs.oracle.com/cd/E19397-01/816-5549-10/contents.htm
# thats someone needs
# other resources:  news group mozilla.dev.tech.crypto
# http://www.mozilla.org/projects/security/pki/nss/tools/

NAME = nss
MAJOR_VERSION = 3
MINOR_VERSION = 17
PATCHLEVEL    = 4
VERSION = $(MAJOR_VERSION).$(MINOR_VERSION).$(PATCHLEVEL)
# #VERSION = $(MAJOR_VERSION).$(MINOR_VERSION)
GARTYPE = v2
 lib
GARTYPE = v2
DESCRIPTION = Network Security Services library
define BLURB
  Network Security Services (NSS) is a set of libraries designed to support
  cross-platform development of security-enabled client and server
  applications. Applications built with NSS can support SSL v2 and v3, TLS,
  PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3 certificates, and
  other security standards.
endef
SPKG_SOURCEURL = http://www.mozilla.org/projects/security/pki/nss/
# TODO: Generate RTM_NRTM_NAME = NSS_$(MAJOR_VERSION)_$(MINOR_VERSION)_$(PATCHLEVEL)_RTM
## RTM_NAME = NSS_$(MAJOR_VERSION)_$(MINOR_VERSIONION)_$(PATCHLEVEL)_RTM
MASTER_SITES = http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/$(RTM_NAME)/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += mpl
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
# GARCOMPILER = GCC4
# GARFLAVOR = DBG
GARCOMPILER = SOS12U4

# Required patches.
# PATCHFILES += include.patch
# PATCHFILES += ld-options.patch
# PATCHFILES += 0004-fix-xarch-and-add-SQLITE_LIB_DIR-var.patch
# PATCHFILES += 0006-platlibs.mk-linking-bltest.patch
# PATCHFILES += 0006-config.mk-linking.patch
# PATCHFILES += 0005-change-rpath-for-bins-in-platlibs.mk.patch
PATCHFILES += 0001-softtoken-config.mk.patch
PATCHFILES += 0002-cmd-platlib.mk.patch
PATCHFILES += 0003-sysinit-config.mk.patch
PATCHFILES += 0005-SunOS5.mk.patch

# For DBG builds
PATCHFILES_DBG  = whoami.patch
PATCHFILES_DBG += 0007-skip-assertion.patch

PATCHFILES += $(PATCHFILES_$(GARFLAVOR))rc solaris10-i386

PACKAGES += CSWlibnss3
CATALOGNAME_CSWlibnss3 = libnss3
SPKG_DESC_CSWlibnss3 += $(DESCRIPTION), libnss3.so
PKGFILES_CSWlibnss3 += $(call baseisadirs,$(libdir),libnss3\.so)
PKGFILES_CSWlibnss3 += $(call baseisadirs,$(libdir),libnss3\.so(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibnss3 += CSWlibnssutil3
RUNTIME_DEP_PKGS_CSWlibnss3 += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibnss3 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibnsRUNTIME_DEP_PKGS_CSWlibnss3_GCC4 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibnss3 += soname-equals-filename
# CHECKPKG_OVERRIDES_CSWlibnss3 += shared-lib-pkgname-mismatch/amd64/libnss3.so

PACKAGES += CSWlibnssckbi
CATALOGNAME_CSWlibnssckbi = libnssckbi
PKGFILES_CSWlibnssckbi += $(call baseisadirs,$(libdir),libnssckbi\.so)
PKGFILES_CSWlibnssckbi += $(call baseisadirs,$(libdir),libnssckbi\.so(\.\d+)*)
SPKG_DESC_CSWlibnssckbi += $(DESCRIPTION), libnssckbi.so
RUNTIME_DEP_PKGS_CSWlibnssckbi += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibnssckbi += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibnssckRUNTIME_DEP_PKGS_CSWlibnssckbi_GCC4 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibnssckbi += soname-equals-filename
# CHECKPKG_OVERRIDES_CSWlibnssckb1 += shared-lib-pkgname-mismatchkbi += CSWlibplc4

PACKAGES += CSWlibnssdbm3
CATALOGNAME_CSWlibnssdbm3 = libnssdbm3
PKGFILES_CSWlibnssdbm3 += $(call baseisadirs,$(libdir),libnssdbm3\.so)
PKGFILES_CSWlibnssdbm3 += $(call baseisadirs,$(libdir),libnssdbm3\.so(\.\d+)*)
PKGFILES_CSWlibnssdbm3 += $(call baseisadirs,$(libdir),libnssdbm3\.chk)
SPKG_DESC_CSWlibnssdbm3 += $(DESCRIPTION), libnssdbm3.so
RUNTIME_DEP_PKGS_CSWlibnssdbm3 += CSWlibnssutil3 
RUNTIME_DEP_PKGS_CSWlibnssdbm3 += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibnssdbm3 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibnssdbRUNTIME_DEP_PKGS_CSWlibnssdbm3_GCC4 += CSWlibgcc-s1b# i368 needs that, sparcs hates that
CHECKPKG_OVERRIDES_CSWlibnssdbm3 += surplus-dependency|CSWlibplc4
CHECKPKG_OVERRIDES_CSWlibnssdbm3 += soname-equals-filename
# CHECKPKG_OVERRIDES_CSWlibnssdbm3 += shared-lib-pkgname-mismatchd64/libnssdbm3.so

PACKAGES += CSWlibnssutil3
CATALOGNAME_CSWlibnssutil3 = libnssutil3
PKGFILES_CSWlibnssutil3 += $(call baseisadirs,$(libdir),libnssutil3\.so)
PKGFILES_CSWlibnssutil3 += $(call baseisadirs,$(libdir),libnssutil3\.so(\.\d+)*)
SPKG_DESC_CSWlibnssutil3 += $(DESCRIPTION), libnssutil3.so
RUNTIME_DEP_PKGS_CSWlibnssutil3 += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibnssutil3 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibnssutiRUNTIME_DEP_PKGS_CSWlibnssutil3_GCC4 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibnssutil3 += soname-equals-filename
# CHECKPKG_OVERRIDES_CSWlibnssutil3 += shared-lib-pkgname-mismatch64/libnssutil3.so

PACKAGES += CSWlibsmime3
CATALOGNAME_CSWlibsmime3 = libsmime3
SPKG_DESC_CSWlibsmime3 += $(DESCRIPTION), libsmime3.so
PKGFILES_CSWlibsmime3 += $(call baseisadirs,$(libdir),libsmime3\.so)
PKGFILES_CSWlibsmime3 += $(call baseisadirs,$(libdir),libsmime3\.so(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibsmime3 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibsmime3 += CSWlibnssutil3 
RUNTIME_DEP_PKGS_CSWlibsmime3 += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibsmime3 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibsmimRUNTIME_DEP_PKGS_CSWlibsmime3_GCC4 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibsmime3 += soname-equals-filename
# CHECKPKG_OVERRIDES_CSWlibsmine3 += shared-lib-pkgname-mismatchmd64/libsmime3.so

PACKAGES += CSWlibsoftokn3
CATALOGNAME_CSWlibsoftokn3 = libsoftokn3
PKGFILES_CSWlibsoftokn3 += $(call baseisadirs,$(libdir),libsoftokn3\.so)
PKGFILES_CSWlibsoftokn3 += $(call baseisadirs,$(libdir),libsoftokn3\.so(\.\d+)*)
PKGFILES_CSWlibsoftokn3 += $(call baseisadirs,$(libdir),libsoftokn3\.chk)
SPKG_DESC_CSWlibsoftokn3 += $(DESCRIPTION), libsoftokn3.so
RUNTIME_DEP_PKGS_CSWlibsoftokn3 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibsoftokn3 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibsoftokn3 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibsoftokn3 += CSWlibnssutil3 
RUNTIME_DEP_PKGS_CSWlibsoftoknRUNTIME_DEP_PKGS_CSWlibsoftokn3_GCC4 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibsoftokn3 += soname-equals-filename
# CHECKPKG_OVERRIDES_CSWlibsoftokn3 += shared-lib-pkgname-mismatch64/libsoftokn3.so

PACKAGES += CSWlibssl3
CATALOGNAME_CSWlibssl3 = libssl3
SPKG_DESC_CSWlibssl3 += $(DESCRIPTION), libssl3.so
PKGFILES_CSWlibssl3 += $(call baseisadirs,$(libdir),libssl3\.so)
PKGFILES_CSWlibssl3 += $(call baseisadirs,$(libdir),libssl3\.so(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibssl3 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibssl3 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibssl3 += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibssl3 +RUNTIME_DEP_PKGS_CSWlibssl3_GCC4 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibssl3 += soname-equals-filename
# CHECKPKG_OVERRIDES_CSWlibssl3 += shared-lib-pkgname-mismatch/amd64/libssl3.so

PACKAGES += CSWlibfreebl3
CATALOGNAME_CSWlibfreebl3 = libfreebl3
SPKG_DESC_CSWlibfreebl3 += $(DESCRIPTION)# PKGFILES_CSWlibfreebl3 += $(call baseisadirs,$(libdir),libfreebl.*3\.so)
# PKGFILES_CSWlibfreebl3 += $(call baseisadirs,$(libdir),libfreebl.*3\.so(\.\d+)*)
# PKGFILES_CSWlibfreebl3 += $(call baseisadirs,$(libdir),libfreebl.*3\.chk)
PKGFILES_CSWlibfreebl3 += $(call baseisadirs,$(libdir),libfreebl.*libfreebl.*3\.chk)
RUNTIME_DEP_PKGS_CSWlibfreebl3 += CSWlibnssutil3
RUNTIME_DEP_PKGS_CSWlibfreeblRUNTIME_DEP_PKGS_CSWlibfreebl3_GCC4 += CSWlibgcc-s1lCHECKPKG_OVERRIDES_CSWlibfreebl3 += soname-equals-filename
CHECKPKG_OVERRIDES_CSWlibfreebl3_sparc += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWlibfreebl3 += $(CHECKPKG_OVERRIDES_CSWlibfreebl3_$(GARCH))-ib/libfreebl3.so

PACKAGES += CSWlibnss-dev
CATALOGNAME_CSWlibnss-dev = libnss_dev
SPKG_DESC_CSWlibnss-dev = Network Security Services library, development files
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibssl3
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibplds4
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibplc4
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibsoftokn3
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibsmime3
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibnssutil3
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibnssdbm3
RUNTIME_DEP_PKGS_CSWlibnss-dev += CSWlibnssckbi
RUNTIME_DEP_PKGS_CSWlibnss-dev 64/libnssckbi.so
# OBSOLETED_BY_CSWlibnss-dev = CSWlibnss3-develnss3-tools
SPKG_DESC_CSWnss3-tools = Network Security Services library, command-line utilities
PKGFILES_CSWnss3-tools = $(bindir).*
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibnss3
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibplc4
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibplds4
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibsmime3
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibnssutil3
# plugins accessed via dlopen
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibsoftokn3
RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibnssdbm3 +RUNTIME_DEP_PKGS_CSWnss3-tools += CSWlibfreebl3+CHECKPKG_OVERRIDES_CSWnss3-tools += surplus-dependency|CSWlibfreebl3
CHECKPKG_OVERRIDES_CSWnss3-tools += surplus-dependency|CSWlibnssdbm3
CHECKPKG_OVERRIDES_CSWnss3-tools += surplus-dependency|CSWlibsoftokn3
OBSOLETED_BY_CSWnss3-tools = CSWlibnss3-tools+= CSWlibnssutil3+= CSWnspr-dev
BUILD_DEP_PKGS += CSWlibsqlite3-dev

BUILD64 = 1CSTS =
BUILD64 = 1
MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amd64   = $(libdir)

EXTRA_INC = $(prefix)/include

libdir_install = $(prefix)/lib
includedir = $(prefix)/include/nss

ifneq (DBG,$(GARFLAVOR))
	BUILD_OPT = 1
	# no configure target
#export BUILD_OPT
	CONFIGURE_ARGS += --disable-debug --enable-optimize
endif

# NSPR is installed in /opt/csw/lib/nspr, nspr.pc is in /opt/csw/lib/pkgconfig
NSPR_INCLUDE_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --cflags-only-I nspr | gsed 's/-I//')
export NSPR_INCLUDE_DIR

NSS_ENABLE_ECC = 1
export NSS_ENABLE_ECC

# To avoid creating /opt/csw/lib/libsqlite3.so (already exists)
NSS_USE_SYSTEM_SQLITE = 1
export NSS_USE_SYSTEM_SQLITE

# 64-bit suppport
ifeq ($(MODULATION),isa-sparcv9)
	USE_64 = 1
	export USE_64
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')/64
else
ifeq ($(MODULATION),isa-amd64)
	USE_64 = 1
	export USE_64
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')/64
else
	NSPR_LIB_DIR = $(shell PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig pkg-config --libs-only-L nspr | gsed 's/-L//' | tr -d ' ')
endif
endif
expo# LD_OPTIONS = -z ignore
ifeq ($(USE_64),1) 
  SQLITE_LIB_DIR = /opt/csw/lib/64
#   LD_OPTIONS += -R/opt/csw/lib/64/\$$ISALIST
else
  SQLITE_LIB_DIR = /opt/csw/lib
#   LD_OPTIONS += -R/opt/csw/lib/\$$ISALIST
endif
export SQLITE_LIB_DIR
rt SQLITE_LIB_DIR
SQLITE_INCLUDE_DIR = /opt/csw/include
export SQLITE_INCLUDE_DIR

# Based on:
# http://mxr.mozilla.org/security/source/security/nss/pkg/solaris/SUNWtlsu/prototype_com
NSS_BINARIES  = addbuiltin
NSS_BINARIES += certutil
NSS_BINARIES += cmsutil
NSS_BINARIES += crlutil
NSS_BINARIES += modutil
NSS_BINARIES += pk12util
NSS_BINARIES += signtool
NSS_BINARIES += signver
NSS_BINARIES += ssltap

LICENSE = mpl-trlibs.mk.patch

# http://lists.opencsw.org/pipermail/pkgsubmissions/2010-February/000167.html
GARCOMP_FLAGS_GCC4 = NS_USE_GCC=1
GARCOMP_FLAGS_SOS12U4 = 

# for whoami
EXTRA_BUILD_ENV = PATH=$(PATH):/usr/ucb

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = nss
INSTALL_SCRIPTS = nss
TEST_SCRIPTS =
 -R'$$ORIGIN'



include # build-nss: build-coreconf build-dbm build-nss-compile
build-nss: 
	(cd $(WORKSRC)/nss \
         CPPFLAGS='$(CPPFLAGS)' LD_OPTIONS='$(LD_OPTIONS)' \
        && env && gmake all prefix=$(prefix) BUILD_SUN_PKG=1 $(GARCOMP_FLAGS_$(GARCOMPILER)) NO_MDUPDATE=1)
	@$(MAKECOOKIE)

build-coreconf:
	(cd $(WORKSRC)/nss/coreconf \
	CPPFLAGS='$(CPPFLAGS)' LD_OPTIONS='$(LD_OPTIONS)' \
	&& (LD_OPTIO $(GARCOMP_FLAGS_$(GARCOMPILER)) NO_MDUPDATE=ONS)' \
	gmake -j1)
build-dbm:
	(cd $(WORKSRC)/nss/lib/dbm \
	CPPFLAGS='$(CPPFLAGS)' LD_OPTIONS='$(LD_OPTIONS)' \
	&& (LD_OPTIO $(GARCOMP_FLAGS_$(GARCOMPILER)) NO_MDUPDATE=ONS)' \
	gmake -j1)
	@$(MAKECOOKIE)

# There's an extra interpolation somehwere inside nss' build system, so $$$$
# needs to be used instead of $$.
bui@echo $(LD_OPTIONS)
	(cd $(WORKSRC)/mozilla/security/nss \
	CPPFLAGS='$(CPPFLAGS)' LD_OPTIONS='$(LD_OPTIONS)' \
		&& gmake -j1 BUILD_SUN_PKG=1 $(GARCOMP_FLAGS_$(GARCOMPILER)) NO_MDUPDATE=1b/\$$\$$ISALIST\')
	@$(MAKECOOKIE)

install-nss:
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	forWORKSRC)/mozilla/dist/SunOS5*/lib/*.so; do \
	  ginstall -m 755 $${f} $(DESTDIR)$(libdir); \
	  ifWORKSRC)/mozilla/dist/SunOS5*/lib/`basename $${f} .so`.chk ]; then \
	    ginstall -m 644 \
	WORKSRC)/mozilla/dist/SunOS5*/lib/`basename $${f} .so`.chk \
	      $(DESTDIR)$(libdir); \
	  fi \
	done
	ginstall -d -m 755 $(DESTDIR)$(bindir)
	# TODO: nss-config
	# gWORKSRC)/mozilla/dist/*/bin/nss-config $(DESTDIR)$(bindir)
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	for f inWORKSRC)/mozilla/dist/public/nss/*.h; \
		do \
		ginstall -m 644 $${f} $(DESTDIR)$(includedir); \
	done
	for bin in $(NSS_BINARIES); do \
	  ginstall -m 755 \WORKSRC)/mozilla/dist/*/bin/$${bin} \
	    $(DESTDIR)$(bindir)/`basename $${file}`; \
	done
	# Asserting that we have the right version in the .pc file
	ggrep "Version: $(VERSION)" $(FILEDIR)/nss.pc \
		|| ( \
			echo "Please adjust nss version in $(FILEDIR)/nss.pc" \
				&& \
			false \
		)
	ginstall -d -m 755 $(DESTDIR)$(libdir)/pkgconfig
	ginstall -m 644 $(FILEDIR)/nss.pc \
		$(DESTDIR)$(libdir)/pkgconfig
	if [ $(MEMORYMODEL) = 64 ]; then \
	    gsed/lib/64+' $(DESTDIR)$(libdir)/pkgconfig/nss.pc ; \
	fi
	@$(MAKECOOKIE)
