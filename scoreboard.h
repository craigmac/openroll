#ifndef SCOREBOARD_H
#define SCOREBOARD_H

#include <QWidget>

namespace Ui {
class Scoreboard;
}

class Scoreboard : public QWidget
{
    Q_OBJECT

public:
    explicit Scoreboard(QWidget *parent = nullptr, Qt::WindowFlags f = Qt::WindowFlags());
    ~Scoreboard();

public slots:
    /* These are connected to signals emitted from another object using
     * QObject::connect() function. We set up emitting signals and their signature in
     * controls.h and create the signal-slot connection in controls.cpp initializer.
     */
    void setCompetitor1Points(int value);
    void setCompetitor1Advantages(int value);
    void setCompetitor1Penalties(int value);

    void setCompetitor2Points(int value);
    void setCompetitor2Advantages(int value);
    void setCompetitor2Penalties(int value);

    void setCompetitor1Name(QString name);
    void setCompetitor2Name(QString name);

private:
    Ui::Scoreboard *ui;
    int m_c1_points = 0;
    int m_c1_advantages = 0;
    int m_c1_penalties = 0;
    int m_c2_points = 0;
    int m_c2_advantages = 0;
    int m_c2_penalties = 0;

};

#endif // SCOREBOARD_H
