# $Id: Makefile 14849 2011-06-21 09:07:58Z skayser $
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Remove /usr references in $(docdir) and drop overrides
# ! Determine how to run the integrated test suite (iptest/nose) and run it
# ! Package contains ipythonx which doesn't work w/o wxpython (can we skip
#   shipping ipythonx?)
# 
NAME    = ipython
VERSION = 1.1.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Enhanced interactive python shell
define BLURB
  IPython is a replacement for the standard Python shell.
endef
LICENSE = COPYING.txt

MASTER_SITES = http://archive.ipython.org/release/$(VERSION)/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
ARCHALL      = 1
PACKAGES     = CSWipython
CATALOGNAME  = ipython

EXTRA_MERGE_EXCLUDE_FILES = .*\.gitignore

CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/IPython/utils/tests/test_path.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/IPython/external/path/_path.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/IPython/external/pexpect/_pexpect.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/IPython/core/magics/osm.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/IPython/core/usage.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/IPython/external/path/_path.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/IPython/external/pexpect/_pexpect.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/IPython/utils/tests/test_path.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/IPython/core/magics/osm.py
CHECKPKG_OVERRIDES_CSWipython += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/IPython/core/usage.py
CHECKPKG_OVERRIDES_CSWipython += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWipython += catalogname-does-not-start-with-py_

SKIPTEST = 1

include gar/category.mk

post-build-modulated:
	@gsed -i '1 s/$(subst _,.,$(PYTHON_VERSION))//' $(WORKSRC)/build/scripts-$(subst _,.,$(PYTHON_VERSION))/*
	@$(MAKECOOKIE)

