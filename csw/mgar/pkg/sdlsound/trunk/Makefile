NAME = SDL_sound
VERSION = 1.0.1
GARTYPE = v1
CATEGORIES = lib

DESCRIPTION = A library that handles the decoding of several popular sound file formats
define BLURB
SDL_sound is a library that handles the decoding of several popular sound file formats, such as .WAV and .MP3. It is meant to make the programmer's sound playback tasks simpler. The programmer gives SDL_sound a filename, or feeds it data directly from one of many sources, and then reads the decoded waveform data back at her leisure. If resource constraints are a concern, SDL_sound can process sound data in programmer-specified blocks. Alternately, SDL_sound can decode a whole sound file and hand back a single pointer to the whole waveform. SDL_sound can also handle sample rate, audio format, and channel conversion on-the-fly and behind-the-scenes, if the programmer desires.
endef

MASTER_SITES = http://icculus.org/SDL_sound/downloads/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWsdlsound,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
