GARNAME = xmlstarlet
GARVERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = XML transformation utility
define BLURB
  XMLStarlet is a set of command line utilities (tools)
  to transform, query, validate, and edit XML documents
  and files using simple set of shell commands in similar
  way it is done for text files with UNIX grep, sed, awk,
  diff, patch, join, etc utilities.
endef

SF_PROJ = xmlstar
MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

RUNTIME_DEP_PKGS = CSWgcrypt CSWggettextrt CSWgpgerr CSWiconv CSWlibxml2 CSWlibxslt CSWzlib   

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=66612
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = $(GARNAME)-$(GARVERSION)-cc.patch

BUILD64 = 1

TEST_TARGET = check

include gar/category.mk

CONFIGURE_ENV += LIBXML_PREFIX=$(prefix)
CONFIGURE_ENV += LIBXML_CFLAGS="$(shell $(bindir)/xml2-config --cflags)"
CONFIGURE_ENV += LIBXML_LIBS="$(shell $(bindir)/xml2-config --libs)"
CONFIGURE_ENV += LIBXSLT_PREFIX=$(prefix)
CONFIGURE_ENV += LIBXSLT_CFLAGS="$(shell $(bindir)/xslt-config --cflags)"
CONFIGURE_ENV += LIBXSLT_LIBS="$(shell $(bindir)/xslt-config --libs) -lexslt"

CONFIGURE_ARGS = $(DIRPATHS)

post-install-modulated:
	@echo " ==> Renaming program to xmlstarlet"
	@mv $(DESTDIR)$(bindir)/xml $(DESTDIR)$(bindir)/xmlstarlet
	@$(MAKECOOKIE)
