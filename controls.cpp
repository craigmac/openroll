#include "controls.h"
#include "scoreboard.h"
#include "ui_controls.h"
#include <QDebug>

static QString OPENROLL_VERSION = "2.0.0";

Controls::Controls(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Controls)
{
    ui->setupUi(this);
    setWindowTitle("Openroll - Controls - " + OPENROLL_VERSION);
    /* Create Scoreboard as a child widget, but pass flags to make it an
     * independent window, otherwise it will try to draw into the parent
     * window.
     */
    Scoreboard *board = new Scoreboard(this, Qt::WindowFlags(Qt::Window));
    board->setWindowTitle("Openroll - Scoreboard - " + OPENROLL_VERSION);
    board->show();

    /* Signal-Slot connections:
     * For every significant event on the controls object, e.g., adding to the
     * score or changing a division, we emit a signal saying we have done so,
     * and then connect that signal here to a slot on the scoreboard object.
    */
    connect(this, &Controls::competitor1PointsChanged,
            board, &Scoreboard::setCompetitor1Points);
    connect(this, &Controls::competitor1AdvantagesChanged,
            board, &Scoreboard::setCompetitor1Advantages);
    connect(this, &Controls::competitor1PenaltiesChanged,
            board, &Scoreboard::setCompetitor1Penalties);

    connect(this, &Controls::competitor2PointsChanged,
            board, &Scoreboard::setCompetitor2Points);
    connect(this, &Controls::competitor2AdvantagesChanged,
            board, &Scoreboard::setCompetitor2Advantages);
    connect(this, &Controls::competitor2PenaltiesChanged,
            board, &Scoreboard::setCompetitor2Penalties);

    connect(this, &Controls::competitor1NameChanged,
            board, &Scoreboard::setCompetitor1Name);
    connect(this, &Controls::competitor2NameChanged,
            board, &Scoreboard::setCompetitor2Name);
}

Controls::~Controls()
{
    delete ui;
}

void Controls::modify_points(QLabel *label, int amount)
{
    qDebug() << "modify_points() entry.";

    int oldValue = label->text().toInt();
    int newValue = oldValue + amount < 0 ? 0 : oldValue + amount;

    label->setText(QString::number(newValue));

    qDebug() << "modify_points() exit.";

}

void Controls::on_c1Add2Button_pressed()
{
    QLabel *label = ui->c1PointsLabel;
    modify_points(label, 2);
    emit competitor1PointsChanged(2);
}

void Controls::on_c1Del2Button_pressed()
{
    QLabel *label = ui->c1PointsLabel;
    modify_points(label, -2);
    emit competitor1PointsChanged(-2);

}

void Controls::on_c1Add3Button_pressed()
{
    QLabel *label = ui->c1PointsLabel;
    modify_points(label, 3);
    emit competitor1PointsChanged(3);
}

/* When division combobox is changed, switch on the index and set
 * ui widgets accordingly.
 */
void Controls::on_divisionComboBox_currentIndexChanged(int index)
{
    switch (index) {

    case 0: // MIGHTY MITE 1 - AGE 4
        break;
    case 1: // MIGHTY MITE 2 - AGE 5
        break;
    case 2: // MIGHTY MITE 3 - AGE 6
        break;
    case 3: // PEEWEE 1 - AGE 7
        break;
    case 4: // PEEWEE 2 - AGE 8
        break;
    case 5: // PEEWEE 3 - AGE 9 - ALL BELTS
        break;
    case 6: // JUNIOR 1 - AGE 10 - ALL BELTS
        break;
    case 7:  // JUNIOR 2 - AGE 11 - ALL BELTS
        break;
    case 8:  // JUNIOR 3 - AGE 12 - ALL BELTS
        break;
    case 9: // TEEN 1 - AGE 13 - ALL BELTS
        break;
    case 10: // TEEN 2 - AGE 14 - ALL BELTS
        break;
    case 11: // TEEN 3 - AGE 15 - ALL BELTS
        break;
    case 12: // JUVENILE 1 - AGE 16 - ALL BELTS
        break;
    case 13: // JUVENILE 2 - AGE 17 - ALL BELTS
        break;
    case 14: // ADULT 1A - AGE 18-29 - WHITE
        break;
    case 15: // ADULT 1B - AGE 18-29 - BLUE
        break;
    case 16: // ADULT 1C - AGE 18-29 - PURPLE
        break;
    case 17: // ADULT 1D - AGE 18-29 - BROWN
        break;
    case 18: // ADULT 1E - AGE 18-29 - BLACK
        break;
    case 19: // MASTER 1A - AGE 30-35 - WHITE
        break;
    case 20: // MASTER 1B - AGE 30-35 - BLUE
        break;
    case 21: // MASTER 1C - AGE 30-35 - PURPLE
        break;
    case 22: // MASTER 1D - AGE 30-35 - BROWN
        break;
    case 23: // MASTER 1E - AGE 30-35 - BLACK
        break;
    case 24: // MASTER 2 - AGE 36-40 - ALL BELTS
        break;
    case 25: // MASTER 3 - AGE 41-45 - ALL BELTS
        break;
    case 26: // MASTER 4 - AGE 46-50 - ALL BELTS
        break;
    case 27: // MASTER 5 - AGE 51-55+ - ALL BELTS
        break;
    case 28: // MASTER 6 - AGE 56+ - ALL BELTS
        break;

    default:
        qDebug() << "division_combobox index error.";
        break;
    }

}

