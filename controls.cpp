#include "controls.h"
#include "scoreboard.h"
#include "ui_controls.h"
#include <map>
#include <QDebug>
#include <QTime>
#include <QtWidgets>
#include <QDir>
#include <QStringList>
#include <QFileDialog>

Controls::Controls(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Controls)
{
    ui->setupUi(this);
    setWindowTitle("Openroll - Controls - " + Controls::s_VERSION);
    /* Create Scoreboard as a child widget, but pass flags to make it an
     * independent window, otherwise it will try to draw into the parent
     * window.
     */
    Scoreboard *board = new Scoreboard(this, Qt::WindowFlags(Qt::Window));
    board->setWindowTitle("Openroll - Scoreboard - " + Controls::s_VERSION);
    board->show();

    // HACK: must be cleaner way to do this....
    divisionIdxToTimeMap[0] = 120;
    divisionIdxToTimeMap[1] = 120;
    divisionIdxToTimeMap[2] = 120;
    divisionIdxToTimeMap[3] = 180;
    divisionIdxToTimeMap[4] = 180;
    divisionIdxToTimeMap[5] = 180;
    divisionIdxToTimeMap[6] = 240;
    divisionIdxToTimeMap[7] = 240;
    divisionIdxToTimeMap[8] = 240;
    divisionIdxToTimeMap[9] = 240;
    divisionIdxToTimeMap[10] = 240;
    divisionIdxToTimeMap[11] = 240;
    divisionIdxToTimeMap[12] = 300;
    divisionIdxToTimeMap[13] = 300;
    divisionIdxToTimeMap[14] = 300;
    divisionIdxToTimeMap[15] = 360;
    divisionIdxToTimeMap[16] = 420;
    divisionIdxToTimeMap[17] = 480;
    divisionIdxToTimeMap[18] = 600;
    divisionIdxToTimeMap[19] = 300;
    divisionIdxToTimeMap[20] = 300;
    divisionIdxToTimeMap[21] = 360;
    divisionIdxToTimeMap[22] = 360;
    divisionIdxToTimeMap[23] = 360;
    divisionIdxToTimeMap[24] = 300;
    divisionIdxToTimeMap[25] = 300;
    divisionIdxToTimeMap[26] = 300;
    divisionIdxToTimeMap[27] = 300;
    divisionIdxToTimeMap[28] = 300;

    qDebug() << "totalTime is: " << totalTime;
    qDebug() << "clockMinutes default is: " << clockMinutes;
    qDebug() << "clockSeconds default is: " << clockSeconds;

    timer = new QTimer(this);
    m_player = new QMediaPlayer(this);
    m_player->setMedia(Controls::m_defaultSound);
    m_player->setVolume(100);

    /* Signal-Slot connections:
     * For every significant event on the controls object, e.g., adding to the
     * score or changing a division, we emit a signal saying we have done so,
     * and then connect that signal here to a slot on the scoreboard object.
    */

    connect(timer, &QTimer::timeout, this, &Controls::updateClock);

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

    connect(this, &Controls::timerUpdated,
            board, &Scoreboard::setTimeLabel);
    connect(this, &Controls::divisionUpdated,
            board, &Scoreboard::setDivisionLabel);
    connect(this, &Controls::beltUpdated,
            board, &Scoreboard::setBeltLabel);

    connect(this, &Controls::logoUpdated,
            board, &Scoreboard::setLogo);

    connect(this, &Controls::matchReset,
            board, &Scoreboard::resetScores);

    connect(this, &Controls::c1FlagChanged,
            board, &Scoreboard::setC1Flag);

    connect(this, &Controls::c2FlagChanged,
            board, &Scoreboard::setC2Flag);

    populateFlagDropDowns();

    timer->start(1000); // every 1 second
}

Controls::~Controls()
{
    delete ui;
    delete board;
    delete m_player;
    delete timer;
}

void Controls::modify_points(QLabel *label, int amount)
{
    int oldValue = label->text().toInt();
    int newValue = oldValue + amount < 0 ? 0 : oldValue + amount;
    label->setText(QString::number(newValue));
}

QString Controls::calcNewTimeString()
{
    clockMinutes = totalTime / 60;
    clockSeconds = totalTime % 60;

    QString minutes = QString::number(clockMinutes);
    QString seconds = QString::number(clockSeconds);

    if (clockSeconds < 10) {
        QString extraZero = "0";
        seconds.prepend(extraZero);
    }

    QString newTime = minutes + ":" + seconds;
    return newTime;
}

