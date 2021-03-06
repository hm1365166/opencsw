# $Id$

NAME = tex_rcsinfo
VERSION = 1.11
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = Extract the information provided by the RCS revision control system from TeX documents
define BLURB
  This package is used to extract the revision and file information provided
  by the RCS revision control system.
  A PERL-package supporting rcsinfo and LaTeX2HTML is provided too.
endef

DISTNAME		=	rcsinfo
MASTER_SITES	=	http://mirror.ctan.org/macros/latex/contrib/
DISTFILES		=	$(DISTNAME).zip
# taken from http://www.latex-project.org/lppl.txt
DISTFILES		+=	README.CSW
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-Adapt-build.patch

BUILD_xlive
BUILD_DEP_PKGS		+=	CSWlatex2htmlP_PKGS	+=	CSWtetex

PACKAGES					=	CSWtex-rcsinfo
SPKG_DESC_CSWtex-rcsinfo	=	$(DESCRIPTION)
CATALOGNAME_CSWtex-rcsinfo	=	tex_rcsinfo
OBSOLETED_BY_CSWtex-rcsinfo	=	CSWtexrcsinfo
CATALOGNAME_CSWtexrcsinfo	=RUNTIME_DEP_PKGS	+=	CSWtexlive
CHECKPKG_OVERRIDES_CSWtex-rcsinfo += surplus-dependency|CSWtexlive
ARCHALL_CSWtex-rcsinfo		=	1ependency|CSWtetex

CONFIGURE_SCRIPTS	=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

pre-build-modulated:
	cd $(WORKSRC) && gmake realclean
	$(MAKECOOKIE)

install-custom: pkgdocdir = $(docdir)/$(NAME)
install-custom: GNUinstall = ginstall
install-custom: TEXDIR = $(texmflocaldir)
install-custom: CONTRIB = $(TEXDIR)/tex/latex/$(BASE)
install-custom: DOCDIR  = $(TEXDIR)/doc/latex/styles
install-custom:
	$(GNUinstall) --directory $(DESTDIR)/$(CONTRIB)
	$(GNUinstall) $(WORKSRC)/rcsinfo.cfg $(WORKSRC)/rcsinfo.sty $(WORKSRC)/rcsinfo.perl $(DESTDIR)/$(CONTRIB)
	$(GNUinstall) --directory $(DESTDIR)/$(DOCDIR)
	$(GNUinstall) $(WORKSRC)/rcsinfo.dvi $(WORKSRC)/rcsinfo.ps $(WORKSRC)/rcsinfo.pdf $(DESTDIR)/$(DOCDIR)
	$(GNUinstall) $(WORKSRC)/rcsinfo2html.dvi $(WORKSRC)/rcsinfo2html.ps $(WORKSRC)/rcsinfo2html.pdf $(DESTDIR)/$(DOCDIR)
	$(GNUinstall) --directory $(DESTDIR)/$(DOCDIR)/html
	$(GNUinstall) $(WORKSRC)/html/*.html $(WORKSRC)/html/*.css $(DESTDIR)/$(DOCDIR)/ht