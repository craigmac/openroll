#include "logger.h"

/* Have to initialize static vars here, can't do it in constructor */
QString logger::filename = QDir::currentPath() + QDir::separator() + "log.txt";
bool logger::logging = false; // don't log until we attach()
/* All this does is call qInstallMessageHandler to get back the default QtMessageHandler that
 * Qt uses. We want this to pass on anything we handle to let it do its default thing after we've
 * handled it.
 */
static const QtMessageHandler QT_DEFAULT_MESSAGE_HANDLER = qInstallMessageHandler(nullptr);



logger::logger(QObject *parent) : QObject(parent)
{

}

/**
 * @brief logger::attach - Install our QtMessageHandler and turn on logging.
 */
void logger::attach()
{
    logger::logging = true;
    qInstallMessageHandler(logger::handler);
}

/**
 * @brief logger::handler - The custom QtMessageHandler implementation.
 * @param type
 * @param context
 * @param msg
 * @
 */
void logger::handler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
{
    if(logger::logging) {
        QString txt;

        switch (type) {
        case QtInfoMsg:
            txt = QString("Info: %1").arg(msg);
            break;
        case QtDebugMsg:
            txt = QString("Debug: %1").arg(msg);
            break;
        case QtWarningMsg:
            txt = QString("Warning: %1").arg(msg);
            break;
        case QtCriticalMsg:
            txt = QString("Critical: %1").arg(msg);
            break;
        case QtFatalMsg:
            txt = QString("Fatal: %1").arg(msg);
            break;
        }

        QFile file(logger::filename);

        if(file.open(QIODevice::WriteOnly | QIODevice::Append)) {
            QTextStream ts(&file);
            ts << QDateTime::currentDateTime().toString() << " - "
               << txt << " file: " << context.file
               << " line: " << context.line << "\r\n";
            ts.flush(); // not required but makes faster
            file.close();
        } else {
            qWarning() << "Could not open log file for appending!";
        }
    }

    // Regardless of what we've done, pass it on to the default handler to print to stdout
    (*QT_DEFAULT_MESSAGE_HANDLER)(type, context, msg);
}
