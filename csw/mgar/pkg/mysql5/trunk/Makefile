# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mysql55
BASE_VERSION = 5.5
PATCHLEVEL = 9
VERSION = $(BASE_VERSION).$(PATCHLEVEL)
CATEGORIES = server
GARTYPE = v2

# Useful when making a series of builds on the same day
GARFLAVOR ?= DBG

DISTNAME = mysql-$(VERSION)
SPKG_SOURCEURL = http://www.mysql.com/

DESCRIPTION = Multithreaded SQL database server
define BLURB
  MySQL is a very fast, multi-threaded, multi-user and robust SQL
  (Structured Query Language) database server.
endef

# Change prefix to /opt/csw/$(NAME)
prefix = /opt/csw/$(NAME)
localstatedir = /var/opt/csw/$(NAME)
sysconfdir = /etc/opt/csw/$(NAME)

# Where to put the init script
global_sysconfdir = /etc/opt/csw
# Where to link the binaries
global_bindir = /opt/csw/bin

INITSMF = $(global_sysconfdir)/init\.d/cswmysql-$(BASE_VERSION)

PACKAGES  = CSW$(NAME) CSW$(NAME)bench CSW$(NAME)client CSW$(NAME)devel
PACKAGES += CSW$(NAME)rt CSW$(NAME)test

PATCHFILES  = 0001-Use-libc-not-libcrypt.patch
PATCHFILES += 0002-cast-user_info-pw_gid-to-gid_t.patch
PATCHFILES += 0003-OpenCSW-perl-for-tests.patch
PATCHFILES += 0004-basedir-and-datadir-in-the-cnf-files.patch

SPKG_DESC_CSW$(NAME)       = Multithreaded SQL database
SPKG_DESC_CSW$(NAME)bench  = MySQL $(BASE_VERSION) benchmarking
SPKG_DESC_CSW$(NAME)client = MySQL $(BASE_VERSION) client binaries
SPKG_DESC_CSW$(NAME)devel  = MySQL $(BASE_VERSION) header files
SPKG_DESC_CSW$(NAME)rt     = MySQL $(BASE_VERSION) runtime files
SPKG_DESC_CSW$(NAME)test   = MySQL $(BASE_VERSION) testing files

CATALOGNAME_CSW$(NAME)       = $(NAME)
CATALOGNAME_CSW$(NAME)bench  = $(NAME)bench
CATALOGNAME_CSW$(NAME)client = $(NAME)client
CATALOGNAME_CSW$(NAME)devel  = $(NAME)devel
CATALOGNAME_CSW$(NAME)rt     = $(NAME)rt
CATALOGNAME_CSW$(NAME)test   = $(NAME)test

# Defining the client programs, which are going to pick up the 32- and 64-bit
# binaries, symbolic links, isaexec stuff and man pages.
CSW$(NAME)client_programs  = myisamlog
CSW$(NAME)client_programs += myisampack
CSW$(NAME)client_programs += mysql
CSW$(NAME)client_programs += mysqlaccess
CSW$(NAME)client_programs += mysqladmin
CSW$(NAME)client_programs += mysqlbin
CSW$(NAME)client_programs += mysqlbinlog
CSW$(NAME)client_programs += mysqlcheck
CSW$(NAME)client_programs += mysql_client_test
CSW$(NAME)client_programs += mysqldump
CSW$(NAME)client_programs += mysqlhotcopy
CSW$(NAME)client_programs += mysqlimport
CSW$(NAME)client_programs += mysqlshow
CSW$(NAME)client_programs += mysql_zap
CSW$(NAME)client_programs += perror
CSW$(NAME)client_programs += replace

# Without this EXTRA_LD_OPTIONS setting, /opt/csw/bin/mysql fails with a shared
# library not found.  EXTRA_LIB was tried too, but did not work, as the -R path
# ended up with having two $ISALIST tokens.
#
# Without this setting it looks for:
# /opt/csw/$(NAME)/lib/amd64/libmysqlclient.so.15
# The library is at:
# /opt/csw/$(NAME)/lib/amd64/mysql/libmysqlclient.so.15
EXTRA_LD_OPTIONS  = -R$(libdir)/\$$ISALIST/mysql

