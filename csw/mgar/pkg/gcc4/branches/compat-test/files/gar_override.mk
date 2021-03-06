
#COOKIEDIR     = $(COOKIEROOTDIR)/$(MODULATION)-$(GAROSREL)-$(GARCH)
#WORKDIR       = $(WORKROOTDIR)/build-$(MODULATION)-$(GAROSREL)-$(GARCH)
#PATCHDIR      = $(WORKDIR)/$(NAME)-$(VERSION)
#INSTALLISADIR = $(WORKROOTDIR)/install-$(MODULATION)-$(GAROSREL)-$(GARCH)
#PKGROOT       = $(abspath $(WORKROOTDIR)/pkgroot-$(GAROSREL)-$(GARCH))
#OBJECT_DIR    = $(WORKDIR)/objdir
#WORKSRC       = $(OBJECT_DIR)
DIRPATHS      = 
OPTFLAGS      =
CONFIG_SHELL  = /opt/csw/bin/bash
GARCOMPILER   = GCC3
#GCC3_CC       = /opt/csw/gcc3/bin/gcc -g -O2 -mcpu=v8 -pipe
#CFLAGS        = -I/opt/csw/include
#CPPFLAGS      = -I/opt/csw/include
#CXXFLAGS      = -I/opt/csw/include
#LDFLAGS       = -L/opt/csw/lib -R/opt/csw/lib
#BOOT_CFLAGS   = -I/opt/csw/include -mcpu=v8 -g -O2 -pipe
#BOOT_LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib

#ifeq ($(shell uname -p),i386)
#ifeq ($(shell uname -r),5.10)
#    GCC3_CC       = /opt/csw/gcc3/bin/gcc -g -O2 -pipe
#    BOOT_CFLAGS   = -I/opt/csw/include -g -O2 -pipe
#    BOOT_LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib
#else
#    GCC3_CC       = /opt/csw/gcc3/bin/gcc -march=i386 -g -O2 -pipe
#    BOOT_CFLAGS   = -I/opt/csw/include -m32 -march=i386 -g -O2 -pipe
#    BOOT_LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib
#endif
#endif

export CONFIG_SHELL
#export CFLAGS CPPFLAGS CXXFLAGS
#export LDFLAGS
#export BOOT_CFLAGS BOOT_LDFLAGS

# FIXCONFIG_DIRS         += $(DESTDIR)$(BUILD_PREFIX)/gcc4/lib
#STRIP_DIRS             += $(DESTDIR)$(BUILD_PREFIX)/gcc4/bin
# CONFIGURE_SCRIPTS       = objdir

SKIPTEST ?= 1

# post-configure-modulated: fix-bootflags
MERGE_SCRIPTS_isa-i386  = amd

# <maciej> This should not be necessary any more thanks to checkpkg overrides.
# ## Run checkpkg Manually
# ENABLE_CHECK            = 0