void Controls::on_soundComboBox_currentIndexChanged(const QString &arg1)
{

}

void Controls::on_MuteRadioButton_pressed()
{

}

void Controls::on_OnRadioButton_pressed()
{

}

void Controls::on_loadLogoButton_pressed()
{

}

void Controls::on_c1FlagComboBox_currentIndexChanged(int index)
{
    // TODO
    emit competitor1FlagChanged(index);

}

void Controls::on_c1CustomFlagButton_pressed()
{
    // TODO
    QString flag = "";
    emit competitor1CustomFlagLoaded(flag);
}

void Controls::on_c2CustomLogoButton_pressed()
{
    // TODO
    QString flag = "";
    emit competitor2CustomFlagLoaded(flag);
}

void Controls::on_c2FlagComboBox_currentIndexChanged(int index)
{
    // TODO
    emit competitor2FlagChanged(index);

}

void Controls::on_playPauseButton_pressed()
{
    // TODO
    bool isPaused = false;
    emit playPauseStateChanged(isPaused);
}

void Controls::on_resetButton_pressed()
{
    // TODO
    emit matchReset();
}

void Controls::on_c1Del3Button_pressed()
{
    QLabel *label = ui->c1PointsLabel;
    modify_points(label, -3);
    emit competitor1PointsChanged(-3);
}

void Controls::on_c1Add4Button_pressed()
{
    QLabel *label = ui->c1PointsLabel;
    modify_points(label, 4);
    emit competitor1PointsChanged(4);

}

void Controls::on_c1Del4Button_pressed()
{
    QLabel *label = ui->c1PointsLabel;
    modify_points(label, -4);
    emit competitor1PointsChanged(-4);
}

void Controls::on_c1AddAButton_pressed()
{
    QLabel *label = ui->c1AdvantagesLabel;
    modify_points(label, 1);
    emit competitor1AdvantagesChanged(1);
}

void Controls::on_c1DelAButton_pressed()
{
    QLabel *label = ui->c1AdvantagesLabel;
    modify_points(label, -1);
    emit competitor1AdvantagesChanged(-1);

}

void Controls::on_c1AddPButton_pressed()
{
    QLabel *label = ui->c1PenaltiesLabel;
    modify_points(label, 1);
    emit competitor1PenaltiesChanged(1);
}

void Controls::on_c1DelPButton_pressed()
{
    QLabel *label = ui->c1PenaltiesLabel;
    modify_points(label, -1);
    emit competitor1PenaltiesChanged(-1);
}

void Controls::on_c2Add2Button_pressed()
{
   QLabel *label = ui->c2PointsLabel;
   modify_points(label, 2);
   emit competitor2PointsChanged(2);
}

void Controls::on_c2Del2Button_pressed()
{
   QLabel *label = ui->c2PointsLabel;
   modify_points(label, -2);
   emit competitor2PointsChanged(-2);
}

void Controls::on_c2Add3Button_pressed()
{
   QLabel *label = ui->c2PointsLabel;
   modify_points(label, 3);
   emit competitor2PointsChanged(3);
}

void Controls::on_c2Del3Button_pressed()
{
   QLabel *label = ui->c2PointsLabel;
   modify_points(label, -3);
   emit competitor2PointsChanged(-3);
}

void Controls::on_c2Add4Button_pressed()
{

   QLabel *label = ui->c2PointsLabel;
   modify_points(label, 4);
   emit competitor2PointsChanged(4);
}

void Controls::on_c2Del4Button_pressed()
{
   QLabel *label = ui->c2PointsLabel;
   modify_points(label, -4);
   emit competitor2PointsChanged(-4);
}

void Controls::on_c2AddAButton_pressed()
{
   QLabel *label = ui->c2AdvantagesLabel;
   modify_points(label, 1);
   emit competitor2AdvantagesChanged(1);
}

void Controls::on_c2DelAButton_pressed()
{
   QLabel *label = ui->c2AdvantagesLabel;
   modify_points(label, -1);
   emit competitor2AdvantagesChanged(-1);
}

void Controls::on_c2AddPButton_pressed()
{
   QLabel *label = ui->c2PenaltiesLabel;
   modify_points(label, 1);
   emit competitor2PenaltiesChanged(1);
}

void Controls::on_c2DelPButton_pressed()
{
   QLabel *label = ui->c2PenaltiesLabel;
   modify_points(label, -1);
   emit competitor2PenaltiesChanged(-1);
}

void Controls::on_c1LineEdit_textEdited(const QString &str)
{
    ui->c1NameLabel->setText(str);
    emit competitor1NameChanged(str);
}

void Controls::on_c2LineEdit_textEdited(const QString &str)
{
   ui->c2NameLabel->setText(str);
   emit competitor2NameChanged(str);
}
