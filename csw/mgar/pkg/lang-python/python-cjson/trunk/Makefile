# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = python-cjson
VERSION = 1.0.3x7
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Very fast JSON encoder/decoder
define BLURB
	This project is the python equivalent of google-gflags, a Google commandline
	flag implementation for C++. It is intended to be used in situations where a
	project wants to mimic the command-line flag handling of a C++ app that uses
	google-gflags, or for a Python app that, via swig or some other means, is
	linked with a C++ app that uses google-gflags.
endef
VENDOR_URL = http://python.cx.hu/python-cjson/
MASTER_SITES = http://python.cx.hu/python-cjson/
DISTFILES  = $(DISTNAME).tar.gz
TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWpy-cjson += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-cjson += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-cjson += CSWlibpython2-7-1-0

CHECKPKG_OVERRIDES_CSWpy-cjson += python-package-missing-py-files

PACKAGES = CSWpy-cjson
include gar/category.mk
