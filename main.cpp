#include "controls.h"
#include <QApplication>

int main(int argc, char* argv[])
{
    QApplication app(argc, argv);
    Controls controls;
    const Qt::WindowFlags flags(Qt::Window | Qt::WindowStaysOnTopHint);
    controls.setWindowFlags(flags);
    QObject::connect(&app, &QCoreApplication::aboutToQuit, &controls, &Controls::onAboutToQuit);
    controls.show();

    return QApplication::exec();
}
