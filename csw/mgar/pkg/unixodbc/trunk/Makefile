# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = unixodbc
VERSION = 2.3.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = ODBC drivers for Unix systems
define BLURB
endef

MASTER_SITES = http://www.unixodbc.org/

DISTNAME = unixODBC-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

FOREIGN_PACKAGES += CSWlibodbc1
FOREIGN_PACKAGES += CSWlibodbccr1
FOREIGN_PACKAGES += CSWlibodbcinst1

PACKAGES += CSWunixodbc
SPKG_DESC_CSWunixodbc = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbcinst2
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbc2
# These are legacy dependencies for packages depending on CSWunixodbc and expecting *.so.1 libraries
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbc1
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbccr1
RUNTIME_DEP_PKGS_CSWunixodbc += CSWlibodbcinst1
CHECKPKG_OVERRIDES_CSWunixodbc += surplus-dependency|CSWlibodbcinst1
CHECKPKG_OVERRIDES_CSWunixodbc += surplus-dependency|CSWlibodbccr1
CHECKPKG_OVERRIDES_CSWunixodbc += surplus-dependency|CSWlibodbc1

PACKAGES += CSWunixodbc-dev
CATALOGNAME_CSWunixodbc-dev = unixodbc_dev
SPKG_DESC_CSWunixodbc-dev = Development files for libodbc*.so.2
PKGFILES_CSWunixodbc-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWunixodbc-dev += $(call baseisadirs,$(bindir),odbc_config)
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbc2
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbccr2
RUNTIME_DEP_PKGS_CSWunixodbc-dev += CSWlibodbcinst2

PACKAGES += CSWlibodbc2
SPKG_DESC_CSWlibodbc2 = $(DESCRIPTION), libodbc.so.2
PKGFILES_CSWlibodbc2 += $(call pkgfiles_lib,libodbc.so.2)
PKGFILES_CSWlibodbc2 += $(sysconfdir)/.*
RUNTIME_DEP_PKGS_CSWlibodbc2 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibodbc2 += CSWlibiconv2

PACKAGES += CSWlibodbccr2
SPKG_DESC_CSWlibodbccr2 = $(DESCRIPTION), libodbccr.so.2
PKGFILES_CSWlibodbccr2 += $(call pkgfiles_lib,libodbccr.so.2)

PACKAGES += CSWlibodbcinst2
SPKG_DESC_CSWlibodbcinst2 = $(DESCRIPTION), libodbcinst.so.2
PKGFILES_CSWlibodbcinst2 += $(call pkgfiles_lib,libodbcinst.so.2)
RUNTIME_DEP_PKGS_CSWlibodbcinst2 += CSWlibltdl7

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS += $(DIRPATHS)

PRESERVECONF += $(sysconfdir)/odbc.ini
PRESERVECONF += $(sysconfdir)/odbcinst.ini

MIGRATE_FILES_CSWunixodbc += odbc.ini
MIGRATE_FILES_CSWunixodbc += odbcinst.ini
MIGRATE_FILES_CSWunixodbc += ODBCDataSources

include
post-merge-all:
	gdiff -D 64bit \
		$(WORKROOTDIR)/install-isa-$(ISA_DEFAULT64)$(includedir)/unixodbc_conf.h \
		$(WORKROOTDIR)/install-isa-$(ISA_DEFAULT)$(includedir)/unixodbc_conf.h \
	| sed -e 's/ifndef 64bit/if defined __amd64 || defined __x86_64 || defined __sparcv9/' \
	> $(PKGROOT)$(includedir)/unixodbc_conf.h
	@$(MAKECOOKIE)
