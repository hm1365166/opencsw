NAME = ruby18
DISTVERSION = 1.8.7
PATCHLEVEL = p357
VERSION = $(DISTVERSION)
CATEGORIES = lang
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

TEST_SCRIPTS =
TEST_ARGS = test-all

BUIbdb48devel
BUI CSWbdb48devel CSWlibgdbm-dev CSWcoreutils CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibreadline-dev CSWlibz-dev CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibncurses-dev

PACKAGES = CSWruby18 CSWrubtkby18 CSWrubby18-tk CSWruby18-dev CSWruby18-mode
PACKAGES += CSWruby18-mode-el CSWlibruby18-1 CSWruby18-gcc4

EXTRA_MODULATORS = COMPILER
MODULATIONS_COMPILER = sun gcc4
MERGE_SCRIPTS_isa-default-compiler-sun = copy-all
MERGE_SCRIPTS_isa-default-compiler-gcc4 = copy-custom

OBSOLETED_BY_CSWruby18 = CSWruby
OBSOLETED_BY_CSWruby18-doc = CSWrubydoc
OBSOLtk = CSWrubytk8-doc = CSWrubydoc
OBSOLETED_BY_CSWruby18-dev = CSWrubydev
OBSOLETED_BY_CSWruby18-mode = CSWrubymode
OBSOLETED_BY_CSWruby18-mode-el = CSWrubymodeel

ALTERNATIVES_CSWruby18 = ruby rbconfig18
ALTERNATIVE_ruby = $(bindir)/ruby ruby $(bindir)/ruby18 10 $(bindir)/irb irb $(bindir)/irb18 $(bindir)/erb erb $(bindir)/erb18 $(bindir)/rdoc rdoc $(bindir)/rdoc18 $(bindir)/ri ri $(bindir)/ri18 $(bindir)/testrb testrb $(bindir)/testrb18 $(mandir)/man1/ruby.1 ruby.1 $(mandir)/man1/ruby18.1
ALTERNATIVE_rbconfig18 = $(libdir)/ruby/1.8/$(GARCH)-solaris2.10/rbconfig.rb rbconfig18 $(libdir)/ruby/1.8/$(GARCH)-solaris2.10/rbconfig.rb.sun 5

ALTERNATIVES_CSWruby18-gcc4 = rbconfig18_gcc
ALTERNATIVE_rbconfig18_gcc = $(libdir)/ruby/1.8/$(GARCH)-solaris2.10/rbconfig.rb rbconfig18 $(libdir)/ruby/1.8/$(GARCH)-solaris2.10/rbconfig.rb.gcc4 10

ARCHALL_CSWruby18-doc = 1
ARCHALL_CSWruby18-mode = 1
ARCHALL_CSWruby18-mode-el = 1

LICENSE = COPYING

RUNTIME_DEP_PKy18 = CSWbdb48 CSWlibgdbm4 CSWlibiconv2 CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWruby18 += CSWlibncurses5 CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWruby18 += CSWlibreadline6 CSWlibz1

RUNTIME_DEP_PKGS_CSWruby18-gcc4 = CSWruby18 CSWgcc4core

RUNTIME_DEP_PKGS_CSWruby18-doc = CSWruby18

RUNTIME_Dtk = CSWruby18 CSWlibtk8-5 CSWlibtcl8-5 CSWlibruby18-118-doc = CSWruby18

RUNTIME_Ddev = CSWruby18 CSWlibruby18-1 CSWcoreutils

RUNTIME_DEP_PKGS_CSWruby18-mode = CSWemacs-common

RUNTIME_DEP_PKGS_CSWruby18-mode-el = CSWemacs-mode-el = CSWemacscommon

DESCRIPTION = An object-oriented language for quick and easy programming.
define BLURB
  Ruby is a language for quick and easy programming. Similar in scope to Perl
  and Python, it has high-level data types, automatic memory management,
  dynamic typing, a module system, exceptions, and a rich standard library.
  What sets Ruby apart is a clean and consistent language design where
  everything is an object. Other distinguishing features are CLU-style
  iterators for loop abstraction, singleton classes/methods and lexical
  closures.
endef

SPKG_DESC_CSWruby18  = $(DESCRIPTION)

SPKG_DESC_CSWruby18-gcc4  = A gcc4 compatible rbconfig.rb (Ruby 1.8)

SPKG_DESC_CSWlibruby18-1 = The libruby.so.1* files (Ruby 1.8)

SPKG_DESC_CSWruby18-doc = Documentation for Ruby 1.8

SPtk = Ruby 1.8 Tcl/TK Extensionation for Ruby 1.8

SPKG_DESC_CSWruby18-dev = Ruby 1.8 Extension Development Files

SPKG_DESC_CSWruby18-mode = Ruby 1.8 major mode for Emacs

SPKG_DESC_CSWruby18-mode-el = Elisp source for ruby mode (Ruby 1.8)

PKGFILES_CSWruby18-doc = $(datadir)/ri/.* $(docdir)/$(NAME)/sample.*

PKGFILES_CSWruby18-gcc4 = $(libdir)/ruby/1.8/$(GARCH)-solaris2.10/.*gcc4

Ptk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rbso# These are samples and comments
CHECKPKG_OVERRIDES_CSWruby18-tk += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.8/tkextlib/itk/setup.rb
CHECKPKG_OVERRIDES_CSWruby18-tk += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.8/tkextlib/itcl/setup.rb
CHECKPKG_OVERRIDES_CSWruby18-tk += file-with-bad-content|/usr/share|root/opt/csw/lib/ruby/1.8/tk/dialog.rbsolaris2.10/.*gcc4

PKGFILES_CSWruby18-dev = $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a
PKGFILES_CSWruby18-dev += /opt/csw/lib/libruby.*.so

