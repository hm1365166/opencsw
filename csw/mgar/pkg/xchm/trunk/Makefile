NAME = xchm
VERSION = 1.20
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Cross-platform GUI front-end to chmlib (.chm reader)
define BLURB
  xCHM is a cross-platform GUI front-end to chmlib, with borrowed bits from Pabs' chmdeco project.
  xCHM can show the content tree if one is available, print pages, change font face and size,
  remember bookmarks, display a searchable index, and search for words in the current page and the whole book.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES  = 0001-Fix-extra-comma-at-end-of-enum.patch
PATCHFILES += 0002-Remove-W-Wall-fo#r-Sun-Studio.patch
PATCHFILES += 0003-Use-inttypes-instead-of-stdint.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(BUILD_DEP_PKGS += CSWwxwidgets-dev
BUILD_DEP_PKGS += CSWlibncurses-dev+BUILD_DEP_PKGS += CSWlibchm-dev+(?:\.\d+)*).tar.gz

RUNTIM+= CSWlibchm0
RUNTIME_DEP_PKGS_CSWxchm += CSWwxwidgets
RUNTIME_DEP_PKGS_CSWxchm += CSWwxwidgetsgtk2

EXTRA_CFLAGS = -xnorunpath
EXTRA_CXXFLAGS = -norunpath

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
