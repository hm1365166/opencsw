# $Id$
#
NAME 		= nagios-plugins
VERSION 	= 1.5
GARTYPE 	= v2

#
# package definitions
#

PACKAGES 			= CSWnagios-plugins
CATALOGNAME_CSWnagios-plugins 	= nagios_plugins

OBSOLETED_BY_CSWnagios-plugins	= CSWnagiosp
CATALOGNAME_CSWnagiosp 	= nagiosp_stub

SPKG_DESC_CSWnagios-plugins = Plugins for Nagios

MASTER_SITES 	 = http://assets.nagios.com/downloads/nagiosplugins/
DISTFILES  	 = $(DISTNAME).tar.gz
DISTFILES	+= README.CSW

PATCHFILES	+= 0002-Use-32-bit-pst3-on-Solaris.patch

#REINPLACE_USRLOCAL += contrib/*
REINPLACE_USRLOCAL += plugins/*
REINPLACE_USRLOCAL += plugins-scripts/*
#REINPLACE_USRLOCAL += ChangeLog
REINPLACE_USRLOCAL += README

POSTMSG		+= /opt/csw/share/doc/nagios-plugins/README.CSW

# check_swap won't be compiled if --enable-largefile is provided. So
# we employ a modulation using --disable-largefile which builds
# check_swap. This is the only file from that particular modulation
# that makes it into the final package (so far).
EXTRA_MODULATORS = FILEBITS
MODULATIONS_FILEBITS = large small

CONFIGURE_ARGS_isa-sparcv8plus-filebits-large = --enable-largefile
CONFIGURE_ARGS_isa-sparcv8plus-filebits-small = --disable-largefile

CONFIGURE_ARGS_isa-pentium_pro-filebits-large = --enable-largefile
CONFIGURE_ARGS_isa-pentium_pro-filebits-small = --disable-largefile

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --with-trusted-path=/bin:/sbin:/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin
CONFIGURE_ARGS += --with-mysql=/opt/csw
CONFIGURE_ARGS += --with-pgsql=/opt/csw/postgresql
CONFIGURE_ARGS += --libexecdir=$(prefix)/libexec/nagios-plugins
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --with-gnutls=/opt/csw
CONFIGURE_ARGS += --with-fping-command=/opt/csw/sbin/fping
CONFIGURE_ARGS += --with-trusted-path=/usr/bin:/usr/sbin:/opt/csw/bin:/opt/csw/sbin:$(prefix)/libexec/nagios-plugins
CONFIGURE_ARGS += --with-ping6-command="/usr/sbin/ping -A inet6 -s %s 56 %d"
CONFIGURE_ARGS += --with-snmpget-command=/opt/csw/bin/snmpget
CONFIGURE_ARGS += --with-snmpgetnext-command=/opt/csw/bin/snmpgetnext
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MODULATION))

CHECKPKG_OVERRIDES_CSWnagios-plugins += forbidden-version-interface-dependencies

libexecdir 	?= $(prefix)/libexec/nagios-plugins

EXTRA_INC += /opt/csw/postgresql/include
EXTRA_LIB += /opt/csw/postgresql/lib

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibintl8
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibpq5
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWperl
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWnetsnmp
RUNTIME_DEP_PKGS_CSWnagios-plugins += CSWlibdbi1

# Add this override for now
CHECKPKG_OVERRIDES_CSWnagios-plugins += surplus-dependency|CSWnetsnmp

BUILD_DEP_PKGS	+= CSWmysql-dev
BUILD_DEP_PKGS	+= CSWpostgresql-dev
BUILD_DEP_PKGS	+= CSWlibz-dev
BUILD_DEP_PKGS	+= CSWlibnet-dev

# Testsuite is interactive
SKIPTEST ?= 1

DOCS += FAQ README REQUIREMENTS SUPPORT COPYING 
DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
ROOT_PLUGINS = check_dhcp check_icmp pst3
PLUGINDEST = $(DESTDIR)$(libexecdir)

MERGE_SCRIPTS_isa-sparcv8plus-filebits-large = copy-all
MERGE_SCRIPTS_isa-sparcv8plus-filebits-small = copy-fb-small-only

MERGE_SCRIPTS_isa-pentium_pro-filebits-large = copy-all
MERGE_SCRIPTS_isa-pentium_pro-filebits-small = copy-fb-small-only

include gar/category.mk
post-install-modulated:
	@ginstall -m 755 -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 755 -d $(PLUGINDEST)
	@ginstall -m 644 $(FILEDIR)/README.CSW $(DOCDEST)
	@$(foreach PLUGIN,$(ROOT_PLUGINS),ginstall -m 4755 $(WORKSRC)/plugins-root/$(PLUGIN) $(PLUGINDEST);)
	@( cd $(WORKSRC) ; tar cf contrib.tar contrib ; gzip contrib.tar)
	@ginstall -m 755 -d $(DOCDEST)
	@ginstall -m 644 $(WORKSRC)/contrib.tar.gz $(DOCDEST)
	@$(MAKECOOKIE)

post-merge:
	@-rm $(PKGROOT)$(libdir)/charset.alias
	@$(MAKECOOKIE)

merge-copy-fb-small-only:
	cp $(INSTALLISADIR)$(libexecdir)/check_swap $(PKGROOT)$(libexecdir)/check_swap
	@$(MAKECOOKIE)
