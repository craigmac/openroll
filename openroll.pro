QT       += multimedia widgets

TARGET = openroll
TEMPLATE = app
VERSION = 2.0.0

# for Windows resource-file
QMAKE_TARGET_COMPANY = "Barker Software"
QMAKE_TARGET_DESCRIPTION = "Brazilian jiu-jitsu match timer and scoreboard using IBJJF ruleset."
QMAKE_TARGET_COPYRIGHT = 2019
QMAKE_TARGET_PRODUCT = "Openroll"

CONFIG += c++11

SOURCES += \
        main.cpp \
        controls.cpp \
        scoreboard.cpp

HEADERS += \
    controls.h \
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

# supported by UnixMake specs only, put these in DESTDIR with TARGET
DISTFILES += \
    AUTHORS \
    CHANGELOG \
    LICENSES.txt \
    README.md \
    license.txt

win32: {
    RC_ICONS = openroll.ico
}

osx: {
    # Same, but for Apple, use osx tool to convert .ico to .icns file first
    ICON = openroll.icns
}

linux: {

}
