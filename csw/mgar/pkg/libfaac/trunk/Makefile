NAME = libfaac
VERSION = 1.28
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = AAC encoder library and tool
define BLURB
  FAAC is an open source MPEG-4 and MPEG-2 AAC encodECTer
endef

SF_PROJ = faac
MASTER_SITES = $(SF_MIRRORS)
DISTFECT)-$(VERSION).tar.bz2
DISTNAME = $(SF_PROJECTTNAME = $(SF_PROJ)-$(VERSION)

PACKAGES = CSWfaac
CATALOGNAME = $(NAME)

SPKG_SOURCEURL = http://www.audiocoding.com/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_ECTREGEX = $(SF_PROJ)-(\d+(?:\.\d+)*).tar.bz2

#PATCHFILES += Makefile.am.diff Makefile.in.diff Makefile.in.frontend.diff 
PATCHFILES += Makefile.in.frontend.diff Makefile.in.common.mp4v2.diff
PATCHFILES += aacquant.c.diff aacquant.h.diff config.h.in.diff
#PATCHFILES += configure.in.diff faac.h.diff faaccfg.h.diff frame.h.diff
PATCHFILES += configure.diff faac.h.diff faaccfg.h.diff frame.h.diff
PATCHFILES += input.c.diff ltp.c.diff mp4property.h.diff mp4util.h.diff
PATCHFILES += mpeg4ip.h.diff psych.h.diff

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include