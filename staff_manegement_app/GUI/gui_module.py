import tkinter as tk
from tkinter import ttk
from .new_staff_gui import new_staff_tab
from .staff_search_gui import staff_search_tab

class Apps(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("スタッフ管理")
        self.master.geometry("1020x700")
        self.amount_label = tk.StringVar()
        self.main_widgets()
    
    def main_widgets(self):
        style = ttk.Style()
        style.configure("TabStyle.TNotebook.Tab", font=("HGP教科書体", 16))
        style.configure('Custom.TButton', font=('HGP教科書体', 16))
        style.configure("LabelStyle.TLabel", font=('HGP教科書体', 20))
        style.configure("EntryStyle.TEntry", font=("Arial",18))
        style.configure('Custom.TCombobox', font=('HGP教科書体',16))
        
        notebook = ttk.Notebook(self.master,style="TabStyle.TNotebook")
        notebook.pack(fill='both', expand=True)

        new_staff_tab(notebook,self.amount_label)
        staff_search_tab(notebook)