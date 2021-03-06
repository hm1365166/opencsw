# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = cups
VERSION = 1.5.4
GARTYPE = v2

define BLURB
  CUPS provides a portable printing layer for UNIX(R)-based operating
  systems.  It is developed and maintained by Easy Software Products to
  promote a standard printing solution and is the standard printing system
  in MacOS(R) X and most Linux(R) distributions.

  http://www.cups.org/str.php?L3324
endef

# There's a problem with cups-polld going into a busy-wait loop when polling
# print servers.
#
#   http://www.cups.org/str.php?L3257 (closed)
#   http://www.cups.org/str.php?L3381 (filed again)
#
# The problem with cups-polld seems to be going away when CUPS is compiled with
# debugging symbols. The debugging options is turned on for this package, in
# order to be able to debug the binary if it ever shows the problem.

# This build file support setting GARFLAVOR to DBG in order to build binaries
# with debugging symbols.
# GARFLAVOR = DBG

# These are the source mirrors published on the CUPS home-page.
# CUPS_MIRRORS  = http://ftp.easysw.com/pub
# CUPS_MIRRORS += ftp://ftp2.easysw.com/pub
# CUPS_MIRRORS += ftp://ftp3.easysw.com/pub
CUPS_MIRRORS += http://www.nu6.org/_/mirror/ftp.easysw.com/pub
CUPS_MIRRORS += http://ftp.funet.fi/pub/mirrors/ftp.easysw.com/pub
CUPS_MIRRORS += ftp://ftp.funet.fi/pub/mirrors/ftp.easysw.com/pub
CUPS_MIRRORS += http://ftp.rz.tu-bs.de/pub/mirror/ftp.easysw.com/ftp/pub

# Complete the mirror paths by adding /cups/x.y.z/ at the end.
FULL_MIRRORS  = $(foreach S,$(CUPS_MIRRORS),$(S)/$(NAME)/$(VERSION)/)
MASTER_SITES += $(FULL_MIRRORS)

DISTFILES  = $(NAME)-$(VERSION)-source.tar.bz2
DISTFILES += CSWcupsclient.preinstall
DISTFILES += CSWcupsd.preinstall
DISTFILES += CSWcupsd.postremove
DISTFILES += client.conf.CSW
DISTFILES += CSWcupsclient.README

PATCHFILES += 0001-cswcups-for-the-service-name.patch
PATCHFILES += 0002-use-posix-shell-in-install.sh.patch
# PATCHFILES += 0002-Adding-the-refcount-member-to-mime_type_t.patch
# PATCHFILES += 0003-Reference-counting-for-printers-only.patch
# PATCHFILES += 0006-Fail-compilation-if-no-SSL-impl-chosen.patch
PATCHFILES += 0007-Solaris-zone-support-in-init-script.patch
# PATCHFILES += CFLAGS-leaking-to-C++-compiler.patch
# PATCHFILES += 0008-Adding-CFLAGS-and-CXXFLAGS-to-linker-calls.patch
# PATCHFILES += 0009-Add-workaround-for-krb5-config-outputting-CFLAGS.patch
# PATCHFILES += 0009-giving-precedence-to-statvfs-in-printers.c.patch

