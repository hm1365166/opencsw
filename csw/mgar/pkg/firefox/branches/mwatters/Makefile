NAME = firefox
VERSION = 3.5
GARTYPE = v1
CATEGORIES = apps
DISTNAME = $(NAME)

DESCRIPTION = Firefox Community Edition web browser
define BLURB
 The award-winning, free Web browser is better than ever. Browse the Web with confidence - Firefox protects you from viruses, spyware and pop-ups. Enjoy improvements to performance, ease of use and privacy. It's easy to import your favorites and settings and get started. Download Firefox now and get the most out of the Web. 
endef

DISTFILES  = $(NAME)-$(VERSION)-source.tar.bz2
DISTFILES += CSWfirefox.postremove CSWfirefox.postinstall 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)
MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$(VERSION)/source/
UPSTREAM_MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/

PACKAGES 		= CSWfirefox
CATALOGNAME_CSWfirefox 	= $(NAME)
SPKG_DESC_CSWfirefox 	= $(DESCRIPTION)

# Defines the list of patches to be applied to the sources
# PATCHFILES = autoconf.mk.in.diff
# PATCHFILES += packager.mk.diff
# PATCHFILES += jemalloc.c.diff
# PATCHFILES += nsMathUtils.h.diff
# PATCHFILES += file_id.cc.diff
# PATCHFILES += md5.h.diff
# PATCHFILES += solaris_lwp.h.diff
# PATCHFILES += nsNativeApSuportUnix.cpp.diff
# PATCHFILES += nsExceptionHandler.cpp.diff 

# Use Sun studio 12 to compile it
# GARCOMPILER = SOS12
GARCOMPILER = GCC3

# LD=/opt/csw/bin/gld
# EXTRA_CONFIGURE_EXPORTS = LD

# pkg-config options
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig

# CFLAGS += -xlibmil -D__solaris__ 
CFLAGS += -D__solaris__ 
CFLAGS += -DG_HAVE_ISO_VARARGS 

# CXXFLAGS+= -xlibmil -xlibmopt -features=tmplife -norunpath
CXXFLAGS+= -DG_HAVE_ISO_VARARGS 
CXXFLAGS+= -D_XOPEN_SOURCE=500 -D_XPG5 

LDFLAGS+=-dy
# LDFLAGS+=-L/usr/lib/lwp -L/opt/csw/mozilla/firefox/lib -R/opt/csw/mozilla/firefox/lib -L/opt/csw/lib -R/opt/csw/lib -lsqlite3

PERL=/opt/csw/bin/perl
export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/firefox

TEST_SCRIPTS = 

LICENSE = LICENSE

# Variable for direct access to working dir
WORK_BUILD   = $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(NAME)
WORK_INSTALL = $(WORKROOTDIR)/install-$(firstword $(MODULATIONS))

post-extract:
	@mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/mozilla* $(WORK_BUILD)
	@$(MAKECOOKIE)

pre-configure:
	@cp $(FILEDIR)/.mozconfig  $(WORK_BUILD)/.mozconfig

pre-install:
	( if [ ! -d $(WORK_INSTALL)/opt/csw/bin ] ; then mkdir -p $(WORK_INSTALL)/opt/csw/bin ; fi )
	( cd $(WORK_INSTALL)/opt/csw/bin && if [ -L firefox ] ; then rm firefox ; fi  && ln -s ../mozilla/firefox/bin/firefox . )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/pixmaps )
	( cp $(WORK_BUILD)/other-licenses/branding/firefox/mozicon128.png $(WORK_INSTALL)/opt/csw/share/pixmaps/firefox.png )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/applications )
	( cp $(FILEDIR)/firefox.desktop $(WORK_INSTALL)/opt/csw/share/applications/firefox.desktop )
	( mkdir -p $(WORK_INSTALL)/opt/csw/share/gnome/mime-info )
	( cp $(FILEDIR)/firefox.keys $(WORK_INSTALL)/opt/csw/share/gnome/mime-info/firefox.keys )

post-install:
	( gfind $(WORK_INSTALL)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( mv $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config.temp && gsed -e s\_-L$(WORK_INSTALL)/opt/csw/lib\_\_g  $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config.temp > $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config && rm $(WORK_INSTALL)/opt/csw/mozilla/firefox/bin/firefox-config.temp )
	( mv $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp && gsed -e s\_-L$(WORK_INSTALL)/opt/csw/lib\_\_g  $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp > $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc && rm $(WORK_INSTALL)/opt/csw/mozilla/firefox/lib/pkgconfig/firefox-nspr.pc.temp )
	( gfind $(WORK_INSTALL)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/firefox -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORK_BUILD)/\_\_g {}.temp > {} && rm {}.temp"  \; )
	( gfind $(WORK_INSTALL)/opt/csw/mozilla/firefox -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )

include gar/category.mk
