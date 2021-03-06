# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = facter
VERSION = 1.7.6
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A system fact gatherer
define BLURB
  A cross-platform Ruby library for retrieving facts from operating systems.
  Supports multiple resolution mechanisms, any of which can be restricted to
  working only on certain operating systems or environments. Facter is
  especially useful for retrieving things like operating system names, IP
  addresses, MAC addresses, and SSH keys.

  It is easy to extend Facter to include your own custom facts or to include
  additional mechanisms for retrieving facts.
endef

MASTER_SITES   = http://puppetlabs.com/downloads/facter/
DISTFILES      = $(NAME)-$(VERSION).tar.gz
SPKG_SOURCEURL = http://puppetlabs.com/
LICENSE        = LICENSE

RUNTIME_20P_PKGS = CSWruby18
BUILD_DEP_PKGS  = $(RINCOMPATIBLE_PKGS = CSWfacter-ruby18(INCOMPATIBLE_PKGS = CSWfacter2(RUNTIME_DEP_PKGS)

ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = facter

CHECKPKG_OVERRIDES_CSWfacter += file-with-bad-content|/usr/local|root/opt/csw/l2.0.0/facter/ssh.rbCRIPTS   = facter

CHECKPKG_OVERRIDES_CSWfacter += file-with-bad-content|/usr/local|root/opt/csw/l2.0.0ruby/site_ruby/1.8/facter/Cfkey.rb
CHECKPKG_OVERRIDES_CSWfacter += file-with-bad-content|/usr/local|root/opt/csw/l2.0.0/facter/util/manufacturer.rb
CHECKPKG_OVERRIDES_CSWfacter += file-collision|/opt/csw/bin/facter|CSWfacter|CSWfacter-ruby18
CHECKPKG_OVERRIDES_CSWfacter += file-collision|/opt/csw/share/man/man8/facter.8|CSWfacter|CSWfacter-ruby18

/manufacturer.rb

include gar/category.mk

install-facter:
	(cd $(WORKDIR)2.0 install.rb --destdir=$(DESTDIR))
	# we depend on ruby20 so fix the shebang
	find $(DESTDIR)$(bindir) -type f -depth -print | xargs -n 1 gsed -i -e '1 s|ruby$$|ruby2.0|g'
	gunzip $(DESTDIR)/$(mandir)/man8/facter.8.gz
