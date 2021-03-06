# $Id$

NAME = exim
VERSION = 4.80
CATEGORIES = server
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = The Exim Mail Transfer Agent
define BLURB
  Exim is a message transfer agent (MTA) developed at the University of
  Cambridge for use on Unix systems connected to the Internet. It is freely
  available under the terms of the GNU General Public Licence. In style it
  is similar to Smail 3, but its facilities are more general. There is a
  great deal of flexibility in the way mail can be routed, and there are
  extensive facilities for checking incoming mail. Exim can be installed in
  place of sendmail, although the configuration of exim is quite different
  to that of sendmail.
endef

MASTER_SITES = ftp://ftp.exim.org/pub/exim/exim4/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += CSWexim.cswreleasenotes

# NOTE TO FUTURE MAINTAINERS: This patch should be thoroughly reviewed
# for each update so as not to miss any new config options of
# interest...  Also, we start at 3 since we manually create a few git
# commits in pre-patch below.
PATCHFILES += 0003-Set-OpenCSW-build-options.patch

BUILD_DEP_PKGS = CSWlibspf2-dev CSWsasl-dev

RUNTIME_DEP_PKGS_CSWexim += CSWgzip
RUNTIME_DEP_PKGS_CSWexim += CSWgzipextras
RUNTIME_DEP_PKGS_CSWexim += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWexim += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWexim += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWexim += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWexim += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWexim += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWexim += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWexim += CSWlibspf2-2
RUNTIME_DEP_PKGS_CSWexim += CSWlibpq5
RUNTIME_DEP_PKGS_CSWexim += CSWperl

# They supply the GPL in a non-standard file.
LICENSE = LICENCE

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

INITSMF = /etc/opt/csw/init.d/cswexim

PRESERVECONF += /etc/opt/csw/exim/exim.conf /etc/opt/csw/exim/exim-env.sh
PRESERVECONF += /etc/opt/csw/exim/aliases

ALTERNATIVE = /opt/csw/bin/sendmail sendmail /opt/csw/bin/sendmail.exim 50 /opt/csw/bin/mailq mailq /opt/csw/bin/mailq.exim /opt/csw/bin/newaliases newaliases /opt/csw/bin/newaliases.exim

POSTMSG = /opt/csw/share/doc/$(NAME)/postmsg.CSW

# scripts/exim_install has been patched to use this variable
EXIM_VERSION = $(VERSION)
export EXIM_VERSION

# This is needed for the SPF2 workaround:
PWD = $(shell pwd)

# Local/Makefile has been patched to use these:
CSW_CC = $($(GARCOMPILER)_CC)
CSW_OPT = $(CFLAGS)
CSW_WORKSRC = $(PWD)/$(WORKSRC)

EXTRA_CONFIGURE_EXPORTS += CSW_CC
EXTRA_CONFIGURE_EXPORTS += CSW_OPT
EXTRA_CONFIGURE_EXPORTS += CSW_WORKSRC

EXTRA_BUILD_EXPORTS += CSW_CC
EXTRA_BUILD_EXPORTS += CSW_OPT
EXTRA_BUILD_EXPORTS += CSW_WORKSRC

# exim doesn't use configure
CONFIGURE_SCRIPTS =

# We don't want exim_install to create the exim symlink or run chown
INSTALL_ARGS = "INSTALL_ARG=-no_symlink -no_chown"

# exim doesn't have a test target
TEST_TARGET =

# We use this to strip binaries after we're done building
BINS =  exim-$(VERSION)* exim_dbmbuild exim_dumpdb exim_fixdb exim_lock exim_tidydb
BINS += eximon.bin

UGPATH=/etc/opt/csw/pkg/CSWexim
UGENTRY = exim:exim:CSW Exim User:/var/opt/csw/spool/exim:/bin/false:::NP
USERGROUP = $(UGPATH)/cswusergroup

