# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# vim: ft=make ts=4 sw=4 noet
# This makefile is to be included from Makefiles in each category
# directory.

default:
	@echo "You are in the pkg/cpan directory."

%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* ; \
	done

paranoid-%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || exit 2; \
	done

export BUILDLOG ?= $(shell pwd)/buildlog.txt

report-%:
	@for i in $(filter-out CVS/,$(wildcard */)) ; do \
		$(MAKE) -C $$i $* || echo "	*** make $* in $$i failed ***" >> $(BUILDLOG); \
	done

# You can either use "gmake newpkg-Perl-Module" or "gmake newpkg-Perl::Module".
# Ideally this would also figure out the AUTHOR by querying CPAN. Alternatively
# we might think about dropping the AUTHOR field and determine that on the fly
# during the build. Ideas?
newpkg-%: dir = $(subst ::,-,$*)
newpkg-%:
	@svn mkdir $(dir) $(dir)/tags $(dir)/branches $(dir)/trunk $(dir)/trunk/files
	@python -c 'from mako.template import Template; \
        v = { "name": "$*", "version": "x.y" }; \
        t = Template(filename="newpkg-Makefile"); \
        print t.render(**v)' > $(dir)/trunk/Makefile
	@touch $(dir)/trunk/checksums
	@svn add $(dir)/trunk/Makefile $(dir)/trunk/checksums
	@echo "cookies\ndownload\nwork\n" | svn propset svn:ignore -F /dev/fd/0 $(dir)/trunk
	@echo
	@echo "Your package is set up for editing at $(dir)/trunk"
