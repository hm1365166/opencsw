# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = cups
VERSION = 1.4.0
CATEGORIES = net

define BLURB
  CUPS provides a portable printing layer for UNIX(R)-based operating
  systems.  It is developed and maintained by Easy Software Products to
  promote a standard printing solution and is the standard printing system
  in MacOS(R) X and most Linux(R) distributions.

  http://www.cups.org/str.php?L3324
endef

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

# There's a problem with cups-polld going into a busy-wait loop when polling
# print servers.
#
#   http://www.cups.org/str.php?L3257 (closed)
#   http://www.cups.org/str.php?L3381 (filed again)
#
# The problem with cups-polld seems to be going away when CUPS is compiled with
# debugging symbols. The debugging options is turned on for this package, in
# order to be able to debug the binary if it ever shows the problem.

GARFLAVOR = DBG

# These are the source mirrors published on the CUPS home-page.
CUPS_MIRRORS  = http://ftp.easysw.com/pub
CUPS_MIRRORS += ftp://ftp2.easysw.com/pub
CUPS_MIRRORS += ftp://ftp3.easysw.com/pub
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

PATCHFILES  = 0001-cswcups-for-service-name.patch
PATCHFILES += 0002-Adding-the-refcount-member-to-mime_type_t.patch
PATCHFILES += 0003-Reference-counting-for-printers-only.patch
# PATCHFILES += 0004-Fix-for-usb-unix.c-from-http-www.cups.org-str.php-L3.patch
PATCHFILES += 0005-Mapping-gnutls_record_recv-return-error-codes-to-err.patch
PATCHFILES += 0006-Fail-compilation-if-no-SSL-impl-chosen.patch
PATCHFILES += 0007-Solaris-zone-support-in-init-script.patch

BUILD_DEP_PKGS  = CSWggettext
BUILD_DEP_PKGS += CSWjpeg
BUILD_DEP_PKGS += CSWkrb5libdev
BUILD_DEP_PKGS += CSWoldapdevel
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWtiff
BUILD_DEP_PKGS += CSWzlib
BUILD_DEP_PKGS += SUNWhea
BUILD_DEP_PKGS += SUNWlibm
BUILD_DEP_PKGS += SUNWslpu

UFILES_REGEX = cups-(\d+(?:\.\d+)*)-source.tar.bz2

SPKG_CLASSES = none cswcpsampleconf cswinitsmf

PACKAGES = CSWlibcups CSWcupsd CSWcupsclient CSWcupsdoc CSWcupsdev CSWcups

ARCHALL_CSWcupsdoc = 1
ARCHALL_CSWcupsdev = 1

RUNTIME_DEP_PKGS_CSWcups  = CSWcswclassutils CSWcupsd CSWcupsclient
RUNTIME_DEP_PKGS_CSWcupsd  = CSWcswclassutils CSWlibcups CSWoldaprt CSWzlib
RUNTIME_DEP_PKGS_CSWcupsd += CSWjpeg CSWpng CSWtiff CSWlibtasn1
RUNTIME_DEP_PKGS_CSWcupsd += CSWgcrypt CSWgnutls CSWgpgerr CSWlibdbus
RUNTIME_DEP_PKGS_CSWcupsd += CSWkrb5lib CSWosslrt CSWcupsdoc
RUNTIME_DEP_PKGS_CSWcupsd += CSWdbusglib CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWcupsclient  = CSWcswclassutils CSWlibcups CSWoldaprt CSWzlib
RUNTIME_DEP_PKGS_CSWcupsclient += CSWgcrypt CSWgnutls CSWgpgerr CSWlibtasn1 CSWosslrt
RUNTIME_DEP_PKGS_CSWcupsdoc = CSWcswclassutils
RUNTIME_DEP_PKGS_CSWcupsdev = CSWcswclassutils
RUNTIME_DEP_PKGS_CSWlibcups  = CSWcswclassutils CSWjpeg CSWpng CSWtiff CSWzlib
RUNTIME_DEP_PKGS_CSWlibcups += CSWgcrypt CSWgnutls CSWgpgerr CSWlibtasn1 CSWosslrt

PKGFILES_CSWlibcups  = $(libdir)/libcups.*

PKGFILES_CSWcupsdoc  = $(datadir)/doc
PKGFILES_CSWcupsdoc += $(datadir)/doc/.*
PKGFILES_CSWcupsdoc += $(datadir)/cups/examples.*

PKGFILES_CSWcupsdev  = $(includedir)/cups/?.*
PKGFILES_CSWcupsdev += $(mandir)/man1/cups-config.1
PKGFILES_CSWcupsdev += $(bindir)/cups-config
PKGFILES_CSWcupsdev += $(datadir)/cups/ppdc.*
PKGFILES_CSWcupsdev += $(datadir)/cups/drv.*

