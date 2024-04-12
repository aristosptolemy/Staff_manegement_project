import tkinter as tk
from tkinter import ttk
from staff_manegement_app.data.SQL_center import Rank_List_Manager
import json

class Allowance_change(object):#通勤手当自動判定
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


class Work_place_rank_change(object):
    def __init__(self, widget,variable,widget_c):
        self.widget = widget
        self.widgetc = widget_c
        self.variable = variable
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



    