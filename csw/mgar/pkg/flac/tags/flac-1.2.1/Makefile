NAME = libflac
VERSION = 1.2.1
CATEGORIES = lib
GARTYPE = v2

EXTRA_MODULATORS = VERSION
# Version 1.1.2 is the last to contain libflac.so.7 where most of the binaries depend on
MODULATIONS_VERSION = 1.0.4 1.1.2 1.2.1

# There was no 64 bit legacy version. Do not provide it as new binaries should
# link against the new version.
SKIP_MODULATIONS = isa-sparcv9-version-1.0.4
SKIP_MODULATIONS += isa-amd64-version-1.0.4
SKIP_MODULATIONS += isa-sparcv9-version-1.1.2
SKIP_MODULATIONS += isa-amd64-version-1.1.2

DESCRIPTION = Free lossless audio codec
define BLURB
  FLAC stands for Free Lossless Audio Codec, an audio format similar
  to MP3, but lossless, meaning that audio is compressed in FLAC without
  any loss in quality. This is similar to how Zip works, except with FLAC
  you will get much better compression because it is designed specifically
  for audio, and you can play back compressed FLAC files in your favorite
  player (or your car or home stereo, see supported devices) just like you
  would an MP3 filECTe.
endef

SF_PROJ = flac
MASTER_SITES = $(SF_MIRRORS)
DISECTTNAME = $(SF_PROJ)-$(VERSION)
SOURCEFILES = $(foreach VERSION,$(MODULATIONS_VECT)-$(VERSION).tar.gz)
DISTFILES = $(SOURCEFILES)

NOEXTRACT = $(filter-out $(SF_PROJECTter-out $(SF_PROJ)-$(VERSION).tar.gz,$(SOURCEFILES))

PATCHFILES_isa-sparcv8-version-1.1.2 = libtool-64bit.patch
PATCHFILES_isa-sparcv9-version-1.1.2 = libtool-64bit.patch
PATCHFILES_isa-sparcv8-version-1.2.1 = libtool-64bit.patch no-stdint.patch
PATCHFILES_isa-sparcv9-version-1.2.1 = libtool-64bit.patch no-stdint.patch

PATCHFILES_isa-i386-version-1.0.4 = strip-nasm-1.0.4.patch
PATCHFILES_isa-i386-version-1.1.2 = strip-nasm-1.1.2.patch libtool-64bit.patch
PATCHFILES_isa-amd64-version-1.1.2 = libtool-64bit.patch
PATCHFILES_isa-i386-version-1.2.1 = strip-nasm-1.2.1.patch libtool-64bit.patch no-stdint.patch
PATCHFILES_isa-amd64-version-1.2.1 = strip-nasm-1.2.1.patch libtool-64bit.patch no-stdint.patch

PACKAGES = CSWflac CSWxmmsflac
CATALOGNAME_CSWflac = libflac
CATALOGNAME_CSWxmmsflac = xmms_flac

BUILD_DEP_PKGS = CSWbash CSWnasm

RUNTIME_DEP_PKGS_CSWflac = CSWiconv CSWlibogg
RUNTIME_DEP_PKGS_CSWxmmsflac = CSWglib CSWgtk CSWxmms CSWflac CSWiconv CSWlibogg

SPKG_DESC_CSWflac = Free lossless audio codec
SPKG_DESC_CSWxmmsflac = FLAC plugin for XMMS

SPKG_SOURCEURL = http://flac.sourceforge.net/

LICENSE = $(foreach lic,FDL GPL LGPL Xiph,COPYING.$(lic))

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=13478
UPSTREAM_USE_SF = 1
UFILES_REGEX = flac-(\d+(?:\.\d+)*)-src

BUILD64 = 1

# For 1.0.4
EXTRA_LINKER_FLAGS = -liconv

NODIRPATHS = --includedir
CPPFLAGS =

# Must be defined and empty or -I$(includedir) is added too early
EXTRA_CFLAGS = -D__inline=
EXTRA_BUILD_EXPORTS = AM_CFLAGS

EXTRA_CONFIGURE_ARGS_mm-64 = --disable-xmms-plugin
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_mm-$(MEMORYMODEL))

# XXX: Assembler optimization just doesn't work. Disable for now.
CONFIGURE_ARGS += --disable-asm-optimizations

MERGE_SCRIPTS_isa-default-version-1.0.4 = copy-only
MERGE_DIRS_isa-default-version-1.0.4 = $(libdir)
MERGE_SCRIPTS_isa-extra-version-1.0.4 = copy-relocated-only
MERGE_DIRS_isa-extra-version-1.0.4 = $(libdir)

MERGE_SCRIPTS_isa-default-version-1.1.2 = copy-only
MERGE_DIRS_isa-default-version-1.1.2 = $(libdir)
MERGE_SCRIPTS_isa-extra-version-1.1.2 = copy-relocated-only
MERGE_DIRS_isa-extra-version-1.1.2 = $(libdir)

MERGE_SCRIPTS_isa-default-version-1.2.1 = copy-all
MERGE_SCRIPTS_isa-extra-version-1.2.1 = copy-relocated-only
MERGE_DIRS_isa-extra-version-1.2.1 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

PKGFILES_CSWxmmsflac = $(libdir)/xmms/.*

include gar/category.mk

CC := $(abspath ./bin/cc)
CXX := $(abspath ./bin/CC)
PATH := ./bin:$(PATH):/usr/ccs/bin

post-patch-isa-i386-version-1.0.4:
	perl -pi -e "s/-O3 //g" $(WORKSRC)/configure
	$(MAKECOOKIE)

post-patch-isa-i386-version-1.1.2:
	perl -pi -e "s/-O2 //g" $(WORKSRC)/configure
	$(MAKECOOKIE)

post-patch-isa-sparcv8-version-1.0.4:
	perl -pi -e "s/-O3 //g" $(WORKSRC)/configure
	$(MAKECOOKIE)

post-patch-isa-sparcv8-version-1.1.2:
	perl -pi -e "s/-O2 //g" $(WORKSRC)/configur