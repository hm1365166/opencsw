NAME    = mcabber
VERSION = 0.9.9
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A small terminal-based Jabber client
define BLURB
mcabber is a small Jabber console client.  mcabber includes features such as
SSL support, MUC (Multi-User Chat) support, history logging, command
completion, OpenPGP encryption, OTR (Off-the-Record Messaging) support and
external action triggers.
endef

MASTER_SITES = http://www.lilotux.net/~mikael/mcabber/files/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
SPKG_SOURCEURL = http://www.lilotux.net# Please note: CSWotr-dev at this point refers to a more recent version
# than mcabber 0.9 supports.
# It will be needed to upgrade it to 0.10
BUILD_DEP_PKGS = CSWlibncurses-dev CSWlibssl-dev CSWotr-dev
BUILD_DEP_PKGS += CSWaspell CSWggettext CSWlibglib2-dev CSWpkgconfig
BUILD_DEP_PKGS += CSWlibgpg-error-dev CSWgpgme CSWlibiconv-dev

RUNTIME_DEP_PKGS = CSWlibncursesw5 CSWlibssl1-0-0 CSWlibotr2
RUNTIME_DEP_PKGS += CSWlibaspell15 CSWlibglib2-0-0 
RUNTIME_DEP_PKGS += CSWlibintl8 CSWlibpanelw5 CSWgpgme 
# Don't know yet why but this dependency is only picked under sparc
RUNTIME_DEP_PKGS += $(RUNTIME_DEP_PKGS_$(GARCH))
RUNTIME_DEP_PKGS_sparc = CSWlibgpg-error0

r CSWgpgme CSWiconv

TEST_SCRIPTS = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --witincludepenssl=/opt/csw/lib
CONFIGURE_ARGS += --enable-otr
CONFIGURE_ARGS += --enable-aspell
CONFIGURE_ARGS += --enable-sigwinch

# mcabber is geared towards gcc and heavily uses inline functions without
# static/extern storage qualifiers. Sun Studio needs to emulate gcc 
# behaviour with regards to these inline functions.
#  
# For details see http://blogs.sun.com/dew/entry/c99_inline_function
#
EXTRA_CFLAGS = -features=no%extinl

EXTRA_LDFLAGS = -lsocket -lnsl
EXTRA_INC = /opt/csw/lib/ncursesw

# Get rid of inline functions which are referenced externally (no%extinl
# makes inline functions static and would break linking otherwise)
PATCHFILES = patch-inline.diff

# Solaris 8 doesn't have iswlbank(), provide replacement macro
PATCHFILES += patch-iswblank.diff

include gar/category.mk

pre-build-modulated:
	@perl -pi -e 's|#! /bin/sh|#!/bin/bash|' $(WORKSRC)/hgcset.sh
	@perl -pi -e 's|-O2||' \
		$(WORKSRC)/Makefile \
		$(WORKSRC)/src/Makefile \
		$(WORKSRC)/libjabber/Makefile
	@$(MAKECOOKIE)

post-install-modulated:
	@perl -pi -e '\
		s|/usr/share/ssl/certs/ca-bundle.crt|/opt/csw/ssl/certs/ca-certificates.crt|;' \
		$(WORKSRC)/mcabberrc.example
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/mcabberrc.example $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(NAME)/changel