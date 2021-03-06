NAME = irssi
VERSION = 0.8.17
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = IRC client with IPv6, proxy, bot, socks and Perl support
define BLURB
	Irssi is a modular IRC client that currently has only text mode user
	interface, but 80-90% of the code isn't text mode specific, so other UIs
	could be created pretty easily. Also, Irssi isn't really even IRC
	specific anymore, there's already a working SILC module available.
	Support for other protocols like ICQ could be created some day too.
endef

VENDOR_URL   = http://www.irssi.org/
MASTER_SITES = http://www.irssi.org/files/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

SAMPLECONF = .*/irssi.conf

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-socks
CONFIGURE_ARGS += --with-bot
CONFIGURE_ARGS += --with-proxy
CONFIGURE_ARGS += --with-perl=yes
CONFIGURE_ARGS += --with-perl-lib=vendor
CONFIGURE_ARGS += --with-ncurses=$(prefix)

EXTRA_LIB += $(prefix)/bdb47/lib
EXTRA_INC += $(prefix)/bdb47/include

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

RUNTIME_DEP_PKGS += CSWlibsocks
RUNTIME_DEP_PKGS += CSWlibssl1-0-0
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWlibglib2-0-0
RUNTIME_DEP_PKGS += CRUNTIME_DEP_PKGS += $(RUNTIME_DEP_PKGS_$(GARCH))

RUNTIME_DEP_PKGS_sparc += CSWlibintl8CSWlibgmodule2-0-0

REINPLACE_USRLOCAL += docs/perl.txt
REINPLACE_USRLOCAL += docs/help/load

REINPLACE_USRSHARE += docs/irssi.1

includ