NAME = mm
VERSION = 1.4.2
GARTYPE = v1
CATEGORIES = lib

DESCRIPTION = Shared Memory Allocation abstraction library.
define BLURB
  OSSP mm is a 2-layer abstraction library which simplifies the usage of
  shared memory between forked (and this way strongly related) processes under
  Unix platforms. On the first layer it hides all platform dependent
  implementation details (allocation and locking) when dealing with shared
  memory segments and on the second layer it provides a high-level
  malloc(3)-style API for a convenient and well known way to work with data
  structures inside those shared memory segments.
endef

MASTER_SITES = ftp://ftp.ossp.org/pkg/lib/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibmm,prototype)
DISTFILES += libmm.so.13.0.20.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

include gar/category.mk
