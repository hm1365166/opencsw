# TBD:

NAME = lsof
VERSION = 4.88
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = List open files
define BLURB
  Lsof is a Unix-specific diagnostic tool. Its name stands for LiSt Open Files,
  and it does just that. It lists information about any files that are open by
  processes currently running on the system. It can also list communications
  open by each process.
endef

MASTER_SITES += ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof/
MASTER_SITES += ftp://lsof.itap.purdue.edu/pub/tools/unix/lsof/NEW/
DISTNAME = $(NAME)_$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += lsof-license

# Do not automatically use VxFS
# PATCHFILES += 0002-Disable-VxFS-autodetect.patch

SRCDIST = $(DISTNAME)_src
WORKSRC   = $(WORKDIR)/$(DISTNAME)/$(SRCDIST)

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386

VENDOR_URL = http://people.freebsd.org/~abe/
LICENSEThis is because we build Solaris 9 Sparc on a branded zone
CHECKPKG_OVERRIDES_CSWlsof += soname-unused|s9_preload.so.1|is|needed|by|/opt/csw/bin/sparcv9/lsof|but|never|used
CHECKPKG_OVERRIDES_CSWlsof += soname-unused|s9_preload.so.1|is|needed|by|/opt/csw/bin/sparcv8plus/lsof|but|never|used
CHECKPKG_OVERRIDES_CSWlsof += soname-unused|s9_preload.so.1|is|needed|by|/opt/csw/bin/sparcv8/lsof|but|never|usedENSE = lsof-license

# Do not build a unified 32/64 bit package for Solaris 9 i386
BUILD64-sparc-5.9 = 1
BUILD64-sparc-5.10 = 1
BUILD64-i386-5.10 = 1
BUILD64-sparc-5.11 = 1
BUILD64-i386-5.11 = 1
BUILD64 = $(BUILD64-$(GAGARCOMPILER-5.9 = SOS12
GARCOMPILER-5.10 = SOS12U3
GARCOMPILER-5.11 = SOS12U3
GARCOMPILER = $(GARCOMPILER $(BUILD64-$(GARCH)-$(GAROSREL))

EXTRA_BUILD_ISAS = sparcv8plus

ISAEXEC = 1

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS    = -n solariscc

# Environment variables affecting Solaris builds:
#   SOLARIS_23P101318     If this environment variable has a non-NULL value, the
#   SOLARIS_24P101945     If this environment variable has a non-NULL value, the
#   SOLARIS_24P102303     If this environment variable has a non-NULL value, the
#   SOLARIS_26PR_GWINDOWS If this environment variable has a value of "Y" or "y",
#   SOLARIS_26PR_LDT      If this environment variable has a value of "Y" or "y",
#   SOLARIS_CCDIR         specifies the path to the Sun C compiler -- i.e., when
#   SOLARIS_INSTR         specifies the Sun C compiler target instruction set
#   SOLARIS_KERNBITS      specifies the number of bits in the Solaris 7, 8, 9 or
#   SOLARIS_VSOCK         If this environment variable has a value of "Y" or "y",
#   SOLARIS_VXFSINCL      This environment variable defines the path to the
#   SOLARIS_VXFSLIB       This environment variable defines the path to the

CONFIGURE_EXPORTS = LSOF_CFGF SOLARIS_CCDIR SOLARIS_INSTR SOLARIS_KERNBITS SOLARIS_VXFSINCL SOLARIS_VXFSLIB
SOLARIS_CCDIR = $(CC_HOME)/bin
SOLARIS_INSTR = $(ISA)
SOLARIS_KERNBITS = $(MEMORYMODEL)

# No VxFS for Solaris 11 yet
BUILD_DEP_PKGS-5.9 += VRTSfssdk
BUILD_DEP_PKGS-5.10 += VRTSfssdk
BUILD_DEP_PKGS += $(BUILD_DEP_PKGS-$(GAROSREL))

# The Veritas Filesystem library libvxfsutil.a is sparcv8+, make sure to build that
# specific ISA and not link when building sparcv8
SOLARIS_VXFSINCL-sparcv8plus = /opt/VRTS/include
SOLARIS_VXFSINCL-sparcv9     = /opt/VRTS/include
SOLARIS_VXFSINCL-i386        = /opt/VRTS/include
SOLARIS_VXFSINCL-pentium_pro = /opt/VRTS/include
SOLARIS_VXFSINCL-amd64       = /opt/VRTS/include
SOLARIS_VXFSLIB-sparcv8plus = /opt/VRTS/lib
SOLARIS_VXFSLIB-sparcv9     = /opt/VRTS/lib
SOLARIS_VXFSLIB-i386        = /opt/VRTS/lib
SOLARIS_VXFSLIB-pentium_pro = /opt/VRTS/lib
SOLARIS_VXFSLIB-amd64       = /opt/VRTS/lib
SOLARIS_VXFSINCL = $(SOLARIS_VXFSINCL-$(ISA))
SOLARIS_VXFSLIB = $(SOLARIS_VXFSLIB-$(ISA))

TEST_SCRIPTS = custom

# Tests require root
SKIPTEST ?= 1

INSTALL_SCRIPTS = custom

BUILD_OVERRIDE_VARS = CDEF
BUILD_OVERRIDE_VAR_CDEF = $(CFLAGS)

PROTOTYPE_MODIFIERS = lsof
PROTOTYPE_FILES_lsof = $(call baseisadirs,$(bindir),lsof)
PROTOTYPE_GROUP_lsof = sys
PROTOTYPE_PERMS_lsof = 2755

# This is because the vxfs sdk contains sparcv8+
CHECKPKG_OVERRIDES_CSWlsof += binary-architecture-does-not-match-placement|file=opt/csw/bin/sparcv8/lsof|arch_id=18|arch_name=sparcv8+

include gar/category.mk

INSTALLISADIR ?= $(WORKROOTDIR)/install-$(MODULATION)

post-extract-modulated:
	@echo " ==> Extracting source distribution"
	@$(if $(filter-out global,$(MODULATION)),( cd $(WORKDIR)/$(DISTNAME) ; gtar xf $(SRCDIST).tar ))
	@$(MAKECOOKIE)

configure-custom:
	@echo " ==> Configuring in $(WORKSRC)"
	( cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing in $(WORKSRC)/tests"
	$(MAKE) -C $(WORKSRC)/tests
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) $(VERSION) fginstall -D -m 755 $(WORKSRC)/lsof $(DESTDIR)$(bindir)/lsof
	ginstall -D -m 444 $(WORKSRC)/lsof.8 $(DESTDIR)$(mandir)/man8/lsof.8
	@$(MAKECOOKIE)
