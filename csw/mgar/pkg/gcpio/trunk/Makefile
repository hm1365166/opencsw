NAME = cpio
VERSION = 2.10
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GNU cpio
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# From http://bugs.gentoo.org/275295
PATCHFILES = non-gnu-compiler.patch
PATCHDIRLEVEL = 0

PACKAGES = CSWgcpio

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/cpio/

DEP_PKGS = CSWggettextrt

EXTRA_LINKER_FLAGS = -lnsl

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(prefix)/gnu
	gln -s ../bin/gcpio $(PKGROOT)$(prefix)/gnu/cpio
	@$(MAKECOOKIE)
