# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pexpect
VERSION = 2.3
PACKAGES = CSWpy-pexpect
CATALOGNAME_CSWpy-pexpect = py_pexpect
ARCHALL_CSWpy-pexpect = 1
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = A module for spawning child processes and interacting with them
define BLURB
endef
SPKG_SOURCEURL = http://www.noah.org/wiki/Pexpect
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = LICENSE
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
CHECKPKG_OVERRIDES_CSWpy-pexpect += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/pexpect.py
CHECKPKG_OVERRIDES_CSWpy-pexpect += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/pexpect.py
include gar/category.mk
