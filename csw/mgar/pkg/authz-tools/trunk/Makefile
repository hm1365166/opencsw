NAME = authz-tools
VERSION = 0.6.1
GARTYPE = v1

DESCRIPTION = tools to manipulate authz files
define BLURB
	This is a package that contains several tools to manipulate authz files (as
	used by mod_auth_svn module for Subversion. The main reason for this package
	to exist -- big authz files and authz files located on remote computers.
endef

# Project URL
SPKG_SOURCEURL = http://only.mawhrin.net/~mss/thingies/authz/

# Source files
MASTER_SITES = http://only.mawhrin.net/~mss/thingies/authz/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
#DISTFILES += $(call admfiles,CSWauthztools,depend,prototype)
DISTFILES += $(call admfiles,CSWauthztools,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@( cd $(WORKSRC) ; python ./setup.py install --root=$(DESTDIR) )
	@$(MAKECOOKIE)

