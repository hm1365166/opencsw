NAME = tofrodos
VERSION = 1.7.13
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Text file utility that converts files between MSDOS and Unix format.
define BLURB
It is a useful utility to have around when you have to convert files between 
MSDOS (or Windows) and Unix/Linux/BSD (and her clones and variants). It comes 
standard with a number of systems and is often found on the system as "todos", 
"fromdos", "dos2unix" and "unix2dos".
endef

WORKSRC ?= $(WORKDIR)/$(NAME)/src
MASTER_SITES = http://tofrodos.sourcefVENDOR_URL = http://www.thefreecountry.com/tofrodos/
DISTFILES  = $(NAME)-$(VERSIONAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the valUPSTREAM_MASTER_SITES = http://www.thefreecountry.com/tofrodos/
UFILES_REGEX = Version\s(\d+(?:\.\d+)*)

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
LAGS="$(CFLAGS) -c"
BUILD_ARGS = CC=$(CC) LD=$(CC) MAKE=$(MAKE) CDEBUG= CFLAGS="$(CFLAGS) -c -Dstricmp=strcasecmp"

TEST_SCRIPTS =

INSTALL_ARGS = BINDIR=$(DESTDIR)$(bindir) MANDIR=$(DESTDIR)$(mandir)/man1 INSTALL=$include gar/category.mk=$(bindir)/ginstall

pre-install-modulated:
	@echo "Creating directories"
	mkdir -p $(DESTDIR)$(bindir)
	mkdir -p $(DESTDIR)$(mandir)/man1

post-install-modulated:
	@echo "Creating links"
	ln -s ./fromdos $(DESTDIR)$(bindir)/dos2unix
	ln -s ./fromdos $(DESTDIR)$(bindir)/unix2dos
	ln -s ./fromdos.1 $(DESTDIR)$(mandir)/man1/dos2unix
	ln -s ./fromdos.1 $(DESTDIR)$(man