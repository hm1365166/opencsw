NAME = qucs
VERSION = 0.0.15
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = Integrated circuit simulator
#define BLURB
#  Long descriptECTion
#endef

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES  = 0000-Missing-include.patch
PATCHFILES += 0001-Replace-bin-sh-with-bin-bash.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

GARCOMPILER = GNU

CONFIGURE_ENV  = QTDIR=/opt/csw
CONFIGURE_ENV += LD_LIBRARY_PATH=/opt/csw/gcc4/lib
CONFIGURE_ENV += LDFLAGS="-L/opt/csw/kde-gcc/lib -L/opt/csw/gcc4/lib"
#  -lstdc++"
CONFIGURE_ENV := $(CONFIGURE_ENV)
#LD_LIBRARY_PATH=/opt/csw/gcc4/lib QTDIR=/opt/csw CC=/opt/csw/gcc4/bin/gcc LDFLAGS="-L/opt/csw/kde-gcc/lib/ -lstdc++" CFLAGS="-I/opt/csw/kde-gcc/include -I/opt/csw/include"
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

inclu