CSW$(NAME)devel_programs += mysql_config

# Enable 64 bits build
BUILD64 = 1

PKGFILES_CSW$(NAME)bench   = $(prefix)/sql-bench.*
PKGFILES_CSW$(NAME)client  = $(bindir)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSW$(NAME)client += $(foreach bin_name,$(CSW$(NAME)client_programs),/opt/csw/sbin/$(bin_name))
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),$(call baseisadirs,$(bindir),$(bin_name)))
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),$(mandir)/man1/$(bin_name)\.1)
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),/opt/csw/bin/$(bin_name))
PKGFILES_CSW$(NAME)devel  += $(foreach bin_name,$(CSW$(NAME)devel_programs),/opt/csw/sbin/$(bin_name))
PKGFILES_CSW$(NAME)devel  += $(mandir)/man1/mysql_config\.1
PKGFILES_CSW$(NAME)devel  += $(prefix)/include.*
PKGFILES_CSW$(NAME)devel  += /opt/csw/include/mysql

PKGFILES_CSW$(NAME)rt      = $(libdir)
PKGFILES_CSW$(NAME)rt     += $(libdir)/.*
PKGFILES_CSW$(NAME)test    = $(prefix)/mysql-test.*

RUNTIME_DEP_PKGS_CSW$(NAME)            = CSW$(NAME)client
RUNTIME_DEP_PKGS_CSW$(NAME)           += CSW$(NAME)rt
RUNTIME_DEP_PKGS_CSW$(NAME)           += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)           += CSWzlib
RUNTIME_DEP_PKGS_CSW$(NAME)rt          = CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)rt         += CSWzlib
RUNTIME_DEP_PKGS_CSW$(NAME)bench       = CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME)bench      += CSWperl
RUNTIME_DEP_PKGS_CSW$(NAME)client      = CSW$(NAME)rt
RUNTIME_DEP_PKGS_CSW$(NAME)client     += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)client     += CSWncurses
RUNTIME_DEP_PKGS_CSW$(NAME)client     += CSWzlib
RUNTIME_DEP_PKGS_CSW$(NAME)devel       = CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME)test        = CSW$(NAME)
RUNTIME_DEP_PKGS_CSW$(NAME)test       += CSWperl

MASTER_SITES = ftp://mirror.switch.ch/mirror/mysql/Downloads/MySQL-$(BASE_VERSION)/
DISTFILES  = mysql-$(VERSION).tar.gz
DISTFILES += csw$(NAME) quick_start-csw README.CSW ChangeLog
DISTFILES += CSW$(NAME).preinstall
DISTFILES += CSW$(NAME).postinstall
DISTFILES += cswusergroup

UFILES_REGEX = mysql-(\d+(?:\.\d+)*).tar.gz

# TODO: Do the proper prerequsite pkgs.
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

# MySQL-5.1.40 doesn't compile without setting EXTRA_INC.
EXTRA_INC = /opt/csw/include
EXTRA_LIB = /opt/csw/lib

# The following EXTRA_CFLAGS are necessary to compile on Solaris 8. Otherwise
# the following problem occurs:
#
# "handler/i_s.cc", line 159: Error: The function "localtime_r" must have a
# prototype.
EXTRA_CFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__
EXTRA_CXXFLAGS = -mt -D_POSIX_C_SOURCE=199506L -D__EXTENSIONS__

