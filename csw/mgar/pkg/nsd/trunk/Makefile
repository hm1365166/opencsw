NAME = nsd
VERSION = 4.0.3
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = An authoritative only non-recursive name server
define BLURB
  NSD (Name Server Daemon) is a complete implementation of an
  authoritative DNS nameserver.
endef

MASTER_SITES = http://www.nlnetlabs.nl/downloads/nsd/
SPKG_SOURCE_URL = http://www.nlnetlabs.nl/projects/nsd/

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://www.nlnetlabs.nl/downloads/nsd/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWn = CSWlibssl1-0-0
RUNTIME_DEP_PKGS += CSWlibevent2-0-5KGS = CSWlibssl1-0-0
CATALOGNAME = nsd
SPKG_DESC = An authoritative only non-recursive name server
PACKAGING_PLATFORMS =  solaris10-sparc solaris10-i386
LICENSE = LICENSE

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswusergroup
DISTFILES += cswnsd

SPKG_CLASSES = none cswusergroup ugfiles cswcpsampleconf cswinitsmf
PROTOTYPE_FILTER = awk '$$$$3 ~ /\/init.d\/cswnsd$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/CSWnsd\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } $$$$3 ~ /\/nsd\/nsd.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$2 = "ugfiles" }  $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$5 = "nsd" } $$$$3 ~ /\/var\/opt\/csw\/nsd/ { $$$$6 = "nsd" } $$$$3 ~ /\/var\/run/ { $$$$6 = "sys" } { print }'

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw
CONFIlibeventE_ARGS += --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-pidfile=/var/run/nsd.pid
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --with-dbfile=/var/opt/csw/nsd/nsd.db
CONFIGURE_ARGS += --with-difffile=/var/opt/csw/nsd/ixfr.db
CONFIGURE_ARGS += --with-xfrdfile=/var/opt/csw/nsd/xfrd.s#CHECKPKG_OVERRIDES_CSWnsd += bad-location-of-file|file=/tmp.state

SKIPTEST = 1

post-install-modulated:
	@ginstall -d $(DESTDIR)/var/opt/csw/nsd
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWnsd
	@ginstall -m 755 $(FILEDIR)/cswnsd $(DESTDIR)/etc/opt/csw/init.d/cswnsd
	@mv $(DESTDIR)/etc/opt/csw/nsd/nsd.conf.sample $(DESTDIR)/etc/opt/csw/nsd/nsd.conf.CSW
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/	@rmdir $(DESTDIR)/tmp

include gar/category.mk
