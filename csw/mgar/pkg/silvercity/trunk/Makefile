NAME = SilverCity
VERSION = 0.9.7
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Lexical analysis package for Python
define BLURB
	SilverCity is a lexing package, based on Scintilla, that can provide lexical
	analysis for over 20 programming and markup langauECTges.
endef

SF_PROJ = $(call TOLOWER,$(NAME))
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PACKAGES = CSWsilvercity

RUNTIME_DEP_PKGS_CSWsilvercity = CSWpython-rt
CATALOGNAME_CSWsilvercity = silvercity
SPKG_DESC_CSWsilvercity = Lexical analysis package for Python

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
RUNTIME_DEP_PKGS += CSWcswclassutils


NOISALIST = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

GARCOMPILER = SUN

include gar/category.mk

# When you pass a C++ source file to gcc, it invokes g++ for you
# without complaints.  However, passing a C++ source file to cc just
# results in an error.  So we fool python into using CC instead.
CC = $(CXX)
CF