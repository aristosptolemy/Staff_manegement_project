import tkinter as tk
from tkinter import ttk
import pykakasi
from staff_manegement_app.data.SQL import MySQL_Staff_Search
from staff_manegement_app.GUI.load_config import load_GUI_file
from staff_manegement_app.GUI.load_config import load_List_file

GUI_lists = load_GUI_file()
select_lists = load_List_file()

class Staff_Search_Tab:
    def __init__(self, notebook):
        self.notebook = notebook
        self.setup_tab()

    def setup_tab(self):

        # タブの作成
        tab2 = ttk.Frame(self.notebook)
        self.notebook.add(tab2, text='スタッフ検索')
        self.staff_search_frame = self.search_detail_frame(tab2)
        self.staff_search_tab(self.staff_search_frame)

    def search_detail_frame(self, tab2):
        staff_search_frame = ttk.Frame(tab2)
        staff_search_frame.pack(fill='both', expand=True)  # フレームをパック
        return staff_search_frame

    def staff_search_tab(self, main):
        frame = ttk.Frame(main)
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
        
        def sepa():
            row_max = 13

            top_sepa = ttk.Separator(frame, orient="horizontal")  # 水平
            top_sepa.grid(row=0, column=0, columnspan=13, sticky="ew", pady=4)

            left_sepa = ttk.Separator(frame, orient="vertical")  # 垂直
            left_sepa.grid(row=0, column=0, rowspan=row_max, sticky="ns", padx=4)
            
            right_sepa = ttk.Separator(frame, orient="vertical")  # 垂直
            right_sepa.grid(row=0, column=8, rowspan=row_max, sticky="ns", padx=4)
            
            f4_sepa = ttk.Separator(frame, orient="vertical")  # 垂直
            f4_sepa.grid(row=0, column=4, rowspan=9, sticky="ns", padx=4)
            
            Enrollment_bottom = ttk.Separator(frame, orient="horizontal")  # 水平
            Enrollment_bottom.grid(row=2, column=0, columnspan=13, sticky="ew", pady=4)
            
            gender_top_sepa = ttk.Separator(frame, orient="horizontal")  # 水平
            gender_top_sepa.grid(row=4, column=0, columnspan=13, sticky="ew", pady=4)
            
            gender_b_sepa = ttk.Separator(frame, orient="horizontal")  # 水平
            gender_b_sepa.grid(row=6, column=0, columnspan=13, sticky="ew", pady=4)
            
            name_t_sepa = ttk.Separator(frame, orient="horizontal")  # 水平
            name_t_sepa.grid(row=8, column=0, columnspan=13, sticky="ew", pady=4)
            
            name_b_sepa = ttk.Separator(frame, orient="horizontal")  # 水平
            name_b_sepa.grid(row=10, column=0, columnspan=13, sticky="ew", pady=4)
            
            kana_b_sepa = ttk.Separator(frame, orient="horizontal")  # 水平
            kana_b_sepa.grid(row=12, column=0, columnspan=13, sticky="ew", pady=4)


        def Enrollment_status():
            label = ttk.Label(frame, text=GUI_lists["Enrollment"], style=style_list["L"])
            label.grid(row=1, column=1)
            
            self.roll_status = ttk.Combobox(frame,width=10, values=select_lists['Enrollment'],font=style_list["E"],state=style_list["S"])
            self.roll_status.grid(row=1, column=3)
            
            
        def gender_select():
            label = ttk.Label(frame, text=GUI_lists["gender"], style=style_list["L"])
            label.grid(row=5, column=1)
            
            self.gender_status = ttk.Combobox(frame,width=10, values=select_lists['gender'],font=style_list["E"],state=style_list["S"])
            self.gender_status.grid(row=5, column=3)
            
            
        def staff_name_imput():
            label = ttk.Label(frame, text=GUI_lists["name"], style=style_list["L"])
            label.grid(row=9, column=1)
            
            name_frame = ttk.Frame(frame)
            name_frame.grid(row=9, column=2,columnspan=6)
            
            self.fname_search = ttk.Entry(name_frame,width=15,font=style_list["E"])
            self.fname_search.grid(row=0,column=0)
            
            self.lname_search = ttk.Entry(name_frame,width=15,font=style_list["E"])
            self.lname_search.grid(row=0,column=1)
        
        
        def staff_name_kana_imput():
            label = ttk.Label(frame, text=GUI_lists["kana_name"], style=style_list["L"])
            label.grid(row=11, column=1)
            
            name_frame = ttk.Frame(frame)
            name_frame.grid(row=11, column=2,columnspan=6)
            
            self.fkana_search = ttk.Entry(name_frame,width=15,font=style_list["E"])
            self.fkana_search.grid(row=0,column=0)
            
            self.lkana_search = ttk.Entry(name_frame,width=15,font=style_list["E"])
            self.lkana_search.grid(row=0,column=1)
            
        
        
        def Work_place_select():
            label = ttk.Label(frame, text=GUI_lists["work_place"], style=style_list["L"])
            label.grid(row=1, column=5)
            
            self.work_place_status = ttk.Combobox(frame,width=10, values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.work_place_status.grid(row=1, column=7)
            
            
        def emp_type_select():
            label = ttk.Label(frame, text=GUI_lists["emp_type"], style=style_list["L"])
            label.grid(row=5, column=5)
            
            self.emp_type_status = ttk.Combobox(frame,width=10, values=select_lists['emp_type'],font=style_list["E"],state=style_list["S"])
            self.emp_type_status.grid(row=5, column=7)
            
        
        def search_Button():
            Search_button = ttk.Button(frame,text=GUI_lists["Search"], style=style_list["B"],command=Search_start)
            Search_button.grid(row=14,column=0,columnspan=8,pady=10)
        
        
        def Search_start():
            data = {
                "在籍状況": self.roll_status.get(),
                "スタッフ詳細": {"性別": self.gender_status.get()},
                "氏": {
                    "カナ": self.fkana_search.get(),
                    "氏": self.fname_search.get()
                },
                "名": {
                    "カナ": self.lkana_search.get(),
                    "名": self.lname_search.get()
                },
                "就業場所": self.work_place_status.get(),
                "雇用形態": self.emp_type_status.get()
            }
            
            MySQL_Staff_Search(data)
            
            
        def search_result_list():
            column_names = select_lists['search_result_columnname']
            # ここでカラム名の設定を行う
            #column_names = ['就業場所', '氏', '名', '雇用形態', '在籍状況']

            # Treeviewの作成
            result_box = ttk.Treeview(frame, columns=column_names, show="headings", style=style_list["T"])
            result_box.column('就業場所', anchor='center', width=100)
            result_box.column('氏', anchor='center', width=100)
            result_box.column('名', anchor='center', width=100)
            result_box.column('雇用形態', anchor='center', width=100)
            result_box.column('在籍状況', anchor='center', width=100)

            result_box.heading('就業場所', text='就業場所', anchor='center')
            result_box.heading('氏', text='氏', anchor='center')
            result_box.heading('名', text='名', anchor='center')
            result_box.heading('雇用形態', text='雇用形態', anchor='center')
            result_box.heading('在籍状況', text='在籍状況', anchor='center')

            result_box.grid(row=20, column=0, columnspan=8, sticky='nsew')
            
            
            
            
            
            
            

        sepa()
        Enrollment_status()
        gender_select()
        staff_name_imput()
        staff_name_kana_imput()
        Work_place_select()
        emp_type_select()
        search_Button()
        search_result_list()