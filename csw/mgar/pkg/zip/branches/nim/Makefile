# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = zip
VERSION = 3.0
ZIPVERSION = $(subst .,,$(VERSION))
GARTYPE = bts
CATEGORIES = utils

DESCRIPTION = Info-Zip Zip compression and file packaging/archive utility 
define BLURB
 Info-Zip Zip compression and file packaging/archive utility 
endef

SPKG_SOURCEURL = http://www.info-zip.org/

SF_PROJECT = infozip
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)$(UNZIPVERSION)
DISTFILES  #= $(DISTNAME).tgz

NIMOSSTIME_DEP_PKGS = CSWlibbz2-1-0
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)

# zip's configure is... "special". We use a custom version
CONFIGURE_SCRIPTS = 

# Further, nothing respects our LDFLAGS, so we have to set
# those specifically:
BUILD_ARGS = -f unix/Makefile LOCAL_ZIP="$(CFLAGS)" BIND="$(CC) $(LDFLAGS)"  generic
INSTALL_ARGS = -f unix/Makefile INSTALL=ginstall BINDIR=$(DESTDIR)$(bindir) MANDIR=$(DESTDIR)$(mandir)/man1 install

BUILD64 = 1
ISAEXEC = 1

LICENSE = LICENSE

# There is no test suite
TEST_SCRIPTS = 

includ