# Set ./configure options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-assembler
# Why not have a docs package?
# CONFIGURE_ARGS += --without-docs
CONFIGURE_ARGS += --enable-local-infile
CONFIGURE_ARGS += --with-charset=utf8
CONFIGURE_ARGS += --with-extra-charsets=all
CONFIGURE_ARGS += --with-low-memory
CONFIGURE_ARGS += --with-pthread
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-zlib-dir=/opt/csw
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-plugins=max-no-ndb
CONFIGURE_ARGS += --with-comment
CONFIGURE_ARGS += --with-mysqld-libs=-lmtmalloc
CONFIGURE_ARGS += --with-big-tables
CONFIGURE_ARGS += --enable-thread-safe-client
CONFIGURE_ARGS_DBG = --with-debug
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))

# TODO: Make the tests pass. They don't at the moment.
SKIPTEST ?= 1
TEST_SCRIPTS = custom
TEST_TARGETS = check


USERGROUP = /etc/opt/csw/pkg/CSW$(NAME)/cswusergroup

PROTOTYPE_MODIFIERS = dbdir
PROTOTYPE_FILES_dbdir = $(localstatedir)
PROTOTYPE_USER_dbdir = mysql
PROTOTYPE_GROUP_dbdir = mysql
PROTOTYPE_PERMS_dbdir = 0700
PROTOTYPE_CLASS_dbdir = ugfiles

SPKG_CLASSES = none ugfiles

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))

test-custom:
	alias sh=/usr/bin/bash;                                 \
		cd $(WORKSRC)/mysql-test;                       \
		perl mysql-test-run.pl --mem --big-test --force \
		--skip-test=archive-big --skip-test=/gis/

pre-configure-modulated:
	# To work around the following libtool version mismatch problem:
	# libtool: Version mismatch error.  This is libtool 2.2.6, but the
	# libtool: definition of this LT_INIT comes from libtool 2.2.6b.
	# libtool: You should recreate aclocal.m4 with macros from libtool 2.2.6
	# http://lists.opencsw.org/pipermail/maintainers/2009-December/005066.html
	cd $(WORKSRC) && autoreconf --force --install --symlink
	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(localstatedir)
	ginstall -m 755 -d $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 644 $(FILEDIR)/ChangeLog $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 644 $(FILEDIR)/README.CSW $(PKGROOT)$(datadir)/mysql/doc
	ginstall -m 755 -d $(PKGROOT)/opt/csw/share/mysql/doc
	ln -sf ../../../$(NAME)/share/mysql/doc/README.CSW \
		$(PKGROOT)/opt/csw/share/mysql/doc/README.CSW
	ginstall -m 755 -d $(PKGROOT)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/csw$(NAME) $(PKGROOT)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/quick_start-csw $(PKGROOT)$(datadir)/mysql
	ginstall -m 755 -d $(PKGROOT)$(global_sysconfdir)/pkg/CSW$(NAME)
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		        $(PKGROOT)$(global_sysconfdir)/pkg/CSW$(NAME)
	# A symlink for mysql5 include files
	ginstall -m 755 -d $(PKGROOT)/opt/csw/include
	# I believe this is broken:
	ln -s ../$(NAME)/include/mysql $(PKGROOT)/opt/csw/include/mysql
	# Create symlinks to binaries
	ginstall -m 755 -d $(PKGROOT)$(global_bindir)
	for f in $(PKGROOT)$(bindir)/*; do \
		ln -s ../$(NAME)/bin/`basename $$f` \
		      $(PKGROOT)$(global_bindir)/`basename $$f`; \
	done
	# /opt/csw/$(NAME)/lib/sparc9/mysql -- by GAR, it's logical
	# /opt/csw/$(NAME)/lib/mysql/sparcv9 -- expected by other packages
	gln -s ../$(ISA_DEFAULT64)/mysql $(PKGROOT)$(libdir)/mysql/$(ISA_DEFAULT64)
	# For other applications to link against
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/mysql/64
	gln -s . $(PKGROOT)$(libdir)/$(ISA_DEFAULT)
	gln -s . $(PKGROOT)$(libdir)/mysql/$(ISA_DEFAULT)
	@$(MAKECOOKIE)
