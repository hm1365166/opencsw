NAME = libtool
VERSION = 2.4.5
CATEGORIES = devel
GARTYPE = v2

EXTRA_MODULA#MODULATIONS_GARCOMPILER = GCC3 GCC4 SOS12
MODULATIONS_GARCOMPILER =_GARCOMPILER = GCC3 GCC4 SOS12

# Modulate over compiler only for 2.4
# Compile 64 bit libraries only with SOS12
SKIP_MODULATIONS += $(foreach I,sparcv9 amd64,$(foreach C,GCC3 GCC4,isa-$I-garcompiler-$C))

DESCRIPTION = A generic library support tool
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.xz
DISTFILES += README.CSW

PATCH_LIBTOOL = 0002-Forward-port-GCC-tags-patch.patch
PATCHFILES_POSTINSTALL_isa-pentium_pro-garcompiler-SOS12 = $(PATCH_LIBTOOL)
PATCHFILES_POSTplus-garcompiler-SOS12 = $(PATCH_LIBTOOL)
DISTFILES += $(PATCH_LIBTOOL)

PATCHFILES  = 0001-Preserve-norunpath.patch

#EXTRA_TAGS = gcc3 gcc4 sos12
EXTRA_TAGS =

EXTRA_TAGS = gcc3 gcc4 sos12
COMPILER_TAGNAME_GCC3 = gcc3
COMPILER_TAGNAME_GCC4 = gcc4
COMPILER_TAGNAME_SOS12 = sos12

VENDOR_URL = http://www.gnu.org/software/libtool/

PACKAGES += CSWlibtool
CATALOGNAME_CSWlibtool = libtool
SPKG_DESC_CSWlibtool = A generic library support tool
# Double-legacy packages may not even depend on CSWlibtoolrt, so we must
# also directly depend on CSWlibltdl3
RUNTIME_DEP_PKGS_CSWlibtool += CSWlibltdl3
RUNTIME_DEP_PKGS_CSWlibtool += CSWlibltdl7
CHECKPKG_OVERRIDES_CSWlibtool += surplus-dependency|CSWlibltdl3
CHECKPKG_OVERRIDES_CSWlibtool += surplus-dependency|CSWlibltdl7

# These *may* be ok, as users could have installed stuff to /usr/local
# However, I think it is best to make linkage to /opt/csw/lib explicit and not
# auto-enable this as a simple replacement.
CHECKPKG_OVERRIDES_CSWlibtool += file= libtool_rt_stub

PACKAGES += CSWlibltdl7
CATALOGNAME_CSWlibltdl7 = libltdl7
SPKG_DESC_CSWlibltdl7 = Libtool libltdl.so.7 from libtool 2.x
PKGFILEcall pkgfiles_lib,libltdl.so.7)dl7 += CSWlibtoolrt

# To get around __sync_fetch_and_add_4 either the buildlevel could be raised to Solaris 10
# which is not acceptable for libtool or the base ISA could be raised to pentium_pro allowing
# the specific command set.
ISA_DEFAULT_i386-5.9 = pentium_pro

CONFIGURE_ARGS = $(DIRPATHFor SOS12 the following tests fail: 137 138 143 153 154 156 157 169
ot that important
#SKIPTEST ?= 1

   MERGE_SCRIPTS_isa-default-garcompiler-SOS12 = copy-all
 MERGE_SCRIPTS_isa-default64-garcompiler-SOS12 = copy-relocated-only
    MERGE_DIRS_isa-default64-garcompiler-SOS12 = $(libdir)

    MERGE_SCRIPTS_isa-default-garcompiler-GCC3 = copy-tags
    MERGE_SCRIPTS_isa-default-garcompiler-GCC4 = copy-tags

include gar/catego: $(if $(PATCHFILES_POSTINSTALL_$(MODULATION)),patch-libtool)
post-installt-install-modulated: $(if $(COMPILER_TAGNAME_$(GARCOMPILER)),install-libtool-$(COMPILER_TAGNAME_$(GARCOMPILER)))
	ginstall -d $(DESTDIR)$(docdir)/libtool
	ginstall $(WORKDIR)/README.CSW $(DESTDIR)$(docdir)/libtool/README.CSW
	@$(MAKECOOKIE)

patch-libtool:
	-cat $(WORKDIR)/$(PATCHFILES_POSTINSTALL_$(MODULATION)) | (cd $(DESTDIR)$(bindir) && 0patch --forward -p1)
	# Remove arch-specific flags from the libtool-compilation so they don't spoil the target build
	# Instead we inherit from CFLAGS as removing the arch specified leads to the default arch which
	# may very well be wrong (especially on sparc default is v8+ instead of the requested default v8
	# thus resulting in a different binary being generated).
	perl -pi -e 's/^LTCFLAGS=.*/if [ -z "\$$LTCFLAGS" ]; then \
  if [ -z "\$$CFLAGS" ]; then \
    LTCFLAGS="-O" \
  else \
    LTCFLAGS="\$$CFLAGS" \
  fi \
fi/' $(DESTDIR)$(bindir)/libtool

install-libtool-%:
	perl -ane 'print if( /^available_tags/ ); $$p = 1 if( /^# ### BEGIN LIBTOOL CONFIG/ ); print if( $$p ); $$p = 0 if( /^# ### END LIBTOOL CONFIG/ )' \
		<$(DESTDIR)$(bindir)/libtool >$(DESTDIR)$(datadir)/libtool/$*.conf
	perl -ane '$$p = 1 if( /^# ### BEGIN LIBTOOL TAG CONFIG/ ); print if( $$p ); if( /^# ### END LIBTOOL TAG CONFIG/ ) { $$p = 0; print "\n"; }' \
		<$(DESTDIR)$(bindir)/libtool >$(DESTDIR)$(datadir)/libtool/$*.tags

merge-copy-tags: $(PKGROOT)
	$(_DBG_MERGE)(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		-s ",^\(\..*\.conf\)\$$,\1,p" \
		-s ",^\(\..*\.tags\)\$$,\1,p" \
		-s ",.*,," \
		. $(PKGROOT) \
	)