CHECKPKG_OVERRIDES_CSWexim += surplus-dependency|CSWgzipextras
CHECKPKG_OVERRIDES_CSWexim += surplus-dependency|CSWgzip
CHECKPKG_OVERRIDES_CSWexim += file-with-bad-content|/usr/local|root/opt/csw/bin/exim-4.80-2
CHECKPKG_OVERRIDES_CSWexim += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswexim.xml

PROTOTYPE_MODIFIERS = eximsuid eximowned
PROTOTYPE_PERMS_eximsuid = 4755
PROTOTYPE_FILES_eximsuid = $(sbindir)/exim
PROTOTYPE_CLASS_eximowned = ugfiles
PROTOTYPE_USER_eximowned = exim
PROTOTYPE_GROUP_eximowned = exim
PROTOTYPE_PERMS_eximowned = 750
PROTOTYPE_FILES_eximowned = /var$(prefix)/log/exim /var$(prefix)/spool/exim

include gar/category.mk

pre-patch-modulated:
	(cd $(WORKSRC); \
	test -r Local/Makefile || cp -p src/EDITME Local/Makefile; \
	test -r Local/eximon.conf || cp -p exim_monitor/EDITME Local/eximon.conf; \
	perl -pi -e 's/Local.*//' .gitignore; \
	git add .gitignore; \
	git add Local/; git commit -m 'Setup Local build default files'; \
	test -d spf2 || cp -pr /opt/csw/include/spf2 .; \
	git add spf2; git commit -m 'import spf2 header files' )
	@$(MAKECOOKIE)

pre-build-modulated:
	(cd $(WORKSRC); make makefile)
	@$(MAKECOOKIE)

DOC_LIST = ChangeLog Exim3.upgrade Exim4.upgrade NewStuff OptionLists.txt
DOC_LIST += README README.SIEVE dbm.discuss.txt filter.txt spec.txt

post-install-modulated:
	(mkdir -p $(DESTDIR)$(prefix)/sbin; \
	cd $(DESTDIR)$(prefix)/sbin; \
	ln -s  ../bin/exim-$(VERSION)-2 exim; \
	cd ../bin; ln -s exim-$(VERSION)-* exim; \
	/usr/ccs/bin/strip $(BINS); \
	/usr/ccs/bin/mcs -d $(BINS))
	(cd $(DESTDIR); mkdir -p var/opt/csw/svc/manifest/network; \
		cp $(abspath $(FILEDIR)/cswexim.xml) var/opt/csw/svc/manifest/network )
	(cd $(DESTDIR); mkdir -p etc/opt/csw/init.d; \
		cp $(abspath $(FILEDIR)/cswexim) etc/opt/csw/init.d )
	mkdir -p $(DESTDIR)$(prefix)/share/doc/exim
	mkdir -p $(DESTDIR)/var/$(prefix)/spool/exim
	cp -p files/README.CSW  $(DESTDIR)$(prefix)/share/doc/exim/README.CSW
	cp -p files/postmsg.CSW  $(DESTDIR)$(prefix)/share/doc/exim/
	cp -p files/exim-env.sh $(DESTDIR)/etc/$(prefix)/exim/
	(cd $(WORKSRC)/doc; \
	cp -p $(DOC_LIST) $(DESTDIR)$(prefix)/share/doc/exim)
	gzip -f $(DESTDIR)$(prefix)/share/doc/exim/ChangeLog
	gzip -f $(DESTDIR)$(prefix)/share/doc/exim/spec.txt
	@$(MAKECOOKIE)

post-merge:
	( cd $(PKGROOT); mkdir -p ./$(UGPATH); \
		echo "$(UGENTRY)" > ./$(UGPATH)/cswusergroup )
	( cd $(PKGROOT); mkdir -p opt/csw/bin var/opt/csw/log/exim )
	@( cd $(PKGROOT)/$(bindir); \
		ln -s ../sbin/exim sendmail.exim; \
		ln -s ../sbin/exim mailq.exim; \
		ginstall -m 0755 $(abspath $(FILEDIR))/newaliases $(PKGROOT)/$(bindir)/newaliases.exim )
	@$(MAKECOOKIE)
