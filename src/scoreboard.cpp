#include "scoreboard.h"
#include "ui_scoreboard.h"
#ifdef QT_DEBUG
#include "logger.h"
#include <QDebug>
#endif

/*!
 * \brief Scoreboard::closeEvent
 * \param event
 */
void Scoreboard::closeEvent(QCloseEvent *event) { event->accept(); }

/*!
 * \brief Scoreboard::Scoreboard
 * \param parent
 * \param f
 */
Scoreboard::Scoreboard(QWidget *parent, Qt::WindowFlags f) : QWidget(parent), ui(new Ui::Scoreboard) {
  ui->setupUi(this);
  setWindowFlags(f);
}

Scoreboard::~Scoreboard() { delete ui; }

void Scoreboard::setCompetitor1Points(int value) {
  int oldValue = ui->comp1_points->text().toInt();
  int newValue = oldValue + value < 0 ? 0 : oldValue + value;
  ui->comp1_points->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor1Advantages(int value) {
  int oldValue = ui->comp1_advantages->text().toInt();
  int newValue = oldValue + value < 0 ? 0 : oldValue + value;
  ui->comp1_advantages->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor1Penalties(int value) {
  int oldValue = ui->comp1_penalties->text().toInt();
  int newValue = oldValue + value < 0 ? 0 : oldValue + value;
  ui->comp1_penalties->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor2Points(int value) {
  int oldValue = ui->comp2_points->text().toInt();
  int newValue = oldValue + value < 0 ? 0 : oldValue + value;
  ui->comp2_points->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor2Advantages(int value) {
  int oldValue = ui->comp2_advantages->text().toInt();
  int newValue = oldValue + value < 0 ? 0 : oldValue + value;
  ui->comp2_advantages->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor2Penalties(int value) {
  int oldValue = ui->comp2_penalties->text().toInt();
  int newValue = oldValue + value < 0 ? 0 : oldValue + value;
  ui->comp2_penalties->setText(QString::number(newValue));
}

/*!
 * \brief Scoreboard::setCompetitor1Name
 * \param name
 */
void Scoreboard::setCompetitor1Name(const QString& name)
{
    ui->comp1_name->setText(name);
}

/*!
 * \brief Scoreboard::setCompetitor2Name
 * \param name
 */
void Scoreboard::setCompetitor2Name(const QString& name)
{
    ui->comp2_name->setText(name);
}

/*!
 * \brief Scoreboard::setClockDisplay
 * \param newtime
 */
void Scoreboard::setClockDisplay(const QString &newtime) { ui->lcdClock->display(newtime); }

/*!
 * \brief Scoreboard::setDivisionLabel
 * \param division
 */
void Scoreboard::setDivisionLabel(const QString& division)
{
    ui->divisionLabel->setText(division);
}

/*!
 * \brief Scoreboard::setBeltLabel
 * \param newbelt
 */
void Scoreboard::setBeltLabel(const QString& newbelt)
{
    ui->beltLabel->setText(newbelt);
}

/*!
 * \brief Scoreboard::setLogo
 * \param logo
 */
void Scoreboard::setLogo(const QString &logo) {
  QPixmap img = QPixmap(logo);
  ui->user_logo->setPixmap(img);
}

/**
 * @brief Scoreboard::resetScores
 *
 * @details Resets points labels to 0 and names to generic placeholders.
 */
void Scoreboard::resetScores()
{
    ui->comp1_points->setText("0");
    ui->comp1_advantages->setText("0");
    ui->comp1_penalties->setText("0");
    ui->comp1_name->setText("Competitor 1");

    ui->comp2_points->setText("0");
    ui->comp2_advantages->setText("0");
    ui->comp2_penalties->setText("0");
    ui->comp2_name->setText("Competitor 2");
}

/*!
 * \brief Scoreboard::setC1Flag
 * \param flagpath
 */
void Scoreboard::setC1Flag(const QString& flagpath)
{
    ui->c1FlagLabel->setPixmap(flagpath);
}

/*!
 * \brief Scoreboard::setC2Flag
 * \param flagpath
 */
void Scoreboard::setC2Flag(const QString& flagpath)
{
   ui->c2FlagLabel->setPixmap(flagpath);
}