PKGFILES_CSWruby18-mode = $(datadir)/emacs/site-lisp/.*elc$

PKGFILES_CSWruby18-mode-el = $(datadir)/emacs/site-lisp/.*el$

PKGFILES_CSWlibruby18-1 += /opt/csw/lib/libruby.*.so.1
PKGFILES_CSWlibruby18-1 += /opt/csw/lib/libruby.*.so.1.*

MASTER_SITES  = ftp://ftp.ruby-lang.org/pub/ruby/
MASTER_SITES += ftp://www.ibiblio.org/pub/languages/ruby/

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-p(\d+).tar.bz2

DISTFILES  = ruby-$(DISTVERSION)-$(PATCHLEVEL).tar.bz2
DISTFILES += CSWruby.cswreleasenotes
DISTFILES += CSWrubyd CSWrubytkILES += CSWrubydtk.cswreleasenotes

# See: http://rubyforge.org/tracker/index.php?func=detail&aid=17607&group_id=426&atid=1698
PATCHFILES = rdoc_parse_order_fix.patch
PATCHFILES += 0002-Correct-potential-segfault-caused-during-garbage-col.patch
PATCHFILES += 0003-Force-ld-to-embed-the-proper-SONAME-for-libruby.patch
PATCHFILES += 0004-Patch-a-few-more-usr-local-references.patch
PATCHFILES += 0005-Correct-a-usr-local-reference-in-mkmf.rb.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --# Needed for conformity with Tk
CONFIGURE_ARGS += --enable-pthread-# As a result of pthreads getcontext/setcontext is used massively. These two presets are the essence of the proposed patch:
#   http://timetobleed.com/fix-a-bug-in-rubys-configurein-and-get-a-30-performance-boost/
#   https://github.com/ice799/matzruby/commit/0b9b69f9653782a33aee2b8937d405eae245b60c
CONFIGURE_ARGS += ac_cv_func_getcontext=no
CONFIGURE_ARGS += ac_cv_func_setcontext=no
-program-suffix=18
EXTRA_CONFIGURE_ARGS_isa-default-compiler-sun = --enable-install-doc

INSTALL_ARGS = install

DISTNAME = ruby-$(VERSION)-$(PATCHLEVEL)

# We want libruby-static.a to ship.  mkmf tests for various things using it.
MERGE_EXCLUDE_STATICLIBS = 

COMPILE_ELISP = 1

ifeq ($(COMPILER),gcc4)
# This is for rbconfig.rb: without this, modules built may not get a proper
# setting.
GARCOMPILER = GNU
EXTRA_LDFLAGS = -R $(abspath /opt/csw/gcc4/lib/$(MM_LIBDIR))
else
GARCOMPILER = SUN
SOS12_LD_FLAGS =
endif

CHECKPKG_OVERRIDES_CSWruby18 += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWruby18-dev += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWruby18-doc += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWruby18-doc += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWruby18-gcc4 += surplus-dependency|CSWgcc4core
CHECKPKG_OVERRIDES_CSWrubydev += archall-devel-package

# usr/local overrides
CHECKPKG_OVERRIDES_CSWruby18 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.8/fileutils.rb
CHECKPKG_OVERRIDES_CSWruby18 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/ruby18.1
CHECKPKG_OVERRIDES_CSWruby18 += file-with-bad-content|/usr/local|root/opt/csw/bin/ri18
CHECKPKG_OVERRIDES_CSWruby18-doc += file-with-bad-content

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)$(PATCHLEVEL)

RBCDIR = $(libdir)/ruby/1.8/$(GARCH)-solaris2.10
RBCONFIG = $(RBCDIR)/rbconfig.rb

merge-copy-custom: $(PKGROOT) $(INSTALLISADIR)
	$(_DBUG_MERGE)( [ -d "$(PKGROOT)$(RBCDIR)" ] || \
			mkdir -p $(PKGROOT)$(RBCDIR); \
			cp $(DESTDIR)$(RBCONFIG).$(COMPILER) \
				$(PKGROOT)$(RBCONFIG).$(COMPILER) )

post-install-mDESTDIR) RMDIR=$(PKGROOT)/$(datadir)/emacs/site-lisp/ruby-mode
post-install-modulated:
	@echo "Stripping DESTDIR from rbconfig.rb"
	@gsed -i -e s,$(DESTDIR),, \
		$(DESTDIR)$(libdir)/ruby/1.8/$(GARCH)-solaris2.10/rbconfig.rb
	@$(MAKECOOKIE)
	@echo "Setting up the CSW rbconfig stuff so we can switch between compilers"
	@mv $(DESTDIR)$(RBCONFIG) $(DESTDIR)$(RBCONFIG).$(COMPILER)
	@echo "Installing ruby-mode elisp..."
	@(mkdir -p $(RMDIR); \
		cp $(WORKSRC)/misc/*el $(RMDIR))
	@$(MAKECONFIG)

post-merge:
	@echo "Copying in sample codePKGROOTmkdir -p $(DESTDIR)$(docdir)/ruby18/
	@cp -R $(WORKSRC_FIRSTMOD)/sample $(PKGROOT)$(docdir)/ruby18/
	@for ex tk  bigdecimal dl tk ; do \
		cp -R $(WORKSRC_FIRSTMOD)/ext/$$ext/sample \
			$(PKGROOT)$(docdir)/ruby18/sample/$$ext ; \
	done
	@echo "Fixing shebang path in distributed ruby scripts..."
	@find $(PKGROOT)$(prefix) -type f -name '*.rb' -exec \
		perl -i -plne "s{^#!/usr/local/bin/ruby}{#!$(bindir)/ruby18}g" {} \