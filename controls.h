#ifndef CONTROLS_H
#define CONTROLS_H

#include <QMainWindow>
#include <QLabel>
#include <QTimer>
#include <QCloseEvent>
#include <QtMultimedia/QMediaPlayer>
#include <QMap>
#include "scoreboard.h"

namespace Ui {
class Controls;
}

class Controls : public QMainWindow
{
    Q_OBJECT

public:
    explicit Controls(QWidget *parent = nullptr);
    ~Controls() override;
    static const QString s_VERSION;

private slots:
    // Competitor 1 Controls
    void on_c1Add2Button_pressed();
    void on_c1Del2Button_pressed();
    void on_c1Add3Button_pressed();
    void on_c1CustomFlagButton_pressed();
    void on_c2CustomLogoButton_pressed();
    void on_c1Del3Button_pressed();
    void on_c1Add4Button_pressed();
    void on_c1Del4Button_pressed();
    void on_c1AddAButton_pressed();
    void on_c1DelAButton_pressed();
    void on_c1AddPButton_pressed();
    void on_c1DelPButton_pressed();
    void on_c1LineEdit_textEdited(const QString &arg1);

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
    void on_c2FlagComboBox_currentIndexChanged(int index);
    void on_c2LineEdit_textEdited(const QString &arg1);

    // General Buttons
    void on_playPauseButton_pressed();
    void on_resetButton_pressed();
    void on_loadLogoButton_pressed();
    void on_testSoundButton_pressed();

    // Dropdowns
    void on_divisionComboBox_currentIndexChanged(int index);
    void on_soundComboBox_currentIndexChanged(const QString &sound);
    void populateFlagDropDowns();
    void on_c1FlagComboBox_currentIndexChanged(const QString &flag);
    void on_c2FlagComboBox_currentIndexChanged(const QString &flag);

    // Actions
    void modify_points(QLabel *label, int amount);
    void updateClock();
    void playSound();
    void disableControls();
    void enableControls();
    void updateDisplay();
    QString calcNewTimeString();
    void resetMatchStates();

private:
    Ui::Controls *ui;
    Scoreboard *board;
    int defaultTime = 300; // 5 minutes
    int defaultDivisionIdx = 14; // ADULT 1A - AGE 18- 29 - WHITE

    // Clock-related
    int totalTime = 300; // default time at first
    int clockMinutes = totalTime / 60;
    int clockSeconds = totalTime % 60;

    // State
    bool matchStarted = false;
    bool clockRunning = false;
    bool clockPaused = false;
    bool matchDone = false;

    // Default division and belt
    QString m_currentDivision = "ADULT";
    QString m_currentBelt = "WHITE";

    QTimer *timer;
    QMediaPlayer *m_player;
    QUrl m_defaultSound = QUrl("qrc://sounds/airhorn.wav");

    // Used to return division time from dropdown index
    QMap<int, int> divisionIdxToTimeMap;

    // Maps country display name to icon in qrc file
    QMap<QString, QString> countryToResourceMap;

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

    //void soundChanged(int index);

    void playPauseStateChanged(bool isPaused);
    void matchReset();

    void competitor1NameChanged(QString name);
    void competitor2NameChanged(QString name);

    void timerUpdated(QString time);
    void divisionUpdated(QString division);
    void beltUpdated(QString belt);
    void logoUpdated(QString filename);


    // TODO: c1 and c2 Flag changed signals hook up
    void c1FlagChanged(QString flagpath);
    void c2FlagChanged(QString flagpath);

protected:
    void closeEvent(QCloseEvent *event) override;
};

#endif // CONTROLS_H
