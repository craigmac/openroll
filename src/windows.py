#!/usr/bin/env python

import wx

class Controls(wx.Frame):
    """Window that holds the buttons and controls the Scoreboard."""
    def __init__(self, parent=None, ID=wx.ID_ANY, title="Controls Window"):
        super().__init__(parent, ID, title)
        panel = wx.Panel(self)
        btn = wx.Button(panel, label="Control button")
        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()
        self.CenterOnScreen(wx.BOTH)


class Scoreboard(wx.Frame):
    def __init__(self, parent=None, ID=wx.ID_ANY, title="Scoreboard Window"):
        super().__init__(parent, ID, title)
        panel = wx.Panel(self)
        btn = wx.Button(panel, label="Scoreboard button")
        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()


if __name__ == '__main__':
    print("Not meant to be run directly; import windows from here.")

