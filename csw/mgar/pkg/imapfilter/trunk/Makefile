NAME = imapfilter
VERSION = 2.5.2
GARTYPE = v2
CATEGORIES = net

PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

DESCRIPTION = IMAP mail filtering utility
define BLURB
  IMAPFilter is a mail filtering utility. It connects to remote mail servers
  using the Internet Message Access Protocol (IMAP), sends searching queries
  to the server and processes mailboxes based on the results. It can be used
  to delete, copy, move, flag, etc. messages residing in mailboxes at the same
  or different mail servers. The 4rev1 and 4 versions of the IMAP protocol are
  supported.
endef

MASTER_SITES = https://github.com/downloads/lefcha/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlua-dev
BUILD_DEP_PKGS += CSWlibpcre-dev

RUNTIME_DEP_PKGS_CSWimapfilter += CSWliblua5-2
RUNTIME_DEP_PKGS_CSWimapfilter += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWimapfilter += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWimapfilter += CSWlibiconv2

PATCHFILES += 0001-Bludgeon-the-build-system-to-do-what-we-need.patch

GARCOMPILER = GNU

EXTRA_LDFLAGS += -lsocket -liconv

CONFIGURE_SCRIPTS =
BUILD_ARGS = all

# No test suite
TEST_SCRIPTS =

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)
