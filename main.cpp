#include "controls.h"
#include <QApplication>
#ifdef QT_DEBUG
#include "logger.h"
#include <QDebug>
#endif

int main(int argc, char *argv[]) {
  QApplication app(argc, argv);

  Controls controls;

  const Qt::WindowFlags flags(Qt::Window | Qt::WindowStaysOnTopHint);
  controls.setWindowFlags(flags);
  controls.show();

#ifdef QT_DEBUG
  qInfo() << "Using log file named: " << logger::filename;
  logger::attach();
#endif

  return QApplication::exec();
}
