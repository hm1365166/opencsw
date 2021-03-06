NAME = DTraceToolkit
VERSION = 0.99
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A collection of dtrace scripts developed by the DTrace community
define BLURB
  The following are miscellaneous open source tools and examples
  that use the DTrace language provided in Solaris 10 and OpenSolaris.
  DTrace helps troubleshoot problems on servers by providing new detailed
  views of the system internals, to a level that was previously difficult
  to access. The language is similar to C and is event based.
endef

MASTER_SITES = http://www.brendangregg.com/
DISTFILES  = $(NAME)-VENDOR_URL = http://www.brendangregg.com/dtrace.html)-LICENSE = License

PACKAGES += CSWdtracetoolkit
SPKG_DESC_CSWdtracetoolkitE = v2

DESCRIPTION = A collection of dtrace scripts developed by th# PKGFILES is catchall
ARCHALL_CSWdtracetoolkit = 1

# There are lots of references to system components in there
CHECKPKG_OVERRIDES_CSWdtracetoolkit += file-with-bad-content

# No need to depend on it, these are just for inspection
CHECKPKG_OVERRIDES_CSWdtracetoolkit += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWdtracetoolkit += missing-dependency|CSWlibruby1-9-1-1|or|CSWruby|or|CSWruby18|or|CSWruby191
CHECKPKG_OVERRIDES_CSWdtracetoolkit += missing-dependency|CSWperl

# This distracts us from installing and we don't need it
NOGITPATCH = 1t
LICENSE = License

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

includg.com/dtrace.html

USEFUL_SCRIPTS = dexplorer dtruss dvmstat errinfo execsnoop hotkernel hotuser \
	iopattern iosnoop iotop opensnoop procsystime rwsnoop rwtop statsnoop

dtracedir = $(datadir)/dtracetoolkit

install-custom:
	@echo " ==> Installing $(NAME)"
	@ginstall -d $(DESTDIR)$(dtracedir)
	@rm -rf $(DESTDIR)$(dtracedir)
	@cp -r $(WORKSRC) $(DESTDIR)$(dtracedir)
	@rm -f $(DESTDIR)$(dtracedir)/install
	@ginstall -d $(DESTDIR)$(prefix)/bin
	@rm -f $(foreach SCRIPT, $(USEFUL_SCRIPTS), $(DESTDIR)$(prefix)/bin/$(SCRIPT))
	@gln -s $(foreach SCRIPT, $(USEFUL_SCRIPTS), ../share/dtracetoolkit/$(SCRIPT)) \
		$(DESTDIR)$(prefix)/b