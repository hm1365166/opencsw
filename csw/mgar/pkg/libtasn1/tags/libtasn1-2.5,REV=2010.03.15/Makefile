GARNAME = libtasn1
GARVERSION = 2.5
CATEGORIES = lib

DESCRIPTION = GNU ASN1 library
define BLURB
  Libtasn1 is the ASN.1 library used by GnuTLS, GNU Shishi and some other packages.
  It was written by Fabio Fiorina, and has been shipped as part of GnuTLS for some
  time but is now a proper GNU package.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWlibtasn1 CSWlibtasn1devel

CATALOGNAME_CSWlibtasn1 = libtasn1
CATALOGNAME_CSWlibtasn1devel = libtasn1_devel

SPKG_DESC_CSWlibtasn1 = $(DESCRIPTION)
SPKG_DESC_CSWlibtasn1devel = Development files for libtasn1

RUNTIME_DEP_PKGS_CSWlibtasn1devel = CSWlibtasn1

SPKG_SOURCEURL = http://www.gnu.org/software/gnutls/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

PKGFILES_CSWlibtasn1devel = $(PKGFILES_DEVEL)

include gar/category.mk

