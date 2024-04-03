import tkinter as tk
from tkinter import ttk

from datetime import datetime

import json

from staff_manegement_app.data.SQL import MySQL_New_Registration



class Interim_arrangement(object):
    def __init__(self, data):
        self.data = data
        self.date_conversion()
        self.Data_Organization()
        
    def date_conversion(self):
        
        con_date = datetime.strptime(self.data["入社日"], "%Y/%m/%d")
        self.joining_date = con_date.strftime("%Y-%m-%d")
    
    def Data_Organization(self):
        
        Mr_data = {"氏": self.data["f名前"],"カナ": self.data["fカナ"]}
        Name = {"名":self.data["l名前"],"カナ":self.data["lカナ"]}
        Staff_details = {"性別":self.data["性別"],"生年月日":self.data["生年月日"],"電話番号":self.data["電話番号"],"郵便番号":self.data["郵便番号"],"住所":self.data["住所"]}
        Soc_details = {"有無":self.data["社会保険の有無"],"番号":self.data["社会保険番号"]}
        Emp_details = {"有無":self.data["雇用保険の有無"],"番号":self.data["雇用保険番号"]}
        Dependent_details = {"扶養":self.data["扶養"],"人数":self.data["扶養の人数"]}
        Under1_details = {"名前":self.data["1名前"],"続柄":self.data["1続柄"],"電話番号":self.data["1電話番号"],"勤務先":self.data["1勤務先"]}
        Under2_details = {"名前":self.data["2名前"],"続柄":self.data["2続柄"],"電話番号":self.data["2電話番号"],"勤務先":self.data["2勤務先"]}
        Renewal_details = {"更新":self.data["更新の有無"],"更新日":self.data["更新日"]}
        Job_time_details = {"出勤":self.data["出勤時間"],"退勤":self.data["退勤時間"],"休憩":self.data["休憩時間"],"1週間":self.data["週の勤務時間"]}
        Over_time_details = {"有無":self.data["残業の有無"],"開始":self.data["残業開始時間"],"終了":self.data["残業終了時間"]}
        Means_details = {"通勤手段":self.data["通勤手段"],"交通費":self.data["メインの交通費"]}
        Sub_means_details = {"店舗1":0,"店舗2":0,"店舗3":0,"店舗4":0}
        
        
        
        
        
        Mr_data = json.dumps(Mr_data, ensure_ascii=False)
        Name_data = json.dumps(Name, ensure_ascii=False)
        Staff_data = json.dumps(Staff_details, ensure_ascii=False)
        Soc_data = json.dumps(Soc_details, ensure_ascii=False)
        Emp_data = json.dumps(Emp_details, ensure_ascii=False)
        Dependent_data = json.dumps(Dependent_details, ensure_ascii=False)
        Under1_data = json.dumps(Under1_details, ensure_ascii=False)
        Under2_data = json.dumps(Under2_details, ensure_ascii=False)
        Renewal_data = json.dumps(Renewal_details, ensure_ascii=False)
        Job_time_data = json.dumps(Job_time_details, ensure_ascii=False)
        Over_time_data = json.dumps(Over_time_details, ensure_ascii=False)
        Means_data = json.dumps(Means_details, ensure_ascii=False)
        Sub_means_data = json.dumps(Sub_means_details, ensure_ascii=False)
        
        
        
        
        
        
        
        Datail_list = {"氏": Mr_data, "名": Name_data, "スタッフ詳細": Staff_data, "社会保険": Soc_data, "雇用保険": Emp_data,
                       "扶養": Dependent_data, "身元引受人1": Under1_data, "身元引受人2": Under2_data, "入社日": self.joining_date,
                       "更新": Renewal_data, "期間の定め": self.data["定めの期間の有無"], "試用期間": self.data["試用期間"], 
                       "勤務形態": self.data["雇用形態"], "所属店舗": self.data["就業場所"],"等級": self.data["等級"], 
                       "勤務時間": Job_time_data,"残業": Over_time_data,"休日": self.data["休日"],"主な交通費": Means_data, 
                       "サブ交通費": Sub_means_data, "備考欄": self.data["備考"], "給与備考": self.data["給与備考"], "在籍状況": "在籍中"}
        
        
        MySQL_New_Registration(Datail_list)
        

        
        
        
        
