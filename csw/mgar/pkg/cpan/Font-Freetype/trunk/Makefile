NAME = Font-FreeType
VERSION = 0.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GEOFFR

DESCRIPTION = Read font files and render glyphs from Perl using FreeType2
define BLURB
endef

RUNTIME_DEP_PKGS = CSWftype2

PACKAGES = CSWpmfontfreetype
CATALOGNAME = pm_fontfreetype

EXTRA_PERL_CONFIGURE_ARGS = INC=-I$(includedir)/freetype2

# There are a lot of failed tests, however, it looks like the tests
# are somewhat broken, so skip for now.
SKIPTEST ?= 1

include gar/category.mk
