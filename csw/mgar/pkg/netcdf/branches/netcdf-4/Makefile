# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = netcdf
VERSION = 4.1.1
CATEGORIES = lib
DESCRIPTION = Machine-independent data formats for array-oriented scientific data
SPKG_SOURCEURL = http://www.unidata.ucar.edu/software/netcdf/
MASTER_SITES = http://www.unidata.ucar.edu/downloads/netcdf/ftp/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = COPYRIGHT

BUILD_DEP_PKGS += CSWhdf5rt CSWzlib
BUILD_DEP_PKGS += CSWgcc4gfortranrt CSWgcc4corert CSWgcc4g++rt
BUILD_DEP_PKGS += CSWtetex 
BUILD_DEP_PKGS += CSWgcc4gfortran

PACKAGES = CSWnetcdf
CATALOGNAME_CSWnetcdf = netcdf
SPKG_DESC_CSWnetcdf = Machine-independent data formats for array-oriented scientific data
RUNTIME_DEP_PKGS_CSWnetcdf += CSWhdf5rt
RUNTIME_DEP_PKGS_CSWnetcdf += CSWzlib
RUNTIME_DEP_PKGS_CSWnetcdf += CSWlibnetcdf6

PACKAGES += CSWlibnetcdf6
CATALOGNAME_CSWlibnetcdf6 = libnetcf6
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/libnetcdf.so.6.0.0
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/libnetcdf.so.6\.[0-9\.]+
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/libnetcdf.so.6
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/sparcv9/libnetcdf.so.6.0.0
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/sparcv9/libnetcdf.so.6\.[0-9\.]+
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/sparcv9/libnetcdf.so.6
SPKG_DESC_CSWlibnetcdf6 = Machine-independent data formats for array-oriented scientific data, libnetcdf.so.6
RUNTIME_DEP_PKGS_CSWlibnetcdf6  = CSWhdf5rt
RUNTIME_DEP_PKGS_CSWlibnetcdf6 += CSWgcc4corert

PACKAGES += CSWlibnetcdf-c++5
CATALOGNAME_CSWlibnetcdf-c++5 = libnetcdf_c++5
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/libnetcdf_c\+\+.so.5.0.0
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/libnetcdf_c\+\+.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/libnetcdf_c\+\+.so.5
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so.5.0.0
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so.5
SPKG_DESC_CSWlibnetcdf-c++5 += Machine-independent data formats for array-oriented scientific data, libnetcdf_c++.so.5
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++5  = CSWhdf5rt
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++5 += CSWgcc4corert CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++5 += CSWlibnetcdf6

PACKAGES += CSWlibnetcdff5
CATALOGNAME_CSWlibnetcdff5 = libnetcdff5
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/libnetcdff.so.5.0.0
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/libnetcdff.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/libnetcdff.so.5
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/sparcv9/libnetcdff.so.5.0.0
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/sparcv9/libnetcdff.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/sparcv9/libnetcdff.so.5
SPKG_DESC_CSWlibnetcdff5 = Machine-independent data formats for array-oriented scientific data, libnetcdff.so.5
RUNTIME_DEP_PKGS_CSWlibnetcdff5  = CSWhdf5rt
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWgcc4gfortranrt CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibnetcdf6

PACKAGES += CSWnetcdf-devel
CATALOGNAME_CSWnetcdf-devel = netcdf_devel
SPKG_DESC_CSWnetcdf-devel = Development files for NetCDF 
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/libnetcdf.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/libnetcdf_c\+\+.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/libnetcdff.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/sparcv9/libnetcdf.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/sparcv9/libnetcdff.so
PKGFILES_CSWnetcdf-devel += $(PKGFILES_DEVEL)

## CFLAGS AND LDFLAGS are necessary due to problems with the fortran bindings when
## building 64-bit
BUILD_ARGS  = CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)" 
BUILD_ARGS += FFLAGS="$(FFLAGS)" FCFLAGS="$(FCFLAGS)"
## CXXFLAGS are necessary due to the gcc3core_rt problem noted below
BUILD_ARGS += CXXFLAGS="$(CXXFLAGS)"

## Test args need to be the same otherwise various tests don't link
TEST_ARGS = $(BUILD_ARGS)

GARCOMPILER = GCC4
## Attempt to fix problem with configure not finding libgfortran.so.3 when 
## compiling with GCC4
CONFIGURE_ENV += LD_LIBRARY_PATH=/opt/csw/gcc4/lib/$(MM_LIBDIR)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += F77=$(F77) FC=$(FC) CC=$(CC) CXX=$(CXX)
CONFIGURE_ARGS += CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)" FFLAGS="$(FFLAGS)" FCFLAGS="$(FCFLAGS)"
CONFIGURE_ARGS += --enable-netcdf-4
## DAP is disabled due to bugs on Sparc Solaris 9 GCC4. Bug filed with UCAR:
## netCDF #ARO-502165
#CONFIGURE_ARGS += --enable-dap
CONFIGURE_ARGS += --disable-dap
CONFIGURE_ARGS += --enable-ncgen4
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-separate-fortran
CONFIGURE_ARGS += --enable-cxx4
CONFIGURE_ARGS += --enable-docs-install
CONFIGURE_ARGS += --enable-udunits
CONFIGURE_ARGS += --disable-logging
CONFIGURE_ARGS += --with-hdf5=/opt/csw
CONFIGURE_ARGS += --with-zlib=/opt/csw

BUILD64 = 1

## Needed for "Large file support" in NetCDF
EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64


DEBUG_PACKAGING = 1
## Add GCC4 lib dir to CFLAGS and friends because gcc3core_rt puts it's 
## libgcc_s.so in /opt/csw/lib and this breaks the build in all sorts of weird 
## places.
## Rationale: Automake keeps wanting to put /opt/csw/lib in the front of the 
## -L options during the linking phase, so the GCC3 libgcc_s gets pulled in 
## first and an unresolved symbol error occurs. By adding to the 
## CFLAGS/FFLAGS/FCFLAGS/CXXFLAGS, it is pulled in before AM_LDFLAGS in the 
## linking stage in most automake-generated Makefiles. Ugly hack but it works.
##
## Adding -dalign to *FLAGS in attempt to fix bus error in nf_test/ftst_vars4
## in fuction nf_put_vlen_element
EXTRA_CFLAGS = -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
EXTRA_FFLAGS= -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
EXTRA_FCFLAGS = -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
EXTRA_CXXFLAGS = -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
## OPT_FLAGS_GCC = -O2 -pipe

## During the 32-bit sparc build, the C++ bindings were barfing with an error 
## about undefined symbol __sync_fetch_and_add_4 in libnetcdf_c++
## From Porting FAQ: http://wiki.opencsw.org/porting-faq#toc5
OPT_FLAGS_GCC = 

include gar/category.mk
