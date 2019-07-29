#!/usr/bin/env python

"""Main entry point to the openroll application."""

import argparse

import wx

from board import Board
from controls import Controls
from local_version import __VERSION__

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true',
                    required=False, help='Enable debug window and tools.',
                    default=False)

args = parser.parse_args()

# Bool, gets True is -d or --debug given, e.g. main.py -d
DEBUG = args.debug

AppBaseClass = wx.App
if DEBUG:
    from wx.lib.mixins.inspection import InspectableApp
    AppBaseClass = InspectableApp
    print('Using debugging mode.')


class Application(AppBaseClass):
    """wxPython entry, inheriting from wx.App and which should override
    OnInit method to create a main frame and return True."""
    def OnInit(self):
        """
        Required override method. Must return True.

        :returns: bool: Returns True if exited without error. This is wxPython
        required.
        """
        self.controls = Controls(None, wx.ID_ANY, 'Openroll - Controls - v{}'.format(__VERSION__))
        self.SetTopWindow(self.controls)
        self.controls.Show()
        self.scoreboard = Board(self.controls, wx.ID_ANY, 'Openroll - Scoreboard - v{}'.format(__VERSION__))
        self.scoreboard.Show()

        if DEBUG:
            print("Press Ctrl-Alt-I (Cmd-Opt-I on Mac) to launch the WIT.")
            self.InitInspection()
        return True

if __name__ == '__main__':
    app = Application(redirect=True)
    app.MainLoop()
