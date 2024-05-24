import tkinter as tk
from tkinter import ttk
import win32print

class Working_conditions_notice:
    
    def __init__(self,notebook):
        self.notebook = notebook
        self.setup_tab ()
    
    def setup_tab(self):

        # タブの作成
        tab4 = ttk.Frame(self.notebook)
        self.notebook.add(tab4, text='各種設定')
        self.setting_frame = self.setting_tab_frame(tab4)
        self.staff_search_tab(self.setting_frame)

    def setting_tab_frame(self, tab4):
        sett_frame = ttk.Frame(tab4)
        sett_frame.pack(fill='both', expand=True)  # フレームをパック
        return sett_frame

    def staff_search_tab(self, main):
        frame = ttk.Frame(main)
        

        printers = win32print.EnumPrinters(2)
        printer_list = [printer[2] for printer in printers]

        frame.pack()
        style_list = {
            "L":"LabelStyle.TLabel",
            "E":("Arial", 18),
            "S":"read_only",
            "U":"UnderStyle.TLabel",
            "B":"ButtonStyle.TButton",
            "T":"Treeview",
            "TV":"Treeview.Heading",
            "F":('HGP教科書体', 16),
        }
        def set_all():
            printer_set()
            setting_update()
        
        def printer_set():
            from data.SQL_center import setting_select
            printer_select = setting_select(1)
            printer_name = printer_select.get_data()
            printer_frame = ttk.Frame(frame)
            printer_frame.pack()
            label = ttk.Label(printer_frame,text="プリンター指定:",style=style_list["L"])
            label.pack(side=tk.LEFT)
            
            self.printer_set_C = ttk.Combobox(printer_frame,values=printer_list,width=20,font=style_list["E"],state=style_list["S"])
            self.printer_set_C.pack(side=tk.LEFT)
            self.printer_set_C.insert(tk.END,printer_name)
        
        def setting_update():
            
            Button = ttk.Button(frame,text="更新",style=style_list["B"],command=printer_get)
            Button.pack()
        
        def printer_get(event=None):
            from data.SQL_center import setting_update
            setting_update(self.printer_set_C.get(),1)
        
        def get(self):
            return self.printer_set_C.get()
            
        
        set_all()
        