NAME = maven3
VERSION = 3.0.5
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Java software project management and comprehension tool
define BLURB
Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a
project's build, reporting and documentation from a central
piece of information.

Maven's primary goal is to allow a developer to comprehend the complete
state of a development effort in the shortest period of time. In order
to attain this goal there are several areas of conce rn that Maven
attempts to deal with:

   * Making the build process easy
   * Providing a uniform build system
   * Providing quality project information
   * Providing guidelines for best practices development
   * Allowing transparent migration to new features
endef

MASTER_SITES = http://www.eu.apache.org/dist/maven/maven-3/${VERSION}/binaries/

DISTNAME = apache-maven-$(VERSION)
DISTFILES  = $(DISTNAME)-bin.tar.gz

LICENSE = LICENSE.txt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = apache-maven-(\d+(?:\.\d+)*)-bin.tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWmaven3 += file-with-bad-content|/usr/local|root/opt/csw/share/maven3/home/README.txt

include gar/category.mk

install-custom: MAVENHOME=$(DESTDIR)$(sharedstatedir)/maven3/home
install-custom:
	mkdir -p $(DESTDIR)/opt/csw/bin
	rm -rf $(MAVENHOME)
	mkdir -p $(MAVENHOME)
	(cd $(WORKDIR)/$(DISTNAME); pax -r -w -s ',.*/\.git.*,,' . $(MAVENHOME))
	#cp $(WORKDIR)/bin-mvn $(DESTDIR)/opt/csw/bin/mvn
	#chmod +x $(DESTDIR)/opt/csw/bin/mvn
	$(MAKECOOKIE)
