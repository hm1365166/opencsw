# $Id$

NAME = libgnet2
VERSION = 2.0.8
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Network library based on glib2
define BLURB
  GNet is a simple network library. It is written in C, object-oriented,
  and built upon GLib. It is intended to be easy to use and port.
endef

DISTNAME		=	gnet-$(VERSION)
MASTER_SITES	=	http://ftp.gnome.org/pub/GNOME/sources/gnet/2.0/
DISTFILES		=	$(DISTNAME).tar.gz
DISTFILES		+=	GNUMakefile

# until the glib development package is installed on Solaris 9 we
# limit the scope:
PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev

CONFIGURE_ARGS = $(DIRPATHS)

GARCOMPILER			=	GNU

INSTALL_ARGS	+=	TARGET_DIR=$(docdir)/$(NAME)_doc/html

PACKAGES					+=	CSWlibgnet2-doc
SPKG_DESC_CSWlibgnet2-doc	=	$(DESCRIPTION), documentation
OBSOLETED_BY_CSWlibgnet2-doc=	CSWlibgnet2doc
CATALOGNAME_CSWlibgnet2doc	=	libgnet2_doc_stub
ARCHALL_CSWlibgnet2-doc		=	1

PACKAGES							+=	CSWlibgnet2-0-0
CATALOGNAME_CSWlibgnet2-0-0			=	libgnet2_0_0
PKGFILES_CSWlibgnet2-0-0			+=	$(call baseisadirs,$(libdir),libgnet-2\.0\.so\.0\.8\.0)
PKGFILES_CSWlibgnet2-0-0			+=	$(call baseisadirs,$(libdir),libgnet-2\.0\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgnet2-0-0			=	$(DESCRIPTION), libgnet-2.0.so.0
OBSOLETED_BY_CSWlibgnet2-0-0		=	CSWlibgnet2rt
CATALOGNAME_CSWlibgnet2rt			=	libgnet2_rt_stub
RUNTIME_DEP_PKGS_CSWlibgnet2-0-0	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgnet2-0-0	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnet2-0-0	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgnet2-0-0	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgnet2-0-0	+=	CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibgnet2-0-0 += surplus-dependency|CSWlibiconv2

PACKAGES							+= CSWlibgnet2-dev
SPKG_DESC_CSWlibgnet2-dev			=	$(DESCRIPTION), development files
PKGFILES_CSWlibgnet2-dev			+=	/opt/csw/lib/libgnet-2.0.so
PKGFILES_CSWlibgnet2-dev			+=	$(PKGFILES_DEVEL)
PKGFILES_CSWlibgnet2-dev			+=	/opt/csw/lib/gnet-2.0/include/gnetconfig.h
OBSOLETED_BY_CSWlibgnet2-dev		=	CSWlibgnet2
CATALOGNAME_CSWlibgnet2				=	libgnet2_stub
ARCHALL_CSWlibgnet2-dev				=	1
RUNTIME_DEP_PKGS_CSWlibgnet2-dev	+=	CSWlibgnet2-0-0
CHECKPKG_OVERRIDES_CSWlibgnet2-dev += archall-devel-package

include gar/category.mk

post-install-modulated:
	ginstall --directory $(DESTDIR)$(docdir)/$(NAME)_doc/examples
	cd $(WORKSRC)/examples && ginstall --preserve-timestamps --mode=u=rw,go=r *.c $(DESTDIR)$(docdir)/$(NAME)_doc/examples
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKDIR)/GNUMakefile $(DESTDIR)$(docdir)/$(NAME)_doc/examples
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
