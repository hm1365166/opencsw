# $Id$
# TODO
# - Move this to a pymodules/ subdirectory with the rest of the
#   python modules (similar to the cpan directory).
NAME = lxml
VERSION = 3.2.3
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Easy to use and powerful libxml2/libxslt binding for Python
define BLURB
  lxml is a Pythonic binding for the libxml2 and libxslt libraries. It is
  unique in that it combines the speed and feature completeness of these
  libraries with the simplicity of a native Python API, mostly compatible
  but superior to the well-known ElementTree API.
endef

VENDOR_URL   = http://lxml.de/
DISTNAME     = lxml-$(VERSION)
DISTFILES    = $(DISTNAME).tar.gz

# See http://codespeak.net/lxml/index.html#license
LICENSE = doc/licenses/BSD.txt

BUILD_DEP_PKGS	+=	CSWpython-dev
BUILD_DEP_PKGS	+=	CSWpython27-dev
BUILD_DEP_PKGS	+=	CSWlibxml2-dev
BUILD_DEP_PKGS	+=	CSWlibxslt-dev

PACKAGES = CSWpy-lxml
SPKG_DESC_CSWpy-lxml = Easy to use and powerful libxml2/libxslt binding for Python
RUNTIME_DEP_PKGS_CSWpy-lxml += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-lxml += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWpy-lxml += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-lxml += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-lxml += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWpy-lxml += CSWlibxml2-2

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated: DOCS=CHANGES.txt CREDITS.txt
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	@$(MAKECOOKIE)
