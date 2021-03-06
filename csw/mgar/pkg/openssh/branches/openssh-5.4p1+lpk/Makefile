#####################################################################
# OpenCSW build recipe for openssh
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = openssh
VERSION = 5.4p1
GSSKEX_PATCH_VERSION = $(VERSION)
GSSKEX_PATCH_DATE = 20100313
CATEGORIES = server

DESCRIPTION = OpenSSH Secure Shell

define BLURB
  OpenSSH is a FREE version of the SSH connectivity tools that technical users 
  of the Internet rely on. Users of telnet, rlogin, and ftp may not realize that 
  their password is transmitted across the Internet unencrypted, but it is. 
  OpenSSH encrypts all traffic (including passwords) to effectively eliminate 
  eavesdropping, connection hijacking, and other attacks. Additionally, OpenSSH 
  provides secure tunneling capabilities and several authentication methods, 
  and supports all SSH protocol versions.
endef


PACKAGES = CSWossh CSWosshclient

CATALOGNAME_CSWossh = openssh
SPKG_DESC_CSWossh = OpenSSH Secure Shell server 
RUNTIME_DEP_PKGS_CSWossh = CSWosslrt CSWtcpwrap CSWzlib CSWkrb5lib CSWosshclient
SPKG_CLASSES_CSWossh = none cswpreserveconf cswinitsmf

CATALOGNAME_CSWosshclient = openssh_client
SPKG_DESC_CSWosshclient = OpenSSH Secure Shell client 
RUNTIME_DEP_PKGS_CSWosshclient = CSWosslrt CSWzlib CSWkrb5lib 
SPKG_CLASSES_CSWosshclient = none cswpreserveconf

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386

###### Upstream and OpenCSW files information #######

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/ http://www.sxw.org.uk/computing/patches/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*p\d+).tar.gz

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWossh.prototype CSWossh.preinstall CSWossh.checkinstall
DISTFILES += CSWosshlpk.prototype CSWosshlpk.preinstall CSWosshlpk.checkinstall
DISTFILES += CSWosshclient.prototype
DISTFILES += changelog.CSW

DISTFILES += cswopenssh sshd.smf_wrapper cswopenssh.xml

LICENSE = LICENCE

# The GSSAPI key exchange patch
PATCHFILES = openssh-$(GSSKEX_PATCH_VERSION)-gsskex-all-$(GSSKEX_PATCH_DATE).patch

# Prevent TIOCSCTTY from being used to avoid error:
# ioctl(TIOCSCTTY): Invalid argument
PATCHFILES += don_t_use_TIOCSCTTY.patch

# Fix a X11 forwarding bug on machine installed with ipv6 disabled
# see https://bugzilla.mindrot.org/show_bug.cgi?id=1457
PATCHFILES += no_x_forwarding_bug.patch

# Fix an incorrect usage of getcwd under Solaris
# see https://bugzilla.mindrot.org/show_bug.cgi?id=1739
PATCHFILES += derelativise_path_bugfix.patch

# AuthorizedKeysFile option value should not be derelativized !!
# see https://bugzilla.mindrot.org/show_bug.cgi?id=1739
PATCHFILES += dont_derelativise_authorizedkeysfile_option.patch

# documentation files to install (not a gar variable)
DOCFILES = CREDITS ChangeLog ChangeLog.gssapi INSTALL LICENCE OVERVIEW README README.dns 
DOCFILES += README.platform README.privsep README.tun TODO WARNING.RNG    

# we're using conf handling class from the cswclassutils package
RUNTIME_DEP_PKGS += CSWcswclassutils


##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)

TEST_SCRIPTS	=


## Optional addition to add Ldap Public Key support 
## see http://code.google.com/p/openssh-lpk/

