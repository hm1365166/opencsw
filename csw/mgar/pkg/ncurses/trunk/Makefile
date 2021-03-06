# $Id$
#
# Things to keep in mind:
# - Link to libtinfo5 in downstream packages if possible to avoid *w/*non-w bindings
#   as described in this posting "Craig Small: ncurses library split - Planet Debian":
#     https://plus.google.com/105567297772267099132/posts/Bv5GSTQvfzC

NAME = ncurses
VERSION = 5.9
CATEGORIES = lib
GARTYPE = v2

define BLURB
 The ncurses (new curses) library is a free software emulation of curses
  in System V Release 4.0 and more. It uses terminfo format, supports pads
  and color and multiple highlights and forms charcters and function-key
  mapping, and has all the other SYSV-curses enhancements over BSD curses.
  It should port easily to any ANSI/POSIX-conforming UNIX-like system.
  On systems supporting libiconv, the library can be built to support
  wide- and multibyte-character applications, e.g., UTF-8. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = README

PACKAGES += CSWncurses
SPKG_DESC_CSWncurses = A free software emulation of curses
RUNTIME_DEP_PKGS_CSWncurses += CSWterminfo
CHECKPKG_OVERRIDES_CSWncurses += surplus-dependency|CSWterminfo
RUNTIME_DEP_PKGS_CSWncurses += CSWlibncursesw5
# These are legacy dependencies for packages still depending on CSWncurses
# instead of the specific libraries
RUNTIME_DEP_PKGS_CSWncurses += CSWlibncurses5
CHECKPKG_OVERRIDES_CSWncurses += surplus-dependency|CSWlibncurses5
RUNTIME_DEP_PKGS_CSWncurses += CSWlibpanel5
CHECKPKG_OVERRIDES_CSWncurses += surplus-dependency|CSWlibpanel5
RUNTIME_DEP_PKGS_CSWncurses += CSWlibpanelw5
CHECKPKG_OVERRIDES_CSWncurses += surplus-dependency|CSWlibpanelw5

PACKAGES += CSWlibform5
PKGFILES_CSWlibform5 += $(call pkgfiles_lib,libform.so.5)
SPKG_DESC_CSWlibform5 += A free software emulation of curses, libform.so.5
RUNTIME_DEP_PKGS_CSWlibform5 += CSWlibncurses5

PACKAGES += CSWlibformw5
PKGFILES_CSWlibformw5 += $(call pkgfiles_lib,libformw.so.5)
SPKG_DESC_CSWlibformw5 += A free software emulation of curses, libformw.so.5
RUNTIME_DEP_PKGS_CSWlibformw5 += CSWlibncursesw5

PACKAGES += CSWlibmenu5
PKGFILES_CSWlibmenu5 += $(call pkgfiles_lib,libmenu.so.5)
SPKG_DESC_CSWlibmenu5 += A free software emulation of curses, libmenu.so.5
RUNTIME_DEP_PKGS_CSWlibmenu5 += CSWlibncurses5

PACKAGES += CSWlibmenuw5
PKGFILES_CSWlibmenuw5 += $(call pkgfiles_lib,libmenuw.so.5)
SPKG_DESC_CSWlibmenuw5 += A free software emulation of curses, libmenuw.so.5
RUNTIME_DEP_PKGS_CSWlibmenuw5 += CSWlibncursesw5

PACKAGES += CSWlibncurses5
PKGFILES_CSWlibncurses5 += $(call pkgfiles_lib,libncurses.so.5)
SPKG_DESC_CSWlibncurses5 += A free software emulation of curses, libncurses.so.5
# If we access via libncurses we also need the terminal definitions (undetected by checkpkg)
RUNTIME_DEP_PKGS_CSWlibncurses5 += CSWterminfo
CHECKPKG_OVERRIDES_CSWlibncurses5 += surplus-dependency|CSWterminfo

PACKAGES += CSWlibncursesw5
PKGFILES_CSWlibncursesw5 += $(call pkgfiles_lib,libncursesw.so.5)
SPKG_DESC_CSWlibncursesw5 += A free software emulation of curses, libncursesw.so.5
# If we access via libncursesw we also need the terminal definitions (undetected by checkpkg)
RUNTIME_DEP_PKGS_CSWlibncursesw5 += CSWterminfo
CHECKPKG_OVERRIDES_CSWlibncursesw5 += surplus-dependency|CSWterminfo