void Controls::updateDisplay()
{
    QString newTime = calcNewTimeString();
    // Update label
    ui->timerLabel->setText(newTime);

    // emit signals saying what we did
    emit timerUpdated(newTime);
    emit divisionUpdated(m_currentDivision);
    emit beltUpdated(m_currentBelt);
}

void Controls::updateClock()
{
    if (matchDone) {
        qDebug() << "updateClock(): matchDone = true condition hit.";
        /* GOTCHA: just update the display and stop here, this handles
         * case where match was started and clock was ticking and
         * user hits reset button without hitting pause first.
         */
        updateDisplay();
        return;
    }

    if (totalTime <= 0) {
        qDebug() << "updateClock(): totalTime <=0 condition hit.";
        Controls::playSound();
        matchDone = true;
        return; // stop here
    }

    if (matchStarted && clockRunning) {
        qDebug() << "updateClock(): matchStarted && clockRunning = true condition hit.";
        totalTime--;
        updateDisplay();
    }

}

void Controls::playSound()
{
    if (ui->OnRadioButton->isChecked()) {
        m_player->play();
    }
    ui->playPauseButton->setDisabled(true);

}

// TODO: combine disable/enable to single flip state call
void Controls::disableControls()
{
    ui->divisionComboBox->setDisabled(true);
}

void Controls::enableControls()
{
    ui->playPauseButton->setDisabled(false);
    ui->divisionComboBox->setDisabled(false);
}

