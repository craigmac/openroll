#############################################################################
##
# Copyright (C) 2018 The Qt Company Ltd.
# Contact: http://www.qt.io/licensing/
##
# This file is part of the Qt for Python examples of the Qt Toolkit.
##
# $QT_BEGIN_LICENSE:BSD$
# You may use this file under the terms of the BSD license as follows:
##
# "Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in
# the documentation and/or other materials provided with the
# distribution.
# * Neither the name of The Qt Company Ltd nor the names of its
# contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
##
##
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
# $QT_END_LICENSE$
##
#############################################################################

"""Qt Windows used in openroll program"""


from PySide2.QtWidgets import (QMainWindow, QWidget, QFileDialog, QMessageBox)
from PySide2.QtCore import (Qt, QTimer, QUrl, QDir, qDebug)
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtGui import QCloseEvent, QPixmap, QIcon

from ui_control import Ui_Control
from ui_scoreboard import Ui_Scoreboard

import functools


DEBUG = True
DEBUG_TIME = 60 * 1
DEFAULT_DIVISION_IDX = 14  # ADULT WHITE 18-29 5:00
DEFAULT_TIME = 60 * 5  # 5 minutes -> 300 seconds


class Control_Window(QMainWindow):
    """Main window--controls the `self.scoreboard` `Scoreboard`
    instance via buttons and Signal/Slot (i.e., callback) mechanisms.
    """

    def __init__(self, version, parent=None):
        super(Control_Window, self).__init__(parent)

        if DEBUG:
            qDebug("========== Control_Window.__init__() ==========")

        self.ui = Ui_Control()
        self.ui.setupUi(self)

        self.version = version

        # HACK: somewhat stops user on some platforms from clicking on close button.
        # Although they may close the window in other ways, or click on close on
        # platforms where some of these WindowFlags are not supported. We do this
        # because we setup scoreboard instance as independent Qt.Window, not a child of
        # the control window (to make 2 separate windows, otherwise Qt would draw
        # scoreboard window INSIDE control window).
        self.scoreboard = Scoreboard_Window(self, Qt.Window | Qt.CustomizeWindowHint
                                            | Qt.WindowTitleHint | Qt.WindowMinMaxButtonsHint)
        self.scoreboard.show()
        self.scoreboard.setWindowTitle("Openroll {}".format(self.version))

        self.default_time = DEBUG_TIME if DEBUG else DEFAULT_TIME
        self.total_time = DEBUG_TIME if DEBUG else DEFAULT_TIME
        self.clock_minutes, self.clock_seconds = divmod(self.total_time, 60)
        self.match_started = False
        self.match_done = False
        self.clock_running = False
        self.clock_paused = False
        self.current_division = ""
        self.current_belt = ""

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.media_player = QMediaPlayer()
        self.default_sound = QUrl("qrc:///sounds/airhorn.wav")
        self.media_player.setMedia(self.default_sound)
        self.media_player.setVolume(100)

        self.populate_default_sounds_dropdown()

        # DEV: move these to a method call
        self.c1_add2 = functools.partial(self.modify_points, self.ui.comp1_pts_label, 2)
        self.c1_add2_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_points, 2)

        self.c1_add3 = functools.partial(self.modify_points, self.ui.comp1_pts_label, 3)
        self.c1_add3_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_points, 3)

        self.c1_add4 = functools.partial(self.modify_points, self.ui.comp1_pts_label, 4)
        self.c1_add4_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_points, 4)

        self.c1_del2 = functools.partial(self.modify_points, self.ui.comp1_pts_label, -2)
        self.c1_del2_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_points, -2)

        self.c1_del3 = functools.partial(self.modify_points, self.ui.comp1_pts_label, -3)
        self.c1_del3_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_points, -3)

        self.c1_del4 = functools.partial(self.modify_points, self.ui.comp1_pts_label, -4)
        self.c1_del4_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_points, -4)

        self.c1_addA = functools.partial(self.modify_points, self.ui.comp1_adv_label, 1)
        self.c1_addA_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_advantages, 1)

        self.c1_addP = functools.partial(self.modify_points, self.ui.comp1_pen_label, 1)
        self.c1_addP_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_penalties, 1)

        self.c1_delA = functools.partial(self.modify_points, self.ui.comp1_adv_label, -1)
        self.c1_delA_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_advantages, -1)

        self.c1_delP = functools.partial(self.modify_points, self.ui.comp1_pen_label, -1)
        self.c1_delP_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp1_penalties, -1)

        self.c2_add2 = functools.partial(self.modify_points, self.ui.comp2_pts_label, 2)
        self.c2_add2_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_points, 2)

        self.c2_add3 = functools.partial(self.modify_points, self.ui.comp2_pts_label, 3)
        self.c2_add3_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_points, 3)

        self.c2_add4 = functools.partial(self.modify_points, self.ui.comp2_pts_label, 4)
        self.c2_add4_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_points, 4)

        self.c2_del2 = functools.partial(self.modify_points, self.ui.comp2_pts_label, -2)
        self.c2_del2_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_points, -2)

        self.c2_del3 = functools.partial(self.modify_points, self.ui.comp2_pts_label, -3)
        self.c2_del3_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_points, -3)

        self.c2_del4 = functools.partial(self.modify_points, self.ui.comp2_pts_label, -4)
        self.c2_del4_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_points, -4)

        self.c2_addA = functools.partial(self.modify_points, self.ui.comp2_adv_label, 1)
        self.c2_addA_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_advantages, 1)

        self.c2_addP = functools.partial(self.modify_points, self.ui.comp2_pen_label, 1)
        self.c2_addP_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_penalties, 1)

        self.c2_delA = functools.partial(self.modify_points, self.ui.comp2_adv_label, -1)
        self.c2_delA_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_advantages, -1)

        self.c2_delP = functools.partial(self.modify_points, self.ui.comp2_pen_label, -1)
        self.c2_delP_scoreboard = functools.partial(self.modify_points,
                                                    self.scoreboard.ui.comp2_penalties, -1)

        self.setup_signal_slot_connections()

        # self.ui.division_combobox.setCurrentIndex(14)

        if DEBUG:
            self.debug_dump()
            qDebug("========== Control_Window.__init__() done. ==========")

    def modify_points(self, label, amount):
        """Base method that we use to construct our partials
        from to save lots of repeated code.
        """
        oldvalue = int(label.text())
        newvalue = 0 if (oldvalue + amount) < 0 else oldvalue + amount
        label.setText(str(newvalue))

    def closeEvent(self, event: QCloseEvent):
        """Method MUST be named this way to work."""
        if DEBUG:
            qDebug("Control_Window caught close signal.")

        # DEV: change to QMessageBox.question() to simplify with yes/no/cancel
        # built in buttons, reducing code here.
        msgBox = QMessageBox()
        msgBox.setText("Do you really want to close the application?")

        yesButton = msgBox.addButton("Yes", QMessageBox.YesRole)
        noButton = msgBox.addButton("No", QMessageBox.NoRole)
        msgBox.setDefaultButton(noButton)
        msgBox.exec_()
        if msgBox.clickedButton() == yesButton:
            event.accept()
        elif msgBox.clickedButton() == noButton:
            event.ignore()

    def setup_signal_slot_connections(self):
        """Creates the Qt SIGNAL->SLOT connections, calling
        functions when certain events happen.
        """
        self.ui.comp1_add2.clicked.connect(self.c1_add2)
        self.ui.comp1_add2.clicked.connect(self.c1_add2_scoreboard)
        self.ui.comp1_add3.clicked.connect(self.c1_add3)
        self.ui.comp1_add3.clicked.connect(self.c1_add3_scoreboard)
        self.ui.comp1_add4.clicked.connect(self.c1_add4)
        self.ui.comp1_add4.clicked.connect(self.c1_add4_scoreboard)
        self.ui.comp1_addA.clicked.connect(self.c1_addA)
        self.ui.comp1_addA.clicked.connect(self.c1_addA_scoreboard)
        self.ui.comp1_addP.clicked.connect(self.c1_addP)
        self.ui.comp1_addP.clicked.connect(self.c1_addP_scoreboard)
        self.ui.comp1_del2.clicked.connect(self.c1_del2)
        self.ui.comp1_del2.clicked.connect(self.c1_del2_scoreboard)
        self.ui.comp1_del3.clicked.connect(self.c1_del3)
        self.ui.comp1_del3.clicked.connect(self.c1_del3_scoreboard)
        self.ui.comp1_del4.clicked.connect(self.c1_del4)
        self.ui.comp1_del4.clicked.connect(self.c1_del4_scoreboard)
        self.ui.comp1_delA.clicked.connect(self.c1_delA)
        self.ui.comp1_delA.clicked.connect(self.c1_delA_scoreboard)
        self.ui.comp1_delP.clicked.connect(self.c1_delP)
        self.ui.comp1_delP.clicked.connect(self.c1_delP_scoreboard)
        self.ui.comp2_add2.clicked.connect(self.c2_add2)
        self.ui.comp2_add2.clicked.connect(self.c2_add2_scoreboard)
        self.ui.comp2_add3.clicked.connect(self.c2_add3)
        self.ui.comp2_add3.clicked.connect(self.c2_add3_scoreboard)
        self.ui.comp2_add4.clicked.connect(self.c2_add4)
        self.ui.comp2_add4.clicked.connect(self.c2_add4_scoreboard)
        self.ui.comp2_addA.clicked.connect(self.c2_addA)
        self.ui.comp2_addA.clicked.connect(self.c2_addA_scoreboard)
        self.ui.comp2_addP.clicked.connect(self.c2_addP)
        self.ui.comp2_addP.clicked.connect(self.c2_addP_scoreboard)
        self.ui.comp2_del2.clicked.connect(self.c2_del2)
        self.ui.comp2_del2.clicked.connect(self.c2_del2_scoreboard)
        self.ui.comp2_del3.clicked.connect(self.c2_del3)
        self.ui.comp2_del3.clicked.connect(self.c2_del3_scoreboard)
        self.ui.comp2_del4.clicked.connect(self.c2_del4)
        self.ui.comp2_del4.clicked.connect(self.c2_del4_scoreboard)
        self.ui.comp2_delA.clicked.connect(self.c2_delA)
        self.ui.comp2_delA.clicked.connect(self.c2_delA_scoreboard)
        self.ui.comp2_delP.clicked.connect(self.c2_delP)
        self.ui.comp2_delP.clicked.connect(self.c2_delP_scoreboard)
        self.ui.sound_combobox.currentIndexChanged[str].connect(self.sound_combobox_changed)
        self.ui.division_combobox.currentIndexChanged.connect(self.division_changed)
        self.ui.loadLogoButton.clicked.connect(self.load_logo_clicked)
        self.ui.play_pause_button.clicked.connect(self.play_pause_button_clicked)
        self.ui.stop_button.clicked.connect(self.stop_button_clicked)
        self.ui.comp1_lineedit.textChanged.connect(self.scoreboard.ui.comp1_name.setText)
        self.ui.comp2_lineedit.textChanged.connect(self.scoreboard.ui.comp2_name.setText)

    def debug_dump(self):
        """Returns a dictionary capturing current values
        of variables in use for the program.
        """
        import json
        state = {
            'total_time': self.total_time,
            'clock_minutes': self.clock_minutes,
            'clock_seconds': self.clock_seconds,
            'clock_running': self.clock_running,
            'clock_paused': self.clock_paused,
            'match_started': self.match_started,
            'match_done': self.match_done,
            'current_division': self.current_division,
            'current_belt': self.current_belt,
                 }
        # qDebug requires str only so we convert using json module
        qDebug(json.dumps(state))

    def division_changed(self, index: int):
        """Run when division dropdown changed.
        """
        if DEBUG:
            qDebug("========== division_changed() ==========")
            qDebug("division_changed() called"
                   " with int value: {}".format(index))

        switch_dict = {
            0: ["ALL BELTS", 2 * 60, 'MIGHTY MITE - AGE 4'],
            1: ["ALL BELTS", 2 * 60, 'MIGHTY MITE 2 - AGE 5'],
            2: ["ALL BELTS", 2 * 60, 'MIGHTY MITE 3 - AGE 6'],
            3: ["ALL BELTS", 3 * 60, 'PEEWEE 1 - AGE 7'],
            4: ["ALL BELTS", 3 * 60, 'PEEWEE 2 - AGE 8'],
            5: ["ALL BELTS", 3 * 60, 'PEEWEE 3 - AGE 9'],
            6: ["ALL BELTS", 4 * 60, 'JUNIOR 1 - AGE 10'],
            7: ["ALL BELTS", 4 * 60, 'JUNIOR 2 - AGE 11'],
            8: ["ALL BELTS", 4 * 60, 'JUNIOR 3 - AGE 12'],
            9: ["ALL BELTS", 4 * 60, 'TEEN 1 - AGE 13'],
            10: ["ALL BELTS", 4 * 60, 'TEEN 2 - AGE 14'],
            11: ["ALL BELTS", 4 * 60, 'TEEN 3 - AGE 15'],
            12: ["ALL BELTS", 5 * 60, 'JUVENILE 1 - AGE 16'],
            13: ["ALL BELTS", 5 * 60, 'JUVENILE 2 - AGE 17'],
            14: ["WHITE", 5 * 60, 'ADULT - AGE 18-29'],
            15: ["BLUE", 6 * 60, 'ADULT - AGE 18-29'],
            16: ["PURPLE", 7 * 60, 'ADULT - AGE 18-29'],
            17: ["BROWN", 8 * 60, 'ADULT - AGE 18-29'],
            18: ["BLACK", 9 * 60, 'ADULT - AGE 18-29'],
            19: ["WHITE", 5 * 60, 'MASTER 1 - AGE 30-35'],
            20: ["BLUE", 5 * 60, 'MASTER 1 - AGE 30-35'],
            21: ["PURPLE", 6 * 60, 'MASTER 1 - AGE 30-35'],
            22: ["BROWN", 6 * 60, 'MASTER 1 - AGE 30-35'],
            23: ["BLACK", 6 * 60, 'MASTER 1 - AGE 30-35'],
            24: ["ALL BELTS", 5 * 60, 'MASTER 2 - AGE 36-40'],
            25: ["ALL BELTS", 5 * 60, 'MASTER 3 - AGE 41-45'],
            26: ["ALL BELTS", 5 * 60, 'MASTER 4 - AGE 46-50'],
            27: ["ALL BELTS", 5 * 60, 'MASTER 5 - AGE 51-55'],
            28: ["ALL BELTS", 5 * 60, 'MASTER 6 - AGE 56+'],
        }

        # Return some defaults here on key error, the 'default:' switch case
        new_values = switch_dict.get(index,
                                     ["WHITE", 5 * 60, 'ADULT - AGE 18-29'])

        # Unpack the list
        self.current_belt, self.total_time, self.current_division = new_values
        self.clock_minutes, self.clock_seconds = divmod(self.total_time, 60)

        # Set scoreboard.
        # FIXME: might be a better way with signal/slot but this works
        self.scoreboard.ui.beltLabel.setText(self.current_belt)
        self.scoreboard.ui.divisionLabel.setText(self.current_division)

        if DEBUG:
            self.debug_dump()
            qDebug("========== division_changed() done. ==========")

    def sound_combobox_changed(self, soundname: str):
        """Callback (Qt 'SLOT') run when sound dropdown
        changed.
        """
        new_sound = QUrl("qrc:///sounds/{}".format(soundname))
        self.media_player.setMedia(new_sound)

        if DEBUG:
            qDebug("sound_combobox_changed(): sound file "
                   "changed to: {}".format(soundname))
            self.debug_dump()
            qDebug("========== sound_combobox_changed() done. ==========")

    def populate_default_sounds_dropdown(self):
        """Get list of sounds from sound directory in the resource
        file, sorted by name and add them to combobox dropdown
        as options.
        """
        sounds_dir = QDir(":/sounds")
        sounds = sounds_dir.entryList(QDir.Files, QDir.Name)
        self.ui.sound_combobox.addItems(sounds)
        self.ui.sound_combobox.setCurrentText("airhorn.wav")

    def toggle_controls(self):
        """Call setDisabled() on widgets using isEnabled() inverse"""

        self.ui.comp1_add2.setDisabled(not self.ui.comp1_add2.isEnabled())
        self.ui.comp1_add3.setDisabled(not self.ui.comp1_add3.isEnabled())
        self.ui.comp1_add4.setDisabled(not self.ui.comp1_add4.isEnabled())
        self.ui.comp1_addA.setDisabled(not self.ui.comp1_addA.isEnabled())
        self.ui.comp1_addP.setDisabled(not self.ui.comp1_addP.isEnabled())
        self.ui.comp1_del2.setDisabled(not self.ui.comp1_del2.isEnabled())
        self.ui.comp1_del3.setDisabled(not self.ui.comp1_del3.isEnabled())
        self.ui.comp1_del4.setDisabled(not self.ui.comp1_del4.isEnabled())
        self.ui.comp1_delA.setDisabled(not self.ui.comp1_delA.isEnabled())
        self.ui.comp1_delP.setDisabled(not self.ui.comp1_delP.isEnabled())

        self.ui.comp2_add2.setDisabled(not self.ui.comp2_add2.isEnabled())
        self.ui.comp2_add3.setDisabled(not self.ui.comp2_add3.isEnabled())
        self.ui.comp2_add4.setDisabled(not self.ui.comp2_add4.isEnabled())
        self.ui.comp2_addA.setDisabled(not self.ui.comp2_addA.isEnabled())
        self.ui.comp2_addP.setDisabled(not self.ui.comp2_addP.isEnabled())
        self.ui.comp2_del2.setDisabled(not self.ui.comp2_del2.isEnabled())
        self.ui.comp2_del3.setDisabled(not self.ui.comp2_del3.isEnabled())
        self.ui.comp2_del4.setDisabled(not self.ui.comp2_del4.isEnabled())
        self.ui.comp2_delA.setDisabled(not self.ui.comp2_delA.isEnabled())
        self.ui.comp2_delP.setDisabled(not self.ui.comp2_delP.isEnabled())

    def play_sound(self):
        """Play media sound if sound option is on."""
        if self.ui.soundOnRadioButton.isChecked():
            self.media_player.play()
        # DEV: is this needed?
        self.ui.play_pause_button.setDisabled(True)

    def play_pause_button_clicked(self):
        """Start match timer."""
        if DEBUG:
            qDebug("========== play_pause_button_clicked() in. ==========")
            self.debug_dump()
        if not self.match_started:
            self.match_started = True
            self.clock_running = True
            self.clock_paused = False
            pause_icon = QIcon(":/images/pause.png")
            self.ui.play_pause_button.setIcon(pause_icon)
            self.ui.division_combobox.setDisabled(True)
            if DEBUG:
                qDebug("Bottom of self.match_started=False branch.")
                # self.debug_dump()
        else:
            if DEBUG:
                qDebug("play_pause_button_clicked() 'else' branch.")
            # self.match_started is true, meaning user pressed play button
            # already to start the match. After first time, the code path
            # should keep hitting this 'else' path until the state of the
            # match is flipped to self.match_started = False
            if self.clock_paused:  # current image is 'play' icon
                if DEBUG:
                    qDebug("match_started=True and clock_paused=True.")
                    # self.debug_dump()
                pause_icon = QIcon(":/images/pause.png")
                self.ui.play_pause_button.setIcon(pause_icon)
                self.clock_paused = False
                self.clock_running = True
            elif self.clock_running:  # current image is 'pause' icon
                if DEBUG:
                    qDebug("match_started=True and clock_running=True branch")
                    # self.debug_dump()
                play_icon = QIcon(":/images/play.png")
                self.ui.play_pause_button.setIcon(play_icon)
                self.clock_running = False
                self.clock_paused = True
            else:  # Here be dragons... we should not reach here.
                if DEBUG:
                    qDebug("ERROR: We should not have reached this branch.")

        if DEBUG:
            self.debug_dump()
            qDebug("========== play_pause_button_clicked() out. ==========")

    def stop_button_clicked(self):
        if DEBUG:
            qDebug("========== stop_button_clicked() ==========")
            # self.debug_dump()

        # GOTCHA: case where we press stop without pressing pause first,
        # the icon doesn't flip back to play icon
        if self.clock_running:
            play_icon = QIcon(":/images/play.png")
            self.ui.play_pause_button.setIcon(play_icon)
        self.match_done = False
        self.match_started = False
        self.clock_running = False
        self.clock_paused = False
        self.ui.play_pause_button.setDisabled(False)
        self.ui.division_combobox.setDisabled(False)

        self.reset_labels()

        if DEBUG:
            # self.debug_dump()
            qDebug("========== stop_button_clicked() done. ==========")

    def reset_labels(self):
        """Resets some labels back to defaults. We respect the name
        labels, sound choice (on/off), sound file, logo file, and
        division selection chosen by user--this is for better UX.
        """
        if DEBUG:
            # self.debug_dump()
            qDebug("========== reset_labels() in. ==========")

        # Reset score labels
        self.ui.comp1_pts_label.setText('0')
        self.ui.comp1_pen_label.setText('0')
        self.ui.comp1_adv_label.setText('0')

        self.ui.comp2_pts_label.setText('0')
        self.ui.comp2_pen_label.setText('0')
        self.ui.comp2_adv_label.setText('0')

        self.scoreboard.ui.comp1_points.setText('0')
        self.scoreboard.ui.comp2_points.setText('0')

        self.scoreboard.ui.comp1_advantages.setText('0')
        self.scoreboard.ui.comp2_advantages.setText('0')

        self.scoreboard.ui.comp1_penalties.setText('0')
        self.scoreboard.ui.comp2_penalties.setText('0')

        # Reset clocks to defaults
        self.total_time = DEBUG_TIME if DEBUG else DEFAULT_TIME
        self.clock_minutes, self.clock_seconds = divmod(self.total_time, 60)

        if self.clock_seconds < 10:
            self.clock_seconds = '0' + str(self.clock_seconds)

        new_time = '{}:{}'.format(self.clock_minutes, self.clock_seconds)

        # Update timer labels
        self.ui.timer_label.setText(new_time)
        self.scoreboard.ui.timer_display.setText(new_time)

        if DEBUG:
            # self.debug_dump()
            qDebug("========== reset_labels() out. ==========")

    def load_logo_clicked(self):
        # returns (fileName: str, selectedFilter: str)
        fname = QFileDialog.getOpenFileName(self, "Open Image",
                                            ".",
                                            "Image Files (*.png *.jpg *.bmp)")
        if DEBUG:
            qDebug(fname[0])
        if fname[0] != "":
            self.load_image(fname[0])

    def load_image(self, fname: str):
        if DEBUG:
            qDebug("load_image(): trying to load {}".format(fname))
        logo = QPixmap(fname)
        self.scoreboard.ui.user_logo.setPixmap(logo)

    def update_clock(self):
        """Update timer labels if match not done and clock running."""
        if self.match_done:
            return

        # GOTCHA: Sometimes the timer fires before
        # we are fully setup loading/altering things so
        # total_time might have not been updated at startup to default
        # 300 seconds yet, so we can't rely on just that,
        # we must check if the match was actually started.
        if self.total_time <= 0 and self.match_started:
            self.match_done = True
            self.play_sound()
            return

        if self.match_started and self.clock_running:
            self.total_time -= 1

        # Update display even if clock_paused or match not started
        self.clock_minutes, self.clock_seconds = divmod(self.total_time, 60)

        # Pad with extra leading zero for better visuals on seconds
        if self.clock_seconds < 10:
            self.clock_seconds = "0{}".format(self.clock_seconds)

        new_time = "{}:{}".format(self.clock_minutes, self.clock_seconds)
        self.ui.timer_label.setText(new_time)
        self.scoreboard.ui.timer_display.setText(new_time)

        # if DEBUG:
        #     qDebug("update_clock(): finished")
        #     self.debug_dump()


class Scoreboard_Window(QWidget):
    """Scoreboard window, child of Control_Window but
    given initialization flags to be an independent window,
    otherwise would draw into same window space as parent.
    """

    def __init__(self, parent, qt_window_flags):
        super(Scoreboard_Window, self).__init__(parent, qt_window_flags)
        self.ui = Ui_Scoreboard()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.CustomizeWindowHint)

    def closeEvent(self, event: QCloseEvent):
        """Override of virtual Qt method. Fired when close signal
        caught by this window. If parent still exists we ignore
        the request to close (e.g., user pressed alt-f4 as we
        try to hide the close button on supported platforms but
        we must cover cases where user still sends close window
        signal to this window somehow)
        """
        if DEBUG:
            qDebug("Scoreboard_Window caught close signal")
            qDebug("My parent window is: {}".format(self.parentWidget()))

        # We should never need to event.accept() anyway because
        # closing the parent class automatically closes this one.
        event.ignore() if self.parentWidget() else event.accept()
