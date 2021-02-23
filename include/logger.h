#ifndef QT_DEBUG_H
#define QT_DEBUG_H

#include <QObject>
#include <QDebug>
#include <QDateTime>
#include <QFile>
#include <QDir>
#include <iostream>
#include <QTextStream>

/* Reusable custom Qt logging class */

class logger : public QObject
{
    Q_OBJECT
public:
    explicit logger(QObject *parent = nullptr);

    // Making static so we don't need an instance to use it
    static bool logging;
    static QString filename;
    static void attach(); // allows attach msg handle to static parts of this class
    static void handler(QtMsgType type, const QMessageLogContext &context, const QString &msg);


signals:

public slots:
};

#endif // QT_DEBUG_H
