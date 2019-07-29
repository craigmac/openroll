#!/usr/bin/env python

"""Controls window."""
from os.path import curdir, join, abspath
import wx

from local_version import __VERSION__


class Controls(wx.Frame):
    """Controls window."""
    def __init__(self, *args, **kwargs):
        """ Creates Controls window instance."""
        kwargs["style"] = kwargs.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.SYSTEM_MENU
        super().__init__(*args, **kwargs)
        self.SetSize((915, 363))

        self.__create_menus()
        self.__create_widgets()
        self.__set_properties()
        self.__do_layout()
        self.__do_bindings()

    def __create_menus(self):
        """Build menus for this frame."""
        self.controls_menubar = wx.MenuBar()
        menu = wx.Menu()
        menu.Append(wx.ID_ANY, "&Mute Sound", "", wx.ITEM_CHECK)
        self.controls_menubar.Append(menu, "&Settings")
        menu = wx.Menu()
        self.controls_menubar.Append(menu, "&About")
        self.SetMenuBar(self.controls_menubar)

    def __create_widgets(self):
        """Create labels, buttons, etc."""
        self.c1_pts_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c1_adv_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c1_pen_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c2_pts_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c2_adv_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c2_pen_label = wx.StaticText(self, wx.ID_ANY, "0", style=wx.ALIGN_CENTER)
        self.c1_name_label = wx.StaticText(self, wx.ID_ANY, "Competitor A", style=wx.ALIGN_CENTER)
        self.timer_label = wx.StaticText(self, wx.ID_ANY, "5:00", style=wx.ALIGN_CENTER)
        self.c2_name_label = wx.StaticText(self, wx.ID_ANY, "Competitor B", style=wx.ALIGN_CENTER)
        self.c1_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.c1_flag_combo_box = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.c1_load_custom_flag = wx.Button(self, wx.ID_ANY, "...")
        self.c2_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.c2_flag_combo_box = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.c2_load_custom_flag = wx.Button(self, wx.ID_ANY, "...")
        self.c1_add_2_btn = wx.Button(self, wx.ID_ANY, "+2")
        self.c1_add_3_btn = wx.Button(self, wx.ID_ANY, "+3")
        self.c1_add_4_btn = wx.Button(self, wx.ID_ANY, "+4")
        self.c1_add_a_btn = wx.Button(self, wx.ID_ANY, "+A")
        self.c1_add_p_btn = wx.Button(self, wx.ID_ANY, "+P")
        self.play_pause_btn = wx.Button(self, wx.ID_ANY, "")
        self.c2_add_2_btn = wx.Button(self, wx.ID_ANY, "+2")
        self.c2_add_3_btn = wx.Button(self, wx.ID_ANY, "+3")
        self.c2_add_4_btn = wx.Button(self, wx.ID_ANY, "+4")
        self.c2_add_a_btn = wx.Button(self, wx.ID_ANY, "+A")
        self.c2_add_p_btn = wx.Button(self, wx.ID_ANY, "+P")
        self.c1_del_2_btn = wx.Button(self, wx.ID_ANY, "-2")
        self.c1_del_3_btn = wx.Button(self, wx.ID_ANY, "-3")
        self.c1_del_4_btn = wx.Button(self, wx.ID_ANY, "-4")
        self.c1_del_a_btn = wx.Button(self, wx.ID_ANY, "-A")
        self.c1_del_p_btn = wx.Button(self, wx.ID_ANY, "-P")
        self.stop_btn = wx.Button(self, wx.ID_ANY, "")
        self.c2_del_2_btn = wx.Button(self, wx.ID_ANY, "-2")
        self.c2_del_3_btn = wx.Button(self, wx.ID_ANY, "-3")
        self.c2_del_4_btn = wx.Button(self, wx.ID_ANY, "-4")
        self.c2_del_a_btn = wx.Button(self, wx.ID_ANY, "-A")
        self.c2_del_p_btn = wx.Button(self, wx.ID_ANY, "-P")


    def __set_properties(self):
        # begin wxGlade: Controls.__set_properties
        self.SetTitle("Openroll - Controls - {}".format(__VERSION__))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap(join(abspath(curdir), 'resources', 'icons', 'Icon.ico'), wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.c1_pts_label.SetMinSize((100, 37))
        self.c1_pts_label.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c1_pts_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_adv_label.SetMinSize((100, 37))
        self.c1_adv_label.SetBackgroundColour(wx.Colour(255, 255, 130))
        self.c1_adv_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_pen_label.SetMinSize((100, 37))
        self.c1_pen_label.SetBackgroundColour(wx.Colour(200, 0, 0))
        self.c1_pen_label.SetForegroundColour(wx.Colour(255, 255, 255))
        self.c1_pen_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_pts_label.SetMinSize((100, 37))
        self.c2_pts_label.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c2_pts_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_adv_label.SetMinSize((100, 37))
        self.c2_adv_label.SetBackgroundColour(wx.Colour(255, 255, 130))
        self.c2_adv_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_pen_label.SetMinSize((100, 37))
        self.c2_pen_label.SetBackgroundColour(wx.Colour(200, 0, 0))
        self.c2_pen_label.SetForegroundColour(wx.Colour(255, 255, 255))
        self.c2_pen_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_name_label.SetMinSize((325, 37))
        self.c1_name_label.SetForegroundColour(wx.Colour(0, 0, 0))
        self.c1_name_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.timer_label.SetMinSize((250, 56))
        self.timer_label.SetFont(wx.Font(36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_name_label.SetMinSize((325, 37))
        self.c2_name_label.SetForegroundColour(wx.Colour(0, 0, 0))
        self.c2_name_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_text_ctrl.SetMinSize((150, 23))
        self.c1_flag_combo_box.SetMinSize((150, 23))
        self.c1_load_custom_flag.SetMinSize((50, 26))
        self.c2_text_ctrl.SetMinSize((150, 23))
        self.c2_flag_combo_box.SetMinSize((150, 23))
        self.c2_load_custom_flag.SetMinSize((50, 26))
        self.c1_add_2_btn.SetMinSize((75, 75))
        self.c1_add_2_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c1_add_2_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_add_3_btn.SetMinSize((75, 75))
        self.c1_add_3_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c1_add_3_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_add_4_btn.SetMinSize((75, 75))
        self.c1_add_4_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c1_add_4_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_add_a_btn.SetMinSize((75, 75))
        self.c1_add_a_btn.SetBackgroundColour(wx.Colour(255, 255, 130))
        self.c1_add_a_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_add_p_btn.SetMinSize((75, 75))
        self.c1_add_p_btn.SetBackgroundColour(wx.Colour(200, 0, 0))
        self.c1_add_p_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.play_pause_btn.SetMinSize((150, 75))
        self.play_pause_btn.SetBitmap(wx.Bitmap(join(abspath(curdir), 'resources', 'ui', 'baseline_play_arrow_black_18dp.png'),
                wx.BITMAP_TYPE_ANY))
        self.c2_add_2_btn.SetMinSize((75, 75))
        self.c2_add_2_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c2_add_2_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_add_3_btn.SetMinSize((75, 75))
        self.c2_add_3_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c2_add_3_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_add_4_btn.SetMinSize((75, 75))
        self.c2_add_4_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c2_add_4_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_add_a_btn.SetMinSize((75, 75))
        self.c2_add_a_btn.SetBackgroundColour(wx.Colour(255, 255, 130))
        self.c2_add_a_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_add_p_btn.SetMinSize((75, 75))
        self.c2_add_p_btn.SetBackgroundColour(wx.Colour(200, 0, 0))
        self.c2_add_p_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_del_2_btn.SetMinSize((75, 75))
        self.c1_del_2_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c1_del_2_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_del_3_btn.SetMinSize((75, 75))
        self.c1_del_3_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c1_del_3_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_del_4_btn.SetMinSize((75, 75))
        self.c1_del_4_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c1_del_4_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_del_a_btn.SetMinSize((75, 75))
        self.c1_del_a_btn.SetBackgroundColour(wx.Colour(255, 255, 130))
        self.c1_del_a_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c1_del_p_btn.SetMinSize((75, 75))
        self.c1_del_p_btn.SetBackgroundColour(wx.Colour(200, 0, 0))
        self.c1_del_p_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.stop_btn.SetMinSize((150, 75))
        self.stop_btn.SetBitmap(wx.Bitmap(join(abspath(curdir), 'resources', 'ui', 'baseline_stop_black_18dp.png'),
                                          wx.BITMAP_TYPE_ANY))
        self.c2_del_2_btn.SetMinSize((75, 75))
        self.c2_del_2_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c2_del_2_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_del_3_btn.SetMinSize((75, 75))
        self.c2_del_3_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c2_del_3_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_del_4_btn.SetMinSize((75, 75))
        self.c2_del_4_btn.SetBackgroundColour(wx.Colour(125, 170, 125))
        self.c2_del_4_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_del_a_btn.SetMinSize((75, 75))
        self.c2_del_a_btn.SetBackgroundColour(wx.Colour(255, 255, 130))
        self.c2_del_a_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.c2_del_p_btn.SetMinSize((75, 75))
        self.c2_del_p_btn.SetBackgroundColour(wx.Colour(200, 0, 0))
        self.c2_del_p_btn.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))

    def __do_layout(self):
        """Creates layout of sizers and window."""
        main_vsizer = wx.BoxSizer(wx.VERTICAL)
        row_del_btns_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        row_add_btns_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Points", style=wx.ALIGN_CENTER)
        label_1.SetMinSize((100, 32))
        label_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_1, 0, wx.ALL, 2)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Advantages", style=wx.ALIGN_CENTER)
        label_2.SetMinSize((100, 32))
        label_2.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_2, 0, wx.ALL, 2)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Penalties", style=wx.ALIGN_CENTER)
        label_3.SetMinSize((100, 32))
        label_3.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_3, 0, wx.ALL, 2)
        sizer_4.Add((275, 20), 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Points", style=wx.ALIGN_CENTER)
        label_4.SetMinSize((100, 32))
        label_4.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_4, 0, wx.ALL, 2)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Advantages", style=wx.ALIGN_CENTER)
        label_5.SetMinSize((100, 32))
        label_5.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_5, 0, wx.ALL, 2)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Penalties", style=wx.ALIGN_CENTER)
        label_6.SetMinSize((100, 32))
        label_6.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_4.Add(label_6, 0, wx.ALL, 2)
        main_vsizer.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_3.Add(self.c1_pts_label, 0, wx.ALL, 2)
        sizer_3.Add(self.c1_adv_label, 0, wx.ALL, 2)
        sizer_3.Add(self.c1_pen_label, 0, wx.ALL, 2)
        sizer_3.Add((275, 37), 0, 0, 0)
        sizer_3.Add(self.c2_pts_label, 0, wx.ALL, 2)
        sizer_3.Add(self.c2_adv_label, 0, wx.ALL, 2)
        sizer_3.Add(self.c2_pen_label, 0, wx.ALL, 2)
        main_vsizer.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_2.Add(self.c1_name_label, 0, wx.ALIGN_CENTER, 0)
        sizer_2.Add(self.timer_label, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_2.Add(self.c2_name_label, 0, wx.ALIGN_CENTER, 0)
        main_vsizer.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.c1_text_ctrl, 0, wx.ALL, 2)
        sizer_1.Add(self.c1_flag_combo_box, 0, wx.ALL, 2)
        sizer_1.Add(self.c1_load_custom_flag, 0, wx.ALL, 2)
        sizer_1.Add((175, 23), 0, wx.ALL, 0)
        sizer_1.Add(self.c2_text_ctrl, 0, wx.ALL, 2)
        sizer_1.Add(self.c2_flag_combo_box, 0, wx.ALL, 2)
        sizer_1.Add(self.c2_load_custom_flag, 0, wx.ALL, 2)
        main_vsizer.Add(sizer_1, 0, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c1_add_2_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c1_add_3_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c1_add_4_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c1_add_a_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c1_add_p_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.play_pause_btn, 0, 0, 0)
        row_add_btns_hsizer.Add(self.c2_add_2_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c2_add_3_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c2_add_4_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c2_add_a_btn, 1, wx.EXPAND, 0)
        row_add_btns_hsizer.Add(self.c2_add_p_btn, 1, wx.EXPAND, 0)
        main_vsizer.Add(row_add_btns_hsizer, 0, wx.FIXED_MINSIZE, 0)
        row_del_btns_hsizer.Add(self.c1_del_2_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c1_del_3_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c1_del_4_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c1_del_a_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c1_del_p_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.stop_btn, 0, 0, 0)
        row_del_btns_hsizer.Add(self.c2_del_2_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c2_del_3_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c2_del_4_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c2_del_a_btn, 1, wx.EXPAND, 0)
        row_del_btns_hsizer.Add(self.c2_del_p_btn, 1, wx.EXPAND, 0)
        main_vsizer.Add(row_del_btns_hsizer, 0, wx.FIXED_MINSIZE, 0)
        self.SetSizer(main_vsizer)
        self.Layout()
        self.Centre()

    def __do_bindings(self):
        """Create wxWidget event binds to methods."""
        self.Bind(wx.EVT_BUTTON, self.on_c1_add_2_clicked, self.c1_add_2_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_del_2_clicked, self.c1_del_2_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_add_3_clicked, self.c1_add_3_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_del_3_clicked, self.c1_del_3_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_add_4_clicked, self.c1_add_4_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_del_4_clicked, self.c1_del_4_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_add_a_clicked, self.c1_add_a_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_del_a_clicked, self.c1_del_a_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_add_p_clicked, self.c1_add_p_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c1_del_p_clicked, self.c1_del_p_btn)

        self.Bind(wx.EVT_BUTTON, self.on_c2_add_2_clicked, self.c2_add_2_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_del_2_clicked, self.c2_del_2_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_add_3_clicked, self.c2_add_3_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_del_3_clicked, self.c2_del_3_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_add_4_clicked, self.c2_add_4_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_del_4_clicked, self.c2_del_4_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_add_a_clicked, self.c2_add_a_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_del_a_clicked, self.c2_del_a_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_add_p_clicked, self.c2_add_p_btn)
        self.Bind(wx.EVT_BUTTON, self.on_c2_del_p_clicked, self.c2_del_p_btn)

    def on_c1_add_2_clicked(self, event):
        """
        Adds 2 to competitor 1 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pts_label.GetLabelText())
        current_value += 2
        self.c1_pts_label.SetLabelText("{}".format(current_value))

    def on_c1_del_2_clicked(self, event):
        """
        Subtract 2 from competitor 1 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pts_label.GetLabelText())
        current_value -= 2
        if current_value <= 0:
            current_value = 0
        self.c1_pts_label.SetLabelText("{}".format(current_value))

    def on_c1_add_3_clicked(self, event):
        """
        Adds 3 to competitor 1 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pts_label.GetLabelText())
        current_value += 3
        self.c1_pts_label.SetLabelText("{}".format(current_value))

    def on_c1_del_3_clicked(self, event):
        """
        Subtract 3 from competitor 1 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pts_label.GetLabelText())
        current_value -= 3
        if current_value <= 0:
            current_value = 0
        self.c1_pts_label.SetLabelText("{}".format(current_value))

    def on_c1_add_4_clicked(self, event):
        """
        Adds 4 to competitor 1 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pts_label.GetLabelText())
        current_value += 4
        self.c1_pts_label.SetLabelText("{}".format(current_value))

    def on_c1_del_4_clicked(self, event):
        """
        Substracts 4 from competitor 1 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pts_label.GetLabelText())
        current_value -= 4
        if current_value <= 0:
            current_value = 0
        self.c1_pts_label.SetLabelText("{}".format(current_value))

    def on_c1_del_a_clicked(self, event):
        """
        Substracts 1 from competitor 1 advantages on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_adv_label.GetLabelText())
        current_value -= 1
        if current_value <= 0:
            current_value = 0
        self.c1_adv_label.SetLabelText("{}".format(current_value))

    def on_c1_del_p_clicked(self, event):
        """
        Substracts 1 from competitor 1 penalties on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pen_label.GetLabelText())
        current_value -= 1
        if current_value <= 0:
            current_value = 0
        self.c1_pen_label.SetLabelText("{}".format(current_value))

    def on_c1_add_a_clicked(self, event):
        """
        Add 1 to competitor 1 advantages on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_adv_label.GetLabelText())
        current_value += 1
        self.c1_adv_label.SetLabelText("{}".format(current_value))

    def on_c1_add_p_clicked(self, event):
        """
        Add 1 to competitor 1 penalties on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c1_pen_label.GetLabelText())
        current_value += 1
        self.c1_pen_label.SetLabelText("{}".format(current_value))

    # ----------------------------------------
    # COMPETITOR 2
    # ----------------------------------------

    def on_c2_add_a_clicked(self, event):
        """
        Add 1 to competitor 2 advantages on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_adv_label.GetLabelText())
        current_value += 1
        self.c2_adv_label.SetLabelText("{}".format(current_value))

    def on_c2_add_p_clicked(self, event):
        """
        Add 1 to competitor 2 penalties on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pen_label.GetLabelText())
        current_value += 1
        self.c2_pen_label.SetLabelText("{}".format(current_value))

    def on_c2_add_2_clicked(self, event):
        """
        Adds 2 to competitor 2 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pts_label.GetLabelText())
        current_value += 2
        self.c2_pts_label.SetLabelText("{}".format(current_value))

    def on_c2_add_3_clicked(self, event):
        """
        Adds 3 to competitor 2 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pts_label.GetLabelText())
        current_value += 3
        self.c2_pts_label.SetLabelText("{}".format(current_value))

    def on_c2_add_4_clicked(self, event):
        """
        Adds 4 to competitor 2 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pts_label.GetLabelText())
        current_value += 4
        self.c2_pts_label.SetLabelText("{}".format(current_value))

    def on_c2_del_2_clicked(self, event):
        """
        Subtract 2 from competitor 2 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pts_label.GetLabelText())
        current_value -= 2
        if current_value <= 0:
            current_value = 0
        self.c2_pts_label.SetLabelText("{}".format(current_value))

    def on_c2_del_3_clicked(self, event):
        """
        Subtract 3 from competitor 2 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pts_label.GetLabelText())
        current_value -= 3
        if current_value <= 0:
            current_value = 0
        self.c2_pts_label.SetLabelText("{}".format(current_value))

    def on_c2_del_4_clicked(self, event):
        """
        Substracts 4 from competitor 2 total score on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pts_label.GetLabelText())
        current_value -= 4
        if current_value <= 0:
            current_value = 0
        self.c2_pts_label.SetLabelText("{}".format(current_value))

    def on_c2_del_a_clicked(self, event):
        """
        Substracts 1 from competitor 2 advantages on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_adv_label.GetLabelText())
        current_value -= 1
        if current_value <= 0:
            current_value = 0
        self.c2_adv_label.SetLabelText("{}".format(current_value))

    def on_c2_del_p_clicked(self, event):
        """
        Substracts 1 from competitor 2 penalties on both windows.

        :param self wx.Frame: default: current instance.
        :param event wx.Event: default: given automatically by event caller.
        """
        current_value = int(self.c2_pen_label.GetLabelText())
        current_value -= 1
        if current_value <= 0:
            current_value = 0
        self.c2_pen_label.SetLabelText("{}".format(current_value))
