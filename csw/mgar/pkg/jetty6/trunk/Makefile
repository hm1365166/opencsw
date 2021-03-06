NAME = jetty6
VERSION = 6.1.14
CATEGORIES = server
GARTYPE = v2
GARCH=all

DESCRIPTION = Standards-based, full-featured web server and servlet container.
define BLURB
Jetty 6 is a fully featured web server for static and dynamic content.
Unlike separate server/container solutions, this means that your web
server and web application run in the same process, without
interconnection overheads and complications. in addition, as a pure
java component, Jetty 6 can be simply included in your application for
demonstration, distribution or deployment. It is available on all Java
supported platforms.
endef

MASTER_SITES = http://dist.codehaus.org/jetty/jetty-$(VERSION)/
DISTFILES  = jetty-$(VERSION).zip default-jetty6 etc-README.txt share-jetty.xml bin-create-instance
DISTFILES += cswjetty6 cswjetty6.xml svc-cswjetty6
DISTFILES += $(call admfiles,CSW$(NAME),prototype csw_usrgrp_config postinstall)
DISTFILES += $(call admfiles,CSW$(NAME)doc,prototype)

RUNTIME_DEP_PKGS = 

SPKG_SOURCEURL = http://jetty.mortbay.org

SPKG_DESC_CSWjetty6doc=Documentation for Jetty 6

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = jetty-(\d+(?:\.\d+)*).zip

#CONFIGURE_SCRIPTS =
#BUILD_SCRIPTS =
SKIPTEST = 1
#INSTALL_SCRIPTS = custom

include gar/category.mk

COPY_FILES=LICENSES README.txt VERSION.txt etc lib resources/log4j.properties start.jar javadoc
TO_COPY=$(foreach file,$(COPY_FILES),cp $(WORKDIR)/jetty-$(VERSION)/$(COPY_FILES) $(DESTDIR)/opt/csw/share/jetty6/$(COPY_FILES))

install-custom:
	mkdir -p $(DESTDIR)/opt/csw/share
	mkdir -p $(DESTDIR)/etc/init.d
	mkdir -p $(DESTDIR)/etc/default
	mkdir -p $(DESTDIR)/etc/opt/csw/jetty6/instances
	# Save a couple of files before pruning the unwanted stuff
	cp $(WORKDIR)/jetty-$(VERSION)/bin/jetty.sh $(DESTDIR)/etc/init.d/cswjetty6
	rm -rf $(DESTDIR)/opt/csw/share/jetty6
	mkdir -p $(DESTDIR)/opt/csw/share/jetty6/home
	mkdir -p $(DESTDIR)/opt/csw/share/jetty6/home/resources
	$(foreach file,$(COPY_FILES),cp -r $(WORKDIR)/jetty-$(VERSION)/$(file) $(DESTDIR)/opt/csw/share/jetty6/home/$(file) &&) true
	rm -rf $(DESTDIR)/opt/csw/share/jetty6/home/lib/ext/libsetuid.so
	mkdir -p $(DESTDIR)/opt/csw/share/jetty6/bin
	mkdir -p $(DESTDIR)/opt/csw/share/jetty6/etc
	# Install CSW specific files
	cp $(WORKDIR)/default-jetty6 $(DESTDIR)/etc/default/jetty6
	cp $(WORKDIR)/etc-README.txt $(DESTDIR)/etc/opt/csw/jetty6/instances/README.txt
	cp $(WORKDIR)/bin-create-instance $(DESTDIR)/opt/csw/share/jetty6/bin/create-instance
	cp $(WORKDIR)/share-jetty.xml $(DESTDIR)/opt/csw/share/jetty6/etc/jetty.xml
	$(MAKECOOKIE)
