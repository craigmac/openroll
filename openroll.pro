QT       += multimedia widgets

TARGET = openroll
TEMPLATE = app
VERSION = 2.0.1

# for Windows resource-file
QMAKE_TARGET_COMPANY = "Barker Software"
QMAKE_TARGET_DESCRIPTION = "Brazilian jiu-jitsu match timer and scoreboard using IBJJF ruleset."
QMAKE_TARGET_COPYRIGHT = 2019
QMAKE_TARGET_PRODUCT = "Openroll"

CONFIG += c++11

SOURCES += \
        logger.cpp \
        main.cpp \
        controls.cpp \
        scoreboard.cpp

HEADERS += \
    controls.h \
    logger.h \
    openroll-config.h \
    scoreboard.h

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

FORMS += \
    controls.ui \
    scoreboard.ui

RESOURCES += \
    resources.qrc

# only works with Unix makefiles, Windows you have to copy these manually or with script
DISTFILES += \
    AUTHORS \
    CHANGELOG \
    LICENSES.txt \
    README.md \
    gpl.txt \
    lgpl.txt

win32 {
    RC_ICONS = openroll.ico
#ifdef QT_DEBUG
    CONFIG += console
#else
    CONFIG -= console
#endif
}

osx {
    # Same, but for Apple, use osx tool to convert .ico to .icns file first
    ICON = openroll.icns
    CONFIG += app_bundle
}

linux {

}
