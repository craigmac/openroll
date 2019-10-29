QT += multimedia widgets
TARGET = openroll
TEMPLATE = app
VERSION = 2.0.2

CONFIG += c++11
CONFIG(debug, debug|release) {
    # adds -DQT_DEBUG to preprocessor so we can use it in ifdef in source
    DEFINES += QT_DEBUG
    message(Debug build configuration selected...)
}

CONFIG(release, debug|release) :message(Release build config selected...)

SOURCES += \
        main.cpp \
        controls.cpp \
        scoreboard.cpp

HEADERS += \
    controls.h \
    openroll-config.h \
    scoreboard.h

FORMS += \
    controls.ui \
    scoreboard.ui

RESOURCES += \
    resources.qrc

# Files to copy on install
EXTRA_FILES += \
    AUTHORS \
    CHANGELOG \
    LICENSES.txt \
    README.md \
    gpl.txt \
    lgpl.txt

win32 {
    CONFIG += windows

    RC_ICONS = openroll.ico
    QMAKE_TARGET_COMPANY = "Barker Software"
    QMAKE_TARGET_DESCRIPTION = "Brazilian jiu-jitsu match timer and scoreboard using IBJJF ruleset."
    QMAKE_TARGET_COPYRIGHT = 2019
    QMAKE_TARGET_PRODUCT = "Openroll"

    CONFIG(debug, debug|release) {
        CONFIG += console
        SOURCES += logger.cpp
        HEADERS += logger.h
    }
}

osx {
    # Same, but for Apple, use osx tool to convert .ico to .icns file first
    ICON = openroll.icns

    CONFIG(debug, debug|release) {
        CONFIG -= app_bundle
        SOURCES += logger.cpp
        HEADERS += logger.h
    }
    CONFIG(release, debug|release) {
        CONFIG += app_bundle
    }
}

linux {
    # only on Linux/unix
    CONFIG += largefile

    CONFIG(debug, debug|release) {
        SOURCES += logger.cpp
        HEADERS += logger.h
    }
}
