import tkinter as tk
from tkinter import ttk

class Allowance_change:#通勤手当自動判定
    def __init__(self, widget,variable):
        self.widget = widget
        self.variable = variable
        self.change()
        self.widget.bind('<<ComboboxSelected>>',self.change)
    
    def change(self,event=None):
        emp = self.widget.get()
        
        if emp in ["パート","継続パート"]:
            self.variable.set("手当(日):")
        else:
            self.variable.set("手当(月):")


class Work_place_rank_change:
    def __init__(self, widget,variable,widget_c):
        self.widget = widget
        self.widgetc = widget_c
        self.variable = variable
        from data.SQL_center import Rank_List_Manager
        self.rank_manager = Rank_List_Manager()
        self.change()
        self.widget.bind('<<ComboboxSelected>>',self.change)
    
    def change(self,event=None):
        Work_place = self.widget.get()
        
        
        if Work_place in ["会議室", "広島本部"]:
            out_put = self.rank_manager.rank_number_list_office_get()
        else:
            out_put = self.rank_manager.rank_number_list_store_get()
            
        
        # コンボボックスにリストをセット
        self.widgetc['values'] = out_put
        return 



class Toggle_Button_rank:
    def __init__(self,frame,table):
        self.frame = frame
        self.table = table
        self.store_on = False
        self.office_on = True
        self.Toggle_buttton_set(self.frame)
        self.toggle(self.store_button,self.office_button)
        
        
    def Toggle_buttton_set(self,frame):
        button_frame = ttk.Frame(frame)
        button_frame.pack()
        self.store_button = ttk.Button(button_frame, text="店舗担当", style="ButtonStyle.TButton", command=lambda: self.toggle(self.store_button,self.office_button))
        self.store_button.id = "rank_list"
        self.store_button.pack(side=tk.LEFT)
        
        self.office_button = ttk.Button(button_frame, text="総務担当", style="ButtonStyle.TButton", command=lambda: self.toggle(self.office_button,self.store_button))
        self.office_button.id = "office_rank_list"
        self.office_button.pack(side=tk.LEFT)
    
    
    def toggle(self,widget,widget2):
        from data.SQL_center import Rank_list_update
        
        self.store_on = not self.store_on
        self.office_on = not self.office_on

        widget.config(style="Green.TButton")
        widget2.config(style="Red.TButton")
        
        
        
        Rank_list_update(widget.id,self.table)
        
        

        #print(widget.id)
            
            