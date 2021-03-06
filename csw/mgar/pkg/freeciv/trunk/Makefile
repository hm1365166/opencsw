NAME = freeciv
VERSION = 2.4.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Free turn-based multiplayer strategy game
define BLURB
Freeciv is a Free and Open Source empire-building strategy game inspired by the history of human civilization. The game commences in prehistory and your mission is to lead your tribe from the stone age to the space age...
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(NAMbz2-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=138322
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibiconv2
RUNTIME_DEP_PKGS_CSz1
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibintl8
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibreadline6eciv += CSWfconfig
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWsdlmixer
RUNTIME_DEP_PKGS_CSWdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibgdk-x11-eeciv RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWliblzma5
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWfreeciv += CSWsdlimage
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibpq5
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWfreeciv += CSWlibmysqlclient18 += CSWlibgio2-0-0

GARCOMPILER = GNU

PATCHFILES += 0001-use-finite-i-functionnstead-PATCHFILES += 0002-restore-previous-version-tile.hnstead-of-isfinite.patch

TEST_SCRIPTS =

CONFIGURE_ARCONFIGURE_ARGS += --enable-fcdb=all
CONFIGURE_ARGS += --enable-client=gtk2,sdl,xaw

# Disable linker map forcing SUNW_1.22.2 as the linked MySQL needs SUNW_1.22.5
LINKER_MAPS =RGS += $(DIRPATHS)

# build package on Solaris 10
PACKAGING_PLATFORMS = solaris10-spar# work around ld out of sync on buildfarm
CHECKPKG_OVERRIDES_CSWfreeciv += surplus-dependency|CSWlibfreetypeparc solaris10-i386

include gar/category.mk

post-install-modulated:

	perl -pi -e 's|/usr/local|/opt/csw|' \
		$(DESTDIR)/opt/csw/share/man