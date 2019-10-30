#ifndef CONTROLS_H
#define CONTROLS_H

#include "scoreboard.h"
#include <QCloseEvent>
#include <QLabel>
#include <QMainWindow>
#include <QMap>
#include <QTime>
#include <QTimer>
#include <QtMultimedia/QMediaPlayer>

namespace Ui {
class Controls;
}

class Controls : public QMainWindow
{
    Q_OBJECT

public:
    explicit Controls(QWidget *parent = nullptr);
    ~Controls() override;

public slots:
  void matchNewSetup();
  void matchPlay();
  void matchPause();

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
  void on_c1LineEdit_textEdited(const QString &str);

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
  void on_c2LineEdit_textEdited(const QString &str);

  // General Buttons
  void on_loadLogoButton_pressed();
  void on_testSoundButton_pressed();

  // Dropdowns
  void on_divisionComboBox_currentIndexChanged(int index);
  void on_soundComboBox_currentIndexChanged(const QString &sound);
  void on_c1FlagComboBox_currentIndexChanged(const QString &flag);
  void on_c2FlagComboBox_currentIndexChanged(const QString &flag);

  // Actions
  void modify_points(QLabel *label, int amount);
  void populateFlagDropDowns();
  void update();
  void updateDisplays();
  void playSound();

private:
    Ui::Controls *ui;
    Scoreboard *board;

    // State
    bool matchDone = false;

    // Default division and belt
    int defaultDivisionIdx = 14; // ADULT 1A - AGE 18- 29 - WHITE
    QString currentDivision = "ADULT";
    QString currentBelt = "WHITE";

    // QTimer *timer; /**<Timer that update function every 1 second. */
    QMediaPlayer *mediaPlayer;
    QUrl defaultSound = QUrl("qrc://sounds/airhorn.wav");

    // Used to return division minutes time from dropdown index
    QMap<int, int> divisionIdxToTimeMap;

    // Maps country display name to icon in qrc file
    QMap<QString, QString> countryToResourceMap;

    // Constants to avoid magic numbers
    const int TWO_MINUTES = 2;
    const int THREE_MINUTES = 3;
    const int FOUR_MINUTES = 4;
    const int FIVE_MINUTES = 5;
    const int SIX_MINUTES = 6;
    const int SEVEN_MINUTES = 7;
    const int EIGHT_MINUTES = 8;
    const int NINE_MINUTES = 9;
    const int TEN_MINUTES = 10;

    /* Holds the time remaining to countdown on the timer in milliseconds, we
     * save this value when pause is pressed so we can continue countdown from this value.
     */
    int timerRemainingTime = 0;
    int minutes = 5;
    int seconds = 0;

    QTimer timer;
    QTime time;
    QTime zeroTime = QTime::fromString("0.00", "m.s");

  signals:
    void competitor1PointsChanged(int value);
    void competitor1AdvantagesChanged(int value);
    void competitor1PenaltiesChanged(int value);
    void competitor1NameChanged(QString name);
    void competitor1FlagChanged(QString flag);

    void competitor2PointsChanged(int value);
    void competitor2AdvantagesChanged(int value);
    void competitor2PenaltiesChanged(int value);
    void competitor2NameChanged(QString name);
    void competitor2FlagChanged(QString flagpath);

    void matchReset();

    void timerUpdated(QString time);
    void divisionUpdated(QString division);
    void beltUpdated(QString belt);
    void logoUpdated(QString filename);

protected:
    void closeEvent(QCloseEvent *event) override;
};

#endif // CONTROLS_H
