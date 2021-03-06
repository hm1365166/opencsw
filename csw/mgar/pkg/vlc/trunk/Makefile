# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# Compilations fails:
#
# ! In file included from libvlc.c:39:0:
# ../include/vlc_common.h: In function 'vlc_memalign':
# ../include/vlc_common.h:940:5: error: implicit declaration of function 'posix_memalign' [-Werror=implicit-function-declaration]

NAME = vlc
VERSION = 2.0.5
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = VideoLAN Client, the cross-platform media player and streaming server
deMASTER_SITES = http://download.videolan.org/pub/videolan/vlc/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.xz

PATCHFILES += 0006-Define-Encoding-in-vlc.desktop.patcharc solaris10-i386

VENDOR_URL = http://www.videolan.org/vlc/

BUILD_DEP_PKGS += CSWliba52
BUILD_DEP_PKGS += CSWlibxcbdevel
BUILD_DEP_PKGS += CSWlibxaudevel
BUILD_DEP_PKGS += CSWlibxdmcpdevel
BUILD_DEP_PKGS BUILD_DEP_PKGS += CSWautoconf
BUILD_DEP_PKGS += CSWautomake
BUILD_DEP_PKGS += CSWlibtool BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWffmpeg-dev $(prefix)/X11/lib

# Sun Studio implements packed attributes differently and compilations bails out:
#   "include/vlc_codecs.h", line 36: #error: FIXME
# GARCOMPILER = SOS12U2
GARtensions -fast

# Solaris has MAXNAMELEN instead of NAME_MAX
EXTRA_CFLAGS += -DNAME_MAX=MAXNAMLEN
# Necessary to include _Xglobal_lock
EXTRA_CFLAGS += -DXTHREADS

# For inet_pton
EXTRA_LINKER_FLAGS = -lsocket -lnsl

# For missing /opt/csw/lib/libgconf-2.la and /opt/csw/lib/libgconf-2.la
STRIP_LIBTOOL = 1

CONFIGURE_ARGS += $(DIRPATHS)

# Not there yet, part of ffmpeg
# CONFIGURE_ARGS += --disable-avcodec

# No QT4 yet
CONFIGURE_ARGS += --disable-qt4
CONFIGURE_ARGS += --disable-skins2

EXTRA_CFLAGS_i386 += -mfpmath=sse -msse
EXTRA_CXXFLAGS_i386 += -mfpmath=sse -msse
EXTRA_CFLAGS += $(EXTRA_CFLAGS_$(GARCH))

CONFIGURE_ARGS += --disable-mmx
CONFIGURE_ARGSCONFIGURE_ARGS += --disable-mad

# There's a problem with the library not being found even though it's
# installed.
# BUILD_DEP_PKGS += CSWlibtheora-dev
# CONFIGURE_ARGS += --enable-theora
CONFIGURE_ARGS += --disable-theoraS += --disable-sse

# Taken from http://wiki.videolan.org/Solaris
# CONFIGURE_ARGS += --disable-libgcrypt
# CONFIGURE_ARGS += --disable-remoteosd
# CONFIGURE_ARGS
# Trouble building with lua.
# /opt/csw/bin/luac: lua/playlist/appletrailers.lua:70: invalid escape sequence near '\.'
CONFIGURE_ARGS += --disable-lua
# BUILD_DEP_PKGS += CSWlua-dev
# RUNTIME_DEP_PKGS_CSWvlc += CSWlua
S += --disable-mad
# CONFIGURE_ARGS += --disable-swscale
# CONFIGURE_ARGS += --disable-postproc
# CONFIGURE_ARGS += --disable-a52
# CONFIGURE_ARGS += --disable-fribidi
# CONFIGURE_ARGS += --with-gnu-ld=no
CONFIGURE_ARGS += --disable-xcb
CONFIGURE_ARGS += --enable-sqlite

SKIPTEST = 1

