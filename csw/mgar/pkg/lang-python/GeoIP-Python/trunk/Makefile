# $Id$

NAME = GeoIP-Python
VERSION = 1.2.7
CATEGORIES = python
GARTYPE = v2

MASTER_SITES = http://www.maxmind.com/download/geoip/api/python/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Remove-usr-local-references-from-setup.py-to-fix-emb.patch

VENDOR_URL = http://www.maxmind.com/app/python

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWgeoip-dev

PACKAGES = CSWpy-geoip
SPKG_DESC_CSWpy-geoip = Python GeoIP bindings
RUNTIME_DEP_PKGS_CSWpy-geoip += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-geoip += CSWlibgeoip1
RUNTIME_DEP_PKGS_CSWpy-geoip += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-geoip += CSWlibpython2-7-1-0
CHECKPKG_OVERRIDES_CSWpy-geoip += surplus-dependency|CSWpython

# The testsuite is complicated to run, skip for now
TEST_SCRIPTS =

STRIP_DIRS += $(DESTDIR)$(SITE_PACKAGES)

include gar/category.mk
