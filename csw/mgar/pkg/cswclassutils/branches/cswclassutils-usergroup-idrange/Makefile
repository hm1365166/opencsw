# $Id$

NAME = cswclassutils
VERSION = 1.31
CATEGORIES = utils

DESCRIPTION = CSW class action utilities

MASTER_SITES =
DISTFILES = COPYING

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org

CASFILES = $(wildcard $(FILEDIR)/CSW$(NAME).[ir].*)
CASLIST = $(foreach F,$(CASFILES), $(subst $(FILEDIR)/CSW$(NAME).,,$(F)))
DISTFILES += $(subst $(FILEDIR)/,,$(CASFILES))

PROTOTYPE_FILTER = sed -e '/^d.*\/usr/d; /scripts/{ s/bin/sys/; }'

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -m 0755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 0755 -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 0755 -d $(DESTDIR)/usr/sadm/install/scripts
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/manifest
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/method
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/cswclassutils
	@ginstall -m 0755 $(FILEDIR)/CSW$(NAME).csw.smf.sample $(DESTDIR)/etc/opt/csw/init.d/csw.smf.sample
	@ginstall -m 0444 $(FILEDIR)/CSW$(NAME).README.CSW $(DESTDIR)$(docdir)/$(NAME)/README.CSW
	@$(foreach CAS,$(CASLIST),ginstall -m 0555 $(FILEDIR)/CSW$(NAME).$(CAS) $(DESTDIR)/usr/sadm/install/scripts/$(CAS);)
	@$(MAKECOOKIE)
