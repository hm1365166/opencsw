#####################################################################
# OpenCSW build recipe for OpenSSL
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

# Uncomment to enable PKCS11 engine
PKCS11 = 1

###### Package information #######

NAME = openssl
VERSION = 0.9.8zf
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endelibssl0-9-8ndency|CSWopenssl

SPKG_DESC_CSWlibssl0-9-8 = Openssl runtime libraries
CATALOGNAME_CSWlibssl0-9-8 = libssl0_9_8
RUNTIME_DEP_PKGS_CSWlibssl0-9-8 = Cyendency|CSWperl

#CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += surplus-dependency|CSWcacertificates

# this package contains several libraries files and we will not split
#CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += non-uniform-lib-versions-in-package|sonames=libcrypto.so.0.9.7,libcrypto.so.0.9.8,libssl.so.0.9.7,libssl.so.0.9.8
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libcrypto.so.0.9.7|soname=libcrypto.so.0.9.7|pkgname=CSWlibssl0-9-8|expected=CSWlibcrypto0-9-7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libcrypto.so.0.9.8|soname=libcrypto.so.0.9.8|pkgname=CSWlibssl0-9-8|expected=CSWlibcrypto0-9-8
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libssl.so.0.9.7|soname=libssl.so.0.9.7|pkgname=CSWlibssl0-9-8|expected=CSWlibssl0-9-7
ifeq ($(shell /usr/bin/uname -p),sparc) 
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv8plus+vis/libcrypto.so.0.9.7|soname=libcrypto.so.0.9.7|pkgname=CSWlibssl0-9-8|expected=CSWlibcrypto0-9-7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv8plus+vis/libcrypto.so.0.9.8|soname=libcrypto.so.0.9.8|pkgname=CSWlibssl0-9-8|expected=CSWlibcrypto0-9-8
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv8plus+vis/libssl.so.0.9.7|soname=libssl.so.0.9.7|pkgname=CSWlibssl0-9-8|expected=CSWlibssl0-9-7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/libcrypto.so.0.9.7|soname=libcrypto.so.0.9.7|pkgname=CSWlibssl0-9-8|expected=CSWlibcrypto0-9-7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/libcrypto.so.0.9.8|soname=libcrypto.so.0.9.8|pkgname=CSWlibssl0-9-8|expected=CSWlibcrypto0-9-8
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/libssl.so.0.9.7|soname=libssl.so.0.9.7|pkgname=CSWlibssl0-9-8|expected=CSWlibssl0-9-7
else
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += shared-lib-pkgname-mismatch|file=opt/csw/lib/amd64/libcrypto.so.0.9.8|soname=libcrypto.so.0.9.8|pkgname=CSWlibssl0-9-8|expected=CSWlibcrypto0-9-8
endif

# we will not recompile old 0.9.7CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += no-direct-binding|/opt/csw/lib/libssl.so.0.9.7|is|not|directly|bound|to|soname|libcrypto.so.0.9.7
ifeq ($(shell /usr/bin/uname -p),sparc) b/sparcv8plus+vis
#CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += bad-rpath-entry|/opt/csw/lib/sparcv8plus+vis
#CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += bad-rpath-entry|/opt/csw/lib/sparcv8plus+vis
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 +=CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += no-direct-binding|/opt/csw/lib/sparcv9/libssl.so.0.9.7|is|not|directly|bound|to|soname|libcrypto.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += no-direct-binding|/opt/csw/lib/sparcv8plus+vis/libssl.so.0.9.7|is|not|directly|bound|to|soname|libcrypto.so.0.9.7
elseibcrypto.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/lib/pentium_pro/libcrypto.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/lib/pentium_pro/libssl.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/lib/libcrypto.so.0.9.7
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/export/home|root/opt/csw/libCHECKPKG_OVERRIDES_CSWlibssl0-9-8 += no-direct-binding|/opt/csw/lib/pentium_pro/libssl.so.0.9.7|is|not|directly|bound|to|soname|libcrypto.so.0.9.77/libssl# the /usr/local references in the documents files are relevantssl_utils/CHANGES
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/usr/local|root/opt/csw/shareINSTALLe/doc/openssl/FAQ
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/usr/local|root/opt/csw/sharehare/doc/openssl/FAQ
CHECKPKG_OVERRIDES_CSWlibssl0-9-8 += file-with-bad-content|/usr/local|root/opt/csw/sharee/doc/lisl_dev/INSTALL



###### Upstream and opencsw files information #######

MASTER_SITES = http://www.openssl.org/source/ http://openssl.org/news/
UPSTREAM_MASTER_SITES = http://www.openssl.org/source/ 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $( = $(NAME)-(0.9.8[a-z]).tar.gz

DISTFILES  = $(NAME)-$(VERSION).tar.gz 
DISTFILES +l CSWlibssl0-9-8.prototype-i386 CSWlibssl0-9-8.prototype-sppe 
DISTFILES += changelog.CSW README.CSW

DOCFILES = CHANGES CHANGES.SSLeay PROBLEMS README FAQ README.ASN1 INSTALL NEWS README.ENGINE

