import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from ..GUI_Logic.format_change import FormatConvert,FormatConvert_tell,FormatConvert_Post



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


class ToolTip_time(object):
    def __init__(self, widget, text='ToolTip_time'):
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
        #FormatConvert(self.widget)

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

class ToolTip_error(object):
    def __init__(self, widget, title):
        self.waittime = 200     # ミリ秒
        self.wraplength = 180   # ピクセル
        self.widget = widget
        self.title = title
        self.widget.bind("<FocusOut>", self.try_convert)
        self.id = None
        self.tw = None
        
    def try_convert(self,event=None):
        
        if self.title == "携帯電話:":
            if len(self.widget.get()) > 0:
                len_num = 11
                self.converting(len_num)
            else:
                return
        else:
            if len(self.widget.get()) > 0:
                len_num = 10
                self.converting(len_num)
            else:
                return
    
    def converting(self,len_num):
          
        self.caveat_text = f"{self.title}はハイフン無しで{len_num}桁で入力してください"
        tell = self.widget.get()
        
        try:
            tell_num = tell.replace("-","")
        except:
            tell_num = tell

        if len(tell_num) == len_num:
            FormatConvert_tell(self.widget,self.title,len_num,tell_num)
            self.leave()
        else:
            self.leave()
            self.enter()
            


    def enter(self, event=None):
        self.schedule()
        
        

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        

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
        label = tk.Label(self.tw, text=self.caveat_text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         wraplength = self.wraplength,
                         font=12)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()



class ToolTip_error_Post(object):
    def __init__(self, widget,title,widget_2,widget_3):
        self.waittime = 200     # ミリ秒
        self.wraplength = 180   # ピクセル
        self.widget = widget
        self.widget_address = widget_2
        self.widget_address_kana = widget_3
        self.title = title
        self.widget.bind("<FocusOut>", self.try_convert)
        self.id = None
        self.tw = None
        
    def try_convert(self,event=None):
        if len(self.widget.get()) > 0:
            len_num = 7
            self.converting(len_num)
        else:
            return

    
    def converting(self,len_num):
          
        self.caveat_text = f"{self.title}はハイフン無しで{len_num}桁で入力してください"
        post = self.widget.get()
        try:
            post_num = post.replace("-","")
        except:
            post_num = post
        


        if len(post_num) == len_num:
            FormatConvert_Post(self.widget,post_num,len_num,self.widget_address,self.widget_address_kana)
            self.leave()
        else:
            self.leave()
            self.enter()
            


    def enter(self, event=None):
        self.schedule()
        
        

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        

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
        label = tk.Label(self.tw, text=self.caveat_text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         wraplength = self.wraplength,
                         font=12)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()



