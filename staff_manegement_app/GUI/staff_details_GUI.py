import tkinter as tk
from tkinter import ttk
from ..GUI_Logic.format_change import Kana_change
from ..GUI_Logic.text_box_RE import Open_text_box

from ..GUI_Logic.tooltip_day import ToolTip , ToolTip_time,ToolTip_error,ToolTip_error_Post
#from staff_manegement_app.data.staff_registration import Interim_arrangement
from staff_manegement_app.GUI.load_config import load_GUI_file
from staff_manegement_app.GUI.load_config import load_List_file

GUI_lists = load_GUI_file()
select_lists = load_List_file()




class Staff_Details_Display(object):
    def __init__(self,data):
        self.data = data[0]
        self.amount_label = tk.StringVar()
        
        
        self.setup_tab()

    def setup_tab(self):
        
        self.details_window = tk.Toplevel()
        self.details_window.title("詳細")
        self.details_window.geometry("1000x700")
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
        
        # タッチパッドやトラックパッドによる横スクロールのサポートが必要な場合（例: 横長のコンテンツ）
        def on_shift_mousewheel(event):
            canvas.xview_scroll(int(-1*(event.delta/120)), "units")  # 横スクロール用

        canvas.bind("<MouseWheel>", on_mousewheel)
        canvas.bind("<Shift-MouseWheel>", on_shift_mousewheel)  # 横スクロールのためにShiftキーを使用


        # キャンバス上に配置するウィジェット用のフレーム
        staff_details_frame = ttk.Frame(canvas)
        staff_details_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=staff_details_frame, anchor='nw')
        return staff_details_frame
    
    def details_display(self,frame):
        from ..GUI_Logic.Logic_etc import Allowance_change , Work_place_rank_change
        row_max = 50
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
            
            dependent_area(16)#扶養入力
            dependent_people_area(18)#扶養の人数入力
            Means_of_commuting(20)#通勤手段
            Means_amount(22)#通勤手当
            
            """
            Underwriter()#身元引受人
            U_number()
            Under_name_label()#身元引受人名前
            relationship_label()#続柄
            Under_phone_label()#電話番号
            Under_work()#勤務先
            
            #1人目入力
            Under_1_name()#名前
            Under_1_relationship()#続柄
            Under_1_phone()#電話番号
            Under_1_work()#勤務先

            #2人目入力
            Under_2_name()#名前
            Under_2_relationship()#続柄
            Under_2_phone()#電話番号
            Under_2_work()#勤務先   
            
            Work_place()  
            Employment_status()
            Job_description()
            Rank_status()
            Salary_notes()
            
            Working_conditions()
            Working_start_time()
            Working_end_time()
            Working_break_time()
            Working_week_time()
            
            Overtime_or()
            Overtime_start()
            Overtime_end()
            Holiday()
            
            Employment_insurance()
            Social_insurance()
            Establishment_of_period()
            Period()
            Registration_button()
            Contract_renewal()
            Renewal_day()
            """
            

            
            
        
        
        def sepa():
            c_span_max = 13
            row_max = 50
            
            
            kana_C_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_C_sepa.grid(row=3, column=5, rowspan=5, sticky="ns",padx=4)
            
            kana_R_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_R_sepa.grid(row=3, column=8, rowspan=row_max, sticky="ns",padx=4)
            
            kana_L_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_L_sepa.grid(row=1, column=2, rowspan=row_max, sticky="ns",padx=4)
            
            left_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_sepa.grid(row=1, column=0, rowspan=row_max, sticky="nsew",padx=4)
            
            top_sepa = ttk.Separator(frame,orient="horizontal")#水平
            top_sepa.grid(row=1, column=0, columnspan=13,sticky="sew",pady=4)
            
            kana_sepa = ttk.Separator(frame,orient="horizontal")#水平
            kana_sepa.grid(row=3, column=0, columnspan=13,sticky="ew",pady=4)
            
            right_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_sepa.grid(row=1, column=c_span_max, rowspan=row_max, sticky="nsew",padx=4)
            
            right_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_2_sepa.grid(row=1, column=10, rowspan=row_max, sticky="nsew",padx=4)
            
            left_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_2_sepa.grid(row=7, column=0, rowspan=5, sticky="nsew",padx=4)
            
            top_2_sepa = ttk.Separator(frame,orient="horizontal")#水平
            top_2_sepa.grid(row=7, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            right_2_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_2_sepa.grid(row=7, column=13, rowspan=5, sticky="nsew",padx=4)
            
            phone_sepa = ttk.Separator(frame,orient="horizontal")#水平
            phone_sepa.grid(row=9, column=0, columnspan=c_span_max,sticky="sew",pady=4)
            
            left_p_sepa = ttk.Separator(frame,orient="vertical")#垂直
            left_p_sepa.grid(row=7, column=2, rowspan=5, sticky="nsew",padx=4)
            
            right_p_sepa = ttk.Separator(frame,orient="vertical")#垂直
            right_p_sepa.grid(row=7, column=8, rowspan=5, sticky="nsew",padx=4)
            
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
    
    
    
        def switching_button(row_set):
            Before_button = ttk.Button(frame,text=" ◁ ")
            Before_button.grid(row=row_set,column=1)
            Next_Button = ttk.Button(frame,text=" ▷ ")
            Next_Button.grid(row=row_set,column=11)
            
        
        def Enrollment_detail(row_set):
            self.top_frame = ttk.Frame(frame)
            self.top_frame.grid(row=row_set,column=3,columnspan=5)
            
            label = ttk.Label(self.top_frame,text=GUI_lists["Enrollment"], style=style_list["L"])
            label.pack(side=tk.LEFT)
            
            self.Enrollment_Combobox = ttk.Combobox(self.top_frame,width=6,values=select_lists["Enrollment"],font=style_list["E"],state=style_list["S"])
            self.Enrollment_Combobox.pack(side=tk.LEFT)
            self.Enrollment_Combobox.set(self.data[22])
        
        
        
        
        
        def kana_area(row_set):#氏名　カナ
            
            
        
            kana_label = ttk.Label(frame, text=GUI_lists['kana_name'], style=style_list["L"])
            kana_label.grid(row=row_set,column=1)
        
            self.kana1_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.kana1_entry.grid(row=row_set,column=3,columnspan=2)
            self.kana1_entry.insert
            
            
            self.kana2_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.kana2_entry.grid(row=row_set,column=6,columnspan=2)
                    
        
        def name_area(row_set):#氏名
            
            
            name_label = ttk.Label(frame,text=GUI_lists["name"], style=style_list["L"])
            name_label.grid(row=row_set,column=1)
            
            self.f_name_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.f_name_entry.grid(row=row_set,column=3,columnspan=2)
            
            Kana_change(self.f_name_entry,self.kana1_entry)
            
            self.l_name_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.l_name_entry.grid(row=row_set,column=6,columnspan=2)
            
            Kana_change(self.l_name_entry,self.kana2_entry)
        
        
        def gender_choice(row_set):#性別選択
            
            gender_label = ttk.Label(frame,text=GUI_lists["gender"], style=style_list["L"])
            gender_label.grid(row=row_set,column=9)
            
            self.gender_combobox = ttk.Combobox(frame,values=select_lists['gender'],width=6,font=style_list["E"],state=style_list["S"])
            self.gender_combobox.grid(row=row_set,column=11)
        
        
        def birthday(row_set):#生年月日
            birthday_label = ttk.Label(frame,text=GUI_lists["birthday"], style=style_list["L"])
            birthday_label.grid(row=row_set,column=9)
            
            self.birthday_entry = ttk.Entry(frame,width=8,font=style_list["E"])
            self.birthday_entry.grid(row=row_set,column=11)
            
            ToolTip(self.birthday_entry, text="yyyy/mm/ddで入力")

        
        def cell_phone_area(row_set):#携帯電話
            
            cell_phone_label = ttk.Label(frame,text=GUI_lists["phone"], style=style_list["L"])
            cell_phone_label.grid(row=row_set,column=1)
            
            self.phone_code = ttk.Entry(frame,width=41,font=style_list["E"])
            self.phone_code.grid(row=row_set,column=3,columnspan=5)


            ToolTip_error(self.phone_code,GUI_lists["phone"])
            
    
            
        def tell_area(row_set):#固定電話
            
            cell_tell_label = ttk.Label(frame,text=GUI_lists["tell"], style=style_list["L"])
            cell_tell_label.grid(row=row_set,column=1)
            
            self.tell_code = ttk.Entry(frame,width=41,font=style_list["E"])
            self.tell_code.grid(row=row_set,column=3,columnspan=5)
            
            
            ToolTip_error(self.tell_code,GUI_lists["tell"])
            
            
            
        def Joining_the_company_day(row_set):#入社日
            #入社日
            label = ttk.Label(frame,text=GUI_lists["Joining"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.Joining_entry = ttk.Entry(frame,width=8,font=style_list["E"])
            self.Joining_entry.grid(row=row_set,column=11)
            
            ToolTip(self.Joining_entry, text="yyyy/mm/ddで入力")
            
        
        def remarks_area(row_set):#備考
            label = ttk.Label(frame,text=GUI_lists["main_remarks"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.remarks_entry = ttk.Entry(frame,width=8,font=style_list["E"])
            self.remarks_entry.grid(row=row_set,column=11)
            
            Open_text_box(self.remarks_entry)
        
        
        def address_kana_area(row_set):#住所　カナ
            
            label = ttk.Label(frame,text=GUI_lists["kana_name"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            self.address_kana_entry = ttk.Entry(frame,width=41,font=style_list["E"])
            self.address_kana_entry.grid(row=row_set,column=3,columnspan=5)
            
            
        def address_area(row_set):#住所
            
            label = ttk.Label(frame,text=GUI_lists["address"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            self.address_entry = ttk.Entry(frame,width=41,font=style_list["E"])
            self.address_entry.grid(row=row_set,column=3,columnspan=5)
            
            Kana_change(self.address_entry,self.address_kana_entry)
            
        
        def post_number_area(row_set):#郵便番号
            
            label = ttk.Label(frame,text=GUI_lists["post"], style=style_list["L"])
            label.grid(row=row_set,column=1)
            
            number_frame = ttk.Frame(frame)
            number_frame.grid(row=row_set,column=3,columnspan=5,sticky=tk.W)
            
            
            self.Post_number = ttk.Entry(number_frame,width=20,font=style_list["E"])
            self.Post_number.grid(row=0,column=0)
            
            #example = ttk.Label(number_frame,text="例)730-0001⇒7300001",style=style_list["L"])
            #example.grid(row=0,column=1)
            
            
            
            ToolTip_error_Post(self.Post_number,GUI_lists["post"],self.address_entry,self.address_kana_entry)
            
            
        def dependent_area(row_set):#扶養
            label = ttk.Label(frame,text=GUI_lists["dependent"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.dependent_entry = ttk.Entry(frame,width=8,font=style_list["E"])
            self.dependent_entry.grid(row=row_set,column=11)
            
            Open_text_box(self.dependent_entry)
            
        
        def dependent_people_area(row_set):#扶養の人数
            label = ttk.Label(frame,text=GUI_lists["people"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.dependent_people_entry = ttk.Entry(frame,width=8,font=style_list["E"])
            self.dependent_people_entry.grid(row=row_set,column=11)
            
        
        def Means_of_commuting(row_set):#通勤手段
            label = ttk.Label(frame,text=GUI_lists["means"], style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.Means_combobox = ttk.Combobox(frame,width=6,values=select_lists['means'],font=style_list["E"])
            self.Means_combobox.option_add("*TCombobox*Listbox.Font", ('HGP教科書体', 16))
            self.Means_combobox.grid(row=row_set,column=11)
        
        
        def Means_amount(row_set):#メインの交通費
            
            label = ttk.Label(frame,textvariable=self.amount_label, style=style_list["L"])
            label.grid(row=row_set,column=9)
            
            self.Means_entry = ttk.Entry(frame,width=8,font=style_list["E"])
            self.Means_entry.grid(row=row_set,column=11)
            
        
        def Underwriter(row_set):#身元引受人(ラベル)
            main_label = ttk.Label(frame,text=f'{GUI_lists["under"]}', style=style_list["U"])
            main_label.grid(row=22,column=1)
            
        
        def U_number(row_set):
            label = ttk.Label(frame,text="1人目", style=style_list["L"])
            label.grid(row=22,column=3,columnspan=2)
            label_2 = ttk.Label(frame,text="2人目", style=style_list["L"])
            label_2.grid(row=22,column=6,columnspan=2)
            
        
        def Under_name_label(row_set):#身元引受人　名前(ラベル)
            label = ttk.Label(frame,text=GUI_lists["name"], style=style_list["L"])
            label.grid(row=24,column=1)
            

        def relationship_label(row_set):#身元引受人　続柄(ラベル)
            label = ttk.Label(frame,text=GUI_lists["relationship"], style=style_list["L"])
            label.grid(row=26,column=1)
            
        
        def Under_phone_label(row_set):#身元引受人　電話番号(ラベル)
            label = ttk.Label(frame,text=GUI_lists["phone"], style=style_list["L"])
            label.grid(row=28,column=1)
            
        
        def Under_work(row_set):#身元引受人　勤務先(ラベル)
            label = ttk.Label(frame,text=GUI_lists["place_of_work"], style=style_list["L"])
            label.grid(row=30,column=1)
        
            
        #1人目入力    
        def Under_1_name(row_set):
            self.Under_1_name_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_name_Entry.grid(row=24,column=3,columnspan=2)
            
            
        def Under_1_relationship(row_set):
            self.Under_1_relationship_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_relationship_Entry.grid(row=26,column=3,columnspan=2)
            
        
        def Under_1_phone(row_set):
            self.Under_1_phone_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_phone_Entry.grid(row=28,column=3,columnspan=2)
        
        
        def Under_1_work(row_set):
            self.Under_1_work_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_work_Entry.grid(row=30,column=3,columnspan=2)
        
        
        #2人目入力
        
        def Under_2_name(row_set):
            self.Under_2_name_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_name_Entry.grid(row=24,column=6,columnspan=2)
            
            
        def Under_2_relationship(row_set):
            self.Under_2_relationship_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_relationship_Entry.grid(row=26,column=6,columnspan=2)
            
        
        def Under_2_phone(row_set):
            self.Under_2_phone_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_phone_Entry.grid(row=28,column=6,columnspan=2)
        
        
        def Under_2_work(row_set):
            self.Under_2_work_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_work_Entry.grid(row=30,column=6,columnspan=2)
          
            
        
        def Work_place(row_set):#就業場所
            label = ttk.Label(frame,text=GUI_lists["work_place"], style=style_list["L"])
            label.grid(row=34,column=1)
            
            self.Work_place_combobox = ttk.Combobox(frame,width=10,values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.Work_place_combobox.grid(row=34,column=3)
            
                 
        def Employment_status(row_set):#雇用形態
            
            label = ttk.Label(frame,text=GUI_lists["emp_type"], style=style_list["L"])
            label.grid(row=36,column=1)
            
            self.emp_entry = ttk.Combobox(frame,width=10,values=select_lists['emp_type'],font=style_list["E"],state=style_list["S"])
            self.emp_entry.grid(row=36,column=3)
            self.emp_entry.set(select_lists['emp_type'][0])
            
            Allowance_change(self.emp_entry,self.amount_label)
            
            #emp_entry.bind('<<ComboboxSelected>>',)
            
            
        def Job_description(row_set):#仕事内容
            label = ttk.Label(frame,text=GUI_lists["job_description"], style=style_list["L"])
            label.grid(row=38,column=1)
            
            self.job_entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.job_entry.grid(row=38,column=3)
        
        
        def Rank_status(row_set):#等級
            label = ttk.Label(frame,text=GUI_lists["rank_status"], style=style_list["L"])
            label.grid(row=40,column=1)

            self.rank_combobox = ttk.Combobox(frame,width=10,values=self.rank_list,font=style_list["E"],state=style_list["S"])
            self.rank_combobox.grid(row=40,column=3)
            
            Work_place_rank_change(self.Work_place_combobox,self.rank_list,self.rank_combobox)
            
        
        def Contract_renewal(row_set):
            label = ttk.Label(frame,text=GUI_lists["Contract_renewal"], style=style_list["L"])
            label.grid(row=22,column=9)
            
            self.Contract_renewal_combobox = ttk.Combobox(frame,width=10,values=select_lists['presence_or_absence'],font=style_list["E"],state=style_list["S"])
            self.Contract_renewal_combobox.grid(row=22,column=10)
            
        
        def Renewal_day(row_set):
            label = ttk.Label(frame,text=GUI_lists["Renewal_day"], style=style_list["L"])
            label.grid(row=24,column=9)
            
            self.Renewal_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.Renewal_entry.grid(row=24,column=10)
            
            ToolTip(self.Renewal_entry, text="yyyy/mm/ddで入力")
            
            
            
        
        def Salary_notes(row_set):#給与関係の備考
            label = ttk.Label(frame,text=GUI_lists["salary_notes"], style=style_list["L"])
            label.grid(row=42,column=1)
            
            self.salary_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.salary_entry.grid(row=42,column=3)
            
            Open_text_box(self.salary_entry)
            
        
        def Working_conditions(row_set):#労働条件
            label = ttk.Label(frame,text=GUI_lists["working_conditions"], style=style_list["L"])
            label.grid(row=34,column=6,columnspan=2)
            

        def Working_start_time(row_set):#出勤時間
            label = ttk.Label(frame,text=GUI_lists["working_start"], style=style_list["L"])
            label.grid(row=36,column=6)
            
            self.work_start_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_start_entry.grid(row=36,column=7)
            
            ToolTip_time(self.work_start_entry, text="hh:mmで入力")
            
        
        def Working_end_time(row_set):#退勤時間
            label = ttk.Label(frame,text=GUI_lists["working_end"], style=style_list["L"])
            label.grid(row=38,column=6)
            
            self.work_end_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_end_entry.grid(row=38,column=7)
            
            ToolTip_time(self.work_end_entry, text="hh:mmで入力")
        
        
        def Working_break_time(row_set):#休憩時間
            label = ttk.Label(frame,text=GUI_lists["working_break_time"], style=style_list["L"])
            label.grid(row=40,column=6)
            
            self.work_break_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_break_entry.grid(row=40,column=7)
        
        
        def Working_week_time(row_set):#週の勤務時間
            label = ttk.Label(frame,text=GUI_lists["working_week_time"], style=style_list["L"])
            label.grid(row=42,column=6)
            
            self.work_week_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_week_entry.grid(row=42,column=7)
            
            
        def Overtime_or(row_set):#残業の有無
            label = ttk.Label(frame,text=GUI_lists["working_overtime"], style=style_list["L"])
            label.grid(row=36,column=9)
            
            self.work_over_combobox = ttk.Combobox(frame,values=select_lists['presence_or_absence'],
                                                   width=9,font=style_list["E"],state=style_list["S"])
            self.work_over_combobox.grid(row=36,column=10)
            

        def Overtime_start(row_set):#残業開始時間
            label = ttk.Label(frame,text=GUI_lists["working_over_start"], style=style_list["L"])
            label.grid(row=38,column=9)
            
            self.work_over_start_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_over_start_entry.grid(row=38,column=10)
            
            ToolTip_time(self.work_over_start_entry, text="hh:mmで入力")
        
        
        def Overtime_end(row_set):#残業終了時間
            label = ttk.Label(frame,text=GUI_lists["working_over_end"], style=style_list["L"])
            label.grid(row=40,column=9)
            
            self.work_over_end_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_over_end_entry.grid(row=40,column=10)
            
            ToolTip_time(self.work_over_end_entry, text="hh:mmで入力")    
        
        
        def Holiday(row_set):#休日に関して
            label = ttk.Label(frame,text=GUI_lists["holiday"], style=style_list["L"])
            label.grid(row=42,column=9)
            
            self.holiday_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.holiday_entry.grid(row=42,column=10)
            
            Open_text_box(self.holiday_entry)
        
        
        def Employment_insurance(row_set):#雇用保険
            label = ttk.Label(frame,text=GUI_lists["employment_insurance"], style=style_list["L"])
            label.grid(row=46,column=1)
            
            emp_ins_frame = ttk.Frame(frame)
            emp_ins_frame.grid(row=46,column=3,columnspan=5)
            
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
            label.grid(row=48,column=1)
            
            soc_ins_frame = ttk.Frame(frame)
            soc_ins_frame.grid(row=48,column=3,columnspan=5)
            
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
            label.grid(row=46,column=9)
            
            self.est_of_p_combobox = ttk.Combobox(frame,values=select_lists['presence_or_absence'],
                                                   width=9,font=style_list["E"],state=style_list["S"])
            self.est_of_p_combobox.grid(row=46,column=10)
            
        
        def Period(row_set):#試用期間
            label = ttk.Label(frame,text=GUI_lists["period"], style=style_list["L"])
            label.grid(row=48,column=9)
            
            self.trial_period_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.trial_period_entry.grid(row=48,column=10)
            
            ToolTip(self.trial_period_entry, text="試用期間があれば入力")
        
        
        def Registration_button(row_set):
            Registr_button = ttk.Button(frame,text=GUI_lists["Registration"], style=style_list["B"],command=Datail_summarize)
            Registr_button.grid(row=100,column=0,columnspan=11,pady=10)
        
        #,"":
        def Datail_summarize():

            

            
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
                    "週の勤務時間":self.work_week_entry,"残業の有無":self.work_over_combobox,
                    "残業開始時間":self.work_over_start_entry,"残業終了時間":self.work_over_end_entry,"休日":self.holiday_entry,
                    "雇用保険の有無":self.emp_ins_combobox,"雇用保険番号":self.emp_ins_entry,
                    "社会保険の有無":self.soc_ins_combobox,"社会保険番号":self.soc_ins_entry,
                    "定めの期間の有無":self.est_of_p_combobox,"試用期間":self.trial_period_entry,
                    "更新の有無":self.Contract_renewal_combobox,"更新日":self.Renewal_entry}
            
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
                print("登録")
                #Interim_arrangement(data)
            
            
        
        
        
        
        row_set()
        