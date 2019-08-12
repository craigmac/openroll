#include "scoreboard.h"
#include "ui_scoreboard.h"
#include <QDebug>

Scoreboard::Scoreboard(QWidget *parent, Qt::WindowFlags f) :
    QWidget(parent),
    ui(new Ui::Scoreboard)
{
    ui->setupUi(this);
    setWindowFlags(f);
}

Scoreboard::~Scoreboard()
{
    delete ui;
}

void Scoreboard::setCompetitor1Points(int value)
{
    int oldValue = ui->comp1_points->text().toInt();
    int newValue = oldValue + value < 0 ? 0 : oldValue + value;
    ui->comp1_points->setText(QString::number(newValue));
}


void Scoreboard::setCompetitor1Advantages(int value)
{
    int oldValue = ui->comp1_advantages->text().toInt();
    int newValue = oldValue + value < 0 ? 0 : oldValue + value;
    ui->comp1_advantages->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor1Penalties(int value)
{
    int oldValue = ui->comp1_penalties->text().toInt();
    int newValue = oldValue + value < 0 ? 0 : oldValue + value;
    ui->comp1_penalties->setText(QString::number(newValue));
}


void Scoreboard::setCompetitor2Points(int value)
{
    int oldValue = ui->comp2_points->text().toInt();
    int newValue = oldValue + value < 0 ? 0 : oldValue + value;
    ui->comp2_points->setText(QString::number(newValue));
}


void Scoreboard::setCompetitor2Advantages(int value)
{
    int oldValue = ui->comp2_advantages->text().toInt();
    int newValue = oldValue + value < 0 ? 0 : oldValue + value;
    ui->comp2_advantages->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor2Penalties(int value)
{
    int oldValue = ui->comp2_penalties->text().toInt();
    int newValue = oldValue + value < 0 ? 0 : oldValue + value;
    ui->comp2_penalties->setText(QString::number(newValue));
}

void Scoreboard::setCompetitor1Name(QString name)
{
    ui->comp1_name->setText(name);
}

void Scoreboard::setCompetitor2Name(QString name)
{
    ui->comp2_name->setText(name);
}
