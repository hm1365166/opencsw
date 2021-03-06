NAME = firefox
VERSION = 2.0.0.20
CATEGORIES = apps
DISTNAME = $(NAME)

DESCRIPTION = Firefox Community Edition web browser
define BLURB
The award-winning, free Web browser is better than ever. Browse the Web with confidence - Firefox protects you from viruses, spyware and pop-ups. Enjoy improvements to performance, ease of use and privacy. It's easy to import your favorites and settings and get started. Download Firefox now and get the most out of the Web. 
endef

DISTFILES  = $(NAME)-$(VERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWfirefox, postinstall postremove )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)
MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$(VERSION)/source/
UPSTREAM_MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/

PERL="/opt/csw/bin/perl"
CFLAGS=-xlibmil
CXXFLAGS=-xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS=-R'\$\$ORIGIN:\$\$ORIGIN/..' -L/opt/csw/lib -R/opt/csw/lib

export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/firefox
PATCHFILES = autoconf.mk.in.diff
TEST_SCRIPTS =

# Variable for direct access to working dir
WORK_BUILD   = $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(NAME)
WORK_INSTALL = $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))

# Dependencies tracking
RUNTIME_DEP_PKGS_CSWfirefox  += CSWbonobo2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWfconfig
RUNTIME_DEP_PKGS_CSWfirefox  += CSWftype2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWgconf2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWggettextrt
RUNTIME_DEP_PKGS_CSWfirefox  += CSWglib2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWgnomekeyring
RUNTIME_DEP_PKGS_CSWfirefox  += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWgtk2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibart
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibatk
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibbonoboui
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibcairo
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibgnome
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibgnomecanvas
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibgnomeui
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibidl
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibpopt
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibxft2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWlibxrender
RUNTIME_DEP_PKGS_CSWfirefox  += CSWorbit2
RUNTIME_DEP_PKGS_CSWfirefox  += CSWpango
RUNTIME_DEP_PKGS_CSWfirefox  += CSWzlib

post-extract:
	@mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/mozilla $(WORK_BUILD)
	@$(MAKECOOKIE)

pre-configure:
	@cp $(FILEDIR)/.mozconfig  $(WORK_BUILD)/.mozconfig

pre-install:
	( if [ ! -d $(WORK_INSTALL)/opt/csw/bin ] ; then mkdir -p $(WORK_INSTALL)/opt/csw/bin ; fi )
	( cd $(WORK_INSTALL)/opt/csw/bin && ln -sf ../mozilla/firefox/bin/firefox . )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/pixmaps )
	( cp $(WORK_BUILD)/other-licenses/branding/firefox/mozicon128.png $(WORK_INSTALL)/opt/csw/share/pixmaps/firefox.png )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/applications )
	( cp $(FILEDIR)/firefox.desktop $(WORK_INSTALL)/opt/csw/share/applications/firefox.desktop )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/gnome/mime-info )
	( cp $(FILEDIR)/firefox.keys $(WORK_INSTALL)/opt/csw/share/gnome/mime-info/firefox.keys )
	@ginstall -d $(WORK_INSTALL)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORK_BUILD)/LICENSE $(WORK_INSTALL)$(datadir)/doc/$(NAME)/License.txt

post-install:
	( gfind $(WORK_INSTALL)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( mv $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config.temp && gsed -e s\_-L$(WORK_INSTALL)/opt/csw/lib\_\_g  $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config.temp > $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config && rm $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config.temp )
	( mv $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp && gsed -e s\_-L$(WORK_INSTALL)/opt/csw/lib\_\_g  $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp > $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc && rm $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp )
	( gfind $(WORK_INSTALL)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/firefox -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/firefox -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )

# include the rest of GAR
include gar/category.mk

