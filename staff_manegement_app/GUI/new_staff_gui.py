import tkinter as tk
from tkinter import ttk
from ..GUI_Logic.tooltip_day import ToolTip
from ..GUI_Logic.text_box_RE import Open_text_box
from ..GUI_Logic.Logic_etc import Allowance_change





# 新規スタッフ入力タブを作成する関数
def new_staff_tab(notebook,amount_label):
    #def __init__(self):
        
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

        #padx=4 横幅
        #pady=4　縦幅

        # ラベルの作成と配置
        
        top_blank = ttk.Label(frame,text=" ")
        top_blank.grid(row=0,column=0,columnspan=10)


        def kana_area():
        
            kana_label = ttk.Label(frame, text="フリガナ:", style="LabelStyle.TLabel")
            kana_label.grid(row=2,column=1)
        
            kana1_entry = ttk.Entry(frame,width=20, font=("Arial",18))
            kana1_entry.grid(row=2,column=3,columnspan=2)
            
            kana2_entry = ttk.Entry(frame,width=20, font=("Arial",18))
            kana2_entry.grid(row=2,column=6,columnspan=2)
        
        
        def sepa():
            kana_C_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_C_sepa.grid(row=1, column=5, rowspan=5, sticky="ns",padx=4)
            
            kana_R_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_R_sepa.grid(row=1, column=8, rowspan=20, sticky="ns",padx=4)
            
            kana_L_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_L_sepa.grid(row=1, column=2, rowspan=20, sticky="ns",padx=4)
            
            left_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_sepa.grid(row=1, column=0, rowspan=20, sticky="nsew",padx=4)
            
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
            



        
        
        def name_area():
            name_label = ttk.Label(frame,text="氏名:", style="LabelStyle.TLabel")
            name_label.grid(row=4,column=1)
            
            f_name_entry = ttk.Entry(frame,width=20, font=("Arial",18))
            f_name_entry.grid(row=4,column=3,columnspan=2)
            
            kana2_entry = ttk.Entry(frame,width=20, font=("Arial",18))
            kana2_entry.grid(row=4,column=6,columnspan=2)
        
        
        def sex_choice():
            
            sex_list = []#仮設定
            
            sex_label = ttk.Label(frame,text="性別:", style="LabelStyle.TLabel")
            sex_label.grid(row=2,column=9)
            
            sex_combobox = ttk.Combobox(frame,values=sex_list,width=10,font=("Arial",18))
            sex_combobox.grid(row=2,column=11)
        
        
        def birthday():
            birthday_label = ttk.Label(frame,text="生年月日:", style="LabelStyle.TLabel")
            birthday_label.grid(row=4,column=9)
            
            birthday_entry = ttk.Entry(frame,width=12,font=("Arial",18))
            birthday_entry.grid(row=4,column=11)
            
            ToolTip(birthday_entry, text="yyyy/mm/ddで入力")

        
        def cell_phone_area():
            
            phone_entry_frame = ttk.Frame(frame)
            phone_entry_frame.grid(row=8,column=3,columnspan=5)
            
            cell_phone_label = ttk.Label(frame,text="携帯電話:", style="LabelStyle.TLabel")
            cell_phone_label.grid(row=8,column=1)
            
            phone_area_code = ttk.Entry(phone_entry_frame,width=10,font=("Arial",18))
            phone_area_code.grid(row=0,column=0)
            
            phone_hyphen_1 = ttk.Label(phone_entry_frame, text="-", style="LabelStyle.TLabel")
            phone_hyphen_1.grid(row=0,column=1)
            
            phone_city_code = ttk.Entry(phone_entry_frame,width=10,font=("Arial",18))
            phone_city_code.grid(row=0,column=2)
            
            phone_hyphen_2 = ttk.Label(phone_entry_frame, text="-", style="LabelStyle.TLabel")
            phone_hyphen_2.grid(row=0,column=3)
            
            phone_subscriber_number = ttk.Entry(phone_entry_frame,width=10,font=("Arial",18))
            phone_subscriber_number.grid(row=0,column=4)
       
            
        def tell_area():
            tell_entry_frame = ttk.Frame(frame)
            tell_entry_frame.grid(row=10,column=3,columnspan=5)
            
            cell_tell_label = ttk.Label(frame,text="固定電話:", style="LabelStyle.TLabel")
            cell_tell_label.grid(row=10,column=1)
            
            tell_area_code = ttk.Entry(tell_entry_frame,width=10,font=("Arial",18))
            tell_area_code.grid(row=0,column=0)
            
            tell_hyphen_1 = ttk.Label(tell_entry_frame, text="-", style="LabelStyle.TLabel")
            tell_hyphen_1.grid(row=0,column=1)
            
            tell_city_code = ttk.Entry(tell_entry_frame,width=10,font=("Arial",18))
            tell_city_code.grid(row=0,column=2)
            
            tell_hyphen_2 = ttk.Label(tell_entry_frame, text="-", style="LabelStyle.TLabel")
            tell_hyphen_2.grid(row=0,column=3)
            
            tell_subscriber_number = ttk.Entry(tell_entry_frame,width=10,font=("Arial",18))
            tell_subscriber_number.grid(row=0,column=4)
            
            
        def Joining_the_company_day():
            #入社日
            label = ttk.Label(frame,text="入社日:", style="LabelStyle.TLabel")
            label.grid(row=8,column=9)
            
            Joining_entry = ttk.Entry(frame,width=12,font=("Arial",18))
            Joining_entry.grid(row=8,column=11)
            
            ToolTip(Joining_entry, text="yyyy/mm/ddで入力")
            
        
        def remarks_area():
            label = ttk.Label(frame,text="備考:", style="LabelStyle.TLabel")
            label.grid(row=10,column=9)
            
            remarks_entry = ttk.Entry(frame,width=12,font=("Arial",18))
            remarks_entry.grid(row=10,column=11)
            
            Open_text_box(remarks_entry)
        
        
        def address_kana_area():
            label = ttk.Label(frame,text="フリガナ:", style="LabelStyle.TLabel")
            label.grid(row=14,column=1)
            
            address_kana_entry = ttk.Entry(frame,width=40,font=("Arial",18))
            address_kana_entry.grid(row=14,column=3,columnspan=5)
            
            
        def address_area():
            label = ttk.Label(frame,text="住所:", style="LabelStyle.TLabel")
            label.grid(row=16,column=1)
            
            address_entry = ttk.Entry(frame,width=40,font=("Arial",18))
            address_entry.grid(row=16,column=3,columnspan=5)
            
        
        def post_number_area():
            label = ttk.Label(frame,text="郵便番号:", style="LabelStyle.TLabel")
            label.grid(row=18,column=1)
            
            number_frame = ttk.Frame(frame)
            number_frame.grid(row=18,column=3,columnspan=3)
            
            Postal_district_number = ttk.Entry(number_frame,width=8,font=("Arial",18))
            Postal_district_number.grid(row=0,column=0)
            
            post_hyphen_1 = ttk.Label(number_frame, text="-", style="LabelStyle.TLabel")
            post_hyphen_1.grid(row=0,column=1)
            
            Town_area_number = ttk.Entry(number_frame,width=10,font=("Arial",18))
            Town_area_number.grid(row=0,column=2)
            
            
        def dependent_area():
            label = ttk.Label(frame,text="扶養:", style="LabelStyle.TLabel")
            label.grid(row=14,column=9)
            
            dependent_entry = ttk.Entry(frame,width=12,font=("Arial",18))
            dependent_entry.grid(row=14,column=11)
            
            Open_text_box(dependent_entry)
            
        
        def dependent_people_area():
            label = ttk.Label(frame,text="人数:", style="LabelStyle.TLabel")
            label.grid(row=16,column=9)
            
            dependent_people_entry = ttk.Entry(frame,width=12,font=("Arial",18))
            dependent_people_entry.grid(row=16,column=11)
            
        
        def Means_of_commuting():
            label = ttk.Label(frame,text="通勤手段:", style="LabelStyle.TLabel")
            label.grid(row=18,column=9)
            
            Means_entry = ttk.Entry(frame,width=12,font=("Arial",18))
            Means_entry.grid(row=18,column=11)
        
        
        def Means_amount():
            
            label = ttk.Label(frame,textvariable=amount_label, style="LabelStyle.TLabel")
            label.grid(row=20,column=9)
            
            Means_entry = ttk.Entry(frame,width=12,font=("Arial",18))
            Means_entry.grid(row=20,column=11)
            
            
        
        
        def Employment_status():#仮設置 後ほど場所移動
            
            emp_list = ["正社員","パート","継続パート","継続正社員","短時間"]
            
            label = ttk.Label(frame,text="雇用形態", style="LabelStyle.TLabel")
            label.grid(row=22,column=9)
            
            emp_entry = ttk.Combobox(frame,width=12,values=emp_list,font=("Arial",18))
            emp_entry.grid(row=22,column=11)
            emp_entry.set("正社員")
            
            Allowance_change(emp_entry,amount_label)
            
            #emp_entry.bind('<<ComboboxSelected>>',)
            
            
            

            
            
        
        
        
        
        
        
        
        
        Employment_status()#仮
        
        sepa()
        kana_area()#名前のカナ入力エリア
        name_area()#名前入力エリア
        sex_choice()#性別選択
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
        
        
        
        

    # スタッフ詳細入力ウィジェットをフレームに追加
    new_staff_detail(staff_input_frame)