PKGFILES_CSWcupsd  = $(sysconfdir)/.*
PKGFILES_CSWcupsd += $(mandir)/man1m
PKGFILES_CSWcupsd += $(mandir)/man1m/cups(filter|d|-polld|-deviced|-driverd|-lpd).*
PKGFILES_CSWcupsd += $(mandir)/man7/(backend|filter).7
PKGFILES_CSWcupsd += $(mandir)/man5/(cups-snmp.conf|subscriptions.conf).5
PKGFILES_CSWcupsd += $(mandir)/man5/(mime.convs|classes.conf|cupsd.conf).5
PKGFILES_CSWcupsd += $(mandir)/man5/(mime.types|printers.conf|mailto.conf).5
PKGFILES_CSWcupsd += $(datadir)/cups
PKGFILES_CSWcupsd += $(datadir)/cups/(fonts|templates|charmaps|model).*
PKGFILES_CSWcupsd += $(datadir)/cups/(banners|data|profiles|charsets).*
PKGFILES_CSWcupsd += $(datadir)/locale/.*
PKGFILES_CSWcupsd += $(datadir)/applications/.*
PKGFILES_CSWcupsd += $(datadir)/cups/mime.*
PKGFILES_CSWcupsd += $(datadir)/icons.*
PKGFILES_CSWcupsd += $(libdir)/cups/.*
PKGFILES_CSWcupsd += $(libdir)/svc/.*
PKGFILES_CSWcupsd += $(bindir)/ppd(c|html|i|merge|po)
PKGFILES_CSWcupsd += $(sbindir)/(cupsfilter|cupsd)
PKGFILES_CSWcupsd += $(localstatedir)/.*

PKGFILES_CSWcupsclient  = $(sbindir)/(accept|reject|cups(addsmb|ctl|(en|dis)able))
PKGFILES_CSWcupsclient += $(sbindir)/cups(accept|reject)
PKGFILES_CSWcupsclient += $(sbindir)/(lp(admin|p|c|info|move))
PKGFILES_CSWcupsclient += $(bindir)/(cancel|cupstest(dsc|ppd))
PKGFILES_CSWcupsclient += $(bindir)/(lp(|options|passwd|q|r|rm|stat))
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

SPKG_DESC_CSWcups = Common Unix Printing System
SPKG_DESC_CSWlibcups = CUPS libraries
SPKG_DESC_CSWcupsd = CUPS daemon
SPKG_DESC_CSWcupsclient = CUPS client binaries
SPKG_DESC_CSWcupsdoc = CUPS documentation
SPKG_DESC_CSWcupsdev = CUPS header files

# http://lists.opencsw.org/pipermail/maintainers/2009-September/004249.html
SAMPLECONF = $(sysconfdir)/cups/cupsd\.conf\.CSW
INITSMF    = $(sysconfdir)/init\.d/cswcups

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

CONFIGURE_ARGS  = $(DIRPATHS) --enable-pdftops
CONFIGURE_ARGS += --with-menudir=$(datadir)/applications
CONFIGURE_ARGS += --localedir=$(datadir)/locale
CONFIGURE_ARGS += --with-rcdir=$(sysconfdir)
CONFIGURE_ARGS += --with-icondir=$(datadir)/icons

CONFIGURE_ARGS_DBG  = --enable-debug
CONFIGURE_ARGS_DBG += --enable-debug-guards
CONFIGURE_ARGS_DBG += --enable-debug-printfs

CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))


# This is a hack that's needed, because configure (Makedefs) will otherwise
# plase -ltiff, etc. first and -L/opt/csw/lib afterwards, thus being unable
# to find any of the image libraries.
# Fortunately, configure honors values already in $DSOFLAGS, so we can use
# that to make sure -L/opt/csw/lib is the first argument passed to ld.
DSOFLAGS = -L/opt/csw/lib
export DSOFLAGS

# For some reason, the CUPS guys have decided to use DSTROOT for what
# everybody else calls DESTDIR.
DSTROOT = $(DESTDIR)
export DSTROOT

# Don't run tests (at least for now); there are some LD_LIBRARY_PATH issues
TEST_TARGET =

SPKG_SOURCEURL = http://www.cups.org/

PRIVATE_CUPS_INC = $(DESTDIR)$(includedir)/cups

# CUPS uses the 'OPTIM' variable to set the optimization flags.
OPTIM_DBG = -g -xO0
OPTIM = $(OPTIM_$(GARFLAVOR))
export OPTIM

include gar/category.mk

post-install-modulated:
	(cd $(DESTDIR)$(sysconfdir)/cups; \
	echo "Making .CSW configs in $(DESTDIR)$(sysconfdir)/cups"; \
	for i in cupsd.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW"; \
			chmod 0644 "$$i.CSW"; \
		fi \
	done)
	@$(MAKECOOKIE)
