NAME = Gnome2-Wnck
VERSION = 0.02
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MLEHMANN

DESCRIPTION = interface to the Window Navigator Construction Kit
define BLURB
  This module allows a Perl developer to use the Window Navigator Construction
  Kit library (libwnck for short) to write tasklists and pagers.
endef

# Unstable Branch
#MASTER_SITES = $(SF_MIRROR)/gtk2-perl/

DISTFILES += $(call admfiles,CSWpmgnome2wnck,depend)

# Looks like the wrong function is ifdef'd out in
# wnck versions < 2.
PATCHFILES = wscount.diff

DEPENDS += cpan/Gtk2

include gar/category.mk