PACKAGES += CSWlibpanel5
PKGFILES_CSWlibpanel5 += $(call pkgfiles_lib,libpanel.so.5)
SPKG_DESC_CSWlibpanel5 += A free software emulation of curses, libpanel.so.5
RUNTIME_DEP_PKGS_CSWlibpanel5 += CSWlibncurses5

PACKAGES += CSWlibpanelw5
PKGFILES_CSWlibpanelw5 += $(call pkgfiles_lib,libpanelw.so.5)
SPKG_DESC_CSWlibpanelw5 += A free software emulation of curses, libpanelw.so.5
RUNTIME_DEP_PKGS_CSWlibpanelw5 += CSWlibncursesw5

PACKAGES += CSWlibncurses-dev
SPKG_DESC_CSWlibncurses-dev = Development files for libncurses.so.5 and assorted libraries
PKGFILES_CSWlibncurses-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibmenuw5
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibpanel5
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibformw5
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibform5
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibpanelw5
RUNTIME_DEP_PKGS_CSWlibncurses-dev += CSWlibmenu5

PACKAGES += CSWterminfo
SPKG_DESC_CSWterminfo = Database of terminal information, part of ncurses
ARCHALL_CSWterminfo = 1
PKGFILES_CSWterminfo = $(datRUNTIME_DEP_PKGS_CSWterminfo += CSWterminfo-rxvt-unicode
CHECKPKG_OVERRIDES_CSWterminfo += surplus-dependency|CSWterminfo-rxvt-unicodetadir)/terminfo.*

VENDOR_URL = http://www.gnu.org/software/ncurses/ncurses.html

BUILD64 = 1

EXTRA_MODULATORS = WIDEC
MODULATIONS_WIDEC = disable enable

EXTRA_CONFIGURE_WIDEC-disable = --disable-widec
EXTRA_CONFIGURE_WIDEC-enable = --enable-widec

# Switch to larger model or these kinds of errors occur:
#   ld.so.1: tic: fatal: relocation error: R_AMD64_PC32: file /home/dam/mgar/pkg/ncurses/trunk/work/solaris9-i386/build-isa-amd64-widec-disable/ncurses-5.9/lib/libncurses.so.5: symbol putc: value 0x280010b35b0 does not fit
# (only valid on 64 bit x86)
# See for details
#   http://developers.sun.com/solaris/articles/about_amd64_abi.html
#EXTRA_CFLAGS-amd64 = -xmodel=medium
EXTRA_CFLAGS-amd64 = -Kpic
EXTRA_CFLAGS = $(EXTRA_CFLAGS-$(ISA))
EXTRA_LDFLAGS = $(EXTRA_CFLAGS-$(ISA))

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --without-libtool
CONFIGURE_ARGS += --with-shared 
CONFIGURE_ARGS += --disable-overwrite
CONFIGURE_ARGS += --without-ada
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_WIDEC-$(WIDEC))

# Don't use capabilities HPA and VPA as Solaris xterm doesn't understand it.
# See for details
#   <http://opencsw.org/bugtrack/view.php?id=2961>
#   <http://opencsw.org/bugtrack/view.php?id=2942>
#   <http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6569261>
CONFIGURE_ARGS += --without-xterm-new

TEST_TARGET = test

MERGE_SCRIPTS_isa-default-widec-disable = copy-only copy-config-only
   MERGE_DIRS_isa-default-widec-disable = $(libdir) $(includedir)
MERGE_SCRIPTS_isa-extra-widec-disable = copy-relocated-only copy-config-only
   MERGE_DIRS_isa-extra-widec-disable = $(libdir)

 MERGE_SCRIPTS_isa-default-widec-enable = copy-all
 MERGE_SCRIPTS_isa-extra-widec-enable = copy-relocated-only copy-config-only
    MERGE_DIRS_isa-extra-widec-enable = $(libdir)

# This is termcap location which defaults to 
#   /etc/termcap, /usr/share/misc/termcap and $HOME/.termcap
# which I think is ok
CHECKPKG_OVERRIDES_CSWlibncurses-dev += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/ncurses.3x

# I *think* this is a default, but keep an eye on it
CHECKPKG_OVERRIDES_CSWlibncurses-dev += file-with-bad-content|/usr/share|root/opt/csw/include/ncursesw/tic.h
CHECKPKG_OVERRIDES_CSWlibncurses-dev += file-with-bad-content|/usr/share|root/opt/csw/include/ncurses/tic.h

# I have no idea what this is. Inspect on problems.
CHECKPKG_OVERRIDES_CSWterminfo += file-with-bad-content|/usr/share|root/opt/csw/share/terminfo/p/pcmw

include gar/category.mk

LDFLAGS := $(filter-out