# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# * pyconfig.h (via "Python.h") unconditionally sets _FILE_OFFSET_BITS = 64.
#   "/opt/csw/include/python2.6/pyconfig.h", line 1016: warning: macro redefined: _FILE_OFFSET_BITS
#
# * setup.py unconditionally passes gcc flags
#     cc: Warning: illegal option -d=c99
#     cc: Warning: illegal option -fomit-frame-pointer
#

NAME = pycrypto
VERSION = 2.6.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = The Python Cryptography Toolkit
define BLURB
  The Python cryptography toolkit is intended to provide a reliable and
  stable base for writing Python programs that require cryptographic
  functions.
endef

MASTER_SITES = http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/
DISTFILES += $(DISTNAME).tar.gz

# Make sure to skip test when sem_open is not available. Use patch until this is fixed:
#   https://github.com/dlitz/pycrypto/pull/61
PATCHFILES += 0001-Allow-testing-when-sem_open-does-not-exist.-See-http.patch

LICENSE = COPYRIGHT

BUILD_DEP_PACKAGES += CSWlibgmp-dev

PACKAGES += CSWpy-crypto
SPKG_DESC_CSWpy-crypte = The Python Cryptography Toolkit
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-crypto += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-crypto += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWpy-crypto += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-crypto += CSWlibpython2-7-1-0

include gar/category.mk
