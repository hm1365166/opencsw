NAME = libpthread-stubs
VERSION = 0.3
CATEGORIES = x11

DESCRIPTION = pthread stubs not provided by native libc
define BLURB
This library provides weak aliases for pthread functions not provided in libc or otherwise available by default. Libraries like libxcb rely on pthread stubs to use pthreads optionally, becoming thread-safe when linked to libpthread, while avoiding any performance hit when running single-threaded. libpthread-stubs supports this behavior even on platforms which do not supply all the necessary pthread stubs. On platforms which already supply all the necessary pthread stubs, this package has no content. 
endef

MASTER_SITES = $(XCB_MASTER_SITES)
DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWlibpthreadstubs

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWx11common

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

