# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = buildbot
VERSION = 0.8.10
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A system to automate the compile/test cycle
define BLURB
  The BuildBot is a system to automate the compile/test cycle required by most
  software projects to validate code changes. By automatically rebuilding and
  testing the tree each time something has changed, build problems are
  pinpointed quickly, before other developers are inconvenienced by the
  failure. The guilty developer can be identified and harassed without human
  intervention. By running the builds on a variety of platforms, developers who
  do not have the facilities to test their changes everywhere before checkin
  will at least know shortly afterwards whether they have broken the build or
  not. Warning counts, lint checks, image size, compile time, and other build
  parameters can be tracked over time, are more visible, and are therefore
  easier to improve. 
endef

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

DISTFILES += cswbuildbot.xml

# Buildbot is 2.7 only and the server is Solaris 10 only
MODULATIONS_PYTHON_VERSION = 2_7
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWbuildbot
SPKG_DESC_CSWbuildbot = A system to automate the compile/test cycle
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-twisted
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-zope-interface
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-jinja2
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-tempita
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-decorator
RUNTIME_DEP_PKGS_CSWbuildbot += CSWpy-openssl
# This was a private version of the library which is no longer necessary.
# The current buildbot version is compatible with the latest sqlalchemy.
INCOMPATIBLE_PKGS_CSWbuildbot += CSWbuildbot-sqlalchemy

CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-twisted
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-zope-interface
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-jinja2
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-tempita
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-decorator
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWpy-openssl
CHECKPKG_OVERRIDES_CSWbuildbot += surplus-dependency|CSWbuildbot-sqlalchemy

# That is the URI for the DTD
CHECKPKG_OVERRIDES_CSWbuildbot += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswbuildbot.xml

# This is more like an application than a python module
CHECKPKG_OVERRIDES_CSWbuildbot += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWbuildbot += catalogname-does-not-start-with-py_

ARCHALL_CSWbuildbot = 1

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswbuildbot.xml
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

post-install:
	ginstall -D -m 0644 $(WORKDIR)/cswbuildbot.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswbuildbot.xml
	@$(MAKECOOKIE)
