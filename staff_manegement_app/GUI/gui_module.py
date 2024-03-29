import tkinter as tk
from tkinter import ttk
from .new_staff_gui import StaffDetailTab
from .staff_search_gui import staff_search_tab
from .rank_gui import rank_list_tab
from staff_manegement_app.data.SQL import Rank_List_Manager

class Apps(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("スタッフ管理")
        self.master.geometry("1040x700")
        self.notebook = ttk.Notebook(self.master, style="TabStyle.TNotebook")
        self.amount_label = tk.StringVar()
        self.rank_number_list = []
        self.rank_number_list = self.get_rank_number_list()  # rank_number_list を取得するメソッドを呼び出す
        self.setup_new_staff_tab()  # StaffDetailTab の設定を行うメソッドを呼び出す
        self.main_widgets()

    def get_rank_number_list(self):
        self.rank_list_store = Rank_List_Manager()
        return self.rank_list_store.rank_number_list_store_get()

    def setup_new_staff_tab(self):
        # StaffDetailTab のインスタンスを正しく設定します。
        self.new_staff_tab = StaffDetailTab(self.notebook, self.amount_label, self.rank_number_list)
    
    def main_widgets(self):
        style = ttk.Style()
        #利用可能テーマ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        style.theme_use('xpnative')
        style.configure('TabStyle.TNotebook.Tab', font=("HGP教科書体", 16))
        style.configure('Custom.TButton', font=('HGP教科書体', 16))
        style.configure("LabelStyle.TLabel", font=('HGP教科書体', 20))
        style.configure("UnderStyle.TLabel", font=('HGP教科書体', 16))
        style.configure('Custom.TCombobox', font=('HGP教科書体', 16))
        style.configure('ButtonStyle.TButton', font=('HGP教科書体', 20))
        
        #notebook = ttk.Notebook(self.master,style="TabStyle.TNotebook")
        self.notebook.pack(fill='both', expand=True)
        
        self.rank_manager = Rank_List_Manager()
        self.rank_number_list = self.rank_manager.rank_number_list_store_get()
        
        #self.new_staff_tab = StaffDetailTab()
        #self.new_staff_tab(self.notebook,self.amount_label,self.rank_number_list)
        staff_search_tab(self.notebook)
        #rank_list_tab(notebook)