void Controls::closeEvent(QCloseEvent *event)
{
    qDebug() << "Close event caught on control window.";
    QMessageBox::StandardButton resBtn = QMessageBox::question(this,
                                      "Openroll",
                                      "Are you sure?",
                                      QMessageBox::No | QMessageBox::Yes,
                                      QMessageBox::No);
    if (resBtn != QMessageBox::Yes) {
        event->ignore();
    }
    else {
        event->accept();
    }
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

void Controls::on_divisionComboBox_currentIndexChanged(int index)
{
    switch (index) {
    case 0: // MIGHTY MITE 1
        m_currentDivision = "MIGHTY MITE 1 - AGE 4";
        m_currentBelt = "ALL BELTS";
        totalTime = 2 * 60;
        break;
    case 1: // MIGHTY MITE 2
        m_currentDivision = "MIGHTY MITE 2 - AGE 5";
        m_currentBelt = "ALL BELTS";
        totalTime = 2 * 60;
        break;
    case 2: // MIGHTY MITE 3
        m_currentDivision = "MIGHTY MITE 3 - AGE 6";
        m_currentBelt = "ALL BELTS";
        totalTime = 2 * 60;
        break;
    case 3: // PEEWEE 1
        m_currentDivision = "PEEWEE 1 - AGE 7";
        m_currentBelt = "ALL BELTS";
        totalTime = 3 * 60;
        break;
    case 4: // PEEWEE 2
        m_currentDivision = "PEEWEE 2 - AGE 8";
        m_currentBelt = "ALL BELTS";
        totalTime = 3 * 60;
        break;
    case 5: // PEEWEE 3
        m_currentDivision = "PEEWEE 3 - AGE 9";
        m_currentBelt = "ALL BELTS";
        totalTime = 3 * 60; // 3 minutes
        break;
    case 6: // JUNIOR 1
        m_currentDivision = "JUNIOR 1 - AGE 10";
        m_currentBelt = "ALL BELTS";
        totalTime = 4 * 60;
        break;
    case 7: // JUNIOR 2
        m_currentDivision = "JUNIOR 2 - AGE 11";
        m_currentBelt = "ALL BELTS";
        totalTime = 4 * 60;
        break;
    case 8: // JUNIOR 3
        m_currentDivision = "JUNIOR 3 - AGE 12";
        m_currentBelt = "ALL BELTS";
        totalTime = 4 * 60;
        break;
    case 9: // TEEN 1
        m_currentDivision = "TEEN 1 - AGE 13";
        m_currentBelt = "ALL BELTS";
        totalTime = 4 * 60;
        break;
    case 10: // TEEN 2
        m_currentDivision = "TEEN 2 - AGE 14";
        m_currentBelt = "ALL BELTS";
        totalTime = 4 * 60;
        break;
    case 11: // TEEN 3
        m_currentDivision = "TEEN 3 - AGE 15";
        m_currentBelt = "ALL BELTS";
        totalTime = 4 * 60;
        break;
    case 12: // JUVENILE 1
        m_currentDivision = "JUVENILE 1 - AGE 16";
        m_currentBelt = "ALL BELTS";
        totalTime = 5 * 60;
        break;
    case 13: // JUVENILE 2
        m_currentDivision = "JUVENILE 2 - AGE 17";
        m_currentBelt = "ALL BELTS";
        totalTime = 5 * 60;
        break;
    case 14: // ADULT 1A
        m_currentDivision = "ADULT 1A - AGE 18-29";
        m_currentBelt = "WHITE";
        totalTime = 5 * 60;
        break;
    case 15: // ADULT 1B
        m_currentDivision = "ADULT 1B - AGE 18-29";
        m_currentBelt = "BLUE";
        totalTime = 6 * 60;
        break;
    case 16: // ADULT 1C
        m_currentDivision = "ADULT 1C - AGE 18-29";
        m_currentBelt = "PURPLE";
        totalTime = 7 * 60;
        break;
    case 17: // ADULT 1D
        m_currentDivision = "ADULT 1D - AGE 18-29";
        m_currentBelt = "BROWN";
        totalTime = 8 * 60;
        break;
    case 18: // ADULT 1E
        m_currentDivision = "ADULT 1E - AGE 18-29";
        m_currentBelt = "BLACK";
        totalTime = 10 * 60;
        break;
    case 19: // MASTER 1A
        m_currentDivision = "MASTER 1A - AGE 30-35";
        m_currentBelt = "WHITE";
        totalTime = 5 * 60;
        break;
    case 20: // MASTER 1B
        m_currentDivision = "MASTER 1B - AGE 30-35";
        m_currentBelt = "BLUE";
        totalTime = 5 * 60;
        break;
    case 21: // MASTER 1C
        m_currentDivision = "MASTER 1C - AGE 30-35";
        m_currentBelt = "PURPLE";
        totalTime = 6 * 60;
        break;
    case 22: // MASTER 1D
        m_currentDivision = "MASTER 1D - AGE 30-35";
        m_currentBelt = "BROWN";
        totalTime = 6 * 60;
        break;
    case 23: // MASTER 1E
        m_currentDivision = "MASTER 1E - AGE 30-35";
        m_currentBelt = "BLACK";
        totalTime = 6 * 60;
        break;
    case 24: // MASTER 2
        m_currentDivision = "MASTER 2 - AGE 36-40";
        m_currentBelt = "ALL BELTS";
        totalTime = 5 * 60;
        break;
    case 25: // MASTER 3
        m_currentDivision = "MASTER 3 - AGE 41-45";
        m_currentBelt = "ALL BELTS";
        totalTime = 5 * 60;
        break;
    case 26: // MASTER 4
        m_currentDivision = "MASTER 4 - AGE 46-50";
        m_currentBelt = "ALL BELTS";
        totalTime = 5 * 60;
        break;
    case 27: // MASTER 5
        m_currentDivision = "MASTER 5 - AGE 51-55+";
        m_currentBelt = "ALL BELTS";
        totalTime = 5 * 60;
        break;
    case 28: // MASTER 6
        m_currentDivision = "MASTER 6 - AGE 56+";
        m_currentBelt = "ALL BELTS";
        totalTime = 5 * 60;
        break;
    default: // NO MATCH FROM DROPDOWN CASE!
        m_currentDivision = "UNKNOWN";
        m_currentBelt = "UNKNOWN";
        totalTime = 5 * 60;
        break;
    };
}

void Controls::on_soundComboBox_currentIndexChanged(const QString &sound)
{
   QString f = "qrc:///sounds/" + sound;
   qDebug() << "Changing to sound file: " << f;
   m_player->setMedia(QUrl(f));
   //playSound();
}

/*
 * Add all the countries and related flag icons to
 * each competitor dropdown.
 */
void Controls::populateFlagDropDowns()
{
    // TODO: use a thread/parallel to do this for speed!
    countryToResourceMap.insert("ad", ":/flags/ad");
    countryToResourceMap.insert("ae", ":/flags/ae");
    countryToResourceMap.insert("af", ":/flags/af");
    countryToResourceMap.insert("ag", ":/flags/ag");
    countryToResourceMap.insert("al", ":/flags/al");
    countryToResourceMap.insert("am", ":/flags/am");
    countryToResourceMap.insert("ao", ":/flags/ao");
    countryToResourceMap.insert("ar", ":/flags/ar");
    countryToResourceMap.insert("at", ":/flags/at");
    countryToResourceMap.insert("au", ":/flags/au");
    countryToResourceMap.insert("az", ":/flags/az");
    countryToResourceMap.insert("ba", ":/flags/ba");
    countryToResourceMap.insert("bb", ":/flags/bb");
    countryToResourceMap.insert("bd", ":/flags/bd");
    countryToResourceMap.insert("be", ":/flags/be");
    countryToResourceMap.insert("bf", ":/flags/bf");
    countryToResourceMap.insert("bg", ":/flags/bg");
    countryToResourceMap.insert("bh", ":/flags/bh");
    countryToResourceMap.insert("bi", ":/flags/bi");
    countryToResourceMap.insert("bj", ":/flags/bj");
    countryToResourceMap.insert("bn", ":/flags/bn");
    countryToResourceMap.insert("bo", ":/flags/bo");
    countryToResourceMap.insert("br", ":/flags/br");
    countryToResourceMap.insert("bs", ":/flags/bs");
    countryToResourceMap.insert("bt", ":/flags/bt");
    countryToResourceMap.insert("bw", ":/flags/bw");
    countryToResourceMap.insert("by", ":/flags/by");
    countryToResourceMap.insert("bz", ":/flags/bz");
    countryToResourceMap.insert("ca", ":/flags/ca");
    countryToResourceMap.insert("cd", ":/flags/cd");
    countryToResourceMap.insert("cf", ":/flags/cf");
    countryToResourceMap.insert("cg", ":/flags/cg");
    countryToResourceMap.insert("ch", ":/flags/ch");
    countryToResourceMap.insert("ci", ":/flags/ci");
    countryToResourceMap.insert("cl", ":/flags/cl");
    countryToResourceMap.insert("cm", ":/flags/cm");
    countryToResourceMap.insert("cn", ":/flags/cn");
    countryToResourceMap.insert("co", ":/flags/co");
    countryToResourceMap.insert("cr", ":/flags/cr");
    countryToResourceMap.insert("cu", ":/flags/cu");
    countryToResourceMap.insert("cv", ":/flags/cv");
    countryToResourceMap.insert("cy", ":/flags/cy");
    countryToResourceMap.insert("cz", ":/flags/cz");
    countryToResourceMap.insert("de", ":/flags/de");
    countryToResourceMap.insert("dj", ":/flags/dj");
    countryToResourceMap.insert("dk", ":/flags/dk");
    countryToResourceMap.insert("dm", ":/flags/dm");
    countryToResourceMap.insert("do", ":/flags/do");
    countryToResourceMap.insert("dz", ":/flags/dz");
    countryToResourceMap.insert("ec", ":/flags/ec");
    countryToResourceMap.insert("ee", ":/flags/ee");
    countryToResourceMap.insert("eg", ":/flags/eg");
    countryToResourceMap.insert("eh", ":/flags/eh");
    countryToResourceMap.insert("er", ":/flags/er");
    countryToResourceMap.insert("es", ":/flags/es");
    countryToResourceMap.insert("et", ":/flags/et");
    countryToResourceMap.insert("fi", ":/flags/fi");
    countryToResourceMap.insert("fj", ":/flags/fj");
    countryToResourceMap.insert("fm", ":/flags/fm");
    countryToResourceMap.insert("fr", ":/flags/fr");
    countryToResourceMap.insert("ga", ":/flags/ga");
    countryToResourceMap.insert("gb", ":/flags/gb");
    countryToResourceMap.insert("gd", ":/flags/gd");
    countryToResourceMap.insert("ge", ":/flags/ge");
    countryToResourceMap.insert("gh", ":/flags/gh");
    countryToResourceMap.insert("gm", ":/flags/gm");
    countryToResourceMap.insert("gn", ":/flags/gn");
    countryToResourceMap.insert("gq", ":/flags/gq");
    countryToResourceMap.insert("gr", ":/flags/gr");
    countryToResourceMap.insert("gt", ":/flags/gt");
    countryToResourceMap.insert("gw", ":/flags/gw");
    countryToResourceMap.insert("gy", ":/flags/gy");
    countryToResourceMap.insert("hn", ":/flags/hn");
    countryToResourceMap.insert("hr", ":/flags/hr");
    countryToResourceMap.insert("ht", ":/flags/ht");
    countryToResourceMap.insert("hu", ":/flags/hu");
    countryToResourceMap.insert("id", ":/flags/id");
    countryToResourceMap.insert("ie", ":/flags/ie");
    countryToResourceMap.insert("il", ":/flags/il");
    countryToResourceMap.insert("in", ":/flags/in");
    countryToResourceMap.insert("iq", ":/flags/iq");
    countryToResourceMap.insert("ir", ":/flags/ir");
    countryToResourceMap.insert("is", ":/flags/is");
    countryToResourceMap.insert("it", ":/flags/it");
    countryToResourceMap.insert("jm", ":/flags/jm");
    countryToResourceMap.insert("jo", ":/flags/jo");
    countryToResourceMap.insert("jp", ":/flags/jp");
    countryToResourceMap.insert("ke", ":/flags/ke");
    countryToResourceMap.insert("kg", ":/flags/kg");
    countryToResourceMap.insert("kh", ":/flags/kh");
    countryToResourceMap.insert("ki", ":/flags/ki");
    countryToResourceMap.insert("km", ":/flags/km");
    countryToResourceMap.insert("kn", ":/flags/kn");
    countryToResourceMap.insert("kp", ":/flags/kp");
    countryToResourceMap.insert("kr", ":/flags/kr");
    countryToResourceMap.insert("ks", ":/flags/ks");
    countryToResourceMap.insert("kw", ":/flags/kw");
    countryToResourceMap.insert("kz", ":/flags/kz");
    countryToResourceMap.insert("la", ":/flags/la");
    countryToResourceMap.insert("lb", ":/flags/lb");
    countryToResourceMap.insert("lc", ":/flags/lc");
    countryToResourceMap.insert("li", ":/flags/li");
    countryToResourceMap.insert("lk", ":/flags/lk");
    countryToResourceMap.insert("lr", ":/flags/lr");
    countryToResourceMap.insert("ls", ":/flags/ls");
    countryToResourceMap.insert("lt", ":/flags/lt");
    countryToResourceMap.insert("lu", ":/flags/lu");
    countryToResourceMap.insert("lv", ":/flags/lv");
    countryToResourceMap.insert("ly", ":/flags/ly");
    countryToResourceMap.insert("ma", ":/flags/ma");
    countryToResourceMap.insert("mc", ":/flags/mc");
    countryToResourceMap.insert("md", ":/flags/md");
    countryToResourceMap.insert("me", ":/flags/me");
    countryToResourceMap.insert("mg", ":/flags/mg");
    countryToResourceMap.insert("mh", ":/flags/mh");
    countryToResourceMap.insert("mk", ":/flags/mk");
    countryToResourceMap.insert("ml", ":/flags/ml");
    countryToResourceMap.insert("mm", ":/flags/mm");
    countryToResourceMap.insert("mn", ":/flags/mn");
    countryToResourceMap.insert("mr", ":/flags/mr");
    countryToResourceMap.insert("mt", ":/flags/mt");
    countryToResourceMap.insert("mu", ":/flags/mu");
    countryToResourceMap.insert("mv", ":/flags/mv");
    countryToResourceMap.insert("mw", ":/flags/mw");
    countryToResourceMap.insert("mx", ":/flags/mx");
    countryToResourceMap.insert("my", ":/flags/my");
    countryToResourceMap.insert("mz", ":/flags/mz");
    countryToResourceMap.insert("na", ":/flags/na");
    countryToResourceMap.insert("ne", ":/flags/ne");
    countryToResourceMap.insert("ng", ":/flags/ng");
    countryToResourceMap.insert("ni", ":/flags/ni");
    countryToResourceMap.insert("nl", ":/flags/nl");
    countryToResourceMap.insert("no", ":/flags/no");
    countryToResourceMap.insert("np", ":/flags/np");
    countryToResourceMap.insert("nr", ":/flags/nr");
    countryToResourceMap.insert("nz", ":/flags/nz");
    countryToResourceMap.insert("om", ":/flags/om");
    countryToResourceMap.insert("pa", ":/flags/pa");
    countryToResourceMap.insert("pe", ":/flags/pe");
    countryToResourceMap.insert("pg", ":/flags/pg");
    countryToResourceMap.insert("ph", ":/flags/ph");
    countryToResourceMap.insert("pk", ":/flags/pk");
    countryToResourceMap.insert("pl", ":/flags/pl");
    countryToResourceMap.insert("pt", ":/flags/pt");
    countryToResourceMap.insert("pw", ":/flags/pw");
    countryToResourceMap.insert("py", ":/flags/py");
    countryToResourceMap.insert("qa", ":/flags/qa");
    countryToResourceMap.insert("ro", ":/flags/ro");
    countryToResourceMap.insert("rs", ":/flags/rs");
    countryToResourceMap.insert("ru", ":/flags/ru");
    countryToResourceMap.insert("rw", ":/flags/rw");
    countryToResourceMap.insert("sa", ":/flags/sa");
    countryToResourceMap.insert("sb", ":/flags/sb");
    countryToResourceMap.insert("sc", ":/flags/sc");
    countryToResourceMap.insert("sd", ":/flags/sd");
    countryToResourceMap.insert("se", ":/flags/se");
    countryToResourceMap.insert("sg", ":/flags/sg");
    countryToResourceMap.insert("si", ":/flags/si");
    countryToResourceMap.insert("sk", ":/flags/sk");
    countryToResourceMap.insert("sl", ":/flags/sl");
    countryToResourceMap.insert("sm", ":/flags/sm");
    countryToResourceMap.insert("sn", ":/flags/sn");
    countryToResourceMap.insert("so", ":/flags/so");
    countryToResourceMap.insert("sr", ":/flags/sr");
    countryToResourceMap.insert("st", ":/flags/st");
    countryToResourceMap.insert("sv", ":/flags/sv");
    countryToResourceMap.insert("sy", ":/flags/sy");
    countryToResourceMap.insert("sz", ":/flags/sz");
    countryToResourceMap.insert("td", ":/flags/td");
    countryToResourceMap.insert("tg", ":/flags/tg");
    countryToResourceMap.insert("th", ":/flags/th");
    countryToResourceMap.insert("tj", ":/flags/tj");
    countryToResourceMap.insert("tl", ":/flags/tl");
    countryToResourceMap.insert("tm", ":/flags/tm");
    countryToResourceMap.insert("tn", ":/flags/tn");
    countryToResourceMap.insert("to", ":/flags/to");
    countryToResourceMap.insert("tr", ":/flags/tr");
    countryToResourceMap.insert("tt", ":/flags/tt");
    countryToResourceMap.insert("tv", ":/flags/tv");
    countryToResourceMap.insert("tw", ":/flags/tw");
    countryToResourceMap.insert("tz", ":/flags/tz");
    countryToResourceMap.insert("ua", ":/flags/ua");
    countryToResourceMap.insert("ug", ":/flags/ug");
    countryToResourceMap.insert("us", ":/flags/us");
    countryToResourceMap.insert("uy", ":/flags/uy");
    countryToResourceMap.insert("uz", ":/flags/uz");
    countryToResourceMap.insert("va", ":/flags/va");
    countryToResourceMap.insert("vc", ":/flags/vc");
    countryToResourceMap.insert("ve", ":/flags/ve");
    countryToResourceMap.insert("vn", ":/flags/vn");
    countryToResourceMap.insert("vu", ":/flags/vu");
    countryToResourceMap.insert("ws", ":/flags/ws");
    countryToResourceMap.insert("ye", ":/flags/ye");
    countryToResourceMap.insert("za", ":/flags/za");
    countryToResourceMap.insert("zm", ":/flags/zm");
    countryToResourceMap.insert("zw", ":/flags/zw");

    QMap<QString, QString>::const_iterator i = countryToResourceMap.constBegin();
    int j = 0;
    while (i != countryToResourceMap.constEnd()) {
        ui->c1FlagComboBox->insertItem(j, QIcon(i.value()), i.key());
        ui->c2FlagComboBox->insertItem(j, QIcon(i.value()), i.key());
        ++j;
        ++i;
    }
}

void Controls::on_loadLogoButton_pressed()
{
    QString logoFilename = QFileDialog::getOpenFileName(this,
                                        tr("Open Image"), ".",
                        tr("Image Files (*.png *.jpg *.bmp)"));
    if (!logoFilename.isEmpty()) {
        emit logoUpdated(logoFilename);
    }
}

void Controls::on_c1CustomFlagButton_pressed()
{
    // TODO: c1 -- pick custom flag to load
    QString flag = "";
    emit competitor1CustomFlagLoaded(flag);
}

void Controls::on_c2CustomLogoButton_pressed()
{
    // TODO: c2 -- load custom logo
    QString flag = "";
    emit competitor2CustomFlagLoaded(flag);
}

void Controls::on_c2FlagComboBox_currentIndexChanged(int index)
{
    // TODO: c2 -- pick new flag from dropdown
    emit competitor2FlagChanged(index);

}

void Controls::on_playPauseButton_pressed()
{
    qDebug() << "----------------------------------------------";
    qDebug() << "Control:on_play_button_clicked() entry state: " <<
                "matchStarted: " << matchStarted << ", " <<
                "clockRunning: " << clockRunning << ", " <<
                "clockPaused: " << clockPaused;
    qDebug() << "----------------------------------------------";

    if (!matchStarted) {
        /* current image is play icon, flip to pause icon and
         * disable any controls we don't want user pressing
         * after match has officially started.
         */
        matchStarted = true;
        clockRunning = true;
        clockPaused = false;
        ui->playPauseButton->setIcon(QIcon(":/ui/pause"));
        disableControls();
    }
    else {
        /* matchStarted is true, meaning user pressed play button
         * already to start the match. After first time
         * on_play_button_clicked() is fired, the code path will keep
         * hitting this 'else' path until the state of the match is
         * flipped to matchStarted = false
         */
        if (clockPaused) { // current image is 'play' icon, flip to pause icon
            ui->playPauseButton->setIcon(QIcon(":/ui/pause"));
            clockPaused = false;
            clockRunning = true;
        }
        else if (clockRunning) { // current image is 'pause' icon
            // stop clock and flip image to 'play'
            ui->playPauseButton->setIcon(QIcon(":/ui/play"));
            clockRunning = false;
            clockPaused = true;
        }
    }

    qDebug() << "----------------------------------------------";
    qDebug() << "Control:on_play_button_clicked() exit state: " <<
                "matchStarted: " << matchStarted << ", " <<
                "clockRunning: " << clockRunning << ", " <<
                "clockPaused: " << clockPaused;
    qDebug() << "----------------------------------------------";
}

void Controls::on_resetButton_pressed()
{
    qDebug() << "------------------------------------------";
    qDebug() << "Controls::on_resetButton_pressed() -- in.";
    qDebug() << "------------------------------------------";
    ui->c1NameLabel->setText("Competitor 1");
    ui->c1PointsLabel->setText("0");
    ui->c1AdvantagesLabel->setText("0");
    ui->c1PenaltiesLabel->setText("0");
    ui->c1PointsLabel->setText("0");

    ui->c2NameLabel->setText("Competitor 2");
    ui->c2PointsLabel->setText("0");
    ui->c2AdvantagesLabel->setText("0");
    ui->c2PenaltiesLabel->setText("0");
    ui->c2PointsLabel->setText("0");

    ui->playPauseButton->setIcon(QIcon(":/ui/play"));

    // re-enable any controls that were disabled during running of match timer
    enableControls();

    /* Give current index to our map to get total seconds for reset value,
     * because we to keep the same division and timings when reset is pressed rather
     * than requiring user to change those each time they hit reset.
     */
    totalTime = divisionIdxToTimeMap[ui->divisionComboBox->currentIndex()];

    qDebug() << "Contents of divisionIdxToTimeMap: " << divisionIdxToTimeMap;

    clockMinutes = totalTime / 60;
    clockSeconds = totalTime % 60;

    qDebug() << "Using totalTime: " << totalTime;
    qDebug() << "Using clockMinutes: " << clockMinutes;
    qDebug() << "Using clockSeconds: " << clockSeconds;

    // require updating display here to show reset values
    updateDisplay();

    // Update match states
    resetMatchStates();

    qDebug() << "------------------------------------------";
    qDebug() << "Controls::on_resetButton_pressed() -- out.";
    qDebug() << "------------------------------------------";
}

void Controls::resetMatchStates()
{
    matchStarted = false;
    clockRunning = false;
    clockPaused = false;
    matchDone = false;
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

void Controls::on_testSoundButton_pressed()
{
    playSound();
}

void Controls::on_c1FlagComboBox_currentIndexChanged(const QString &flag)
{
    QString flagpath = countryToResourceMap[flag];
    emit c1FlagChanged(flagpath);
}

void Controls::on_c2FlagComboBox_currentIndexChanged(const QString &flag)
{
    QString flagpath = countryToResourceMap[flag];
    emit c2FlagChanged(flagpath);

}
