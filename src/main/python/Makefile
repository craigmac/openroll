.PHONY: build
build:
	cd ../../.. && fbs run

.PHONY: compile
compile:
	cd ../../.. && fbs build

.PHONY: clean
clean:
	cd ../../.. && fbs clean

.PHONY: convert-ui
convert-ui:
	pyside2-uic control.ui > ui_control.py && pyside2-uic scoreboard.ui > ui_scoreboard.py

.PHONY: convert-rc
convert-rc:
	pyside2-rcc openroll.qrc > openroll_rc.py

.PHONY: tags
tags:
	ctags --recurse=yes --tag-relative=yes --sort=foldcase --sort=yes --python-kinds=cfmvi --extra=+q --fields=-k+KiaSz --exclude=__pycache__,.git,build/,resources/ .

.PHONY: full
full: convert-ui convert-rc



