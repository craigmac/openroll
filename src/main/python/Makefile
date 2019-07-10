build:
	cd ../../.. && fbs run

compile:
	cd ../../.. && fbs build

clean:
	cd ../../.. && fbs clean

convert-ui:
	pyside2-uic control.ui > ui_control.py && pyside2-uic scoreboard.ui > ui_scoreboard.py

convert-rc:
	pyside2-rcc openroll.qrc > openroll_rc.py

full: convert-ui convert-rc



