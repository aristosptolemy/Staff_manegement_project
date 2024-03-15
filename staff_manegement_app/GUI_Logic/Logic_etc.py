import tkinter as tk
from tkinter import ttk

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
        