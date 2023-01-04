# -*- coding: utf-8 -*-#
#
# generated by wxGlade 1.0.4 on Wed Jan  4 12:45:03 2023
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame")

        self.panel_main = wx.Panel(self, wx.ID_ANY)

        sizer_main = wx.BoxSizer(wx.HORIZONTAL)

        sizer_left = wx.BoxSizer(wx.VERTICAL)
        sizer_main.Add(sizer_left, 1, wx.ALL | wx.EXPAND, 3)

        self.list_box_left = wx.ListBox(self.panel_main, wx.ID_ANY, choices=[])
        sizer_left.Add(self.list_box_left, 5, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.TOP, 3)

        sizer_left_add = wx.BoxSizer(wx.HORIZONTAL)
        sizer_left.Add(sizer_left_add, 0, wx.ALL, 1)

        label_add = wx.StaticText(self.panel_main, wx.ID_ANY, u"\u8ffd\u52a0")
        sizer_left_add.Add(label_add, 0, wx.ALL, 4)

        self.text_ctrl_add = wx.TextCtrl(self.panel_main, wx.ID_ANY, "")
        sizer_left_add.Add(self.text_ctrl_add, 1, 0, 0)

        self.button_add = wx.Button(self.panel_main, wx.ID_ANY, "ADD")
        sizer_left.Add(self.button_add, 1, wx.ALL | wx.EXPAND, 0)

        self.button_move = wx.Button(self.panel_main, wx.ID_ANY, u"\u25b6\u25b6")
        sizer_main.Add(self.button_move, 0, wx.ALL | wx.EXPAND, 5)

        self.list_box_right = wx.ListBox(self.panel_main, wx.ID_ANY, choices=[])
        sizer_main.Add(self.list_box_right, 1, wx.ALL | wx.EXPAND, 5)

        self.panel_main.SetSizer(sizer_main)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.on_add, self.button_add)
        self.Bind(wx.EVT_BUTTON, self.on_move, self.button_move)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.on_dclick, self.list_box_right)
        # end wxGlade

    def on_add(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_add' not implemented!")
        event.Skip()

    def on_move(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_move' not implemented!")
        event.Skip()

    def on_dclick(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_dclick' not implemented!")
        event.Skip()

# end of class MyFrame
