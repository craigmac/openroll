#!/usr/bin/env python

"""Scoreboard window."""
# import os

import wx

from local_version import __VERSION__


class Board(wx.Frame):
    """Scoreboard that scales for viewing on large screens."""
    def __init__(self, *args, **kwargs):
        """Creates a Scoreboard window instance."""
        super().__init__(*args, **kwargs)
        self.SetSize((900, 600))

        self.__set_properties()
        self.__do_layout()
        self.do_stuff()

    def do_stuff(self):
        """
        do_stuff

        :param self [TODO:type]: [TODO:description]
        """
        pass

    def __set_properties(self):
        """Set properties for this window."""
        self.SetTitle("Openroll - Scoreboard - {}".format(__VERSION__))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\cmaceachern\\projects\\openroll\\src\\resources\\icons\\Icon.ico",
                                       wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

    def __do_layout(self):
        """Create sizers and layout."""
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_9.Add((0, 0), 0, 0, 0)
        self.SetSizer(sizer_9)
        self.Layout()
