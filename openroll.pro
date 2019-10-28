QT += multimedia widgets
TARGET = openroll
TEMPLATE = app
VERSION = 2.0.1

CONFIG += c++11
CONFIG(debug) {
    # adds -DLOGGER to preprocessor so we can use it in ifdef in source
    DEFINES += LOGGER
}

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

# only works with Unix makefiles, Windows you have to copy these manually or with script
EXTRA_FILES += \
    AUTHORS \
    CHANGELOG \
    LICENSES.txt \
    README.md \
    gpl.txt \
    lgpl.txt

win32 {
    RC_ICONS = openroll.ico
    QMAKE_TARGET_COMPANY = "Barker Software"
    QMAKE_TARGET_DESCRIPTION = "Brazilian jiu-jitsu match timer and scoreboard using IBJJF ruleset."
    QMAKE_TARGET_COPYRIGHT = 2019
    QMAKE_TARGET_PRODUCT = "Openroll"

    CONFIG(debug) {
        CONFIG += console
        SOURCES += logger.cpp
        HEADERS += logger.h
    }
}

osx {
    # Same, but for Apple, use osx tool to convert .ico to .icns file first
    ICON = openroll.icns
    CONFIG += app_bundle
    CONFIG(debug) {
        SOURCES += logger.cpp
        HEADERS += logger.h
    }
}

linux {
    CONFIG(debug) {
        SOURCES += logger.cpp
        HEADERS += logger.h
    }
}
