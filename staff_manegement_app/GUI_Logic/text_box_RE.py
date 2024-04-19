import tkinter as tk
from tkinter import ttk



class Open_text_box(object):
    def __init__(self, widget):
        self.widget = widget
        self.widget.bind("<Button-1>",self.text_box_window)
        
        
    def text_box_window(self,event=None):
        value = self.widget.get()
        self.top = tk.Toplevel()
        self.top.title("詳細")
        self.RE_text = tk.Text(self.top, wrap="word",height=10,width=30,font=("Arial",16))
        self.RE_text.insert('end', value)
        self.RE_text.pack(expand=True, fill='both')
        self.top.wm_overrideredirect(True)
        button = ttk.Button(self.top,text="入力",command=self.closed_window)
        button.pack()


        
    
    def closed_window(self):
        remarks_str = None
        remarks_str = self.RE_text.get("1.0", "end")
        self.widget.delete(0,tk.END)
        self.widget.insert(tk.END,remarks_str)
        self.top.destroy()
        



