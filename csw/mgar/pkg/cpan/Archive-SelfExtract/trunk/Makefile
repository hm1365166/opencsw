NAME = Archive-SelfExtract
VERSION = 1.3
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GREGFAST

DESCRIPTION = bundle compressed archives with Perl code
define BLURB
  Archive::SelfExtract allows you create Perl programs out of compressed zip
  archives. Given a piece of code and an archive, it creates a single file
  which, when run, unpacks the archive and then runs the code.
endef

DISTFILES = $(call admfiles,CSWpmarchivesfx,depend)

DEPENDS += cpan/Archive-Zip cpan/IO-stringy

# Archive-Zip bug
TEST_SCRIPTS =

include gar/category.mk