# This patch add optimised build targets for some solaris isa, ie:
# solaris-386-cc, solaris-pentium-cc, solaris-pentium_pro-cc, solaris-sparcv9+vis-cc
PATCHFILES = more_configure_targets.patch

# Update openssl.cnf path in man page to follow opencsw standard
PATCHFILES += opencsw_paths.patch

# Let's always block some compromised CA, whatever the CA configured
# (patchs taken from Debian Package)
PATCHFILES += block_bad_certificates.patch

LICENSE=LICENSE

##### Build and installation information #####

# Sun Studio 12 incorrectly outputs v8plus code instead of
# v8 code under Solaris 10 so we use Sun Studio 12 update 1
ifneq ($(shell /usr/bin/uname -r),5.9)
	GARCOMPILER = SOS12U1
endif

# The list of instructions set for which we will 
# provide optimized libraries and binaries
BUILD64 = 1
BUILD64_LIBS_ONLY = 1
EXTRA_BUILD_ISAS_i386 = pentium_pro 
EXTRA_BUILD_ISAS_sparc = sparcv8plus+vis

# we keep building the i386 even under 5.10 to keep the 
# same prototype file for Solaris 9 and Solaris 10 packages
# (could switch to dynamic prototype to avoid that)
ISA_DEFAULT_i386-5.10 = i386

# GAR wants and puts sparcv9 in lib/64 but openssl build system
# isn't the standard autoconf/automake one so we disable this
# relocation for now
ISALIBDIR_sparcv9 = .
libdir = /opt/csw/lib

# we include *.a files in the devel package so we don't want them excluded
MERGE_EXCLUDE_STATICLIBS = 

# The corresponding os/compiler to pass to the
# openssl Configure script
i386_OS_COMPILER 	= solaris-386-cc
pentium_OS_COMPILER	= solaris-pentium-cc
pentium_pro_OS_COMPILER	= solaris-pentium_pro-cc
amd64_OS_COMPILER 	= solaris64-x86_64-cc

sparcv8_OS_COMPILER 		= solaris-sparcv8-cc
sparcv8plus_OS_COMPILER		= solaris-sparcv9-cc
sparcv8plus+vis_OS_COMPILER	= solaris-sparcv9+vis-cc
sparcv9_OS_COMPILER		= solaris64-sparcv9-cc

CONFIGURE_ARGS = --prefix=$(prefix) shared $($(ISA)_OS_COMPILER) --install_prefix=$(DESTDIR)

# We want the csw perl to be used
#CONFIGURE_ENV += PERL="/opt/csw/bin/perl"
# For now we want the sun perl to be used
CONFIGURE_ENV += PERL="/usr/bin/perl"

# Some optimization
EXT_CFLAGS   += -mt -xstrconst
EXT_CXXFLAGS += -noex -mt

# By default, the install target put man pages under
# /opt/csw/ssl/man, but we want them under /opt/csw/share/man
INSTALL_ARGS += MANDIR=$(mandir)

# we include previous release of libraries file for comptability purpose
OLDLIBS                 = 0.9.7m

# support for pkcs11 engine http://blogs.sun.com/chichang1/entry/how_to_integrate_pkcs11_engine
ifdef PKCS11
	PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386
ifneq ($(shell /usr/bin/uname -r),5.9) 
	PATCHFILES += pkcs11_engine-0.9.8o.patch.2010-09-03
	CONFIGURE_ARGS += --pk11-libname=$(abspath /usr/lib/$(MM_LIBDIR)/libpkcs11.so) 
endif
endif 

TEST_SCRIPTS =

include gar/category.mk


pre-configure-modulated: 
	echo " ==> Creating configure script"
	cd $(WORKSRC) && ln -nf Configure configure
	@$(MAKECOOKIE)

# we remove every debug information except symbol table
# (should rather be done in the gar scripts)
post-install-modulated:
	echo " ==> Stripping libraries"
	chmod -R u+w $(DESTDIR)$(libdir)
	find $(DESTDIR)$(libdir) -name "*.so*" -exec strip -x '{}' ';'

install-changelog:
	for CATALOGNAME in $(foreach PKG, $(PACKAGES), $(call catalogname,$(PKG))); do \
		ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/$$CATALOGNAME/changelog.CSW; \
	done	
	@$(MAKECOOKIE)

install-doc:
	for CATALOGNAME in $(foreach PKG, $(PACKAGES), $(call catalogname,$(PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$CATALOGNAME; \
		(cd $(WORKSRC_FIRSTMOD)/ && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/$$CATALOGNAME/); \
		ginstall -D $(WORKDIR_FIRSTMOD)/README.CSW $(PKGROOT)/$(docdir)/$$CATALOGNAME/README.CSW; \
	done
	@$(MAKECOOKIE)

install-oldlibs: $(addprefix install-oldlibs-,$(OLDLIBS))
install-oldlibs-%:
	@echo " ==> Installing old libraries $* from archive oldlibs.$*-$(GARCH).tar.gz"
	cd $(PKGROOT) && gunzip -c $(CURDIR)/$(FILEDIR)/oldlibs.$*-$(GARCH).tar.gz | tar xvf -
	@$(MAKECOOKIE)

pre-oldlibs install-changelog install-doc
