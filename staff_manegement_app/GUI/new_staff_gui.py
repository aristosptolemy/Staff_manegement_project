import tkinter as tk
from tkinter import ttk
from ..GUI_Logic.tooltip_day import ToolTip , ToolTip_time,ToolTip_error,ToolTip_error_Post
from ..GUI_Logic.text_box_RE import Open_text_box
from ..GUI_Logic.Logic_etc import Allowance_change , Work_place_rank_change
from ..GUI_Logic.format_change import FormatConvert_tell
from staff_manegement_app.data.SQL import Rank_List_Manager
from staff_manegement_app.data.staff_registration import Interim_arrangement
from staff_manegement_app.GUI.load_config import load_GUI_file
from staff_manegement_app.GUI.load_config import load_List_file




GUI_lists = load_GUI_file()
select_lists = load_List_file()



class StaffDetailTab:
    def __init__(self, notebook, amount_label, rank_list):
        self.notebook = notebook
        self.amount_label = amount_label
        self.rank_list = rank_list
        self.setup_tab()

    def setup_tab(self):
        

        # スタイル設定
        style = ttk.Style()
        style.configure("EntryStyle.TEntry", font=("Arial", 18))

        # タブの作成
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text='新規スタッフ入力')

        # スクロール機能を持つフレームの設定
        self.staff_input_frame = self.setup_scrollable_frame(tab1)
        
        self.new_staff_detail(self.staff_input_frame)

        # スタッフ詳細入力ウィジェットの設定
        #self.setup_staff_detail_widgets(self.staff_input_frame)
        
    def setup_scrollable_frame(self, tab1):
        # スクロールバーの設定
        tab1_scrollbar = ttk.Scrollbar(tab1, orient='vertical')
        tab1_scrollbar.pack(side='right', fill='y')

        # スクロール可能なキャンバスの作成
        canvas = tk.Canvas(tab1, yscrollcommand=tab1_scrollbar.set)
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

        # Linux用のバインディング（上スクロール）
        canvas.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
        # Linux用のバインディング（下スクロール）
        canvas.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))

        # キャンバス上に配置するウィジェット用のフレーム
        staff_input_frame = ttk.Frame(canvas)
        staff_input_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=staff_input_frame, anchor='nw')
        return staff_input_frame



    # スタッフ詳細入力ウィジェットの設定
    def new_staff_detail(self,frame):
        style_list = {
            "L":"LabelStyle.TLabel",
            "E":("Arial", 18),
            "S":"read_only",
            "U":"UnderStyle.TLabel",
            "B":"ButtonStyle.TButton"
        }
        c_span_max = 13
        row_max = 50

        #padx=4 横幅
        #pady=4　縦幅

        # ラベルの作成と配置
        
        


        
        def sepa():
            kana_C_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_C_sepa.grid(row=1, column=5, rowspan=5, sticky="ns",padx=4)
            
            kana_R_sepa = ttk.Separator(frame,orient="vertical")#垂直
            kana_R_sepa.grid(row=1, column=8, rowspan=row_max, sticky="ns",padx=4)
            
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
            


        def kana_area():#氏名　カナ
        
            kana_label = ttk.Label(frame, text=GUI_lists['kana_name'], style=style_list["L"])
            kana_label.grid(row=2,column=1)
        
            self.kana1_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.kana1_entry.grid(row=2,column=3,columnspan=2)
            
            self.kana2_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.kana2_entry.grid(row=2,column=6,columnspan=2)
                    
        
        def name_area():#氏名
            name_label = ttk.Label(frame,text=GUI_lists["name"], style=style_list["L"])
            name_label.grid(row=4,column=1)
            
            self.f_name_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.f_name_entry.grid(row=4,column=3,columnspan=2)
            
            self.l_name_entry = ttk.Entry(frame,width=20, font=style_list["E"])
            self.l_name_entry.grid(row=4,column=6,columnspan=2)
        
        
        def gender_choice():#性別選択
            
            gender_label = ttk.Label(frame,text=GUI_lists["gender"], style=style_list["L"])
            gender_label.grid(row=2,column=9)
            
            self.gender_combobox = ttk.Combobox(frame,values=select_lists['gender'],width=10,font=style_list["E"],state=style_list["S"])
            self.gender_combobox.grid(row=2,column=10)
        
        
        def birthday():#生年月日
            birthday_label = ttk.Label(frame,text=GUI_lists["birthday"], style=style_list["L"])
            birthday_label.grid(row=4,column=9)
            
            self.birthday_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.birthday_entry.grid(row=4,column=10)
            
            ToolTip(self.birthday_entry, text="yyyy/mm/ddで入力")

        
        def cell_phone_area():#携帯電話
            
            cell_phone_label = ttk.Label(frame,text=GUI_lists["phone"], style=style_list["L"])
            cell_phone_label.grid(row=8,column=1)
            
            self.phone_code = ttk.Entry(frame,width=41,font=style_list["E"])
            self.phone_code.grid(row=8,column=3,columnspan=5)


            ToolTip_error(self.phone_code,GUI_lists["phone"])
            
    
            
        def tell_area():#固定電話
            
            cell_tell_label = ttk.Label(frame,text=GUI_lists["tell"], style=style_list["L"])
            cell_tell_label.grid(row=10,column=1)
            
            self.tell_code = ttk.Entry(frame,width=41,font=style_list["E"])
            self.tell_code.grid(row=10,column=3,columnspan=5)
            
            
            ToolTip_error(self.tell_code,GUI_lists["tell"])
            
            
            
        def Joining_the_company_day():#入社日
            #入社日
            label = ttk.Label(frame,text=GUI_lists["Joining"], style=style_list["L"])
            label.grid(row=8,column=9)
            
            self.Joining_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.Joining_entry.grid(row=8,column=10)
            
            ToolTip(self.Joining_entry, text="yyyy/mm/ddで入力")
            
        
        def remarks_area():#備考
            label = ttk.Label(frame,text=GUI_lists["main_remarks"], style=style_list["L"])
            label.grid(row=10,column=9)
            
            self.remarks_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.remarks_entry.grid(row=10,column=10)
            
            Open_text_box(self.remarks_entry)
        
        
        def address_kana_area():#住所　カナ
            label = ttk.Label(frame,text=GUI_lists["kana_name"], style=style_list["L"])
            label.grid(row=14,column=1)
            
            self.address_kana_entry = ttk.Entry(frame,width=41,font=style_list["E"])
            self.address_kana_entry.grid(row=14,column=3,columnspan=5)
            
            
        def address_area():#住所
            label = ttk.Label(frame,text=GUI_lists["address"], style=style_list["L"])
            label.grid(row=16,column=1)
            
            self.address_entry = ttk.Entry(frame,width=41,font=style_list["E"])
            self.address_entry.grid(row=16,column=3,columnspan=5)
            
        
        def post_number_area():#郵便番号
            label = ttk.Label(frame,text=GUI_lists["post"], style=style_list["L"])
            label.grid(row=18,column=1)
            
            number_frame = ttk.Frame(frame)
            number_frame.grid(row=18,column=3,columnspan=3)
            
            self.Post_number = ttk.Entry(number_frame,width=20,font=style_list["E"])
            self.Post_number.grid(row=0,column=0)
            
            ToolTip_error_Post(self.Post_number,GUI_lists["post"])
            
            
        def dependent_area():#扶養
            label = ttk.Label(frame,text=GUI_lists["dependent"], style=style_list["L"])
            label.grid(row=14,column=9)
            
            self.dependent_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.dependent_entry.grid(row=14,column=10)
            
            Open_text_box(self.dependent_entry)
            
        
        def dependent_people_area():#扶養の人数
            label = ttk.Label(frame,text=GUI_lists["people"], style=style_list["L"])
            label.grid(row=16,column=9)
            
            self.dependent_people_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.dependent_people_entry.grid(row=16,column=10)
            
        
        def Means_of_commuting():#通勤手段
            label = ttk.Label(frame,text=GUI_lists["means"], style=style_list["L"])
            label.grid(row=18,column=9)
            
            self.Means_combobox = ttk.Combobox(frame,width=10,values=select_lists['means'],font=style_list["E"])
            self.Means_combobox.option_add("*TCombobox*Listbox.Font", ('HGP教科書体', 16))
            self.Means_combobox.grid(row=18,column=10)
        
        
        def Means_amount():#メインの交通費
            
            label = ttk.Label(frame,textvariable=self.amount_label, style=style_list["L"])
            label.grid(row=20,column=9)
            
            self.Means_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.Means_entry.grid(row=20,column=10)
            
        
        def Underwriter():#身元引受人(ラベル)
            main_label = ttk.Label(frame,text=f'{GUI_lists["under"]}', style=style_list["U"])
            main_label.grid(row=22,column=1)
            
        
        def U_number():
            label = ttk.Label(frame,text="1人目", style=style_list["L"])
            label.grid(row=22,column=3,columnspan=2)
            label_2 = ttk.Label(frame,text="2人目", style=style_list["L"])
            label_2.grid(row=22,column=6,columnspan=2)
            
        
        def Under_name_label():#身元引受人　名前(ラベル)
            label = ttk.Label(frame,text=GUI_lists["name"], style=style_list["L"])
            label.grid(row=24,column=1)
            

        def relationship_label():#身元引受人　続柄(ラベル)
            label = ttk.Label(frame,text=GUI_lists["relationship"], style=style_list["L"])
            label.grid(row=26,column=1)
            
        
        def Under_phone_label():#身元引受人　電話番号(ラベル)
            label = ttk.Label(frame,text=GUI_lists["phone"], style=style_list["L"])
            label.grid(row=28,column=1)
            
        
        def Under_work():#身元引受人　勤務先(ラベル)
            label = ttk.Label(frame,text=GUI_lists["place_of_work"], style=style_list["L"])
            label.grid(row=30,column=1)
        
            
        #1人目入力    
        def Under_1_name():
            self.Under_1_name_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_name_Entry.grid(row=24,column=3,columnspan=2)
            
            
        def Under_1_relationship():
            self.Under_1_relationship_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_relationship_Entry.grid(row=26,column=3,columnspan=2)
            
        
        def Under_1_phone():
            self.Under_1_phone_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_phone_Entry.grid(row=28,column=3,columnspan=2)
        
        
        def Under_1_work():
            self.Under_1_work_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_1_work_Entry.grid(row=30,column=3,columnspan=2)
        
        
        #2人目入力
        
        def Under_2_name():
            self.Under_2_name_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_name_Entry.grid(row=24,column=6,columnspan=2)
            
            
        def Under_2_relationship():
            self.Under_2_relationship_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_relationship_Entry.grid(row=26,column=6,columnspan=2)
            
        
        def Under_2_phone():
            self.Under_2_phone_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_phone_Entry.grid(row=28,column=6,columnspan=2)
        
        
        def Under_2_work():
            self.Under_2_work_Entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.Under_2_work_Entry.grid(row=30,column=6,columnspan=2)
          
            
        
        def Work_place():#就業場所
            label = ttk.Label(frame,text=GUI_lists["work_place"], style=style_list["L"])
            label.grid(row=34,column=1)
            
            self.Work_place_combobox = ttk.Combobox(frame,width=10,values=select_lists['work_place'],font=style_list["E"],state=style_list["S"])
            self.Work_place_combobox.grid(row=34,column=3)
            
                 
        def Employment_status():#雇用形態
            
            label = ttk.Label(frame,text=GUI_lists["emp_type"], style=style_list["L"])
            label.grid(row=36,column=1)
            
            self.emp_entry = ttk.Combobox(frame,width=10,values=select_lists['emp_type'],font=style_list["E"],state=style_list["S"])
            self.emp_entry.grid(row=36,column=3)
            self.emp_entry.set(select_lists['emp_type'][0])
            
            Allowance_change(self.emp_entry,self.amount_label)
            
            #emp_entry.bind('<<ComboboxSelected>>',)
            
            
        def Job_description():#仕事内容
            label = ttk.Label(frame,text=GUI_lists["job_description"], style=style_list["L"])
            label.grid(row=38,column=1)
            
            self.job_entry = ttk.Entry(frame,width=20,font=style_list["E"])
            self.job_entry.grid(row=38,column=3)
        
        
        def Rank_status():#等級
            label = ttk.Label(frame,text=GUI_lists["rank_status"], style=style_list["L"])
            label.grid(row=40,column=1)

            self.rank_combobox = ttk.Combobox(frame,width=10,values=self.rank_list,font=style_list["E"],state=style_list["S"])
            self.rank_combobox.grid(row=40,column=3)
            
            Work_place_rank_change(self.Work_place_combobox,self.rank_list,self.rank_combobox)
            
        
        def Contract_renewal():
            label = ttk.Label(frame,text=GUI_lists["Contract_renewal"], style=style_list["L"])
            label.grid(row=22,column=9)
            
            self.Contract_renewal_combobox = ttk.Combobox(frame,width=10,values=select_lists['presence_or_absence'],font=style_list["E"],state=style_list["S"])
            self.Contract_renewal_combobox.grid(row=22,column=10)
            
        
        def Renewal_day():
            label = ttk.Label(frame,text=GUI_lists["Renewal_day"], style=style_list["L"])
            label.grid(row=24,column=9)
            
            self.Renewal_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.Renewal_entry.grid(row=24,column=10)
            
            ToolTip(self.Renewal_entry, text="yyyy/mm/ddで入力")
            
            
            
        
        def Salary_notes():#給与関係の備考
            label = ttk.Label(frame,text=GUI_lists["salary_notes"], style=style_list["L"])
            label.grid(row=42,column=1)
            
            self.salary_entry = ttk.Entry(frame,width=12,font=style_list["E"])
            self.salary_entry.grid(row=42,column=3)
            
            Open_text_box(self.salary_entry)
            
        
        def Working_conditions():#労働条件
            label = ttk.Label(frame,text=GUI_lists["working_conditions"], style=style_list["L"])
            label.grid(row=34,column=6,columnspan=2)
            

        def Working_start_time():#出勤時間
            label = ttk.Label(frame,text=GUI_lists["working_start"], style=style_list["L"])
            label.grid(row=36,column=6)
            
            self.work_start_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_start_entry.grid(row=36,column=7)
            
            ToolTip_time(self.work_start_entry, text="hh:mmで入力")
            
        
        def Working_end_time():#退勤時間
            label = ttk.Label(frame,text=GUI_lists["working_end"], style=style_list["L"])
            label.grid(row=38,column=6)
            
            self.work_end_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_end_entry.grid(row=38,column=7)
            
            ToolTip_time(self.work_end_entry, text="hh:mmで入力")
        
        
        def Working_break_time():#休憩時間
            label = ttk.Label(frame,text=GUI_lists["working_break_time"], style=style_list["L"])
            label.grid(row=40,column=6)
            
            self.work_break_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_break_entry.grid(row=40,column=7)
        
        
        def Working_week_time():#週の勤務時間
            label = ttk.Label(frame,text=GUI_lists["working_week_time"], style=style_list["L"])
            label.grid(row=42,column=6)
            
            self.work_break_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_break_entry.grid(row=42,column=7)
            
            
        def Overtime_or():#残業の有無
            label = ttk.Label(frame,text=GUI_lists["working_overtime"], style=style_list["L"])
            label.grid(row=36,column=9)
            
            self.work_over_combobox = ttk.Combobox(frame,values=select_lists['presence_or_absence'],
                                                   width=9,font=style_list["E"],state=style_list["S"])
            self.work_over_combobox.grid(row=36,column=10)
            

        def Overtime_start():#残業開始時間
            label = ttk.Label(frame,text=GUI_lists["working_over_start"], style=style_list["L"])
            label.grid(row=38,column=9)
            
            self.work_over_start_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_over_start_entry.grid(row=38,column=10)
            
            ToolTip_time(self.work_over_start_entry, text="hh:mmで入力")
        
        
        def Overtime_end():#残業終了時間
            label = ttk.Label(frame,text=GUI_lists["working_over_end"], style=style_list["L"])
            label.grid(row=40,column=9)
            
            self.work_over_end_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.work_over_end_entry.grid(row=40,column=10)
            
            ToolTip_time(self.work_over_end_entry, text="hh:mmで入力")    
        
        
        def Holiday():#休日に関して
            label = ttk.Label(frame,text=GUI_lists["holiday"], style=style_list["L"])
            label.grid(row=42,column=9)
            
            self.holiday_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.holiday_entry.grid(row=42,column=10)
            
            Open_text_box(self.holiday_entry)
        
        
        def Employment_insurance():#雇用保険
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
        
        
        def Social_insurance():#社会保険
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
            
            
        def Establishment_of_period():#定めの期間の有無
            label = ttk.Label(frame,text=GUI_lists["establishment_of_period"], style=style_list["L"])
            label.grid(row=46,column=9)
            
            self.est_of_p_combobox = ttk.Combobox(frame,values=select_lists['presence_or_absence'],
                                                   width=9,font=style_list["E"],state=style_list["S"])
            self.est_of_p_combobox.grid(row=46,column=10)
            
        
        def Period():#試用期間
            label = ttk.Label(frame,text=GUI_lists["period"], style=style_list["L"])
            label.grid(row=48,column=9)
            
            self.trial_period_entry = ttk.Entry(frame,width=10,font=style_list["E"])
            self.trial_period_entry.grid(row=48,column=10)
            
            ToolTip(self.trial_period_entry, text="試用期間があれば入力")
        
        
        def Registration_button():
            Registr_button = ttk.Button(frame,text=GUI_lists["Registration"], style=style_list["B"],command=Datail_summarize)
            Registr_button.grid(row=100,column=0,columnspan=11,pady=10)
        
        #,"":
        def Datail_summarize():
            data = {"fカナ":self.kana1_entry.get(),"lカナ":self.kana2_entry.get(),
                    "f名前":self.f_name_entry.get(),"l名前":self.l_name_entry.get(),
                    "性別":self.gender_combobox.get(),"生年月日":self.birthday_entry.get(),"携帯電話":self.phone_code.get(),"固定電話":self.tell_code.get(),
                    "入社日":self.Joining_entry.get(),"備考":self.remarks_entry.get(),"住所カナ":self.address_kana_entry.get(),"住所":self.address_entry.get(),
                    "郵便番号":self.Post_number.get(),"扶養":self.dependent_entry.get(),"扶養の人数":self.dependent_people_entry.get(),"通勤手段":self.Means_combobox.get(),
                    "メインの交通費":self.Means_entry.get(),"1名前":self.Under_1_name_Entry.get(),"1続柄":self.Under_1_relationship_Entry.get(),
                    "1電話番号":self.Under_1_phone_Entry.get(),"1勤務先":self.Under_1_work_Entry.get(),
                    "2名前":self.Under_2_name_Entry.get(),"2続柄":self.Under_2_relationship_Entry.get(),"2電話番号":self.Under_2_phone_Entry.get(),
                    "2勤務先":self.Under_2_work_Entry.get(),"就業場所":self.Work_place_combobox.get(),"雇用形態":self.emp_entry.get(),
                    "仕事内容":self.job_entry.get(),"等級":self.rank_combobox.get(),"給与備考":self.salary_entry.get(),
                    "出勤時間":self.work_start_entry.get(),"退勤時間":self.work_end_entry.get(),"休憩時間":self.work_break_entry.get(),
                    "週の勤務時間":self.work_break_entry.get(),"残業の有無":self.work_over_combobox.get(),
                    "残業開始時間":self.work_over_start_entry.get(),"残業終了時間":self.work_over_end_entry.get(),"休日":self.holiday_entry.get(),
                    "雇用保険の有無":self.emp_ins_combobox.get(),"雇用保険番号":self.emp_ins_entry.get(),
                    "社会保険の有無":self.soc_ins_combobox.get(),"社会保険番号":self.soc_ins_entry.get(),
                    "定めの期間の有無":self.est_of_p_combobox.get(),"試用期間":self.trial_period_entry.get(),
                    "更新の有無":self.Contract_renewal_combobox.get(),"更新日":self.Renewal_entry.get()}
            Interim_arrangement(data)
            
            
        
        
        
        
        
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
