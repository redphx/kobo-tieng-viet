include NickelHook/NickelHook.mk

override PKGCONF  += Qt5Widgets
override LIBRARY  := libtiengviet.so
override SOURCES  += src/tiengviet.cc
override MOCS     += src/tiengviet.h
override CFLAGS   += -Wall -Wextra -Werror
override CXXFLAGS += -Wall -Wextra -Werror -Wno-missing-field-initializers

include NickelHook/NickelHook.mk
