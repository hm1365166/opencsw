ACLOCAL_AMFLAGS = -I m4

bin_PROGRAMS=hello
hello_SOURCES=hello.c hello.1 system.h aclocal.m4 getopt.c getopt1.c getopt.h

#  uncomment the following if hello requires the math library
#hello_LDADD=-lm

EXTRA_DIST=hello.lsm.in hello.spec.in hello.texinfo

# AUTOMAKE_OPTIONS = gnu

lib_LTLIBRARIES = libhello.la
libhello_la_SOURCES = libhello.c
libhello_la_LDFLAGS = -version-info 0:0:0

#  if you write a self-test script named `chk', uncomment the
#  following and add `chk' to the EXTRA_DIST list
#TESTS=chk

#  build and install the .info pages
info_TEXINFOS = hello.texinfo
hello_TEXINFOS = gpl.texinfo

#  install the man pages
man_MANS=hello.1