REINPLACE_USRLOCAL += doc/help/*.html
REINPLACE_USRSHARE += doc/help/*.html

VENDOR_URL = http://www.cups.org/

LICENSE = LICENSE.txt

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

BUILD_DEP_PKGS  = CSWggettext-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWopenldap-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += SUNWhea
BUILD_DEP_PKGS += SUNWlibm
BUILD_DEP_PKGS += CSWlibslp-dev

# The main metapackage
PACKAGES += CSWcups
SPKG_DESC_CSWcups = Common Unix Printing System
# PKFILES is catchall
ARCHALL_CSWcups = 1
RUNTIME_DEP_PKGS_CSWcups += CSWcupsd
RUNTIME_DEP_PKGS_CSWcups += CSWcupsclient
CHECKPKG_OVERRIDES_CSWcups += surplus-dependency|CSWcupsclient

PACKAGES += CSWphp5-cups
SPKG_DESC_CSWphp5-cups = PHP5 bindings for CUPS
PKGFILES_CSWphp5-cups += $(prefix)/php5/.*
RUNTIME_DEP_PKGS_CSWphp5-cups += CSWlibcups2
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWphp5-cups_sparc += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWphp5-cups += $(RUNTIME_DEP_PKGS_CSWphp5-cups_$(GARCH))
# lib is located in /opt/csw/php5, not in csw standard bin path
CHECKPKG_OVERRIDES_CSWphp5-cups += 64-bit-binaries-missing

# The daemon
PACKAGES += CSWcupsd
SPKG_DESC_CSWcupsd = CUPS daemon
PKGFILES_CSWcupsd += $(bindir)/ppd(c|html|i|merge|po)
PKGFILES_CSWcupsd += $(datadir)/applications/.*
PKGFILES_CSWcupsd += $(datadir)/cups
PKGFILES_CSWcupsd += $(datadir)/cups/(banners|data|profiles|charsets).*
PKGFILES_CSWcupsd += $(datadir)/cups/(fonts|templates|charmaps|model).*
PKGFILES_CSWcupsd += $(datadir)/cups/mime.*
PKGFILES_CSWcupsd += $(datadir)/doc/cups/.*
PKGFILES_CSWcupsd += $(datadir)/icons.*
PKGFILES_CSWcupsd += $(datadir)/locale/.*
PKGFILES_CSWcupsd += $(libdir)/cups/.*
PKGFILES_CSWcupsd += $(libdir)/svc/.*
PKGFILES_CSWcupsd += $(localstatedir)/.*
PKGFILES_CSWcupsd += $(mandir)/man1m
PKGFILES_CSWcupsd += $(mandir)/man1m/cups(filter|d|-polld|-deviced|-driverd|-lpd)\.1m
PKGFILES_CSWcupsd += $(mandir)/man5/(cups-snmp.conf|subscriptions.conf).5
PKGFILES_CSWcupsd += $(mandir)/man5/(mime.convs|classes.conf|cupsd.conf).5
PKGFILES_CSWcupsd += $(mandir)/man5/(mime.types|printers.conf|mailto.conf).5
PKGFILES_CSWcupsd += $(mandir)/man7/(backend|filter).7
PKGFILES_CSWcupsd += $(sbindir)/(cupsfilter|cupsd)
PKGFILES_CSWcupsd += $(sysconfdir)/cups/cupsd.*
PKGFILES_CSWcupsd += $(sysconfdir)/cups/interfaces.*
PKGFILES_CSWcupsd += $(sysconfdir)/cups/ppd.*
PKGFILES_CSWcupsd += $(sysconfdir)/cups/snmp.*
PKGFILES_CSWcupsd += $(sysconfdir)/cups/ssl.*
PKGFILES_CSWcupsd += $(sysconfdir)/init\.d/.*
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibcups2
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibcupscgi1
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibcupsdriver1
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibcupsmime1
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibcupsppdc1
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWcupsd_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWcupsd_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcupsd_sparc += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibslp1
RUNTIME_DEP_PKGS_CSWcupsd += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWcupsd += $(RUNTIME_DEP_PKGS_CSWcupsd_$(GARCH))
# pdftops filter needs poppler's /opt/csw/bin/pdftops
RUNTIME_DEP_PKGS_CSWcupsd += CSWpoppler
CHECKPKG_OVERRIDES_CSWcupsd += surplus-dependency|CSWpoppler

PACKAGES += CSWcupsclient
SPKG_DESC_CSWcupsclient = CUPS client binaries
PKGFILES_CSWcupsclient  = $(sbindir)/(accept|reject|cups(addsmb|ctl|(en|dis)able))
PKGFILES_CSWcupsclient += $(sbindir)/cups(accept|reject)
PKGFILES_CSWcupsclient += $(sbindir)/(lp(admin|p|c|info|move))
PKGFILES_CSWcupsclient += $(bindir)/(cancel|cupstest(dsc|ppd))
PKGFILES_CSWcupsclient += $(bindir)/(lp(|options|passwd|q|r|rm|stat))
PKGFILES_CSWcupsclient += $(bindir)/ipptool
PKGFILES_CSWcupsclient += $(mandir)/man1/ipptool.1
PKGFILES_CSWcupsclient += $(mandir)/man5/ipptoolfile.5
PKGFILES_CSWcupsclient += $(sharedstatedir)/cups/ipptool/.*
PKGFILES_CSWcupsclient += $(mandir)/man1/(cancel|cupstest(dsc|ppd)|lp).1
PKGFILES_CSWcupsclient += $(mandir)/man1/(lpoptions|lppasswd|lpq|lpr|lprm).1
PKGFILES_CSWcupsclient += $(mandir)/man1/lpstat.1
PKGFILES_CSWcupsclient += $(mandir)/man1/ppd.*\.1
PKGFILES_CSWcupsclient += $(mandir)/man1m/(cups|)(accept|reject)\.1m
PKGFILES_CSWcupsclient += $(mandir)/man1m/cups(en|dis)able\.1m
PKGFILES_CSWcupsclient += $(mandir)/man1m/cups(addsmb|ctl)\.1m
PKGFILES_CSWcupsclient += $(mandir)/man1m/lp(admin|c|info|move)\.1m
PKGFILES_CSWcupsclient += $(mandir)/man5/client.conf.5
PKGFILES_CSWcupsclient += $(mandir)/man5/ppdcfile\.5
PKGFILES_CSWcupsclient += $(mandir)/man7/(drv|notifier)\.7
PKGFILES_CSWcupsclient += $(sysconfdir)/cups/client\.conf\.CSW
PKGFILES_CSWcupsclient += $(datadir)/doc/cupsclient.*
RUNTIME_DEP_PKGS_CSWcupsclient += CSWlibcups2
RUNTIME_DEP_PKGS_CSWcupsclient += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWcupsclient_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWcupsclient_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcupsclient_sparc += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWcupsclient += $(RUNTIME_DEP_PKGS_CSWcupsclient_$(GARCH))

PACKAGES += CSWcups-dev
SPKG_DESC_CSWcups-dev = CUPS header files
CATALOGNAME_CSWcups-dev = cups_dev
PKGFILES_CSWcups-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWcups-dev += $(datadir)/cups/ppdc.*
PKGFILES_CSWcups-dev += $(datadir)/cups/drv.*
PKGFILES_CSWcups-dev += $(datadir)/cups/examples.*
# The development package needs all the libraries
RUNTIME_DEP_PKGS_CSWcups-dev += CSWlibcupsppdc1
RUNTIME_DEP_PKGS_CSWcups-dev += CSWlibcupsdriver1
RUNTIME_DEP_PKGS_CSWcups-dev += CSWlibcups2
RUNTIME_DEP_PKGS_CSWcups-dev += CSWlibcupsmime1
RUNTIME_DEP_PKGS_CSWcups-dev += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWcups-dev += CSWlibcupscgi1

# The problematic cupslinks package
# PACKAGES += CSWcupslinks
CATALOGNAME_CSWcupslinks = cups_links
SPKG_DESC_CSWcupslinks = Drop-in replacement for SUNWpcu and SUNWpcr
ARCHALL_CSWcupslinks = 1
PKGFILES_CSWcupslinks  = /usr/sbin/.*
PKGFILES_CSWcupslinks += /usr/bin/.*
INCOMPATIBLE_PKGS_CSWcupslinks = SUNWpcr SUNWpcu
CUPSLINKS_TARGET = cupslinks

# Packages compliant with the shared library policy.
PACKAGES += CSWlibcups2
SPKG_DESC_CSWlibcups2 = CUPS libraries, libcups.so.2
PKGFILES_CSWlibcups2 += $(call pkgfiles_lib,libcups.so.2)
RUNTIME_DEP_PKGS_CSWlibcups2 += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibcups2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcups2_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibcups2_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcups2_sparc += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibcups2_sparc += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWlibcups2_sparc += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibcups2_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibcups2 += $(RUNTIME_DEP_PKGS_CSWlibcups2_$(GARCH))

PACKAGES += CSWlibcupscgi1
SPKG_DESC_CSWlibcupscgi1 = CUPS libraries, libcupscgi.so.1
PKGFILES_CSWlibcupscgi1 += $(call pkgfiles_lib,libcupscgi.so.1)
RUNTIME_DEP_PKGS_CSWlibcupscgi1 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibcupscgi1_sparc += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWlibcupscgi1 += $(RUNTIME_DEP_PKGS_CSWlibcupscgi1_$(GARCH))

PACKAGES += CSWlibcupsdriver1
SPKG_DESC_CSWlibcupsdriver1 = CUPS libraries, libcupsdriver.so.1
PKGFILES_CSWlibcupsdriver1 += $(call pkgfiles_lib,libcupsdriver.so.1)
RUNTIME_DEP_PKGS_CSWlibcupsdriver1 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibcupsdriver1_sparc += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWlibcupsdriver1 += $(RUNTIME_DEP_PKGS_CSWlibcupsdriver1_$(GARCH))

PACKAGES += CSWlibcupsimage2
SPKG_DESC_CSWlibcupsimage2 = CUPS libraries, libcupsimage.so.2
PKGFILES_CSWlibcupsimage2 += $(call pkgfiles_lib,libcupsimage.so.2)
RUNTIME_DEP_PKGS_CSWlibcupsimage2 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibcupsimage2 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibcupsimage2 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibcupsimage2 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibcupsimage2_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcupsimage2_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcupsimage2_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibcupsimage2_sparc += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibcupsimage2_sparc += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibcupsimage2_sparc += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibcupsimage2_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibcupsimage2 += $(RUNTIME_DEP_PKGS_CSWlibcupsimage2_$(GARCH))

PACKAGES += CSWlibcupsmime1
SPKG_DESC_CSWlibcupsmime1 = CUPS libraries, libcupsmime.so.1
PKGFILES_CSWlibcupsmime1 += $(call pkgfiles_lib,libcupsmime.so.1)
RUNTIME_DEP_PKGS_CSWlibcupsmime1 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibcupsmime1_sparc += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWlibcupsmime1 += $(RUNTIME_DEP_PKGS_CSWlibcupsmime1_$(GARCH))


PACKAGES += CSWlibcupsppdc1
SPKG_DESC_CSWlibcupsppdc1 = CUPS libraries, libcupsppdc.so.1
PKGFILES_CSWlibcupsppdc1 += $(call pkgfiles_lib,libcupsppdc.so.1)
RUNTIME_DEP_PKGS_CSWlibcupsppdc1 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibcupsppdc1_sparc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibcupsppdc1_sparc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcupsppdc1_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcupsppdc1_sparc += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibcupsppdc1_sparc += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibcupsppdc1_sparc += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibcupsppdc1_sparc += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibcupsppdc1 +=$(RUNTIME_DEP_PKGS_CSWlibcupsppdc1_$(GARCH))

# For some reason -norunpath is not used here, investigate later
# CHECKPKG_OVERRIDES_CSWlibcupsppdc1 += bad-rpath-entry

### commented out if libtasn1.so.3 needed by libgnutls is not availible for 64bit (at the moment)
BUILD64_LIBS_ONLY = 1

EXTRA_LINKER_FLAGS += -liconv
EXTRA_LINKER_FLAGS += -norunpath

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-menudir=$(datadir)/applications
CONFIGURE_ARGS += --localedir=$(datadir)/locale
CONFIGURE_ARGS += --with-rcdir=$(sysconfdir)
CONFIGURE_ARGS += --with-icondir=$(datadir)/icons
CONFIGURE_ARGS += --with-openslp-includes=/opt/csw/include

# This breaks non-global sparse zone support.  The class action script is
# executed in the global zone, but not in the non-global zones, if /opt is
# shared.
# CONFIGURE_ARGS += --with-rcdir=/opt/csw/etc

CONFIGURE_ARGS_DBG  = --enable-debug
CONFIGURE_ARGS_DBG += --enable-debug-guards
CONFIGURE_ARGS_DBG += --enable-debug-printfs

CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# This is a hack that's needed, because configure (Makedefs) will otherwise
# plase -ltiff, etc. first and -L/opt/csw/lib afterwards, thus being unable
# to find any of the image libraries.
# Fortunately, configure honors values already in $DSOFLAGS, so we can use
# that to make sure -L/opt/csw/lib is the first argument passed to ld.
CONFIGURE_ARGS += "DSOFLAGS=-L$(libdir) -z ignore -norunpath"

# PRIVATE_CUPS_INC = $(DESTDIR)$(includedir)/cups

# CUPS uses the 'OPTIM' variable to set the optimization flags.
# OPTIM_OPT = -xO0
# OPTIM_DBG = -g -xO0
# OPTIM = $(OPTIM_$(GARFLAVOR))
# OPT_FLAGS_SOS = -xO0
# export OPTIM

# Don't run tests (at least for now); there are some LD_LIBRARY_PATH issues
SKIPTEST ?= 1

# For some reason, the CUPS guys have decided to use DSTROOT for what
# everybody else calls DESTDIR.
INSTALL_OVERRIDE_VARS = DSTROOT
INSTALL_OVERRIDE_VAR_DSTROOT = $(DESTDIR)

EXTRA_MERGE_EXCLUDE_FILES += .*\.default

PROTOTYPE_MODIFIERS = lp_group_etc
PROTOTYPE_FILES_lp_group_etc = $(sysconfdir).*
PROTOTYPE_GROUP_lp_group_etc = lp

PROTOTYPE_MODIFIERS = lp_group_var
PROTOTYPE_FILES_lp_group_var += $(localstatedir)/cache/.*
PROTOTYPE_FILES_lp_group_var += $(localstatedir)/log/.*
PROTOTYPE_FILES_lp_group_var += $(localstatedir)/run/.*
PROTOTYPE_FILES_lp_group_var += $(localstatedir)/spool/.*
PROTOTYPE_GROUP_lp_group_var = lp

# http://lists.opencsw.org/pipermail/maintainers/2009-September/004249.html
PRESERVECONF += $(sysconfdir)/cups/client\.conf
PRESERVECONF += $(sysconfdir)/cups/cupsd\.conf
# https://www.opencsw.org/mantis/view.php?id=5037
PRESERVECONF += $(datadir)/cups/mime/mime.convs
PRESERVECONF += $(datadir)/cups/mime/mime.types
INITSMF = $(sysconfdir)/init\.d/cswcups

include gar/category.mk

post-install-modulated:
	ginstall -m 644 \
		$(WORKDIR)/client.conf.CSW \
		$(DESTDIR)$(sysconfdir)/cups/client.conf.CSW
	for f in $(DESTDIR)$(libdir_install)/cups/backend/*; do \
		chmod 0700 $${f}; \
	done
	# https://www.opencsw.org/mantis/view.php?id=4532
	ginstall -m 755 -d $(DESTDIR)$(datadir)/doc/cupsclient
	ginstall -m 755 $(WORKDIR)/CSWcupsclient.README \
		$(DESTDIR)$(datadir)/doc/cupsclient/README
	@$(MAKECOOKIE)

# This has been disabled and should be pulled in through post-install-modulated
cupslinks:
	# https://www.opencsw.org/mantis/view.php?id=2924
	ginstall -d -m 755 $(DESTDIR)/usr/bin
	for f in cancel lp lpoptions lppassd lpq lpr lprm lpstat; do \
		ln -s ../../opt/csw/bin/$$f $(DESTDIR)/usr/bin/$$f; \
	done
	ginstall -d -m 755 $(DESTDIR)/usr/sbin
	for f in accept lpadmin lpc lpinfo lpmove reject; do \
		ln -s ../../opt/csw/sbin/$$f $(DESTDIR)/usr/sbin/$$f; \
	done
