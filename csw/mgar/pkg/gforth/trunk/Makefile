NAME = gforth
VERSION = 0.6.9-20070604
GARTYPE = v1
CATEGORIES = lang

DESCRIPTION = gforth - a fast and portable implementation of the ANS Forth language
define BLURB
  Gforth is a fast and portable implementation of the ANS Forth language.
  It works nicely with the Emacs editor, offers some nice features such as
  input completion and history and a powerful locals facility, and it even
  has (the beginnings of) a manual. Gforth employs traditional implementation
  techniques: its inner interpreter is indirect or direct threaded.
endef

MASTER_SITES = http://www.complang.tuwien.ac.at/forth/gforth/Snapshots/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
DISTFILES   += $(call admfiles,CSWgforth,prototype)
PATCHFILES   = gforth-DESTDIR.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Compile with GCC
GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install:
	@cp $(WORKDIR)/
