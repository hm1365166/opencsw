NAME = docbook
VERSION = 1.68.1
GARTYPE = v1
CATEGORIES = lib

DESCRIPTION = docbook xsl stylesheets
define BLURB
  DocBook is an XML/SGML vocabulary that enables you to create document
  content in a presentation-neutral form that captures the logical structure
  of the content. Using the DocBook stylesheets, you can publish DocBook
  content as HTML pages and PDF files and other formats, including man pages,
  HTML Help, and JavaHelp.
endef

MASTER_SITES = $(SF_MIRROR)/$(NAME)/
DISTFILES = $(NAME)-xsl-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=21935
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo how the heck does this get installed??!
	@false
