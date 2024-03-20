import tkinter as tk
from tkinter import ttk
from ..GUI_Logic.tooltip_day import ToolTip
from ..GUI_Logic.text_box_RE import Open_text_box
from ..GUI_Logic.Logic_etc import Allowance_change
from staff_manegement_app.GUI.load_config import load_GUI_file
from staff_manegement_app.GUI.load_config import load_List_file








# 新規スタッフ入力タブを作成する関数
def new_staff_tab(notebook,amount_label):
    GUI_lists = load_GUI_file()
    select_lists = load_List_file()

        
    style = ttk.Style()
    style.configure("EntryStyle.TEntry", font=("Arial",18))
    
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text='新規スタッフ入力')
    # スクロール機能を持つフレームの設定
    def scroll_def(): 
        # スクロールバーの設定
        tab1_scrollbar = ttk.Scrollbar(tab1, orient='vertical')
        tab1_scrollbar.pack(side='right', fill='y')

        # スクロール可能なキャンバスの作成
        canvas = tk.Canvas(tab1, yscrollcommand=tab1_scrollbar.set)
        canvas.pack(side='top', fill='both', expand=True)

        # スクロールバーとキャンバスの連動設定
        tab1_scrollbar.configure(command=canvas.yview)

        # キャンバス上に配置するウィジェット用のフレーム
        staff_input_frame = ttk.Frame(canvas)
        staff_input_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"), width=canvas.winfo_width(), height=canvas.winfo_height()))
        canvas.create_window((0, 0), window=staff_input_frame, anchor='nw')
        
        return staff_input_frame  # スクロール可能フレームを返す

    # スクロール可能フレームを作成
    staff_input_frame = scroll_def()
    

    
    # スタッフ詳細入力ウィジェットの設定
    def new_staff_detail(frame):
        style_list = {
            "L":"LabelStyle.TLabel",
            "E":("Arial",18),
            "S":"read_only"
        }

        #padx=4 横幅
        #pady=4　縦幅

        # ラベルの作成と配置
        
        top_blank = ttk.Label(frame,text=" ")
        top_blank.grid(row=0,column=0,columnspan=10)


        def kana_area():
        
            kana_label = ttk.Label(frame, text=GUI_lists['kana_name'], style=style_list["L"])
            kana_label.grid(row=2,column=1)
        
            kana1_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            kana1_entry.grid(row=2,column=3,columnspan=2)
            
            kana2_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            kana2_entry.grid(row=2,column=6,columnspan=2)
        
        
        def sepa():
            kana_C_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_C_sepa.grid(row=1, column=5, rowspan=5, sticky="ns",padx=4)
            
            kana_R_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_R_sepa.grid(row=1, column=8, rowspan=40, sticky="ns",padx=4)
            
            kana_L_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_L_sepa.grid(row=1, column=2, rowspan=40, sticky="ns",padx=4)
            
            left_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_sepa.grid(row=1, column=0, rowspan=40, sticky="nsew",padx=4)
            
            top_sepa = ttk.Separator(frame,orient="horizontal")#水平
            top_sepa.grid(row=1, column=0, columnspan=13,sticky="sew",pady=4)
            
            kana_sepa = ttk.Separator(frame,orient="horizontal")#水平
            kana_sepa.grid(row=3, column=0, columnspan=13,sticky="ew",pady=4)
            
            right_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_sepa.grid(row=1, column=13, rowspan=20, sticky="nsew",padx=4)
            
            left_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_2_sepa.grid(row=7, column=0, rowspan=5, sticky="nsew",padx=4)
            
            top_2_sepa = ttk.Separator(frame,orient="horizontal")#水平
            top_2_sepa.grid(row=7, column=0, columnspan=13,sticky="sew",pady=4)
            
            right_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_2_sepa.grid(row=7, column=13, rowspan=5, sticky="nsew",padx=4)
            
            phone_sepa = ttk.Separator(frame,orient="horizontal")#水平
            phone_sepa.grid(row=9, column=0, columnspan=13,sticky="sew",pady=4)
            
            left_p_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_p_sepa.grid(row=7, column=2, rowspan=5, sticky="nsew",padx=4)
            
            right_p_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_p_sepa.grid(row=7, column=8, rowspan=5, sticky="nsew",padx=4)
            
            tell_sepa = ttk.Separator(frame,orient="horizontal")#水平
            tell_sepa.grid(row=11, column=0, columnspan=13,sticky="sew",pady=4)
            
            name_sepa = ttk.Separator(frame,orient="horizontal")#水平
            name_sepa.grid(row=5, column=0, columnspan=13,sticky="ew",pady=4)
            
            address_top = ttk.Separator(frame,orient="horizontal")#水平
            address_top.grid(row=13, column=0, columnspan=13,sticky="sew",pady=4)
            
            address_center = ttk.Separator(frame,orient="horizontal")#水平
            address_center.grid(row=15, column=0, columnspan=13,sticky="sew",pady=4)
            
            address_center_2 = ttk.Separator(frame,orient="horizontal")#水平
            address_center_2.grid(row=17, column=0, columnspan=13,sticky="sew",pady=4)
            
            address_bottom = ttk.Separator(frame,orient="horizontal")#水平
            address_bottom.grid(row=19, column=0, columnspan=13,sticky="sew",pady=4)
            
            Means_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Means_sepa.grid(row=21, column=8, columnspan=13,sticky="sew",pady=4)
            
            Underwriter_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Underwriter_sepa.grid(row=21, column=0, columnspan=3,sticky="sew",pady=4)



        
        
        def name_area():
            name_label = ttk.Label(frame,text=GUI_lists["name"], style=style_list["L"])
            name_label.grid(row=4,column=1)
            
            f_name_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            f_name_entry.grid(row=4,column=3,columnspan=2)
            
            kana2_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            kana2_entry.grid(row=4,column=6,columnspan=2)
        
        
        def gender_choice():
            
            gender_label = ttk.Label(frame,text=GUI_lists["gender"], style=style_list["L"])
            gender_label.grid(row=2,column=9)
            
            gender_combobox = ttk.Combobox(frame,values=select_lists['gender'],width=10,font=style_list["E"],state=style_list["S"])
            gender_combobox.grid(row=2,column=11)
        
        
        def birthday():
            birthday_label = ttk.Label(frame,text=GUI_lists["birthday"], style=style_list["L"])
            birthday_label.grid(row=4,column=9)
            
            birthday_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            birthday_entry.grid(row=4,column=11)
            
            ToolTip(birthday_entry, text="yyyy/mm/ddで入力")

        
        def cell_phone_area():
            
            phone_entry_frame = ttk.Frame(frame)
            phone_entry_frame.grid(row=8,column=3,columnspan=5)
            
            cell_phone_label = ttk.Label(frame,text=GUI_lists["phone"], style=style_list["L"])
            cell_phone_label.grid(row=8,column=1)
            
            phone_area_code = ttk.Entry(phone_entry_frame,width=10,font=style_list["E"])
            phone_area_code.grid(row=0,column=0)
            
            phone_hyphen_1 = ttk.Label(phone_entry_frame, text=GUI_lists["hyphen"], style=style_list["L"])
            phone_hyphen_1.grid(row=0,column=1)
            
            phone_city_code = ttk.Entry(phone_entry_frame,width=10,font=style_list["E"])
            phone_city_code.grid(row=0,column=2)
            
            phone_hyphen_2 = ttk.Label(phone_entry_frame, text=GUI_lists["hyphen"], style=style_list["L"])
            phone_hyphen_2.grid(row=0,column=3)
            
            phone_subscriber_number = ttk.Entry(phone_entry_frame,width=10,font=style_list["E"])
            phone_subscriber_number.grid(row=0,column=4)
       
            
        def tell_area():
            tell_entry_frame = ttk.Frame(frame)
            tell_entry_frame.grid(row=10,column=3,columnspan=5)
            
            cell_tell_label = ttk.Label(frame,text=GUI_lists["tell"], style=style_list["L"])
            cell_tell_label.grid(row=10,column=1)
            
            tell_area_code = ttk.Entry(tell_entry_frame,width=10,font=style_list["E"])
            tell_area_code.grid(row=0,column=0)
            
            tell_hyphen_1 = ttk.Label(tell_entry_frame, text=GUI_lists["hyphen"], style=style_list["L"])
            tell_hyphen_1.grid(row=0,column=1)
            
            tell_city_code = ttk.Entry(tell_entry_frame,width=10,font=style_list["E"])
            tell_city_code.grid(row=0,column=2)
            
            tell_hyphen_2 = ttk.Label(tell_entry_frame, text=GUI_lists["hyphen"], style=style_list["L"])
            tell_hyphen_2.grid(row=0,column=3)
            
            tell_subscriber_number = ttk.Entry(tell_entry_frame,width=10,font=style_list["E"])
            tell_subscriber_number.grid(row=0,column=4)
            
            
        def Joining_the_company_day():
            #入社日
            label = ttk.Label(frame,text=GUI_lists["Joining"], style=style_list["L"])
            label.grid(row=8,column=9)
            
            Joining_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            Joining_entry.grid(row=8,column=11)
            
            ToolTip(Joining_entry, text="yyyy/mm/ddで入力")
            
        
        def remarks_area():
            label = ttk.Label(frame,text=GUI_lists["main_remarks"], style=style_list["L"])
            label.grid(row=10,column=9)
            
            remarks_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            remarks_entry.grid(row=10,column=11)
            
            Open_text_box(remarks_entry)
        
        
        def address_kana_area():
            label = ttk.Label(frame,text=GUI_lists["kana_name"], style=style_list["L"])
            label.grid(row=14,column=1)
            
            address_kana_entry = ttk.Entry(frame,width=40,font=style_list["E"])
            address_kana_entry.grid(row=14,column=3,columnspan=5)
            
            
        def address_area():
            label = ttk.Label(frame,text=GUI_lists["address"], style=style_list["L"])
            label.grid(row=16,column=1)
            
            address_entry = ttk.Entry(frame,width=40,font=style_list["E"])
            address_entry.grid(row=16,column=3,columnspan=5)
            
        
        def post_number_area():
            label = ttk.Label(frame,text=GUI_lists["post"], style=style_list["L"])
            label.grid(row=18,column=1)
            
            number_frame = ttk.Frame(frame)
            number_frame.grid(row=18,column=3,columnspan=3)
            
            Postal_district_number = ttk.Entry(number_frame,width=8,font=style_list["E"])
            Postal_district_number.grid(row=0,column=0)
            
            post_hyphen_1 = ttk.Label(number_frame, text=GUI_lists["hyphen"], style=style_list["L"])
            post_hyphen_1.grid(row=0,column=1)
            
            Town_area_number = ttk.Entry(number_frame,width=10,font=style_list["E"])
            Town_area_number.grid(row=0,column=2)
            
            
        def dependent_area():
            label = ttk.Label(frame,text=GUI_lists["dependent"], style=style_list["L"])
            label.grid(row=14,column=9)
            
            dependent_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            dependent_entry.grid(row=14,column=11)
            
            Open_text_box(dependent_entry)
            
        
        def dependent_people_area():
            label = ttk.Label(frame,text=GUI_lists["people"], style=style_list["L"])
            label.grid(row=16,column=9)
            
            dependent_people_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            dependent_people_entry.grid(row=16,column=11)
            
        
        def Means_of_commuting():
            label = ttk.Label(frame,text=GUI_lists["means"], style=style_list["L"])
            label.grid(row=18,column=9)
            
            Means_combobox = ttk.Combobox(frame,width=10,values=select_lists['means'],font=style_list["E"])
            Means_combobox.grid(row=18,column=11)
        
        
        def Means_amount():
            
            label = ttk.Label(frame,textvariable=amount_label, style=style_list["L"])
            label.grid(row=20,column=9)
            
            Means_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            Means_entry.grid(row=20,column=11)
            
        
        def Underwriter_1():
            main_label = ttk.Label(frame,text=f'{GUI_lists["under"]}➀', style=style_list["L"])#➁2人目用
            main_label.grid(row=22,column=1)           
            
            
            
            
            
        
        
        def Employment_status():#仮設置 後ほど場所移動
            
            label = ttk.Label(frame,text=GUI_lists["emp_type"], style=style_list["L"])
            label.grid(row=32,column=9)
            
            emp_entry = ttk.Combobox(frame,width=10,values=select_lists['emp_type'],font=style_list["E"],state=style_list["S"])
            emp_entry.grid(row=32,column=11)
            emp_entry.set(select_lists['emp_type'][0])
            
            Allowance_change(emp_entry,amount_label)
            
            #emp_entry.bind('<<ComboboxSelected>>',)
            
            
            

            
            
        
        
        
        
        
        
        
        
        Employment_status()#仮
        
        sepa()
        kana_area()#名前のカナ入力エリア
        name_area()#名前入力エリア
        gender_choice()#性別選択
        birthday()#生年月日入力
        cell_phone_area()#携帯電話番号入力
        tell_area()#固定電話入力
        Joining_the_company_day()#入社日入力
        remarks_area()#備考入力
        address_kana_area()#住所フリガナ入力
        address_area()#住所入力
        post_number_area()#郵便番号入力
        dependent_area()#扶養入力
        dependent_people_area()#扶養の人数入力
        Means_of_commuting()#通勤手段
        Means_amount()#通勤手当
        Underwriter_1()
        
        
        
        

    # スタッフ詳細入力ウィジェットをフレームに追加
    new_staff_detail(staff_input_frame)
