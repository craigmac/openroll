#include "controls.h"
#include <QApplication>

/* Definition of static class member var, does not
 * require object to access, available to all like a
 * global var. Must be defined outside of main or a function.
 */
const QString Controls::s_VERSION = "2.0.0";

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Controls w;
    w.show();

    return a.exec();
}
