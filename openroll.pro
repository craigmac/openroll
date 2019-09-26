QT       += multimedia widgets

TARGET = openroll
TEMPLATE = app

DEFINES += QT_DEPRECATED_WARNINGS

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

DISTFILES += \
    AUTHORS \
    CHANGELOG \
    LICENSES.txt \
    license.txt

# As per docs, to generate Windows icon for .exe file in Explorer
RC_ICONS = openroll.ico
# Same, but for Apple, use osx tool to convert .ico to .icns file first
# ICON = openroll.icns
