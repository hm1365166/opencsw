NAME = dnstracer
VERSION = 1.9
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Trace a chain of DNS servers to the source
define BLURB
  Dnstracer determines where a given Domain Name Server (DNS) gets its
  information from, and follows the chain of DNS servers back to the
  servers which know the data.
endef

MASTER_SITES = http://www.mavetju.org/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

SPKG_SOURCEURL = http://www.mavetju.org/unix/general.php

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-ipv6

EXTRA_LDFLAGS = -lresolv

include gar/category.mk