# we always register the lpk related files so checksum 
# is the same with LPK enabled or not
# Patch taken from http://code.google.com/p/openssh-lpk/issues/detail?id=7
# and modified with
#   perl -e 's/--- g/--- /; s/\+{3} g/+++ /' -pi 
# as all filenames seem to be prefixed with 'g' and redone patch for
# patchdirlevel 1 instead of 0
DISTFILES += 0001-This-is-a-forward-port-of-the-OpenSSH-LPK-support-pa.patch
ifdef LPK
	PACKAGES = CSWosshlpk
	CATALOGNAME_CSWosshlpk = openssh_lpk
	SPKG_DESC_CSWosshlpk = $(SPKG_DESC_CSWossh) with ldap public key support
	RUNTIME_DEP_PKGS_CSWosshlpk = $(RUNTIME_DEP_PKGS_CSWossh) CSWoldaprt
	SPKG_CLASSES_CSWosshlpk = none cswpreserveconf cswinitsmf
	PATCHFILES += 0001-This-is-a-forward-port-of-the-OpenSSH-LPK-support-pa.patch
	CONFIGURE_ARGS += --with-ldap
	DOCFILES += openssh-lpk_openldap.schema openssh-lpk_sun.schema lpk-user-example.txt README.lpk
	
	# we must reset the CSWosshclient description to avoid a bug in the automatic dependancy generation
	SPKG_DESC_CSWosshclient = 
endif

CHECKPKG_OVERRIDES_CSWosshlpk += bad-rpath-entry|/opt/csw/lib/
CHECKPKG_OVERRIDES_CSWosshlpk += bad-rpath-entry|/opt/csw/lib/
CHECKPKG_OVERRIDES_CSWosshlpk += init-file-wrong-location|/etc/opt/csw/init.d/cswopenssh
CHECKPKG_OVERRIDES_CSWosshlpk += surplus-dependency|CSWosshclient

include gar/category.mk


# we re-run autoconf because of the GSSAPI key exchange patch
pre-configure:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

# adding documentation files
post-merge: merge-config-files merge-doc-files merge-init-files merge-contrib-files
	@$(MAKECOOKIE)

merge-contrib-files:
	ginstall -D "$(WORKSRC_FIRSTMOD)/contrib/ssh-copy-id" "$(PKGROOT)/$(bindir)/ssh-copy-id"
	ginstall -D "$(WORKSRC_FIRSTMOD)/contrib/ssh-copy-id.1" "$(PKGROOT)/$(mandir)/man1/ssh-copy-id.1"

merge-init-files:
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswopenssh" "$(PKGROOT)/etc/opt/csw/init.d/cswopenssh"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswopenssh.xml" "$(PKGROOT)/var/opt/csw/svc/manifest/network/cswopenssh.xml"
	ginstall -D "$(WORKDIR_FIRSTMOD)/sshd.smf_wrapper" "$(PKGROOT)/opt/csw/sbin/sshd.smf_wrapper"


merge-doc-files:
	for DOCDIR in $(foreach _PKG,$(PACKAGES),$(call catalogname,$(_PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$DOCDIR; \
		(cd $(WORKSRC_FIRSTMOD) && ginstall $(DOCFILES) $(PKGROOT)/$(docdir)/$$DOCDIR/); \
		ginstall $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/$$DOCDIR/; \
	done

merge-config-files:
	ginstall $(PKGROOT)/$(sysconfdir)/ssh/ssh_config $(PKGROOT)/$(sysconfdir)/ssh/ssh_config.CSW 
	ginstall $(PKGROOT)/$(sysconfdir)/ssh/moduli $(PKGROOT)/$(sysconfdir)/ssh/moduli.CSW 
	# we change some default value in the server config file
	sed -e 's,/etc/ssh/,/opt/csw/etc/ssh/,g' \
		-e 's,/usr/libexec/,/opt/csw/libexec/,g' \
		-e 's,^ *# *UsePAM *.*,UsePAM yes,g' \
		-e 's,^ *# *PrintMotd *.*,PrintMotd no,g' \
	       	-e 's,^ *# *X11Forwarding *.*,X11Forwarding yes,g' "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config" > "$(PKGROOT)/$(sysconfdir)/ssh/sshd_config.CSW