PACKAGES = CSWvlc
# The catch-all package
SPKG_DESC_CSWvlc = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWvlc += CSWfconfig
RUNTIME_DEP_PKGS_CSWvlc += CSWfribidi
RUNTIME_DEP_PKGS_CSWvlc += CSWliba52
RUNTIME_DEP_PKGS_CSWvlc += CSWlibavcodec53
RUNTIME_DEP_PKGS_CSWvlc += CSWlibavformat53
RUNTIME_DEP_PKGS_CSWvlc += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWvlc += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWvlc += CSWlibdvdread
RUNTIME_DEP_PKGS_CSWvlc += CSWlibflac8
RUNTIME_DEP_PKGS_CSWvlc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWvlc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWvlc += CSWlibkate1
RUNTIME_DEP_PKGS_CSWvlc += CSWlibmad0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibogg0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibpostproc52
RUNTIME_DEP_PKGS_CSWvlc += CSWlibproxy
RUNTIME_DEP_PKGS_CSWvlc += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWvlc += CSWlibsamplerate0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibsmbclient0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWvlc += CSWlibspeexdsp1
RUNTIME_DEP_PKGS_CSWvlc += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWvlc += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWvlc += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWvlc += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWvlc += CSWlibvlc5
RUNTIME_DEP_PKGS_CSWvlc += CSWlibvlccore5
RUNTIME_DEP_PKGS_CSWvlc += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWvlc += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWvlc += CSWlibx264-120
RUNTIME_DEP_PKGS_CSWvlc += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWvlc += CSWlibz1
RUNTIME_DEP_PKGS_CSWvlc += CSWsdlimage

# Only needed on Sparc. Not sure why, to be investigated.
RUNTIME_DEP_PKGS_CSWvlc_sparc += CSWlibtheora0
RUNTIME_DEP_PKGS_CSWvlc_sparc += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWvlc += $(RUNTIME_DEP_PKGS_CSWvlc_$(GARCH))

CHECKPKG_OVERRIDES_CSWvlc += file-with-bad-content|/usr/share|root/opt/csw/share/vlc/utils/audio-vlc-default.sh
CHECKPKG_OVERRIDES_CSWvlc += file-with-bad-content|/usr/share|root/opt/csw/share/vlc/utils/video-vlc-default.sh
CHECKPKG_OVERRIDES_CSWvlc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/vlc/intf-vcd.txt
CHECKPKG_OVERRIDES_CSWvlc += file-with-bad-content|/usr/share|root/opt/csw/share/doc/vlc/vlc-thumb.c

PACKAGES += CSWvlc-dev
CATALOGNAME_CSWvlc-dev = vlc_dev
SPKG_DESC_CSWvlc-dev += $(DESCRIPTION), development files
PKGFILES_CSWvlc-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWvlc-dev += CSWlibvlc5
RUNTIME_DEP_PKGS_CSWvlc-dev += CSWlibvlccore5

PACKAGES += CSWlibvlc5
CATALOGNAME_CSWlibvlc5 = libvlc5
PKGFILES_CSWlibvlc5 += $(call baseisadirs,$(libdir),libvlc\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibvlc5 += $(DESCRIPTION), libvlc.so.5
RUNTIME_DEP_PKGS_CSWlibvlc5 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibvlc5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibvlc5 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibvlc5 += CSWlibvlccore5

PACKAGES += CSWlibvlccore5
CATALOGNAME_CSWlibvlccore5 = libvlccore5
PKGFILES_CSWlibvlccore5 += $(call baseisadirs,$(libdir),libvlccore\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibvlccore5 += $(DESCRIPTION), libvlccore.so.5
RUNTIME_DEP_PKGS_CSWlibvlccore5 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibvlccore5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibvlccore5 += CONFIG_SHELL

include gar/category.mk

pre-configure-modulated:
	# bootstrap defines #!/bin/sh and $(dirname ...)
	(cd $(WORKSRC) && $(CONFIGURE_ENV) \
		CONFIG_SHELL=/opt/csw/bin/bash \
		/opt/csw/bin/bash \
		./bootstrap)
	@$(MAKECOOKIE)

PATH := /op