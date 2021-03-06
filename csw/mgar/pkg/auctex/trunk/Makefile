# $Id$
#
NAME = auctex
VERSION = 11.87
GARTYPE = v2

DESCRIPTION = A much enhanced TeX/LaTeX mode for Emacs
define BLURB
  AUCTeX is an integrated environment for editing LaTeX, ConTeXt,
  docTeX, Texinfo, and TeX files.
endef

MASTER_SITES	=	http://ftp.gnu.org/pub/gnu/auctex/
DISTFILES		=	$(DISTNAME).tar.gz
DISTFILES		+=	README.CSW

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-texmf-dir=/opt/csw/share/texmf-local
# this is needed to avoid incorrect interaction with CSWemacssitestart
# installed during the packaging:
CONFIGURE_ARGS	+=	--with-auctexstartfile=/opt/csw/share/emacs/site-lisp/auctex.el
CONFIGURE_ARGS	+=	--with-previewstartfile=/opt/csw/share/emacs/site-lisp/preview-latex.el

BUILD_SCRIPTS	=	nominal
BUILD_SCRIPTS	+=	extradist
BUILD_SCRIPTS	+=	html-docs
BUILD_SCRIPTS	+=	preview-latex.dvi
BUILD_SCRIPTS	+=	preview-latex.ps
BUILD_SCRIPTS	+=	preview-latex.pdf

SKIPTEST		=	1
ARCHALL			=	1

BUILD_DEP_PKGS		=	CSWemacs
BUILD_DEP_PKGS		+=	CSWtexlive
BUILD_DEP_PKGS		+=	CSWtexinfo

RUNTIME_DEP_PKGS	=	CSWemacs-common
RUNTIME_DEP_PKGS	+=	CSWtexlive
RUNTIME_DEP_PKGS	+=	CSWgs

# all the "bad content"s are innocuous:
CHECKPKG_OVERRIDES_CSWauctex += file-with-bad-content
# preview-latex depends on the existence at run-time:
CHECKPKG_OVERRIDES_CSWauctex += surplus-dependency|CSWgs
# the preview-latex can be used only with a graphical Emacs:
CHECKPKG_OVERRIDES_CSWauctex	+=	surplus-dependency|CSWtexlive

include gar/category.mk

build-nominal:
	$(MAKE) -C $(WORKSRC)
	$(MAKECOOKIE)

build-extradist:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-html-docs:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-preview-latex.dvi:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-preview-latex.ps:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

build-preview-latex.pdf:
	$(MAKE) -C $(WORKSRC)/doc $(subst build-,,$@)
	$(MAKECOOKIE)

post-install-modulated:
	@echo "executing $@"
	: miscelaneous formats for all the generated documentation
	ginstall $(WORKSRC)/doc/auctex.dvi $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/auctex.ps $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/auctex.pdf $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/preview-latex.dvi $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/preview-latex.ps $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/preview-latex.pdf $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/tex-ref.dvi $(DESTDIR)$(docdir)/auctex
	ginstall $(WORKSRC)/doc/tex-ref.ps $(DESTDIR)$(docdir)/auctex
	gtar --directory=$(WORKSRC)/doc --create --file=- html | gtar --directory=$(DESTDIR)/$(docdir)/auctex --extract --file=-
	ginstall -d $(DESTDIR)$(docdir)/auctex/examples
	ginstall $(WORKSRC)/preview/circ.tex $(DESTDIR)$(docdir)/auctex/examples
	$(MAKECOOKIE)
