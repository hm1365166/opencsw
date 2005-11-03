# RCS ID: $Id$
#
# gar.pkg.mk - Build Solaris packages
#

SPKG_REVSTAMP  ?= ,REV=$(shell date '+%Y.%m.%d')
SPKG_DESC      ?= $(DESCRIPTION)
SPKG_VERSION   ?= $(GARVERSION)
SPKG_CATEGORY  ?= application
SPKG_SOURCEURL ?= Unknown
SPKG_PACKAGER  ?= Unknown
SPKG_VENDOR    ?= Unknown
SPKG_EMAIL     ?= Unknown
SPKG_PSTAMP    ?= $(LOGNAME)@$(shell hostname)-$(shell date '+%Y%m%d%H%M%S')
SPKG_BASEDIR   ?= $(prefix)
SPKG_CLASSES   ?= none
SPKG_OSNAME    ?= $(shell uname -s)$(shell uname -r)

SPKG_EXPORT    ?= $(WORKDIR)
SPKG_DEPEND_DB  = $(GARDIR)/csw/depend.db

# Is this a full or incremental build?
SPKG_INCREMENTAL ?= 1

PKG_EXPORTS  = GARNAME GARVERSION DESCRIPTION CATEGORIES GARCH GARDIR GARBIN
PKG_EXPORTS += CURDIR WORKDIR WORKSRC
PKG_EXPORTS += SPKG_REVSTAMP SPKG_PKGNAME SPKG_DESC SPKG_VERSION SPKG_CATEGORY
PKG_EXPORTS += SPKG_VENDOR SPKG_EMAIL SPKG_PSTAMP SPKG_BASEDIR SPKG_CLASSES
PKG_EXPORTS += SPKG_OSNAME SPKG_SOURCEURL SPKG_PACKAGER TIMESTAMP

PKG_ENV  = $(BUILD_ENV)
PKG_ENV += $(foreach EXP,$(PKG_EXPORTS),$(EXP)="$($(EXP))")

# package - Use the mkpackage utility to create Solaris packages
PACKAGE_TARGETS = package-create

package: install pre-package $(PACKAGE_TARGETS) post-package

# returns true if package has completed successfully, false otherwise
package-p:
	@$(foreach COOKIEFILE,$(PACKAGE_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# Call mkpackage to transmogrify one or more gspecs into packages
package-create:
	@if test "x$(wildcard $(WORKDIR)/*.gspec)" != "x" ; then \
		for spec in `ls -1 $(WORKDIR)/*.gspec` ; do \
			echo "   ==> Processing $$spec" ; \
			$(PKG_ENV) mkpackage --spec $$spec \
								 --destdir $(SPKG_EXPORT) \
								 --workdir $(WORKDIR) \
                                 --nooverwrite \
                                 -v basedir=$(DESTDIR) ; \
		done ; \
	else \
		echo " ==> No specs defined for $(GARNAME)" ; \
	fi
	$(DONADA)

# Update the dependency database
dependb:
	@dependb --db $(SPKG_DEPEND_DB) \
             --parent $(CATEGORIES)/$(GARNAME) \
             --add $(DEPENDS)

