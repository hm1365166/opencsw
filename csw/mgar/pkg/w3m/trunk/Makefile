NAME = w3m
VERSION = 0.5.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Text-based web browser
define BLURB
	w3m is a text-based web browser as well as a pager like `more' or `less'.
	With w3m you can browse web pages through a terminal emulator window (xterm,
	rxvt or something like that). Moreover, w3m can be used as a text formatting
	tool which typesets HTML into plain text.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://w3m.sourceforge.net/

RUNTIlibgc1 CSWlibssl1-0-0 CSWlibz1 CSWlibintl8 CSWperl CSWosslrt CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=39518
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAMCHECKPKG_OVERRIDES_CSWw3m += file-with-bad-content|/usr/local|root/opt/csw/libexec/w3m/cgi-bin/multipart.cgi
CHECKPKG_OVERRIDES_CSWw3m += file-with-bad-content|/usr/local|root/opt/csw/libexec/w3m/cgi-bin/w3mman2html.cgiAM_MASTER_SITES = 

#LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib -R/usr/openwin/lib
#export LD_OPTIONS

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gc=$(BUILD_PREFIX)
CONFIGURE_ARGS += ---enable-image=no_

TEST_TARGET = 

includ