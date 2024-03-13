import tkinter as tk
from tkinter import ttk



# 新規スタッフ入力タブを作成する関数
def new_staff_tab(notebook):
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
        
        
        def sepa_1():
            kana_C_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_C_sepa.grid(row=1, column=5, rowspan=5, sticky="ns",padx=4)
            
            kana_R_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_R_sepa.grid(row=1, column=8, rowspan=5, sticky="ns",padx=4)
            
            left_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_sepa.grid(row=1, column=0, rowspan=7, sticky="nsew",padx=4)
            
            top_sepa = ttk.Separator(frame,orient="horizontal")#水平
            top_sepa.grid(row=1, column=0, columnspan=13,sticky="sew",pady=4)
            
            kana_sepa = ttk.Separator(frame,orient="horizontal")#水平
            kana_sepa.grid(row=3, column=0, columnspan=13,sticky="ew",pady=4)
            
            right_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_sepa.grid(row=1, column=13, rowspan=7, sticky="nsew",padx=4)
        
        
        def name_area():
            name_label = ttk.Label(frame,text="氏名:", style="LabelStyle.TLabel")
            name_label.grid(row=4,column=1)
            
            f_name_entry = ttk.Entry(frame,width=20, font=("Arial",18))
            f_name_entry.grid(row=4,column=3,columnspan=2)
            
            kana2_entry = ttk.Entry(frame,width=20, font=("Arial",18))
            kana2_entry.grid(row=4,column=6,columnspan=2)
        
        
        def sepa_2():
            name_sepa = ttk.Separator(frame,orient="horizontal")#水平
            name_sepa.grid(row=5, column=0, columnspan=13,sticky="ew",pady=4)
        
        
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
        
        
        
        kana_area()
        sepa_1()
        name_area()
        sepa_2()
        sex_choice()
        birthday()
        
        

    # スタッフ詳細入力ウィジェットをフレームに追加
    new_staff_detail(staff_input_frame)
