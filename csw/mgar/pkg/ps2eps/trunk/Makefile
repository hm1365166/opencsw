# $Id$

NAME = ps2eps
VERSION = 1.68
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Tool for generating Encapsulated Postscript Format files from one-page Postscript documents
define BLURB
  ps2eps is a tool (written in Perl) to produce Encapsulated PostScript
  Files (EPS/EPSF) from usual one-paged Postscript documents. It calculates
  correct Bounding Boxes for those EPS files and filters some special
  postscript command sequences that can produce erroneous results on printers.
  EPS files are often needed for including (scalable) graphics of high quality
  into TeX/LaTeX (or even Word) documents. 
endef

MASTER_SITES = http://www.tm.uka.de/~bless/
DISTNAME = $(NAME)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS	=	CSWperl
# This cannot be tracked with checkpkg
CHECKPKG_OVERRIDES_CSWps2eps += surplus-dependency|CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS	=
GARCOMPILER			=	GNU
PATCHDIR			=	$(WORKSRC)
PATCHFILES			=	0001-Fix-shebang-perl.patch
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom
LICENSE				=	LICENSE.txt

include gar/category.mk

build-custom:	\
				$(WORKSRC)/bbox
	$(MAKECOOKIE)

$(WORKSRC)/bbox:	\
					$(WORKSRC)/bbox.o
	$(CC) $(LDFLAGS) $< -o $@

$(WORKSRC)/bbox.o:	\
					$(WORKSRC)/src/C/bbox.c
	$(CC) -c $(CFLAGS) $< -o $@


install-custom: pkgdocdir = $(docdir)/ps2eps
install-custom:
	cd $(WORKSRC) && ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(bindir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rwx,go=rx bbox $(DESTDIR)$(bindir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rwx,go=rx bin/ps2eps $(DESTDIR)$(bindir)
	cd $(WORKSRC) && ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(pkgdocdir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/pdf/bbox.pdf $(DESTDIR)$(pkgdocdir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/pdf/ps2eps.pdf $(DESTDIR)$(pkgdocdir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/html/bbox.html $(DESTDIR)$(pkgdocdir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/html/ps2eps.html $(DESTDIR)$(pkgdocdir)
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r Changes.txt $(DESTDIR)$(pkgdocdir)
	cd $(WORKSRC) && ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(mandir)/man1
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/man/man1/bbox.1 $(DESTDIR)$(mandir)/man1
	cd $(WORKSRC) && ginstall --preserve-timestamps --mode=u=rw,go=r doc/man/man1/ps2eps.1 $(DESTDIR)$(mandir)/man1
	$(MAKECOOKIE)
