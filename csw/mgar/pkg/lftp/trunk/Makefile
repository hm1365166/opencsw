#####################################################################
# OpenCSW build recipe for lftp
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = lftp
VERSION = 4.6.1
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = A sophisticated command-line ftp/http client
define BLURB
   lftp is a sophisticated command line based file transfer program. Supported protocols include FTP, HTTP, SFTP, and FISH. It has a multithreaded design allowing you to issue and execute multiple commands simultaneously or in the background. It also features mirroring capabilities and will reconnect and continue transfers in the event of a disconnection. Also, if you quit the program while transfers are still in progress, it will switch to nohup mode and finish the transfers in the background. Additional protocols supported: FTP over HTTP proxy, HTTPS and FTP over SSL. There are lots of tunable parameters, including rate limitation, number of connections limitation and more.
endef

PACBUILD_DEP_PKGS = CSWgcc4g++ACKAGES = CSWlftp

RUNTIME_DEP_PKGS = CSWlibexpat1
RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWlibssl1-0-0
RUNTIME_DEP_PKGS += CSWlibsocks
RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS +=RUNTIME_DEP_PKGS += CSWlibz1=RUNTIME_DEP_PKGS += CSWlibidn11=# necessary when compiled with gcc
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibstdc+++= CSWlibreadline6

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

###### Upstream and opencsw files information #######

MASTElftp.yar.ru/ftpt/pub/source/lftp/

DISTFILES  = $(NAME)-$(VERSION).tarCSWlftp.cswreleasenotes += changelog.CSW

# do some type conversion before munmap call
# so lftp can be compiled with sun cc 
# (patch only mandatory to compile with gnutls)
#PATCHFILES_glaris-9.patch

# Update the system-wide lftp.conf path in the man page
PATCHFILES += 0007-update-configuration-files-paths-in-documentation.patch

PRESERVECONF = $(sysconfdir)/lftp.conf
MIGRATE_FILES_CSWlftp = lftp.conf

EXTRA_MERGE_EXCLUDE_FILES  = .*/charset.alias

##### Build and installation inGARCOMPILER = GNUinformation #####

# We don't want Sun Studio RPATH entries
# see http://wiki.opencsw.org/checkpkg-error-tagsifeq ($(GARCOMPILER),SUN)
	EXTRA_LINKER_FLAGS = -norunpath
endifLAGS = -norunpath

CONFIGURE_ARGS = $(DIRPATHS)

# previous maintainer compiled with openssl
# instead of gnutls, no need to change that
CONFIGURE_ARGS += --without-gnutls --with-openssl=/opt/csw
# Requested see https://www.opencsw.org/mantis/view.php?id=4481
CONFIGURE_ARGS += --wiFor an unknown reason so far, lftp crashes when compiled
# with compiled with lazyload enabled
EXTRA_LD_OPTIONS = -z nolazyload--with-socksdante

# No test suite here
TEST_SCRIPTS =


include gar/category.mk

# we re-run autoconf because we p#pre-configure-modulated:
#	cd $(WORKSRC) && autoconf
#SRC) && autoconf
