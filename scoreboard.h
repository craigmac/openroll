#ifndef SCOREBOARD_H
#define SCOREBOARD_H

#include <QWidget>
#include <QCloseEvent>

namespace Ui {
class Scoreboard;
}

class Scoreboard : public QWidget
{
    Q_OBJECT

protected:
    void closeEvent(QCloseEvent *event) override;

public:
    explicit Scoreboard(QWidget *parent = nullptr, Qt::WindowFlags f = Qt::WindowFlags());
    ~Scoreboard() override;

public slots:
    void setCompetitor1Points(int value);
    void setCompetitor1Advantages(int value);
    void setCompetitor1Penalties(int value);

    void setCompetitor2Points(int value);
    void setCompetitor2Advantages(int value);
    void setCompetitor2Penalties(int value);

    void setCompetitor1Name(const QString& name);
    void setCompetitor2Name(const QString& name);

    void setClockDisplay(const QString &newtime);
    void setDivisionLabel(const QString& division);
    void setBeltLabel(const QString& newbelt);

    void setLogo(const QString& logo);
    void resetScores();

    void setC1Flag(const QString& flagpath);
    void setC2Flag(const QString& flagpath);

private:
    Ui::Scoreboard *ui;
};

#endif // SCOREBOARD_H
