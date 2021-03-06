# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mirrorbrain
VERSION = 2.19.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Brief description

MASTER_SITES = http://mirrorbrain.org/files/releases/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += mirrorbrain.conf.CSW

PATCHFILES += 0001-New-locations-for-GeoIP-databases.patch

# We really do only care for MirrorBrain on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = COPYING

WORKSRC = $(WORKDIR)/$(DISTNAME)/mb

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = /etc/mirrorbrain\.conf
REINPLACE_WITH_conf = $(sysconfdir)/mirrorbrain.conf
REINPLACE_FILES_conf += mb.py
REINPLACE_FILES_conf += mb/conf.py

REINPLACEMENTS += scanner
REINPLACE_MATCH_scanner = /usr/bin/scanner
REINPLACE_WITH_scanner = $(bindir)/scanner
REINPLACE_FILES_scanner += mb.py

PACKAGES += CSWpy-mb
SPKG_DESC_CSWpy-mb = Python module used by the MirrorBrain commandline tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-mb += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-mb += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-mb += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-mb += CSWpy-cmdln
RUNTIME_DEP_PKGS_CSWpy-mb += CSWpy-psycopg2
RUNTIME_DEP_PKGS_CSWpy-mb += CSWgeolitedb
# This is for the 'mb' executable
RUNTIME_DEP_PKGS_CSWpy-mb += CSWpython27
RUNTIME_DEP_PKGS_CSWpy-mb += CSWpy-sqlobject
# checkpkg cannot detect these deps
CHECKPKG_OVERRIDES_CSWpy-mb += surplus-dependency|CSWpy-cmdln
CHECKPKG_OVERRIDES_CSWpy-mb += surplus-dependency|CSWpy-psycopg2
CHECKPKG_OVERRIDES_CSWpy-mb += surplus-dependency|CSWgeolitedb
CHECKPKG_OVERRIDES_CSWpy-mb += surplus-dependency|CSWpython27
CHECKPKG_OVERRIDES_CSWpy-mb += surplus-dependency|CSWpy-sqlobject

# PATH gets an additionally /usr/share/mirrorbrain, what for? Overwrite for now.
CHECKPKG_OVERRIDES_CSWpy-mb += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/mb/geoip.py
CHECKPKG_OVERRIDES_CSWpy-mb += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/mb/geoip.py

PRESERVECONF += $(sysconfdir)/mirrorbrain.conf

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

post-merge-all:
	ginstall -D -m 0640 $(WORKDIR)/mirrorbrain.conf.CSW $(PKGROOT)$(sysconfdir)/mirrorbrain.conf.CSW
