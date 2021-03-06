NAME = nano
VERSION = 2.2.6
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Enhanced clone of the Pico text editor
define BLURB
  GNU nano is designed to be a free replacement for the Pico text editor,
  part of the Pine email suite from The University of Washington. It aims
  to "emulate Pico as closely as possible and perhaps include extra
  functionality".
endef

VENDOR_URL   = http://www.nano-editor.org/
MASTER_SITES = http://www.nano-editor.org/dist/v2.2/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS  = CSWncurses
RUNTIME_DEP_PKGS += CSWlibintl8

EXTRA_INC = /opt/csw/include/ncurses

TEST_SCRIPTS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-all 

# Disable automatic line wraps when running as root. See 
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=513443 for 
# some background info
CONFIGURE_ARGS += --disable-wrapping-as-root

include gar/category.mk

post-install-modulated: DOCS=AUTHORS THANKS UPGRADE
post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -d $(DOCDEST)/examples
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(WORKSRC)/doc/nanorc.sample $(DOCDEST)/examples
	cp $(addprefix $(WORKSRC)/, $(DOCS)) $(DOCDEST)
	perl -pi -e 's|/usr/share/doc|$(docdir)|' \
		`find $(DESTDIR)$(sharedir) \
			-name \*.html -o \
			-name \*.1 -o \
			-name \*.5`
	@$(MAKECOOKIE)
