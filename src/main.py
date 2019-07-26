#!/usr/bin/env python

"""Main entry point to the openroll application."""

from windows import Controls, Scoreboard

import wx

DEBUG = True
# WIT gives you a live debugging introspective window with ctrl-alt-i
USE_WIT = False

# We modify this is we want to use WIT
AppBaseClass = wx.App

if DEBUG:
    # print statements will log to this window
    USE_WIT = True
    from wx.lib.mixins.inspection import InspectableApp
    AppBaseClass = InspectableApp

class Application(AppBaseClass):
    """wx Application base class."""
    def OnInit(self):
        """
        Required implementation override.

        :param self wx.App: Will either be wx.App or InspectableApp
        """
        # main_frame = Controls(title="Openroll")
        # self.SetTopWindow(main_frame)
        if DEBUG:
            print("Print statements go to this stdout window by default.")
        if USE_WIT:
            print("Press Ctrl-Alt-I (Cmd-Opt-I on Mac) to launch the debugger (WIT).")
            self.InitInspection()
        return True


if __name__ == '__main__':
    app = Application(redirect=True)

    controls = Controls()
    board = Scoreboard(controls)

    app.SetTopWindow(controls)

    controls.Show()
    board.Show()

    app.MainLoop()
