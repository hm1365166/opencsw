NAME = db
VERSION = 4.8.30
GARTYPE = bts

DESCRIPTION = Berkeley DB 4.8
define BLURB
  Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
  support for both traditional and client/server applications. It includes
  b+tree, queue, extended linear hashing, fixed, and variable-length record
  access methods, transactions, locking, logging, shared memory caching and
  database recovery. DB supports C, C++, Java, and Perl APIs. It is available
  for a wide variety of UNIX platforms as well as Windows NT and Windows 95
  (MSVC 4, 5 and 6).
endef

MASTER_SITES = http://download.oracle.com/berkeley-db/
DISTFILES = $(NAME)-$(VERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)/build_unix

PATCHDIR = $(WORKSRC)/..
PATCHDIRLEVEL = 0
PATCHFILES += $(notdir $(wildcard $(FILEDIR)/patch.*))
RELEASE = p$(words $(filter patch.$(VERSION).%,$(PATCHFILES)))

BUILD64 = 1

CONFIGURE_SCRIPTS = dist

prefix = $(BUILD_PREFIX)/bdb48
docdir = $(BUILD_PREFIX)/share/doc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-compat185
CONFIGURE_ARGS += --enable-o_direct
# No longer there in 4.8
#CONFIGURE_ARGS += --enable-rpc
CONFIGURE_ARGS += --enable-cxx
CONFIGURE_ARGS += --enable-java

# Exclude TCL support for 64 bit until we have a 64 bit TCL
CONFIGURE_ARGS-mm-32 = --enable-tcl --with-tcl=/opt/csw/lib
CONFIGURE_ARGS += $(CONFIGURE_ARGS-mm-$(MEMORYMODEL))

# bdb tests are *very* time consuming
TEST_SCRIPTS =

PACKAGES = NIMOSSbdb48 NIMOSSbdb48devel NIMOSSbdb48doc

CATALOGNAME_NIMOSSbdb48      = berkeleydb48
CATALOGNAME_NIMOSSbdb48devel = berkeleydb48_devel
CATALOGNAME_NIMOSSbdb48doc   = berkeleydb48_doc

ARCHALL_NIMOSSbdb48doc = 1

SPKG_DESC_NIMOSSbdb48      = BerkeleyDB 4.8 embedded database libraries and utilities
SPKG_DESC_NIMOSSbdb48devel = BerkeleyDB 4.8 development support
SPKG_DESC_NIMOSSbdb48doc   = BerkeleyDB 4.8 documentation

SPKG_SOURCEURL = http://www.oracle.com/technology/software/products/berkeley-db/db/index.html

RUNTIME_DEP_PKGS_NIMOSSbdb48devel = NIMOSSbdb48
CHECKPKG_OVERRIDES_NIMOSSbdb48devel += surplus-dependency|NIMOSSbdb48
CHECKPKG_OVERRIDES_NIMOSSbdb48 += missing-dependency|NIMOSSbdb48devel

LICENSE = LICENSE

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/docs,.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME_NIMOSSbdb48),'
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = .*/docs.* $(libdir)/db.jar
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = .*/docs.* $(libdir)/db.jar

# Remove the license from share/doc/berkeleydb/license/.*
# because GAR expects license to be a file instead of a directory
EXTRA_MERGE_EXCLUDE_FILES = .*/license.*

PKGFILES_NIMOSSbdb48doc = $(PKGFILES_DOC)
PKGFILES_NIMOSSbdb48devel = $(includedir)/.*

# Compiler run pathes, skip for now.
CHECKPKG_OVERRIDES_NIMOSSbdb48 += bad-rpath-entry

include gar/category.mk

LIBS += -lnsl
export LIBS

PATH := /usr/jdk1.6.0_20/bin:$(PATH)
export PATH

configure-dist:
	@( cd $(WORKSRC) ; $(CONFIGURE_ENV) ../dist/configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

post-merge:
	gln -s . $(PKGROOT)$(libdir)/32
	gln -s $(ISA_DEFAULT64) $(PKGROOT)$(libdir)/64
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

