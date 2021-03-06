# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = zabbix
VERSION = 2.2.8
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Zabbix monitoring system
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-spREINPLACEMENTS += etc
REINPLACE_MATCH_etc = /usr/local/etc
REINPLACE_WITH_etc = $(sysconfdir)
REINPLACE_FILES_etc += conf/zabbix_proxy.confsparc solaris10-i386

# This is just for the server which is in 64 bit only on Solars 10
BUILD64-5.9 =
BUILD64-5.10 = 1
BUILD64 = $(BUILD64-$(GAROBUILD_DEP_PKGS += CSWlibiksemel-devROSREL))
ISAEXEC = 1

PACKAGES += CSWzabbix-agent
SPKG_DESC_CSWzabbix-agent = Zabbix monitoring system agent
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWzabbix-agent += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWzacurl4
RUNTIME_DEP_PKGS_CSWzabbix-agent += CSWlibssh2-1
RUNTIME_DEP_PKGS_CSWzabbix-agent += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWzabbix-agent += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWzabbix-agent += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWzabbix-agent += CSWliblber2-4-2

# These are just examplesb#bix_agentd.conf.CSW
CHECKPKG_OVERRIDES_CSWzabbix-agent += file-with-bad-content|/usr/local|root/opt/csw/share/man/m#bix_agentd.conf.CSW
CHECKPKG_OVERRIDES_CSWzabbix-agent += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/zabbix_sender.1
CHECKPKG_OVERRIDES_CSWzabbix-agent += file-with-bad-content|/usr/local|root/etc/opt/csw/zabbix_agentd.conf.CSW
CHECKPKG_OVERRIDES_CSWzabbix-agent += file-with-bad-content|/usr/local|root/etc/opt/csw/zabbix_agent.conf.CSW

PACKAGES-5.10 += CSWzabbix-server
PACKAGES += $(PACKAGES-$(GAROSREL))
SPKG_DESC_CSWzabbix-server = Zabbix monitoring system server
PKGFILES_CSWzabbix-server += $(call baseisadirs,$(sbindir),zabbix_server)
RUNTIME_DEP_PKGS_CSWzabmysqlclient18 CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWzabcurl4
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibnetsnmp30
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibssh2-1
RUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibldap2-4-2eRUNTIME_DEP_PKGS_CSWzabbix-server += CSWlibiksemel3er# MySQL uses gcc, so we need to do also or the compiler flags bust
GARCOMPILER = GCC4erver += CSWlibidn11

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql=$(bindir)/mysql_config
CONFIGURE_ARGS += --with-libcurl
CONFIGURE_ARGS += --enable-agent
CONFIGURE_ARGS += --enable-ipv6

# We build the server only on Solaris 10 and only on 64 bit
CONFIGURE_ARGS-5.9-32 += --disable-server
CONFIGURE_ARGS-5.10-32 += --disable-server
CONFIGURE_ARGS-5.10-64 += --enable-server
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSRECONFIGURE_ARGS += --enable-proxy

CONFIGURE_ARGS += --with-net-snmp
# This searches libssh2 in $(prefix)/lib regardless if we are building 64 bit or not
CONFIGURE_ARGS += --with-ssh2=$(prefix)
CONFIGURE_ARGS += --with-ldapRE# We need the latest Solaris 10 for the mysql bindings
LINKER_MAP_RELEASE =
CONFIGURE_ARGS += --with-mysql

# CONFIGURE_ARGS += --with-sqlite3
# CONFIGURE_ARGS += --with-postgresql
CONFIGURE_ARGS += --with-libcurl=$(prefix)/bin/curl-config

CONFIGURE_ARGS += --with-net-snmp=$(prefix)/bin/net-snmp-configRECONFIGURE_ARGS += --with-jabberREL)-$(MEMORYMODEL))

PRESERVECONF += $(sysconfdir)/zabbix_agent.conf
PRESERVECONF += $(sysconfdir)/zabbix_agentd.conf

inclu