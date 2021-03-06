NAME = libsmi
VERSION = 0.5.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Allows management applications to access SMI MIB module definitions
define BLURB
  The core of the libsmi distribution is a library that allows management applications
  to access SMI MIB module definitions. On top of this library, there are tools to check,
  analyze dump, convert, and compare MIB definitions. Finally, the distribution contains
  a steadily maintained and revised archive of all IETF and IANA maintained standard MIB
  and PIB modules.
end+= http://www.ibr.cs.tu-bs.de/projects/libsmi/download/
DISTFILES +bsmi/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.ibr.cs.tu-bs.de/projects/libsmi/

PACKAGES += CSWlibsmi2
SPKG_DESC_CSWlibsmi2 = Library to access SMI MIB module definitions, libsmi.so.2
PKGFILES_CSWlibsmi2 = $(call pkgfiles_smi2 = CSWlibsmi

PACKAGES += CSWlibsmi-dev
SPKG_DESC_CSWlibsmi-dev = Development files for libsmi.so.2
PKGFILES_CSWlibsmi-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsmi-dev = CSWlibsmi2

PACKAGES += CSWlibsmi-utils
SPKG_DESC_CSWlibsmi-utils = Utility programs to access MIBs
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibsmi-utils += CSWlibsmi2
RUNTIME_DEP_PKGS_CSWlibsmi-utils += CSWlibsmi-mibs
CHECKPKG_OVERRIDES_CSWlibsmi-utils += surplus-dependency|CSWlibsmi-mibs

PACKAGES += CSWlibsmi-mibs 
SPKG_DESC_CSWlibsmi-mibs = SMI MIB definitions
PKGFILES_CSWlibsmi-mibs = $(sharedstatedir)/mibs/.*
PKGFILES_CSWlibsmi-mibs += $(sharedstatedir)/pibs/.*
ARCHALL_CS
BUILD64_LIBS_ONLY = 1FLAGS_isa-$(ISA))

# Some tests fail, however, these are only whitespace and newline differenceinclude gar/category.mk
