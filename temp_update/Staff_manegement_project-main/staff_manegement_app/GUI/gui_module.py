import tkinter as tk
from tkinter import ttk
from GUI.new_staff_gui import StaffDetailTab
from GUI.staff_search_gui import Staff_Search_Tab
from GUI.rank_gui import rank_list_map
from data.SQL_center import Rank_List_Manager
import threading

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
        
        #threading.Thread(target=self.initialize).start()
        self.initialize()
        self.main_widgets()

    def initialize(self):
        self.rank_number_list = self.get_rank_number_list()
        self.setup_new_staff_tab()
        self.set_up_staff_search_tab()
        self.setup_rank_list_tab()
        self.setup_setting_tab()

    def get_rank_number_list(self):
        
        self.rank_list_store = Rank_List_Manager()
        return self.rank_list_store.rank_number_list_store_get()

    def setup_new_staff_tab(self):
        # StaffDetailTab のインスタンスを正しく設定します。
        self.new_staff_tab = StaffDetailTab(self.notebook, self.amount_label, self.rank_number_list)
        
    def setup_rank_list_tab(self):
        self.rank_list_tab = rank_list_map(self.notebook)
    
    def set_up_staff_search_tab(self):
        self.staff_search_tab = Staff_Search_Tab(self.notebook)
    
    def setup_setting_tab(self):
        from GUI.setting import Working_conditions_notice
        self.setting_tab = Working_conditions_notice(self.notebook)
    
    
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
        style.configure("Treeview", font=('HGP教科書体', 16))
        style.configure("Treeview.Heading", font=('HGP教科書体', 16, 'bold'))
        style.configure('Green.TButton', font=('HGP教科書体', 20),background='springgreen')
        style.configure('Red.TButton', font=('HGP教科書体', 20),background='white')

        
        #notebook = ttk.Notebook(self.master,style="TabStyle.TNotebook")
        self.notebook.pack(fill='both', expand=True)
        
        self.rank_manager = Rank_List_Manager()
        self.rank_number_list = self.rank_manager.rank_number_list_store_get()