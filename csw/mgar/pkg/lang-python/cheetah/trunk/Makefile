# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = Cheetah
VERSION = 2.4.4
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = A template engine and code generation tool
define BLURB
  Cheetah is an open source template engine and code generation tool, written
  in Python. It can be used standalone or combined with other tools and
  frameworks. Web development is its principle use, but Cheetah is very
  flexible and is also being used to generate C++ game code, Java, sql, form
  emails and even Python code.
endef
SPKG_SOURCEURL = http://www.cheetahtemplate.org/
DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
PACKAGES = CSWpy-cheetah
RUNTIME_DEP_PKGS_CSWpy-cheetah += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-cheetah += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-cheetah += CSWlibpython2-7-1-0
include gar/category.mk
