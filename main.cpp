#include "controls.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Controls w;
    w.show();

    return a.exec();
}
