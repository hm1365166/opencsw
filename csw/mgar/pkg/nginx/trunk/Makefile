NAME = nginx
VERSION = 1.7.10
GARTYPE = v2
GARCOMPILER = SOS11

DESCRIPTION = HTTP server and mail proxy server
define BLURB
  Nginx (pronounced "engine x") is a free, open-source, high-performance
  HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
endef

MASTER_SITES = http://nginx.org/downloaDISTNAME).tar.gz
DISTFILES   += cswnginx

LICENSEwnginx

LICENSE      = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar+= CSWlibxslt-dev
BUILD_DEP_PKGS += CSWgeoip-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibgd-dev
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWperl

PACKAGES += CSWnginx
SPKG_DESC_CSWnginx = HTTP server and mail proxy server
RUNTIME_DEP_PKGS_CSWnginx += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWnginx += CSWlibgeoip1
RUNTIME_DEP_PKGS_CSWnginx += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWnginx += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWnginx += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWnginx += CSWlibgd3
RUNTIME_DEP_PKGS_CSWnginx += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWnginx += CSWlibz1
parThere is just one script on contrib/, do not pull in Perl for that
CHECKPKG_OVERRIDES_CSWnginx += missing-dependency|CSWperl
parc solaris10-i386

# default sparc arch is set to sparcv8plus because nginx contains
# assembler parts specific to v8plus and v9 arches:
#	.inline ngx_casa,0
#	casa    [%o2] 0x80, %o1, %o0
#	.end
#
#	.inline ngx_casxa,0
#	casxa   [%o2] 0x8# These are the default now

#ISA_DEFAULT_sparc      = sparcv8plus
#EXTRA_BUILD_ISAS_i386  = pentium_pro amd64
#EXTRA_BUILD_ISAS_sparc = sparcv9

BUILD64 = 1
ISAEXEC = 1

NGINXCPU_i386          = pentium          = pentium3
NGINXCPU_pentium_pro   = pentium3
NGINXCPU_sparcv8plus   = sparc32
NGINXCPU_sparcv9       = sparc64
NGINXCPU_$(ISA)       ?= $(ISA)
NGINXCPU               = $(NGINXCPUtedir=/var/opt/csw

#CONFIGURE_ARGS += --with-debug
CONFIGURE_ARGS += --with-cpu-opt=$(NGINXCPU)
CONFIGURE_ARGS += --with-cc-opt="-I$(includedir) -I$(includedir)/openssl"
CONFIGURE_ARGS += --with-ld-opt="$(LDFLAGS)"
CONFIGURE_ARGS += --lock-path=/var/run/nginx/nginx.lock
CONFIGURE_ARGS += --pid-path=/var/run/nginx/nginx.pid
CONFIGURE_ARGS += --conf-path=$(sysconfdir)/nginx/nginx.conf
CONFIGURE_ARGS += --sbin-path=$(sbindir)/nginx
CONFIGURE_ARGS += --prefix=$(localstatedir)/nginx
CONFIGURE_ARGS += --http-client-body-temp-path=$(localstatedir)/nginx/client
CONFIGURE_ARGS += --http-fastcgi-temp-path=$(localstatedir)/nginx/fastcgi
CONFIGURE_ARGS += --http-scgi-temp-path=$(localstatedir)/nginx/scgi
CONFIGURE_ARGS += --http-uwsgi-temp-path=$(localstatedir)/nginx/uwsgi
CONFIGURE_ARGS += --http-proxy-temp-path=$(localstatedir)/nginx/proxy
CONFIGURE_ARGS += --error-log-path=$(localstatedir)/nginx/logs/error.log
CONFIGURE_ARGS += --http-log-path=$(localstatedir)/nginx/logs/access.log
CONFIGURE_ARGS += --with-ipv6
CONFIGURE_ARGS += --with-http_addition_module
CONFIGURE_ARGS += --with-http_dav_module
CONFIGURE_ARGS += --with-http_flv_module
CONFIGURE_mp4S += --with-http_flv_module
CONFIGURE_realip= --with-http_realip_module
CONFIGURE_ARGS += --with-http_secure_link_module
CONFIGURE_ssl_module
CONFIGURE_ARGS += --with-http_stub_status_module
CONFIGURE_ARGS += --with-http_gzip_static_module
CONFIGURE_ARGS += --with-http_geoip_module
CONFIGURE_ARGS += --with-http_xslt_module
CONFIGURE_ARGS += --with-http_image_filter_module
CONFIGURE_ARGS += --with-http_sub_module
CONFIGURE_ARGS += --with-http_random_index= --with-http_realip_module
CONFIGURE_ARGS += --with-http_secure_link_module
CONFIGURE_degradation_module
CONFIGURE_ARGS += --with-http_stub_status_module
CONFIGURE_ARGS += --with-http_spdy_module
# Enable when we have 64 bit perl
# CONFIGURE_ARGS += --with-http_perl_module
# Specifically enable legacy method for people who want that
CONFIGURE_ARGS += --with-select_module
CONFIGURE_ARGS += --with-poll_module

TEST_SCRIPTS =

INITSMF      = $(sysconfdir)/init.d/cswnginx
PRESERVECONF += $(sysconfdir)/nginx/fastcgi.conf
PRESERVECONF += $(sysconfdir)/nginx/fastcgi_params
PRESERVECONF += $(sysconfdir)/nginx/mime.types
PRESERVECONF += $(sysconfdir)/nginx/nginx.conf
PRESERVECONF += $(sysconfdir)/nginx/scgi_params
PRESERVECONF += $(sysconfdir)/nginx/uwsgi_params
PRESERVECONF += $(localstatedir)/nginx/html/50x.html
PRESERVECONF +=/nginx/html/50x.html $(localstatedir)/nginx/html/index.html

NGINXDOCS    = CHANGES CHANGES.ru LICENSE README


include gar/category.mk

post-configure-modulated:
	gsed -i  s#/...ISALIST#/'$$ISALIST'# $(WORKSRC)/objs/ngx_auto_config.h
	gsed -i 's#  pause#  rep; nop#'      $(WORKSRC)/src/os/unix/n@gx_sunpro_amd64.il
	$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(sysconfdir)/nginx/conf.d
	ginstall -d $(DESTDIR)$(sharedstatedir)/nginx/contrib
	ginstall -d $(DESTDIR)$(docdir)/nginx
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/client
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/fastcgi
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/logs
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/proxy
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/scgi
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/sites
	ginstall -d $(DESTDIR)$(localstatedir)/nginx/uwsgi
	cp $(WORKDIR)/cswnginx $(DESTDIR)$(sysconfdir)/init.d/
	cd $(WORKSRC); \
	cp -r contrib/* $(DESTDIR)$(sharedstatedir)/nginx/contrib; \
	cp $(NGINXDOCS) $(DESTDIR)$(docdir)/nginx
	rm -rf $(DEST@$(MAKECOOKIE)
