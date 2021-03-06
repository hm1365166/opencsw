GARNAME = vim
DISTVERSION = 7.2
PATCHREV = 320
GARVERSION = $(DISTVERSION).$(PATCHREV)
CATEGORIES = utils
SPKG_SOURCEURL = http://www.vim.org/download.php
DESCRIPTION = Vi IMproved
define BLURB
  Vim is an almost fully-compatible version of the Unix editor Vi. Many new
  features have been added including multi-level undo, syntax highlighting,
  commandline history, online help, filename completion, and block operations.
  It is descended from the vi clone "stevie" and runs on many systems, including
  Unix, MS Windows, OS/2, Macintosh, VMS, and Amiga.
endef

PACKAGES = CSWvim CSWvimrt
CATALOGNAME_CSWvim = vim
CATALOGNAME_CSWvimrt = vimrt
SPKG_DESC_CSWvim = Vi IMproved without GUI
SPKG_DESC_CSWvimrt = Vi IMproved runtime and documentation
ARCHALL_CSWvimrt = 1

MASTER_SITES  = ftp://ftp.vim.org/pub/vim/patches/$(DISTVERSION)/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/extra/
MASTER_SITES += ftp://ftp.vim.org/pub/vim/unix/

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.bz2
DISTFILES += $(GARNAME)-$(DISTVERSION)-lang.tar.gz
DISTFILES += $(GARNAME)-$(DISTVERSION)-extra.tar.gz
DISTFILES += vimrc
DISTFILES += vimrc.tiny
DISTFILES += gvimrc
DISTFILES += COPYING

PATCHFILES  = $(foreach T,$(shell gseq -f "%03g" 001 $(PATCHREV)),$(DISTVERSION).$(T))
PATCHFILES += vimtutor.patch

WORKSRC = $(WORKDIR)/$(GARNAME)$(subst .,,$(DISTVERSION))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-xim
CONFIGURE_ARGS += --without-x
CONFIGURE_ARGS += --enable-gui=no
CONFIGURE_ARGS += --disable-gpm
CONFIGURE_ARGS += --with-global-runtime=$(sharedstatedir)/$(GARNAME)
CONFIGURE_ARGS += --with-features=huge
CONFIGURE_ARGS += --with-tlib=ncurses
CONFIGURE_ARGS += --enable-multibyte
CONFIGURE_ARGS += --enable-cscope

BUILD_ARGS  = "VIMRCLOC=/opt/csw/share/vim"
BUILD_ARGS += "VIMRUNTIMEDIR=/opt/csw/share/vim/vim72"

PATCHDIRLEVEL = 0

RUNTIME_DEP_PKGS_CSWvim = CSWggettextrt CSWiconv CSWncurses CSWvimrt
INCOMPATIBLE_PKGS_CSWvim = CSWvim-minimal

PKGFILES_CSWvimrt = /opt/csw/share/.*

# Note: Tests require controlling terminal
TEST_TARGET = test

include gar/category.mk

post-configure: make-interps-lazy

make-interps-lazy:
	@perl -i.bak -plne \
	    's/(-l(?:perl|python|ruby|tcl)\S*)/-zlazyload $$1 -znolazyload/' \
	    $(WORKSRC)/src/auto/config.mk

post-install-isa-sparcv8 post-install-isa-i386:
	@cp $(DOWNLOADDIR)/vimrc $(DOWNLOADDIR)/gvimrc $(DOWNLOADDIR)/vimrc.tiny $(DESTDIR)/opt/csw/share/vim
	@(cd $(DESTDIR)/opt/csw/share/vim;ln -s vim$(subst .,,$(DISTVERSION)) vimcurrent)
	@$(MAKECOOKIE)
	$(DONADA)
