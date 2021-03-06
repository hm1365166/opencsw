# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xpra
VERSION = 0.3.4
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Screen for X
define BLURB
  Xpra is 'screen for X': it allows you to run X programs, usually on a remote host, direct their display to your local machine, and then to disconnect from these programs and reconnect from the same or another machine, without losing any state. It gives you remote access to individual applications.
Xpra is "rootless" or "seamless": programs you run under it show up on your desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt to changing network bandwidth limits.
endef

MASTER_SITES = http://xpra.org/src/
DISTFILES  = $(DISTNAME).tar.bz2

BUILD_DEP_PKGS += CSWpy-gobject-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibxtstdevel
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibxfixesdevel
BUILD_DEP_PKGS += CSWlibxcompositedev
BUILD_DEP_PKGS += CSWlibxdamagedevel
BUILD_DEP_PKGS += CSWlibxrandrdevel
BUILD_DEP_PKGS += CSWx11recordproto
BUILD_DEP_PKGS += CSWlibxextdevel
BUILD_DEP_PKGS += CSWx11fixesproto
BUILD_DEP_PKGS += CSWx11compositeproto
BUILD_DEP_PKGS += CSWx11damageproto
BUILD_DEP_PKGS += CSWx11randrproto
BUILD_DEP_PKGS += CSWcython
BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWlibx264-dev
BUILD_DEP_PKGS += CSWffmpeg-dev

REINPLACE_USRSHARE += $(SITE_PACKAGES)/xpra/xposix/gui.py
REINPLACE_USRSHARE += $(SITE_PACKAGES)/xpra/platform/client_extras_base.py
REINPLACE_WHEN_USRSHARE = postinstall
REINPLACE_USRLOCAL += $(SITE_PACKAGES)/xpra/xposix/gui.py
REINPLACE_WHEN_USRLOCAL = postinstall

PACKAGE += CSWxpra

RUNTIME_DEP_PKGS_CSWxpra += CSWpython
RUNTIME_DEP_PKGS_CSWxpra += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWxpra += CSWlibavcodec54 
RUNTIME_DEP_PKGS_CSWxpra += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWpango
RUNTIME_DEP_PKGS_CSWxpra += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWxpra += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWxpra += CSWlibxdamage
RUNTIME_DEP_PKGS_CSWxpra += CSWlibxcomposite
RUNTIME_DEP_PKGS_CSWxpra += CSWlibx264-125
RUNTIME_DEP_PKGS_CSWxpra += CSWlibxfixes
RUNTIME_DEP_PKGS_CSWxpra += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWxpra += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWxpra += CSWlibxrandr
RUNTIME_DEP_PKGS_CSWxpra += CSWlibxtst

CHECKPKG_OVERRIDES_CSWxpra += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWxpra += catalogname-does-not-start-with-py_

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = python
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

BUILD_ENV += PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig:/opt/csw/X11/lib/pkgconfig
BUILD_ENV += CC=/opt/solarisstudio12.3/bin/cc
PYBUILD_CMD = build_ext
BUILD_ARGS += --without-vpx
BUILD_ARGS += --rpath=$(libdir):$(prefix)/X11/lib

INSTALL_ENV += $(BUILD_ENV)
INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)
INSTALL_ARGS += --without-vpx

include gar/category.mk

build-python:
	(cd $(WORKSRC); \
	python make_constants_pxi.py wimpiggy/lowlevel/constants.txt wimpiggy/lowlevel/constants.pxi; \
	$(BUILD_ENV) python setup.py $(PYBUILD_CMD) $(BUILD_ARGS))
	$(MAKECOOKIE)

