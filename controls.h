#ifndef CONTROLS_H
#define CONTROLS_H

#include <QMainWindow>
#include <QLabel>
#include "scoreboard.h"

namespace Ui {
class Controls;
}

class Controls : public QMainWindow
{
    Q_OBJECT

public:
    explicit Controls(QWidget *parent = nullptr);
    ~Controls();

private slots:
    // Competitor 1 Controls
    void on_c1Add2Button_pressed();

    void on_c1Del2Button_pressed();

    void on_c1Add3Button_pressed();

    void on_divisionComboBox_currentIndexChanged(int index);

    void on_soundComboBox_currentIndexChanged(const QString &arg1);

    void on_MuteRadioButton_pressed();

    void on_OnRadioButton_pressed();

    void on_loadLogoButton_pressed();

    void on_c1FlagComboBox_currentIndexChanged(int index);

    void on_c1CustomFlagButton_pressed();

    void on_c2CustomLogoButton_pressed();

    void on_c2FlagComboBox_currentIndexChanged(int index);

    void on_playPauseButton_pressed();

    void on_resetButton_pressed();

    void on_c1Del3Button_pressed();

    void on_c1Add4Button_pressed();

    void on_c1Del4Button_pressed();

    void on_c1AddAButton_pressed();

    void on_c1DelAButton_pressed();

    void on_c1AddPButton_pressed();

    void on_c1DelPButton_pressed();

    // Competitor 2 Controls
    void on_c2Add2Button_pressed();

    void on_c2Del2Button_pressed();

    void on_c2Add3Button_pressed();

    void on_c2Del3Button_pressed();

    void on_c2Add4Button_pressed();

    void on_c2Del4Button_pressed();

    void on_c2AddAButton_pressed();

    void on_c2DelAButton_pressed();

    void on_c2AddPButton_pressed();

    void on_c2DelPButton_pressed();

    void modify_points(QLabel *label, int amount);

    void on_c1LineEdit_textEdited(const QString &arg1);

    void on_c2LineEdit_textEdited(const QString &arg1);

private:
/*     void populate_default_sounds_dropdown(); */
/*     void populate_flag_combobox(); */
/*     void populate_divisions_combobox(); */

    Ui::Controls *ui;
    Scoreboard *board;
    int default_time = 300; // 5 minutes
    int default_division_idx = 14; // ADULT 1A - AGE 18- 29 - WHITE
    int total_time = 300; // default time at first
    int clock_minutes = total_time / 60;
    int clock_seconds = total_time % 60;
    bool match_started = false;
    bool match_done = false;
    bool clock_running = false;
    bool clock_paused = false;
    QString current_division = "";
    QString current_belt = "";

//    QTimer timer;
//    QMediaPlayer media_player;
//    QSound default_sound = QUrl("qrc:///sounds/airhorn.wav");

signals:
    void competitor1PointsChanged(int value);
    void competitor1AdvantagesChanged(int value);
    void competitor1PenaltiesChanged(int value);

    void competitor2PointsChanged(int value);
    void competitor2AdvantagesChanged(int value);
    void competitor2PenaltiesChanged(int value);

    void competitor1FlagChanged(int index);
    void competitor2FlagChanged(int index);
    void competitor1CustomFlagLoaded(QString flag);
    void competitor2CustomFlagLoaded(QString flag);

    void soundChanged(int index);

    void playPauseStateChanged(bool isPaused);
    void matchReset();

    void competitor1NameChanged(QString name);
    void competitor2NameChanged(QString name);
};

#endif // CONTROLS_H
