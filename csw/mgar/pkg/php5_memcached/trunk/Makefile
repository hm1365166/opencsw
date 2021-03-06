# $Id$
#
NAME = memcached
VERSION = 2.1.0
GARTYPE = v2

# to match php5
PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

DESCRIPTION = memcached Extention for PHP
define BLURB
   This extension uses libmemcached library to provide API for communicating with memcached servers.
endef

PHP_PREFIX = $(prefix)/php5
PHP_BIN = $(PHP_PREFIX)/bin

PHP5_EXT = 1

PHP5ROOT    = $(DESTDIR)/$(PHP_PREFIX)
STRIP_DIRS += $(PHP5ROOT)/lib/php/extensions/*/
STRIP_DIRS += $(PHP5ROOT)/bin

VENDOR_URL = http://us.php.net/memcached/
MASTER_SITES = http://pecl.php.net/get/

DISTFILES = $(DISTNAME).tgz
PATCHFILES += 0001-Use-proper-libmemcached-headers-dir.patch
PATCHFILES += 0002-Include-proper-memcached.h.patch

GARCOMPILER = GNU

PACKAGES = CSWphp5-memcached
CATALOG_NAME_CSWphp5memcached = php5_memcached_stub
SPKG_DESC_CSWphp5-memcached =  Extension memcached for PHP5
RUNTIME_DEP_PKGS_CSWphp5-memcached = CSWphp5
BUILD_DEPS_CSWphp5-memcached = CSWapache2 CSWphp5-dev
RUNTIME_DEP_PKGS_CSWphp5-memcached += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWphp5-memcached += CSWlibmemcached8
RUNTIME_DEP_PKGS_CSWphp5-memcached += CSWlibz1

OBSOLETED_BY_CSWphp5-memcached = CSWphp5memcached
ARCHALL_CSWphp5memcached =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-php-config=$(bindir)/php-config
CONFIGURE_ARGS += --enable-memcached=shared
CONFIGURE_ARGS += --with-libmemcached-dir=shared,$(prefix)
CONFIGURE_ARGS += --enable-memcached-json

LICENSE = LICENSE

# These should stop the test suite from asking to send results by
# mail.
NO_INTERACTION = 1
EXTRA_TEST_EXPORTS = NO_INTERACTION

# this thing doesn't use destdir.  export install_root with the same
# value
INSTALL_ROOT = $(DESTDIR)
EXTRA_INSTALL_EXPORTS = INSTALL_ROOT

TEST_TARGET = test

include gar/category.mk

post-extract-isa-$(ISA_DEFAULT_$(GARCH)):
	@( cd $(WORKSRC) ; $(PHP_BIN)/phpize )
	@$(MAKECOOKIE)
