NAME = perlconsole
VERSION = 0.4
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SUKRIA

DESCRIPTION = Evaluate Perl code interactively
define BLURB
  Perl Console is a light program that lets you evaluate Perl code
  interactively. It uses Readline for grabing input and provides
  completion with all the namespaces loaded during your session.
  
  This is pretty useful for Perl developers that write modules. You can
  load a module in your session and test a function exported by the
  module.
  
  Readline is used to grab user input and provides then all the facilities
  your are used to : completion, key bindings, ... 
endef

PACKAGES = CSWperlconsole
CATALOGNAME = perlconsole
ARCHALL = 1

SPKG_SOURCEURL = http://www.sukria.net/perlconsole.html

RUNTIME_DEP_PKGS = CSWpmmodrefresh CSWpmtermreadlineg CSWpmlexicalpersist
RUNTIME_DEP_PKGS += CSWpmbkeywords

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	# Make directories writable (otherwise gmake clean bails out)
	chmod -R u+w $(INSTALLISADIR)
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
