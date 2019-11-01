QT += multimedia widgets
TARGET = openroll
TEMPLATE = app
VERSION = 2.0.2

CONFIG += c++11

# Extra files to copy into the build output directory
extra_files.files = AUTHORS CHANGELOG gpl.txt lgpl.txt LICENSES.txt

# Debug configuration
CONFIG(debug, debug|release) {
    # adds -DQT_DEBUG to preprocessor so we can use it in ifdef in source
    DEFINES += QT_DEBUG
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

INSTALLS += extra_files

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
        extra_files.path = $$OUT_PWD/debug
    }
    CONFIG(release, debug|release) {
        extra_files.path = $$OUT_PWD/release
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

!build_pass:message("======================================")
!build_pass:message("Building: $${TARGET} with QT_VERSION $${QT_VERSION}")
!build_pass:message("Using pro file at $$_PRO_FILE_PWD_")
!build_pass:message("Compiler: $${QMAKE_CXX}")
!build_pass:message("QMake from: $${QMAKE_QMAKE}")
!build_pass:message("======================================")
