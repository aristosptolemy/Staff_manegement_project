import tkinter as tk
from tkinter import ttk
from datetime import datetime
from GUI_Logic.tooltip_day import ToolTip , ToolTip_time,ToolTip_error,ToolTip_error_Post





class Staff_Details_Display:
    
    def __init__(self,data,widget):
        self.data = data
        #print(data)
        self.widget = widget
        self.amount_label = tk.StringVar()
        self.setup_tab()

    def setup_tab(self):
        #print(self.data)
        
        self.details_window = tk.Toplevel()
        self.details_window.title("詳細")
        self.details_window.geometry("1020x700")
        # スクロール機能を持つフレームの設定
        self.staff_details_frame = self.setup_scrollable_frame(self.details_window)
        
        self.details_display(self.staff_details_frame)

        # スタッフ詳細入力ウィジェットの設定
        #self.setup_staff_detail_widgets(self.staff_input_frame)
        
    def setup_scrollable_frame(self,window):
        # スクロールバーの設定
        tab1_scrollbar = ttk.Scrollbar(window,orient='vertical')
        tab1_scrollbar.pack(side='right', fill='y')

        # スクロール可能なキャンバスの作成
        canvas = tk.Canvas(window,yscrollcommand=tab1_scrollbar.set)
        canvas.pack(side='top', fill='both', expand=True)

        # スクロールバーとキャンバスの連動設定
        tab1_scrollbar.configure(command=canvas.yview)

        # マウスホイールでスクロール
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")


        canvas.bind("<MouseWheel>", on_mousewheel)


        # キャンバス上に配置するウィジェット用のフレーム
        staff_details_frame = ttk.Frame(canvas)
        staff_details_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=staff_details_frame, anchor='nw')
        return staff_details_frame
    
    def details_display(self,frame):
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
        import json
        from GUI.load_config import load_GUI_file,load_List_file
        GUI_lists = load_GUI_file()
        select_lists = load_List_file()
        
        def row_set():
            self.name_row = 5
            self.kana_name_row = 3
            sepa()
            switching_button(2)
            Enrollment_detail(2)
            kana_area(4)#名前のカナ入力エリア
            name_area(6)#名前入力エリア
            
            gender_choice(4)#性別選択
            birthday(6)#生年月日入力
            
            cell_phone_area(10)#携帯電話番号入力
            tell_area(12)#固定電話入力
            
            Joining_the_company_day(10)#入社日入力
            
            remarks_area(12)#備考入力
            
            address_kana_area(18)#住所フリガナ入力
            address_area(20)#住所入力
            post_number_area(16)#郵便番号入力
            Employment_status(38)#雇用形態　先に処理
            dependent_area(16)#扶養入力
            dependent_people_area(18)#扶養の人数入力
            Means_of_commuting(20)#通勤手段
            Means_amount(22)#通勤手当
            
            
            Underwriter(24)#身元引受人
            U_number(24)
            Under_name_label(26)#身元引受人名前
            relationship_label(28)#続柄
            Under_phone_label(30)#電話番号
            Under_work(32)#勤務先
            
            #1人目入力
            Under_1_name(26)#名前
            Under_1_relationship(28)#続柄
            Under_1_phone(30)#電話番号
            Under_1_work(32)#勤務先

            #2人目入力
            Under_2_name(26)#名前
            Under_2_relationship(28)#続柄
            Under_2_phone(30)#電話番号
            Under_2_work(32)#勤務先   
            
            Work_place(36)  
            
            Job_description(40)
            Rank_status(42)
            Salary_notes(44)
            Contract_renewal(24)
            Renewal_day(26)
            
            Working_conditions(36)
            Working_start_time(38)
            Working_end_time(40)
            Working_break_time(42)
            Working_week_time(44)
            
            Overtime_or(38)
            Overtime_start(40)
            Overtime_end(42)
            Holiday(44)
            
            
            Employment_insurance(48)
            Social_insurance(50)
            Establishment_of_period(48)
            Period(50)
            sub_means(54)
            Bottom_button(60)

            

            
            
        
        
        def sepa():
            c_span_max = 13
            row_max = 55
            
            
            kana_C_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_C_sepa.grid(row=3, column=5, rowspan=5, sticky="ns",padx=4)
            
            kana_R_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_R_sepa.grid(row=3, column=8, rowspan=row_max-5, sticky="ns",padx=4)
            
            kana_L_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_L_sepa.grid(row=1, column=2, rowspan=row_max-3, sticky="ns",padx=4)
            
            left_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_sepa.grid(row=1, column=0, rowspan=row_max, sticky="nsew",padx=4)
            
            top_sepa = ttk.Separator(frame,orient="horizontal")#水平
            top_sepa.grid(row=1, column=0, columnspan=13,sticky="sew",pady=4)
            
            kana_sepa = ttk.Separator(frame,orient="horizontal")#水平
            kana_sepa.grid(row=3, column=0, columnspan=13,sticky="ew",pady=4)
            
            right_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_sepa.grid(row=1, column=c_span_max, rowspan=row_max-2, sticky="nsew",padx=4)
            
            right_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_2_sepa.grid(row=1, column=10, rowspan=row_max-2, sticky="nsew",padx=4)
            """
            left_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_2_sepa.grid(row=7, column=0, rowspan=2, sticky="nsew",padx=4)
            """
            top_2_sepa = ttk.Separator(frame,orient="horizontal")#水平
            top_2_sepa.grid(row=7, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            right_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_2_sepa.grid(row=7, column=13, rowspan=2, sticky="nsew",padx=4)
            
            phone_sepa = ttk.Separator(frame,orient="horizontal")#水平
            phone_sepa.grid(row=9, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            """
            left_p_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_p_sepa.grid(row=7, column=2, rowspan=2, sticky="nsew",padx=4)
            
            right_p_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_p_sepa.grid(row=7, column=8, rowspan=2, sticky="nsew",padx=4)
            """
            tell_sepa = ttk.Separator(frame,orient="horizontal")#水平
            tell_sepa.grid(row=11, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            name_sepa = ttk.Separator(frame,orient="horizontal")#水平
            name_sepa.grid(row=5, column=0, columnspan=c_span_max,sticky="ew",pady=4)
            
            address_top = ttk.Separator(frame,orient="horizontal")#水平
            address_top.grid(row=13, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            address_center = ttk.Separator(frame,orient="horizontal")#水平
            address_center.grid(row=15, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            address_center_2 = ttk.Separator(frame,orient="horizontal")#水平
            address_center_2.grid(row=17, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            address_bottom = ttk.Separator(frame,orient="horizontal")#水平
            address_bottom.grid(row=19, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            Means_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Means_sepa.grid(row=21, column=8, columnspan=c_span_max,sticky="sew",pady=4)
            
            Underwriter_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Underwriter_sepa.grid(row=21, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            Under_b_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Under_b_sepa.grid(row=23, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            Under_c_sepa = ttk.Separator(frame,orient="vertical")#垂直
            Under_c_sepa.grid(row=21, column=5, rowspan=25, sticky="nsew",padx=4)
            
            Under_name_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Under_name_sepa.grid(row=25, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            Under_re_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Under_re_sepa.grid(row=27, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            Under_phone_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Under_phone_sepa.grid(row=29, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            Under_work_sepa = ttk.Separator(frame,orient="horizontal")#水平
            Under_work_sepa.grid(row=31, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            work_sepa = ttk.Separator(frame,orient="horizontal")#水平
            work_sepa.grid(row=33, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            work_2_sepa = ttk.Separator(frame,orient="horizontal")#水平
            work_2_sepa.grid(row=35, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            work_3_sepa = ttk.Separator(frame,orient="horizontal")#水平
            work_3_sepa.grid(row=37, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            rank_sepa = ttk.Separator(frame,orient="horizontal")#水平
            rank_sepa.grid(row=39, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            rank_2_sepa = ttk.Separator(frame,orient="horizontal")#水平
            rank_2_sepa.grid(row=41, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            salary_notes_sepa = ttk.Separator(frame,orient="horizontal")#水平
            salary_notes_sepa.grid(row=43, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            salary_2_sepa = ttk.Separator(frame,orient="horizontal")#水平
            salary_2_sepa.grid(row=45, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            insurance_sepa = ttk.Separator(frame,orient="horizontal")#水平
            insurance_sepa.grid(row=47, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            insurance2_sepa = ttk.Separator(frame,orient="horizontal")#水平
            insurance2_sepa.grid(row=49, column=0, columnspan=c_span_max,sticky="sew",pady=4)
    
            button_sepa = ttk.Separator(frame,orient="horizontal")#水平
            button_sepa.grid(row=51, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            sub_sepa = ttk.Separator(frame,orient="horizontal")#水平
            sub_sepa.grid(row=55, column=0, columnspan=c_span_max,sticky="sew",pady=4)
    
    
        def switching_button(row_set):
            record_id = self.widget.focus()
            
            Before_button = ttk.Button(frame,text=" ◁ ",command=before_id)
            Before_button.grid(row=row_set,column=1)

            Next_Button = ttk.Button(frame,text=" ▷ ",command=after_id)
            Next_Button.grid(row=row_set,column=11)
            
            if self.widget.prev(record_id) == "":
                Before_button.config(state=tk.DISABLED)
                
            
            if self.widget.next(record_id) == "":
                Next_Button.config(state=tk.DISABLED)

        
        def before_id():
            record_id = self.widget.focus()
            id_be = int(record_id) - 1
            self.details_window.destroy()
            self.widget.selection_set(id_be)  # アイテムIDを直接使用
            self.widget.focus(id_be)  # 新しいフォーカスを設定
            
        
        def after_id():
            record_id = self.widget.focus()
            id_af = int(record_id) + 1
            self.details_window.destroy()
            self.widget.selection_set(id_af)  # アイテムIDを直接使用
            self.widget.focus(id_af)  # 新しいフォーカスを設定




            
            
        
        def Enrollment_detail(row_set):
            self.top_frame = ttk.Frame(frame)
            self.top_frame.grid(row=row_set,column=3,columnspan=7)
            
            label = ttk.Label(self.top_frame,text=GUI_lists["Enrollment"], style=style_list["L"])
            label.pack(side=tk.LEFT)
            
            self.Enrollment_Combobox = ttk.Combobox(self.top_frame,width=6,values=select_lists["Enrollment"],font=style_list["E"],state=style_list["S"])
            self.Enrollment_Combobox.pack(side=tk.LEFT)
            self.Enrollment_Combobox.set(self.data["在籍状況"])
        
            
            self.birthday_data = datetime.strptime(json.loads(self.data["スタッフ詳細"])['生年月日'], "%Y-%m-%d")
            
            self.today = datetime.now()
            age = self.today.year - self.birthday_data.year
            this_years_birthday = datetime(self.today.year, self.birthday_data.month, self.birthday_data.day)
            if self.today < this_years_birthday:
                age -= 1
                
                
            age_label = ttk.Label(self.top_frame,text=f"　|　年齢:{age}　|", style=style_list["L"])
            age_label.pack(side=tk.LEFT)
            
            
            self.Joining_data = datetime.strptime(self.data["入社日"], "%Y-%m-%d")

            years_of_service = self.today.year - self.Joining_data.year
            months_of_service = self.today.month - self.Joining_data.month
            if self.today.month < self.Joining_data.month or (self.today.month == self.Joining_data.month and self.today.day < self.Joining_data.day):
                years_of_service -= 1
                months_of_service -= 12
            if months_of_service < 0:
                months_of_service += 12

            
            Length_of_service = ttk.Label(self.top_frame,text=f'　勤続年数:{years_of_service}年{months_of_service}ヶ月', style=style_list["L"])
            Length_of_service.pack(side=tk.LEFT)
           
            
        
        def kana_area(row_set):#氏名　カナ
            
            kana_label = ttk.Label(frame, text=GUI_lists['kana_name'], style=style_list["L"])
            kana_label.grid(row=row_set,column=1)
        
            self.kana1_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.kana1_entry.grid(row=row_set,column=3,columnspan=2)
            self.kana1_entry.insert(tk.END,json.loads(self.data["氏"])['カナ'])
            
            
            self.kana2_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.kana2_entry.grid(row=row_set,column=6,columnspan=2)
            self.kana2_entry.insert(tk.END,json.loads(self.data["名"])['カナ'])
                    
        
        def name_area(row_set):#氏名
            
            
            name_label = ttk.Label(frame,text=GUI_lists["name"], style=style_list["L"])
            name_label.grid(row=row_set,column=1)
            
            self.f_name_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.f_name_entry.grid(row=row_set,column=3,columnspan=2)
            self.f_name_entry.insert(tk.END,json.loads(self.data["氏"])['氏'])
            self.f_name_entry.bind('<FocusOut>',lambda event:Kana_f_change(self.f_name_entry,self.kana1_entry))
            
            self.l_name_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.l_name_entry.grid(row=row_set,column=6,columnspan=2)
            self.l_name_entry.insert(tk.END,json.loads(self.data["名"])['名'])
            self.l_name_entry.bind('<FocusOut>',lambda event:Kana_f_change(self.l_name_entry,self.kana2_entry))
        
        
        def gender_choice(row_set):#性別選択
            
            gender_label = ttk.Label(frame,text=GUI_lists["gender"], style=style_list["L"])
            gender_label.grid(row=row_set,column=9)
            
            self.gender_combobox = ttk.Combobox(frame,values=select_lists['gender'],width=6,font=style_list["E"],state=style_list["S"])
            self.gender_combobox.grid(row=row_set,column=11)
            self.gender_combobox.set(json.loads(self.data["スタッフ詳細"])['性別'])
   
        
        def birthday(row_set):#生年月日
            birthday_label = ttk.Label(frame,text=GUI_lists["birthday"], style=style_list["L"])
            birthday_label.grid(row=row_set,column=9)
            
            self.birthday_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.birthday_entry.grid(row=row_set,column=11)
            birthday = self.birthday_data.strftime('%Y/%m/%d')
            self.birthday_entry.insert(tk.END,birthday)
            ToolTip(self.birthday_entry, text="yyyy/mm/ddで入力")

        
        def cell_phone_area(row_set):#携帯電話
            
            cell_phone_label = ttk.Label(frame,text=GUI_lists["phone"], style=style_list["L"])
            cell_phone_label.grid(row=row_set,column=1)
            
            self.phone_code = ttk.Entry(frame,width=41,font=style_list["E"])
            self.phone_code.grid(row=row_set,column=3,columnspan=5)
            self.phone_code.insert(tk.END,json.loads(self.data["スタッフ詳細"])['携帯電話'])


            ToolTip_error(self.phone_code,GUI_lists["phone"])
            
    
            
        def tell_area(row_set):#固定電話
            
            cell_tell_label = ttk.Label(frame,text=GUI_lists["tell"], style=style_list["L"])
            cell_tell_label.grid(row=row_set,column=1)
            
            self.tell_code = ttk.Entry(frame,width=41,font=style_list["E"])
            self.tell_code.grid(row=row_set,column=3,columnspan=5)
            self.tell_code.insert(tk.END,json.loads(self.data["スタッフ詳細"])['固定電話'])

            
            ToolTip_error(self.tell_code,GUI_lists["tell"])
            
            
            
        def Joining_the_company_day(row_set):#入社日
            #入社日
            label = ttk.Label(frame,text=GUI_lists["Joining"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.Joining_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.Joining_entry.grid(row=row_set,column=11)
            Joining_day = self.Joining_data.strftime('%Y/%m/%d')
            self.Joining_entry.insert(tk.END,Joining_day)
            ToolTip(self.Joining_entry, text="yyyy/mm/ddで入力")
            
        
        def remarks_area(row_set):#備考
            label = ttk.Label(frame,text=GUI_lists["main_remarks"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.remarks_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.remarks_entry.grid(row=row_set,column=11)
            self.remarks_entry.insert(tk.END,self.data["備考欄"])
            self.remarks_entry.bind("<Double-1>", lambda event:TEXT_BOX(self.remarks_entry))
            
            
        
        
        def address_kana_area(row_set):#住所　カナ
            
            label = ttk.Label(frame,text=GUI_lists["kana_name"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            self.address_kana_entry = ttk.Entry(frame,width=41,font=style_list["E"])
            self.address_kana_entry.grid(row=row_set,column=3,columnspan=5)
            self.address_kana_entry.insert(tk.END,json.loads(self.data["スタッフ詳細"])["住所カナ"])
            
            
        def address_area(row_set):#住所
            
            label = ttk.Label(frame,text=GUI_lists["address"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            self.address_entry = ttk.Entry(frame,width=41,font=style_list["E"])
            self.address_entry.grid(row=row_set,column=3,columnspan=5)
            self.address_entry.insert(tk.END,json.loads(self.data["スタッフ詳細"])["住所"])
            self.address_entry.bind('<FocusOut>',lambda event:Kana_f_change(self.address_entry,self.address_kana_entry))
            
            
        
        def post_number_area(row_set):#郵便番号
            
            label = ttk.Label(frame,text=GUI_lists["post"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            number_frame = ttk.Frame(frame)
            number_frame.grid(row=row_set,column=3,columnspan=5,sticky=tk.W)
            
            
            self.Post_number = ttk.Entry(number_frame,width=20,font=style_list["E"])
            self.Post_number.grid(row=0,column=0)
            self.Post_number.insert(tk.END,json.loads(self.data["スタッフ詳細"])["郵便番号"])
            
            
            
            ToolTip_error_Post(self.Post_number,GUI_lists["post"],self.address_entry,self.address_kana_entry)
            
            
        def dependent_area(row_set):#扶養
            label = ttk.Label(frame,text=GUI_lists["dependent"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.dependent_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.dependent_entry.grid(row=row_set,column=11)
            self.dependent_entry.bind("<Double-1>", lambda event:TEXT_BOX(self.dependent_entry))
            self.dependent_entry.insert(tk.END,json.loads(self.data["扶養"])["扶養"])
            
            
        
        def dependent_people_area(row_set):#扶養の人数
            label = ttk.Label(frame,text=GUI_lists["people"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.dependent_people_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.dependent_people_entry.grid(row=row_set,column=11)
            self.dependent_people_entry.insert(tk.END,json.loads(self.data["扶養"])["人数"])
            
        
        def Means_of_commuting(row_set):#通勤手段
            label = ttk.Label(frame,text=GUI_lists["means"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.Means_combobox = ttk.Combobox(frame,width=10,values=select_lists['means'],font=style_list["E"])
            self.Means_combobox.option_add("*TCombobox*Listbox.Font", ('HGP教科書体', 16))
            self.Means_combobox.grid(row=row_set,column=11)
            self.Means_combobox.insert(tk.END,json.loads(self.data["主な交通費"])["通勤手段"])
        
        
        def Means_amount(row_set):#メインの交通費
            
            label = ttk.Label(frame,textvariable=self.amount_label, style=style_list["L"])
            label.grid(row=row_set,column=9)
            set_text = f'通勤{self.amount_label.get()}'
            self.Means_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.Means_entry.grid(row=row_set,column=11)
            self.Means_entry.insert(tk.END,json.loads(self.data["主な交通費"])[set_text])
            
        
        def Underwriter(row_set):#身元引受人(ラベル)
            main_label = ttk.Label(frame,text=f'{GUI_lists["under"]}', style=style_list["U"])
            main_label.grid(row=row_set,column=1)
            
        
        def U_number(row_set):
            label = ttk.Label(frame,text="1人目", style=style_list["L"])
            label.grid(row=row_set,column=3,columnspan=2)
            label_2 = ttk.Label(frame,text="2人目", style=style_list["L"])
            label_2.grid(row=row_set,column=6,columnspan=2)
            
        
        def Under_name_label(row_set):#身元引受人　名前(ラベル)
            label = ttk.Label(frame,text=GUI_lists["name"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            

        def relationship_label(row_set):#身元引受人　続柄(ラベル)
            label = ttk.Label(frame,text=GUI_lists["relationship"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
        
        def Under_phone_label(row_set):#身元引受人　電話番号(ラベル)
            label = ttk.Label(frame,text=GUI_lists["phone"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
        
        def Under_work(row_set):#身元引受人　勤務先(ラベル)
            label = ttk.Label(frame,text=GUI_lists["place_of_work"], style=style_list["L"])
            label.grid(row=row_set,column=1)
        
            
        #1人目入力    
        def Under_1_name(row_set):
            self.Under_1_name_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_name_Entry.grid(row=row_set,column=3,columnspan=2)
            self.Under_1_name_Entry.insert(tk.END,json.loads(self.data["身元引受人１"])["名前"])
            
            
        def Under_1_relationship(row_set):
            self.Under_1_relationship_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_relationship_Entry.grid(row=row_set,column=3,columnspan=2)
            self.Under_1_relationship_Entry.insert(tk.END,json.loads(self.data["身元引受人１"])["続柄"])
            
        
        def Under_1_phone(row_set):
            self.Under_1_phone_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_phone_Entry.grid(row=row_set,column=3,columnspan=2)
            self.Under_1_phone_Entry.insert(tk.END,json.loads(self.data["身元引受人１"])["電話番号"])
        
        
        def Under_1_work(row_set):
            self.Under_1_work_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_work_Entry.grid(row=row_set,column=3,columnspan=2)
            self.Under_1_work_Entry.insert(tk.END,json.loads(self.data["身元引受人１"])["勤務先"])
        
        
        #2人目入力
        
        def Under_2_name(row_set):
            self.Under_2_name_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_name_Entry.grid(row=row_set,column=6,columnspan=2)
            self.Under_2_name_Entry.insert(tk.END,json.loads(self.data["身元引受人１"])["名前"])
            
            
        def Under_2_relationship(row_set):
            self.Under_2_relationship_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_relationship_Entry.grid(row=row_set,column=6,columnspan=2)
            self.Under_2_relationship_Entry.insert(tk.END,json.loads(self.data["身元引受人２"])["続柄"])
            
        
        def Under_2_phone(row_set):
            self.Under_2_phone_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_phone_Entry.grid(row=row_set,column=6,columnspan=2)
            self.Under_2_phone_Entry.insert(tk.END,json.loads(self.data["身元引受人２"])["電話番号"])
        
        
        def Under_2_work(row_set):
            self.Under_2_work_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_work_Entry.grid(row=row_set,column=6,columnspan=2)
            self.Under_2_work_Entry.insert(tk.END,json.loads(self.data["身元引受人２"])["勤務先"])
          
            
        
        def Work_place(row_set):#就業場所
            label = ttk.Label(frame,text=GUI_lists["work_place"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            self.Work_place_combobox = ttk.Combobox(frame,width=10,values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.Work_place_combobox.grid(row=row_set,column=3)
            self.Work_place_combobox.insert(tk.END,self.data["就業場所"])
            self.Work_place_combobox.bind('<<ComboboxSelected>>',change_Work_place)
            
            
                 
        def Employment_status(row_set):#雇用形態
            
            label = ttk.Label(frame,text=GUI_lists["emp_type"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            self.emp_entry = ttk.Combobox(frame,width=10,values=select_lists['emp_type'],font=style_list["E"],state=style_list["S"])
            self.emp_entry.grid(row=row_set,column=3)
            self.emp_entry.set(self.data["雇用形態"])

            self.emp_entry.bind('<<ComboboxSelected>>',change_Allowance)
            
            change_Allowance()
            
            
        def Job_description(row_set):#仕事内容
            label = ttk.Label(frame,text=GUI_lists["job_description"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            self.job_entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.job_entry.grid(row=row_set,column=3)
            self.job_entry.insert(tk.END,self.data["仕事内容"])
        
        
        def Rank_status(row_set):#等級
            from data.SQL_center import Rank_List_Manager
            rank_list_d = Rank_List_Manager()
            if self.Work_place_combobox.get() == "広島本部":
                self.rank_list = rank_list_d.rank_number_list_office_get()
            else:
                self.rank_list = rank_list_d.rank_number_list_store_get()
                
            label = ttk.Label(frame,text=GUI_lists["rank_status"], style=style_list["L"])
            label.grid(row=row_set,column=1)

            self.rank_combobox = ttk.Combobox(frame,width=10,values=self.rank_list,font=style_list["E"],state=style_list["S"])
            self.rank_combobox.grid(row=row_set,column=3)
            self.rank_combobox.set(self.data["等級"])
            
            
            
            
            
        
        def Contract_renewal(row_set):
            label = ttk.Label(frame,text=GUI_lists["Contract_renewal"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.Contract_renewal_combobox = ttk.Combobox(frame,width=10,values=select_lists['presence_or_absence'],font=style_list["E"],state=style_list["S"])
            self.Contract_renewal_combobox.grid(row=row_set,column=11)
            self.Contract_renewal_combobox.set(json.loads(self.data["更新"])["更新"])
            
        
        def Renewal_day(row_set):
            label = ttk.Label(frame,text=GUI_lists["Renewal_day"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.Renewal_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.Renewal_entry.grid(row=row_set,column=11)
            date_str = json.loads(self.data["更新"])["更新日"]
            try:  
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                day_set = date_obj.strftime('%Y/%m/%d')
            except:
                date_obj = ""
                day_set = date_obj
            
            self.Renewal_entry.insert(tk.END,day_set)
            ToolTip(self.Renewal_entry, text="yyyy/mm/ddで入力")
            
            
            
        
        def Salary_notes(row_set):#給与関係の備考
            label = ttk.Label(frame,text=GUI_lists["salary_notes"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            self.salary_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.salary_entry.grid(row=row_set,column=3)
            self.salary_entry.insert(tk.END,self.data['給与備考'])
            self.salary_entry.bind("<Double-1>", lambda event:TEXT_BOX(self.salary_entry))
            
        
        def Working_conditions(row_set):#労働条件
            label = ttk.Label(frame,text=GUI_lists["working_conditions"], style=style_list["L"])
            label.grid(row=row_set,column=6,columnspan=2)
            

        def Working_start_time(row_set):#出勤時間
            label = ttk.Label(frame,text=GUI_lists["working_start"], style=style_list["L"])
            label.grid(row=row_set,column=6)
            
            self.work_start_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_start_entry.grid(row=row_set,column=7)
            self.work_start_entry.insert(tk.END,json.loads(self.data['勤務時間'])['出勤'])
            
            ToolTip_time(self.work_start_entry, text="hh:mmで入力")
            
        
        def Working_end_time(row_set):#退勤時間
            label = ttk.Label(frame,text=GUI_lists["working_end"], style=style_list["L"])
            label.grid(row=row_set,column=6)
            
            self.work_end_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_end_entry.grid(row=row_set,column=7)
            self.work_end_entry.insert(tk.END,json.loads(self.data['勤務時間'])['退勤'])
            
            ToolTip_time(self.work_end_entry, text="hh:mmで入力")
        
        
        def Working_break_time(row_set):#休憩時間
            label = ttk.Label(frame,text=GUI_lists["working_break_time"], style=style_list["L"])
            label.grid(row=row_set,column=6)
            
            self.work_break_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_break_entry.grid(row=row_set,column=7)
            self.work_break_entry.insert(tk.END,json.loads(self.data['勤務時間'])['休憩'])
        
        
        def Working_week_time(row_set):#週の勤務時間
            label = ttk.Label(frame,text=GUI_lists["working_week_time"], style=style_list["L"])
            label.grid(row=row_set,column=6)
            
            self.work_week_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_week_entry.grid(row=row_set,column=7)
            self.work_week_entry.insert(tk.END,json.loads(self.data['勤務時間'])['1週間'])
            
            
        def Overtime_or(row_set):#残業の有無
            label = ttk.Label(frame,text=GUI_lists["working_overtime"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.work_over_combobox = ttk.Combobox(frame,values=select_lists['presence_or_absence'],
                                                   width=8,font=style_list["E"],state=style_list["S"])
            self.work_over_combobox.grid(row=row_set,column=11)
            self.work_over_combobox.insert(tk.END,json.loads(self.data['残業'])['有無'])
            

        def Overtime_start(row_set):#残業開始時間
            label = ttk.Label(frame,text=GUI_lists["working_over_start"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.work_over_start_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_over_start_entry.grid(row=row_set,column=11)
            self.work_over_start_entry.insert(tk.END,json.loads(self.data['残業'])['開始'])
            
            ToolTip_time(self.work_over_start_entry, text="hh:mmで入力")
        
        
        def Overtime_end(row_set):#残業終了時間
            label = ttk.Label(frame,text=GUI_lists["working_over_end"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.work_over_end_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_over_end_entry.grid(row=row_set,column=11)
            self.work_over_end_entry.insert(tk.END,json.loads(self.data['残業'])['終了'])
            
            ToolTip_time(self.work_over_end_entry, text="hh:mmで入力")    
        
        
        def Holiday(row_set):#休日に関して
            label = ttk.Label(frame,text=GUI_lists["holiday"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.holiday_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.holiday_entry.grid(row=row_set,column=11)
            self.holiday_entry.bind("<Double-1>", lambda event:TEXT_BOX(self.holiday_entry))
            self.holiday_entry.insert(tk.END,self.data['休日'])
        
        
        def Employment_insurance(row_set):#雇用保険
            label = ttk.Label(frame,text=GUI_lists["employment_insurance"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            emp_ins_frame = ttk.Frame(frame)
            emp_ins_frame.grid(row=row_set,column=3,columnspan=5)
            
            self.emp_ins_combobox = ttk.Combobox(emp_ins_frame,values=select_lists['presence_or_absence'],
                                                   width=5,font=style_list["E"],state=style_list["S"])
            self.emp_ins_combobox.grid(row=1,column=0)
            
            label2 = ttk.Label(emp_ins_frame,text=GUI_lists["number"], style=style_list["L"])
            label2.grid(row=1,column=2)
            
            self.emp_ins_entry = ttk.Entry(emp_ins_frame,width=24,font=style_list["E"])
            self.emp_ins_entry.grid(row=1,column=3)
            
            sepa = ttk.Separator(emp_ins_frame,orient="vertical")#垂直
            sepa.grid(row=0, column=1, rowspan=3, sticky="ns",padx=4)
        
        
        def Social_insurance(row_set):#社会保険
            label = ttk.Label(frame,text=GUI_lists["sosial_insurance"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            soc_ins_frame = ttk.Frame(frame)
            soc_ins_frame.grid(row=row_set,column=3,columnspan=5)
            
            self.soc_ins_combobox = ttk.Combobox(soc_ins_frame,values=select_lists['presence_or_absence'],
                                                   width=5,font=style_list["E"],state=style_list["S"])
            self.soc_ins_combobox.grid(row=1,column=0)
            
            label2 = ttk.Label(soc_ins_frame,text=GUI_lists["number"], style=style_list["L"])
            label2.grid(row=1,column=2)
            
            self.soc_ins_entry = ttk.Entry(soc_ins_frame,width=24,font=style_list["E"])
            self.soc_ins_entry.grid(row=1,column=3)
            
            sepa = ttk.Separator(soc_ins_frame,orient="vertical")#垂直
            sepa.grid(row=0, column=1, rowspan=3, sticky="ns",padx=4)
            
            
        def Establishment_of_period(row_set):#定めの期間の有無
            label = ttk.Label(frame,text=GUI_lists["establishment_of_period"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.est_of_p_combobox = ttk.Combobox(frame,values=select_lists['presence_or_absence'],
                                                   width=9,font=style_list["E"],state=style_list["S"])
            self.est_of_p_combobox.grid(row=row_set,column=11)
            
            self.est_of_p_combobox.set(self.data['期間の定め'])
            
        
        def Period(row_set):#試用期間
            label = ttk.Label(frame,text=GUI_lists["period"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.trial_period_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.trial_period_entry.grid(row=row_set,column=11)
            self.trial_period_entry.insert(tk.END,self.data['試用期間'])
            ToolTip(self.trial_period_entry, text="試用期間があれば入力")
        
        
        def sub_means(row_set):
            sub_means_frame = ttk.Frame(frame)
            sub_means_frame.grid(row=row_set,column=1,columnspan=11)
            place_key = []
            amount = []
            data = json.loads(self.data['サブ交通費'])
            
            for key,value in data.items():
                place_key.append(key)
                amount.append(value)
                
            
            sub_label = ttk.Label(sub_means_frame,text="サブ交通費", style=style_list["L"])
            sub_label.grid(row=0,column=0,columnspan=9)
            
            self.sub1_label = ttk.Label(sub_means_frame,text="サブ1", style=style_list["L"])
            self.sub1_label.grid(row=1,column=0)
            
            self.sub1_place = ttk.Combobox(sub_means_frame,width=8,values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.sub1_place.grid(row=2,column=0)
            self.sub1_place.set(place_key[0])
            
            self.sub1_amount = ttk.Entry(sub_means_frame,width=9,font=style_list["E"],state=style_list["S"])
            self.sub1_amount.grid(row=3,column=0)
            self.sub1_amount.insert(tk.END,amount[0])
            
            
            sub2_label = ttk.Label(sub_means_frame,text="サブ2", style=style_list["L"])
            sub2_label.grid(row=1,column=1)
            
            self.sub2_place = ttk.Combobox(sub_means_frame,width=8,values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.sub2_place.grid(row=2,column=1)
            self.sub2_place.set(place_key[1])
            
            self.sub2_amount = ttk.Entry(sub_means_frame,width=9,font=style_list["E"],state=style_list["S"])
            self.sub2_amount.grid(row=3,column=1)
            self.sub2_amount.insert(tk.END,amount[1])
            
            
            sub3_label = ttk.Label(sub_means_frame,text="サブ3", style=style_list["L"])
            sub3_label.grid(row=1,column=2)
            
            self.sub3_place = ttk.Combobox(sub_means_frame,width=8,values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.sub3_place.grid(row=2,column=2)
            self.sub3_place.set(place_key[2])
            
            self.sub3_amount = ttk.Entry(sub_means_frame,width=9,font=style_list["E"],state=style_list["S"])
            self.sub3_amount.grid(row=3,column=2)
            self.sub3_amount.insert(tk.END,amount[2])
            
            
            sub4_label = ttk.Label(sub_means_frame,text="サブ4", style=style_list["L"])
            sub4_label.grid(row=1,column=3)
            
            self.sub4_place = ttk.Combobox(sub_means_frame,width=8,values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.sub4_place.grid(row=2,column=3)
            self.sub4_place.set(place_key[3])
            
            self.sub4_amount = ttk.Entry(sub_means_frame,width=9,font=style_list["E"],state=style_list["S"])
            self.sub4_amount.grid(row=3,column=3)
            self.sub4_amount.insert(tk.END,amount[3])
        
        
        
        
        
        
        def Bottom_button(row_set):
            bottom_button = ttk.Frame(frame)
            bottom_button.grid(row=row_set,column=0,columnspan=13,pady=10)
            Registr_button = ttk.Button(bottom_button,text=GUI_lists["Update"], style=style_list["B"],command=Datail_summarize)
            Registr_button.pack(side=tk.LEFT)
            P_button = ttk.Button(bottom_button,text=GUI_lists["Print"], style=style_list["B"],command=lambda: Detail_print("Print"))
            P_button.pack(side=tk.LEFT)
            PDF_button = ttk.Button(bottom_button,text=GUI_lists["PDF"], style=style_list["B"],command=lambda: Detail_print("PDF"))
            PDF_button.pack(side=tk.LEFT)
        
        
            
        
        
        
        def widget_summarize():
            data = {"fカナ":self.kana1_entry,"lカナ":self.kana2_entry,
                    "f名字":self.f_name_entry,"l名前":self.l_name_entry,
                    "性別":self.gender_combobox,"生年月日":self.birthday_entry,"携帯電話":self.phone_code,"固定電話":self.tell_code,
                    "入社日":self.Joining_entry,"備考":self.remarks_entry,"住所カナ":self.address_kana_entry,"住所":self.address_entry,
                    "郵便番号":self.Post_number,"扶養":self.dependent_entry,"扶養の人数":self.dependent_people_entry,"通勤手段":self.Means_combobox,
                    "メインの交通費":self.Means_entry,"1名前":self.Under_1_name_Entry,"1続柄":self.Under_1_relationship_Entry,"手当種類":self.amount_label,
                    "1電話番号":self.Under_1_phone_Entry,"1勤務先":self.Under_1_work_Entry,
                    "2名前":self.Under_2_name_Entry,"2続柄":self.Under_2_relationship_Entry,"2電話番号":self.Under_2_phone_Entry,
                    "2勤務先":self.Under_2_work_Entry,"就業場所":self.Work_place_combobox,"雇用形態":self.emp_entry,
                    "仕事内容":self.job_entry,"等級":self.rank_combobox,"給与備考":self.salary_entry,
                    "出勤時間":self.work_start_entry,"退勤時間":self.work_end_entry,"休憩時間":self.work_break_entry,
                    "週の勤務時間":self.work_week_entry,"残業の有無":self.work_over_combobox,"id":self.data['id'],
                    "残業開始時間":self.work_over_start_entry,"残業終了時間":self.work_over_end_entry,"休日":self.holiday_entry,
                    "雇用保険の有無":self.emp_ins_combobox,"雇用保険番号":self.emp_ins_entry,
                    "社会保険の有無":self.soc_ins_combobox,"社会保険番号":self.soc_ins_entry,
                    "定めの期間の有無":self.est_of_p_combobox,"試用期間":self.trial_period_entry,
                    "更新の有無":self.Contract_renewal_combobox,"更新日":self.Renewal_entry,
                    "サブ1店舗":self.sub1_place,"サブ1金額":self.sub1_amount,"サブ2店舗":self.sub2_place,"サブ2金額":self.sub2_amount,
                    "サブ3店舗":self.sub3_place,"サブ3金額":self.sub3_amount,"サブ4店舗":self.sub4_place,"サブ4金額":self.sub4_amount}
            
            return data
        
        
        #,"":
        def Datail_summarize():
            data = widget_summarize()
            

            
            
            
            if (self.kana1_entry.get() == "") or (self.kana2_entry.get() == "") or (self.f_name_entry.get() == "") or (self.l_name_entry.get() == ""):
                message_error = []
                
                if self.kana1_entry.get() == "":
                    message_error.append("カナ姓")
                if self.kana2_entry.get() == "":
                    message_error.append("カナ名")
                if self.f_name_entry.get() == "":
                    message_error.append("名字")
                if self.l_name_entry.get() == "":
                    message_error.append("名前")
                
                message_open = ""
                for i in message_error:
                    if i != message_error[-1]:
                        message_open += (i+"・")
                    else:
                        message_open += i
                        
                def show_message():
                    new_root = tk.Tk()
                    
                    message = f'[{message_open}]\nが入力されていません。'
                    label = ttk.Label(new_root, text=message, font=('HGP教科書体', 20), foreground="#dc143c")
                    label.pack()
                    button = ttk.Button(new_root, text="OK", command=new_root.destroy, style=style_list["B"])
                    button.pack()
                    new_root.mainloop()
                show_message()
                

            else:
                #print("更新")
                from data.staff_registration import Interim_update
                Interim_update(data,self.data['id'])
            
            
        def Detail_print(set):
            Datail_summarize()
            data = widget_summarize()
            from data.Printing import Notice_Printing
            Notice_Printing(data,set)
            #print('印刷')    
            
            
            
            
        def Kana_f_change(widget,widget2):
            from GUI_Logic.format_change import Kana_change
            Kana_change(widget,widget2)
            
        def TEXT_BOX(widget):
            from GUI_Logic.text_box_RE import Open_text_box
            Open_text_box(widget)
        
        def change_Allowance():
            from GUI_Logic.Logic_etc import Allowance_change
            Allowance_change(self.emp_entry,self.amount_label)
            
        def change_Work_place(event=None):
            from GUI_Logic.Logic_etc import Work_place_rank_change
            Work_place_rank_change(self.Work_place_combobox,self.rank_list,self.rank_combobox)
        
        
        
        row_set()
        