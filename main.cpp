#include "controls.h"
#include <QApplication>

/* Definition of static class member var, does not
 * require object to access, available to all like a
 * global var. Must be defined outside of main or a function.
 */
const QString Controls::s_VERSION = "2.0.0-alpha";

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    Controls controls;
    const Qt::WindowFlags flags(Qt::Window | Qt::WindowStaysOnTopHint);
    controls.setWindowFlags(flags);
    QObject::connect(&app, &QCoreApplication::aboutToQuit, &controls, &Controls::onAboutToQuit);
    controls.show();

    return QApplication::exec();
}
