NAME = tightvnc
VERSION = 1.3.10
CATEGORIES = utils

DESCRIPTION = TightVNC server is a free remote control package derived from the popular VNC software

define BLURB
  TightVNC is a free remote control software package. With TightVNC, you can see
  the desktop of a remote machine and control it with your local mouse and
  keyboard, just like you would do it sitting in the front of that computer.
endef

SF_PROJ = vnc-tight
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION)_unixsrc.tar.bz2
DISTFILES += vncservers
PACKAGES = CSWvncs CSWvncv
CATALOGNAME_CSWvncs = vncserver
CATALOGNAME_CSWvncv = vncviewer
SPKG_SOURCEURL = http://www.tightvnc.org/
UPSTREAM_USE_SF = 1
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=14067
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)_unixsrc.tar.bz2
DISTNAME = vnc_unixsrc
PKGFILES_CSWvncv  = $(bindir)/vncviewer
PKGFILES_CSWvncv += $(mandir)/man1/vncviewer\.1
SPKG_DESC_CSWvncs = TightVNC server
SPKG_DESC_CSWvncv = TightVNC viewer

RUNTIME_DEP_PKGS = CSWjpeg CSWtcpwrap CSWzlib
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

EXTRA_DEFINES = -DUSE_LIBWRAP=1
EXTRA_INC = /usr/openwin/share/include/X11
EXTRA_LDFLAGS = /opt/csw/lib
LOCAL_LDFLAGS = $(LINKER_FLAGS)
BUILD_OVERRIDE_DIRS = EXTRA_DEFINES EXTRA_INCLUDE LOCAL_LDFLAGS
CONFIGURE_SCRIPTS = $(WORKSRC)/Imakefile
# Xvnc
CONFIGURE_ARGS = -a
BUILD_SCRIPTS = vnc Xvnc
TEST_SCRIPTS =
INSTALL_SCRIPTS = vnc
# This patch has been sent upstream with a bug report.
# http://sourceforge.net/tracker/?func=detail&aid=2852808&group_id=14067&atid=114067
# PATCHFILES += 0002-Test-for-Makefile-presence.patch
#
PATCHFILES  = 0001-Sun-compiler-in-sun.cf.patch
PATCHFILES += 0002-pass-f-xmakefile-flag-when-appropriate.patch
PATCHFILES += 0003-GNU-make-by-default.patch

include gar/category.mk

pre-configure-modulated:
	perl -pi -e "s|/usr/local/vnc/classes|$(datadir)/vnc/classes|" $(WORKSRC)/vncserver
	@$(MAKECOOKIE)

configure-Xvnc:
	banner "Config Xvnc"
	perl -pi -e "s|^(\s*make)\s*$$|\1 CC=$(CC)|" $(WORKSRC)/Xvnc/configure
	(cd $(WORKSRC)/Xvnc && $(BUILD_ENV) ./configure)
	@$(MAKECOOKIE)

build-vnc:
	banner "Build VNC"
	cd $(WORKSRC) && $(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") World
	# $(MAKE) -C $(WORKSRC) $(BUILD_ENV) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") World
	@$(MAKECOOKIE)

build-Xvnc: configure-Xvnc
	# $(MAKE) -C $(WORKSRC) $(BUILD_ENV) EXTRA_LIBRARIES="-lwrap" EXTRA_DEFINES="-DUSE_LIBWRAP=1" World
	# banner "Config Xvnc"
	# (cd $(WORKSRC)/Xvnc && $(BUILD_ENV) ./configure)
	banner "Build Xvnc"
	$(MAKE) -C $(WORKSRC)/Xvnc $(BUILD_ENV) EXTRA_LIBRARIES="-lwrap -lsocket" EXTRA_DEFINES="-DUSE_LIBWRAP=1" EXTRA_LDOPTIONS="-L/opt/csw/lib -L/usr/lib" World
	# cd $(WORKSRC) && $(MAKE) $(BUILD_ENV) EXTRA_LIBRARIES="-lwrap" EXTRA_DEFINES="-DUSE_LIBWRAP=1" World
	# cd $(WORKSRC)/Xvnc && $(MAKE) $(BUILD_ENV) EXTRA_LIBRARIES="-lwrap -lsocket" EXTRA_DEFINES="-DUSE_LIBWRAP=1" EXTRA_LDOPTIONS="-L/opt/csw/lib -L/usr/lib" World
	@$(MAKECOOKIE)

install-vnc:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	(cd $(WORKSRC); ./vncinstall $(DESTDIR)$(bindir) $(DESTDIR)$(mandir))
	ginstall -d $(DESTDIR)$(datadir)/vnc
	(cd $(WORKSRC); cp -pR classes $(DESTDIR)$(datadir)/vnc)
	#mkdir -p %{buildroot}/etc/rc.d/init.d
	#install -m755 vncserver.init %{buildroot}/etc/rc.d/init.d/vncserver
	ginstall -d $(DESTDIR)$(sysconfdir)/vncservers
	ginstall -m 644 $(WORKDIR)/vncservers $(DESTDIR)$(sysconfdir)/vncservers
