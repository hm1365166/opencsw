NAME = sudo
VERSION = 1.7.2
CATEGORIES = utils
RELEASE = p4

DISTVERSION = $(VERSION)$(RELEASE)
DISTNAME = $(NAME)-$(DISTVERSION)

DESCRIPTION = Provides limited super user privileges
define BLURB
  Sudo (superuser do) allows a system administrator to give certain users (or
  groups of users) the ability to run some (or all) commands as root while
  logging all commands and arguments. Sudo operates on a per-command basis, it
  is not a replacement for the shell.
endef

MASTER_SITES = ftp://ftp.sudo.ws/pub/sudo/
DISTFILES  = $(NAME)-$(DISTVERSION).tar.gz 
PATCHFILES = install.diff

# We define upstream file regex so we can be notifed of new 
# upstream software release
UFILES_REGEX = $(NAME)-((\d+(?:\.\d+)*)(p\d+)?).tar.gz

PACKAGES = CSWsudo CSWsudo-common

CATALOGNAME_CSWsudo = sudo
SPKG_DESC_CSWsudo = $(DESCRIPTION)
SPKG_SOURCEURL_CSWsudo = http://www.sudo.ws
RUNTIME_DEP_PKGS_CSWsudo = CSWsudo-common CSWggettextrt

CATALOGNAME_CSWsudo-common = sudo_common
SPKG_DESC_CSWsudo-common = Common files for sudo
SPKG_SOURCEURL_CSWsudo-common = http://www.sudo.ws
RUNTIME_DEP_PKGS_CSWsudo-common = CSWggettextrt

DISTFILES += CSWsudo-common.postinstall 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-logging=both
CONFIGURE_ARGS += --with-ignore-dot
CONFIGURE_ARGS += --with-env-editor
CONFIGURE_ARGS += --disable-path-info
CONFIGURE_ARGS += --with-logpath=/var/opt/csw/sudo/logs/sudolog
ifneq ($(shell uname -r),5.8)
    CONFIGURE_ARGS += --with-project
endif

TEST_TARGET = check
FIXCONFIG_DIRS = $(DESTDIR)$(libexecdir)

include gar/category.mk

PKGFILES_CSWsudo  = .*$(bindir).*/sudo.minimal

LICENSE = LICENSE

post-install-modulated:
	@( cd $(DESTDIR)$(bindir) ; gmv sudo sudo.minimal )
	@( cd $(DESTDIR)$(bindir) ; gln -s sudo.minimal sudo )
	@( cd $(DESTDIR)$(bindir) ; grm -f sudoedit )
	@( cd $(DESTDIR)$(bindir) ; gcp sudo.minimal sudoedit )
	@( cd $(DESTDIR)$(sysconfdir) ; gmv sudoers sudoers.CSW )
	@$(MAKECOOKIE)

post-merge-modulated:
	@( cd $(PKGROOT)$(bindir); \
		gfind . -type f -name sudo\* -exec gchmod 4755 {} \; )
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)
