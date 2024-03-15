import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from ..GUI_Logic.format_change import FormatConvert



class ToolTip(object):
    def __init__(self, widget, text='ToolTip'):
        self.waittime = 200     # ミリ秒
        self.wraplength = 180   # ピクセル
        self.widget = widget
        self.text = text
        self.widget.bind("<FocusIn>",self.enter)
        self.widget.bind("<FocusOut>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        FormatConvert(self.widget)

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 30
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         wraplength = self.wraplength,
                         font=12)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()