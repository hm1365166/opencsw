NAME = hdf5
VERSION = 1.8.6
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Event notification library
define BLURB
  The libevent API provides a mechanism to execute a callback function when a
  specific event occurs on a file descriptor or after a timeout has been
  reached. Furthermore, libevent also support callbacks due to signals or
  regular timeouts.
endef

MASTER_SITES += http://www.hdfgroup.org/ftp/HDF5/hdf5-$(VERSION)/src/
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWlibhdf5-6
SPKG_DESC_CSWlibhdf5-6 = HDF5 (hierarchical data format 5) library, libhdf5.so.6
PKGFILES_CSWlibhdf5-6 += $(call pkgfiles_lib,libhdf5.so.6)
OBSOLETED_BY_CSWlibhdf5-6 += CSWhdf5rt
CATALOGNAME_CSWhdf5rt = hdf5_rt_stub
RUNTIME_DEP_PKGS_CSWlibhdf5-6 += CSWlibz1

PACKAGES += CSWlibhdf5hl6
SPKG_DESC_CSWlibhdf5hl6 = HDF5 (hierarchical data format 5) library, libhdf5_hl.so.6
PKGFILES_CSWlibhdf5hl6 += $(call pkgfiles_lib,libhdf5_hl.so.6)
RUNTIME_DEP_PKGS_CSWlibhdf5hl6 += CSWlibz1
OBSOLETED_BY_CSWlibhdf5hl6 += CSWhdf5rt

# Now dev is only built for 1.8.7 or newer
#PACKAGES += CSWlibhdf5-dev
#SPKG_DESC_CSWlibhdf5-dev = Development files for libhdf5.so.6 and libhdf5_hl.so.6
## PKGFILES is catchall
#RUNTIME_DEP_PKGS_CSWlibhdf5-dev += CSWlibhdf5-6
#RUNTIME_DEP_PKGS_CSWlibhdf5-dev += CSWlibhdf5hl6

# Same for the binaries, no point in having old ones around
#PACKAGES += CSWhdf5
#SPKG_DESC_CSWhdf5 = HDF5 (hierarchical data format 5) software utilities
#PKGFILES_CSWhdf5 += $(bindir)/.*
#RUNTIME_DEP_PKGS_CSWhdf5 += CSWlibhdf5-6
#RUNTIME_DEP_PKGS_CSWhdf5 += CSWlibhdf5hl6
#RUNTIME_DEP_PKGS_CSWhdf5 += CSWlibz1

VENDOR_URL = http://www.hdfgroup.org/HDF5/

# By default -L/opt/csw/lib is used which makes the new libhdf5_hl.so link to
# the existing /opt/csw/lib/libhdf5.so
LINKER_FLAGS =

BUILD64 = 1

# Image files can be really big
ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)
#CONFIGURE_ARGS += --enable-fortran
#CONFIGURE_ARGS += --enable-cxx

include gar/category.mk
