NAME      = py2cairo
VERSION   = 1.10.0
GARTYPE = v2
# CATEGORIES   = python

DESCRIPTION  = Python binding for Cairo library for Python2
define BLURB
  This package contains the pycairo Python module which implements
  a binding the the cairo Library.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
# DISTFILES     = pycairo-$(VERSION).tar.bz2 
DISTFILES     = $(DISTNAME).tar.bz2

LICENSE = COPYING

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 

EXTRA_MODULATORS += PYTHON_VERSION
MODULATIONS_PYTHON_VERSION = 2.6 2.7
# We need 64 bit just once as it is without python anyway
SKIP_MODULATIONS += isa-sparcv9-python_version-2.7
SKIP_MODULATIONS += isa-amd64-python_version-2.7
PYTHON = $(bindir)/python$(PYTHON_VERSION)
MERGE_SCRIPTS_isa-default-python_version-2.6 += copy-all
MERGE_SCRIPTS_isa-default-python_version-2.7 += copy-all
MERGE_SCRIPTS_isa-default64-python_version-2.6 += copy-relocated-only
MERGE_DIRS_isa-default64-python_version-2.6 += $(libdir)

PACKAGES = CSWpy-cairo
SPKG_DESC_CSWpy-cairo = $(DESCRIPTION); main
OBSOLETED_BY_CSWpy-cairo = CSWpycairo
RUNTIME_DEP_PKGS_CSWpy-cairo += CSWpython
RUNTIME_DEP_PKGS_CSWpy-cairo += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpy-cairo += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWpy-cairo += surplus-dependency|CSWpython

GARCOMPILER = GCC4

CAIRO_LIBS = -L/opt/csw/lib -R/opt/csw/lib/\$$ISALIST -lcairo
CAIRO_CFLAGS = -I/opt/csw/include -I/opt/csw/include/cairo
EXTRA_CONFIGURE_EXPORTS += CAIRO_LIBS CAIRO_CFLAGS

EXTRA_CONFIGURE_ENV = PYTHON=python$(PYTHON_VERSION)

EXTRA_CFLAGS = -D_XPG6
SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure:
	cd $(WORKSRC) && python -c "import sys; print sys.prefix" && \
	touch ChangeLog && \
	autoreconf --force --install 
	$(MAKECOOKIE)
