NAME = gaim
VERSION = 2.0.0beta3
GARTYPE = v1
CATEGORIES = gnome

DESCRIPTION = A GTK2-based instant messaging client.
define BLURB
	Gaim is a GTK2-based instant messenger application. It supports multiple
	protocols via modules, including AIM, ICQ, Yahoo!, MSN, Jabber, IRC,
	Napster, Gadu-Gadu and Zephyr. It has many common features found in other
	clients, as well as many unique features. Gaim is not endorsed by or
	affiliated with AOL TimeWarner, Microsoft, or Yahoo.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=3157
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

ifneq ($(BUILD_XDEPS),0)
LIBDEPS = lib/libao
endif

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
