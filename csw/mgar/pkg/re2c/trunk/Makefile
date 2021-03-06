NAME = re2c
VERSION = 0.13.5
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Utility for writing fast and flexible scanners.
define BLURB
   re2c is a tool for writing very fast and very flexible scanners. 
   Unlike any other such tool, re2c focuses on generating high efficient 
   code for regular expression matching. As a result this allows a much 
   broader range of use than any traditional lexer offers. 
   And Last but not least re2c generates warning free code that is equal 
   to hand-written code in terms of size, speed and quality. 
endef

PACKAGES = CSWre2c

MASTER_SITES = $(SF_MIRRORS)
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES = $(DISTNAME).tar.gz
CATALOGNAME_CSWre2c = re2c
SPKG_DESC_CSWre2c = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWre2c += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWre2c += CSWlibstdc++6
CHECKPKG_OVERRIDES_CSWre2c += license-missing|/opt/csw/share/doc/re2c/license

# Compiling with GNU based on upstream bug-id
# [ 2535084 ] re2c 0.13.5 not compile with Sun C
GARCOMPILER = GNU
PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk

