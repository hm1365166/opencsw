NAME = resin
VERSION = 3.0.9
GARTYPE = v1
CATEGORIES = server

DESCRIPTION = JSP and Servlet engine.
define BLURB
  Resin provides fast Java servlets, JSP (Java Server Pages), XSLT, compiled
  JavaScript and a Java Web server. Its XSL can create JSP pages from XML,
  servlets can be filtered with XSL stylesheets, and JSP pages can use
  server-side JavaScript in addition to Java.
endef

MASTER_SITES = http://www.caucho.com/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
#DISTFILES += CSWresin.gspec
#DISTFILES += CSWap2modcaucho.gspec

#DEPENDS = server/apache2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = --prefix=$(prefix)/resin
CONFIGURE_ARGS += --enable-jni
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-perl=$(bindir)/perl

include gar/category.mk

