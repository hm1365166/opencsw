# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = 389-admin-console
SHORTNAME = 389-admin
VERSION = 1.1.10
MAJOR_VERSION = 1.1
GARTYPE = v2
CATEGORIES = java

DESCRIPTION = 389 Directory Server - Management Console Plugin AdminServer
define BLURB
A Java based remote management console used for managing 389
Administration Server and 389 Directory Server.
endef

MASTER_SITES = https://git.fedorahosted.org/cgit/389/admin-console.git/snapshot/
DISTNAME = admin-console-$(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.xz

BUNDLE = 389-ds

PACKAGES = CSW389-admin-console
BUILD_DEP_PKGS = CSWidm-console-base

ARCHALL = 1
PACKAGING_PLATFORMS = solaris10-sparc

CATALOGNAME_CSW389-admin-console = 389_admin_console

LICENSE = LICENSE

WORKSRC = $(WORKDIR)
EXTRAJARSPATH = /opt/csw/share/java
# EXTRAJARSPATH = /home/cgrzemba/java

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSW389-admin-console += file-with-bad-content|/usr/local|root/opt/csw/share/dirsrv/manual/en/admin/help/create_user_administrator_posix_user.html
CHECKPKG_OVERRIDES_CSW389-admin-console += pkginfo-description-not-starting-with-uppercase|389|Directory|Server|-|Management|Console|Plugin|AdminServer

include gar/category.mk

install-custom: 
	@ginstall -d $(DESTDIR)$(datadir)/dirsrv/html/java
	@ginstall -d $(DESTDIR)$(datadir)/dirsrv/manual/en/admin/help
	@gcp -fp $(WORKSRC)/$(DISTNAME)/built/package/$(SHORTNAME)* $(DESTDIR)$(datadir)/dirsrv/html/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/help/en/*.html $(DESTDIR)$(datadir)/dirsrv/manual/en/admin
	@gcp -fp $(WORKSRC)/$(DISTNAME)/help/en/tokens.map $(DESTDIR)$(datadir)/dirsrv/manual/en/admin
	@gcp -fp $(WORKSRC)/$(DISTNAME)/help/en/help/*.html $(DESTDIR)$(datadir)/dirsrv/manual/en/admin/help
	@( cd $(DESTDIR)$(datadir)/dirsrv/html/java ; \
	   ln -s $(SHORTNAME)-$(VERSION).jar $(SHORTNAME)-$(MAJOR_VERSION).jar ; \
	   ln -s $(SHORTNAME)-$(VERSION).jar $(SHORTNAME).jar ; \
	   ln -s $(SHORTNAME)-$(VERSION)_en.jar $(SHORTNAME)-$(MAJOR_VERSION)_en.jar ; \
	   ln -s $(SHORTNAME)-$(VERSION)_en.jar $(SHORTNAME)_en.jar )
	@$(MAKECOOKIE)

build-custom:
	@( cd $(WORKSRC)/$(DISTNAME); \
	  ant -Dbuilt.dir=`pwd`/built -Dldapjdk.location=$(EXTRAJARSPATH) -Dconsole.location=$(EXTRAJARSPATH) )
	@$(MAKECOOKIE)
