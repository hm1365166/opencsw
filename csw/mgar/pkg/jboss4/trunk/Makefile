NAME      = jboss4
VERSION   = 4.2.2.GA
GARTYPE = v1
CATEGORIES   = server

DESCRIPTION  =  J2EE Application Server
define BLURB
The JBoss/Server is the leading Open Source, standards-compliant, J2EE based application server implemented in 100% Pure Java
endef

MASTER_SITES  = http://kent.dl.sourceforge.net/sourceforge/jboss/
DISTFILES     = jboss-$(VERSION).zip
PKGDIST       = jboss-$(VERSION).zip
DISTFILES    += CSWjboss4.gspec CSWjboss4.prototype CSWjboss4.depend preremove postinstall preinstall checkinstall space i.smfno i.smfyes svc-jboss4 jboss4.xml jboss4.conf cswjboss4
# DISTFILES    += $(call admfiles, CSWjboss4, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = jboss-(\d+(?:\.\d+)*).zip

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = none
TEST_SCRIPTS	  = none
INSTALL_SCRIPTS   = jboss
prefix            = /

include gar/category.mk

configure-none:
	@$(MAKECOOKIE)

test-none:
	@$(MAKECOOKIE)

build-none:
	@$(MAKECOOKIE)

post-extract:
	( mv $(WORKDIR)/jboss-$(VERSION) $(WORKDIR)/$(DISTNAME) )
	( mv $(WORKDIR)/$(DISTNAME)/bin/run.conf $(WORKDIR)/$(DISTNAME)/bin/run.conf.CSW )
	( mv $(WORKDIR)/$(DISTNAME)/client/auth.conf $(WORKDIR)/$(DISTNAME)/client/auth.conf.CSW )
	( mkdir -p $(DESTDIR)/etc/opt/csw/$(NAME) )
	( cp -fr $(FILEDIR)/$(NAME).conf $(DESTDIR)/etc/opt/csw/$(NAME)/$(NAME).conf.CSW )
#	( OLDDIR=`pwd` && cd $(WORKDIR)/$(DISTNAME)/conf && for i in `find . -type file` ; do mv $$i $$i.CSW ; done && cd $$OLDDIR )
#	( for i in temp work logs conf ; do  find $(WORKDIR)/$(DISTNAME)/$$i -type d -exec chmod 0750 {} \;  ; find $(WORKDIR)/$(DISTNAME)/$$i -type f -exec chmod 0640 {} \; ; done )
	@$(MAKECOOKIE)

install-jboss:
	( mkdir -p $(DESTDIR)/etc/init.d )
	( mkdir -p $(DESTDIR)/etc/opt/csw )
	( mkdir -p $(DESTDIR)/etc/rc0.d )
	( mkdir -p $(DESTDIR)/etc/rc1.d )
	( mkdir -p $(DESTDIR)/etc/rc2.d )
	( mkdir -p $(DESTDIR)/etc/rc3.d )
	( mkdir -p $(DESTDIR)/etc/rcS.d )
	( mkdir -p $(DESTDIR)/opt/csw/etc/$(NAME) )
	( mkdir -p $(DESTDIR)/var/opt/csw/$(NAME) )
	( mkdir -p $(DESTDIR)/opt/csw/share )
	( mkdir -p $(DESTDIR)/etc/opt/csw )
	( mkdir -p $(DESTDIR)/etc/opt/csw/$(NAME) )
	( cp -fr  $(WORKDIR)/$(DISTNAME) $(DESTDIR)/opt/csw/$(NAME) )
	( cp -fr $(FILEDIR)/$(NAME).conf $(DESTDIR)/etc/opt/csw/$(NAME) )
	( cp -fr $(FILEDIR)/csw$(NAME) $(DESTDIR)/etc/init.d )
#	( mv     $(DESTDIR)/opt/csw/$(NAME)/conf $(DESTDIR)/opt/csw/etc/$(NAME)/conf )
#	( mv     $(DESTDIR)/opt/csw/$(NAME)/logs $(DESTDIR)/var/opt/csw/$(NAME) )
#	( mv     $(DESTDIR)/opt/csw/$(NAME)/work $(DESTDIR)/var/opt/csw/$(NAME) )
#	( mv     $(DESTDIR)/opt/csw/$(NAME)/temp $(DESTDIR)/var/opt/csw/$(NAME) )
#	( ln -s /opt/csw/etc/$(NAME)/conf $(DESTDIR)/opt/csw/$(NAME)/conf )
#	( ln -s /var/opt/csw/$(NAME)/logs $(DESTDIR)/opt/csw/$(NAME)/logs )
#	( ln -s /var/opt/csw/$(NAME)/work $(DESTDIR)/opt/csw/$(NAME)/work )
#	( ln -s /var/opt/csw/$(NAME)/temp $(DESTDIR)/opt/csw/$(NAME)/temp )
	( ln -s /etc/init.d/cswjboss4 $(DESTDIR)/etc/rc0.d/K17$(NAME) )
	( ln -s /etc/init.d/cswjboss4 $(DESTDIR)/etc/rc1.d/K17$(NAME) )
	( ln -s /etc/init.d/cswjboss4 $(DESTDIR)/etc/rc2.d/K17$(NAME) )
	( ln -s /etc/init.d/cswjboss4 $(DESTDIR)/etc/rc3.d/S51$(NAME) )
	( ln -s /etc/init.d/cswjboss4 $(DESTDIR)/etc/rcS.d/K17$(NAME) )
	@$(MAKECOOKIE)



