NAME = ldns
VERSION = 1.6.17
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library for programs conforming to DNS RFCs and drafts
define BLURB
  Ldns is a library to simplify implementation of recent DNS RFCs. The goal
  is to allow depelopers to easily create software conforming to current RFCs
  and experimental software for current Internet drafts.
  Because ldns is written in C it should be a lot faster than Perl or other
  scripting languages.
endef

MASTER_SITES = http://www.nlnetlabs.nl/downloads/ldns/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWldns.doxyparse.diff

PACKAGING_PLATFORMS =  solaris10-sparc solaris10-i386

PACKAGES = CSWlibldn

SPKG_DESC_CSWlibldns1 = $(DESCRIPTION)
SPKG_DESC_CSWlibldns-dev = $(DESCRIPTION) development package

OBSOLETED_BY_CSWlibldns-dev += CSWlibldns-develvelopment package

SPKG_SOURCEURL = http://www.nlnetlabs.nl/projects/ldns/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://www.nlnetlabs.nl/downloads/ldns

LICENSE = LICENSE

BUILD64 = 1
EXTRA_BUILD_ISAS_sparc += sparcv8plus+vis

RUNTIME_DEP_PKGS_CSWlibldns1 += CSWlibssl1-0-0
RUNTIME_DEP_PK_CSWlibldns-devel += CSWlibldns1

INCOMPATIBLE_PKGS_CSWlibldns1 = CSWldns
INCOMPATIBLE_PKGS_CSWlibldns-devel# = CSWldnsdevel

PATCHFILES = CSWldns.doxyparse.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --enable-sha2

MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amd64 = $(libdir)

TEST_TARGET =

PKGFIL = $(PKGFILES_DEVEL)

include gar/category.mk
