NAME = poppler-data
VERSION = 0.4.6
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Poppler is a PDF rendering library based on the xpdf-3.0 code base
define BLURB
endef

PACKAGES = CSWpoppler-data
CATALOGNAME_CSWpoppler-data = poppler_data
SPKG_DESC_CSWpoppler-data = $(DESCRIPTION), encoding data
OBSOLETED_BY_CSWpoppler-data = CSWpopplerdata
CATALOGNAME_CSWpopplerdata = poppler_data_stub

MASTER_SITES = http://poppler.freedesktop.org/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# UPSTREAM_MASTER_SITES = 

ARCHALL = 1

SPKG_SOURCEURL = http://poppler.freedesktop.org/

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_ARGS = "prefix=$(prefix)"

include gar/category.mk

PATH := /opt