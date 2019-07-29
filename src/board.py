#!/usr/bin/env python

"""Scoreboard window."""
from os.path import curdir, join, abspath
import wx

from local_version import __VERSION__


class Board(wx.Frame):
    """Scoreboard that scales for viewing on large screens."""
    def __init__(self, *args, **kwargs):
        """Creates a Scoreboard window instance."""
        kwargs["style"] = kwargs.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE
        super().__init__(*args, **kwargs)
        self.SetSize((1515, 654))

        self.__create_widgets()
        self.__set_properties()
        self.__do_layout()
        self.__do_bindings()

    def __create_widgets(self):
        self.c1_name_label = wx.StaticText(self, wx.ID_ANY, "Competitor 1", style=wx.ALIGN_CENTER)
        self.c1_flag_image = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(join(abspath(curdir), 'resources', 'flags',
                                             'ca.png'), wx.BITMAP_TYPE_ANY), style=wx.FULL_REPAINT_ON_RESIZE)
        self.c1_points_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c1_adv_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c1_pen_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c2_name_label = wx.StaticText(self, wx.ID_ANY, "Competitor 2", style=wx.ALIGN_CENTER)
        self.c2_flag_label = wx.StaticText(self, wx.ID_ANY, "FLAG GOES HERE", style=wx.ALIGN_CENTER)
        self.c2_points_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c2_adv_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c2_pen_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.logo_image = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(join(abspath(curdir), 'resources', 'icons',
                                          'openroll.png')), style=wx.FULL_REPAINT_ON_RESIZE)
        self.timer_label = wx.StaticText(self, wx.ID_ANY, "5:00", style=wx.ALIGN_CENTER)

    def __do_bindings(self):
        pass

    def __set_properties(self):
        """Set properties for this window."""
        self.SetTitle("Openroll - Scoreboard - {}".format(__VERSION__))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap(join(abspath(curdir), 'resources', 'icons', 'Icon.ico'), wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.c1_name_label.SetBackgroundColour(wx.Colour(0, 0, 255))
        self.c1_name_label.SetForegroundColour(wx.Colour(255, 255, 255))
        self.c1_name_label.SetFont(wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_flag_image.SetMinSize((100, 50))
        self.c1_flag_image.SetBackgroundColour(wx.Colour(50, 50, 204))
        self.c1_points_label.SetBackgroundColour(wx.Colour(66, 111, 66))
        self.c1_points_label.SetFont(wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_adv_label.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.c1_adv_label.SetFont(wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_pen_label.SetBackgroundColour(wx.Colour(204, 50, 50))
        self.c1_pen_label.SetFont(wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_name_label.SetMinSize((496, 213))
        self.c2_name_label.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.c2_name_label.SetFont(wx.Font(48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_points_label.SetBackgroundColour(wx.Colour(66, 111, 66))
        self.c2_points_label.SetFont(wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_adv_label.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.c2_adv_label.SetFont(wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_pen_label.SetBackgroundColour(wx.Colour(204, 50, 50))
        self.c2_pen_label.SetFont(wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.logo_image.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.timer_label.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.timer_label.SetFont(wx.Font(96, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))

    def __do_layout(self):
        """Create sizers and layout."""
        main_vsizer = wx.BoxSizer(wx.VERTICAL)
        info_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        c2_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        c1_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        c1_hsizer.Add(self.c1_name_label, 2, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 2)
        c1_hsizer.Add(self.c1_flag_image, 1, wx.ALL | wx.EXPAND, 2)
        c1_hsizer.Add(self.c1_points_label, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 2)
        c1_hsizer.Add(self.c1_adv_label, 1, wx.ALL | wx.EXPAND, 2)
        c1_hsizer.Add(self.c1_pen_label, 1, wx.ALL | wx.EXPAND, 2)
        main_vsizer.Add(c1_hsizer, 1, wx.EXPAND, 0)
        c2_hsizer.Add(self.c2_name_label, 2, wx.ALL | wx.EXPAND, 2)
        c2_hsizer.Add(self.c2_flag_label, 1, wx.ALL | wx.EXPAND, 2)
        c2_hsizer.Add(self.c2_points_label, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 2)
        c2_hsizer.Add(self.c2_adv_label, 1, wx.ALL | wx.EXPAND, 2)
        c2_hsizer.Add(self.c2_pen_label, 1, wx.ALL | wx.EXPAND, 2)
        main_vsizer.Add(c2_hsizer, 1, wx.EXPAND, 0)
        info_hsizer.Add(self.logo_image, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 0)
        info_hsizer.Add(self.timer_label, 0, wx.ALL | wx.EXPAND, 0)
        label_19 = wx.StaticText(self, wx.ID_ANY, "label_19", style=wx.ALIGN_CENTER)
        label_19.SetBackgroundColour(wx.Colour(255, 255, 255))
        info_hsizer.Add(label_19, 1, wx.ALL | wx.EXPAND, 0)
        main_vsizer.Add(info_hsizer, 1, wx.EXPAND, 0)
        self.SetSizer(main_vsizer)
        self.Layout()
