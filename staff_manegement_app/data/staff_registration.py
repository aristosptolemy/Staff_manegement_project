
from datetime import datetime

import json





class Interim_arrangement(object):
    def __init__(self, data):
        self.data = data
        self.date_conversion()
        self.Data_Organization()
        
    def date_conversion(self):
        try:
            con_date = datetime.strptime(self.data["入社日"].get(), "%Y/%m/%d")
            self.joining_date = con_date.strftime("%Y-%m-%d")
            bir_date = datetime.strptime(self.data["生年月日"].get(), "%Y/%m/%d")
            self.birthday_date = bir_date.strftime("%Y-%m-%d")
            if self.data["更新の有無"].get() == "有":
                up_date = datetime.strptime(self.data["更新日"].get(), "%Y/%m/%d")
                self.update_date = up_date.strftime("%Y-%m-%d")
            else:
                self.update_date = ""
            
        except Exception as e:
            print(e)
            pass
    
    def Data_Organization(self):
        
        Mr_data = {"氏": self.data["f名字"].get(),"カナ": self.data["fカナ"].get()}
        Name = {"名":self.data["l名前"].get(),"カナ":self.data["lカナ"].get()}
        Staff_details = {"性別":self.data["性別"].get(),"生年月日":self.birthday_date,"携帯電話":self.data["携帯電話"].get(),"固定電話":self.data["固定電話"].get(),"郵便番号":self.data["郵便番号"].get(),"住所":self.data["住所"].get(),"住所カナ":self.data["住所カナ"].get()}
        Soc_details = {"有無":self.data["社会保険の有無"].get(),"番号":self.data["社会保険番号"].get()}
        Emp_details = {"有無":self.data["雇用保険の有無"].get(),"番号":self.data["雇用保険番号"].get()}
        Dependent_details = {"扶養":self.data["扶養"].get(),"人数":self.data["扶養の人数"].get()}
        Under1_details = {"名前":self.data["1名前"].get(),"続柄":self.data["1続柄"].get(),"電話番号":self.data["1電話番号"].get(),"勤務先":self.data["1勤務先"].get()}
        Under2_details = {"名前":self.data["2名前"].get(),"続柄":self.data["2続柄"].get(),"電話番号":self.data["2電話番号"].get(),"勤務先":self.data["2勤務先"].get()}
        Renewal_details = {"更新":self.data["更新の有無"].get(),"更新日":self.update_date}
        Job_time_details = {"出勤":self.data["出勤時間"].get(),"退勤":self.data["退勤時間"].get(),"休憩":self.data["休憩時間"].get(),"1週間":self.data["週の勤務時間"].get()}
        Over_time_details = {"有無":self.data["残業の有無"].get(),"開始":self.data["残業開始時間"].get(),"終了":self.data["残業終了時間"].get()}
        Means_details = {"通勤手段":self.data["通勤手段"].get(),f"通勤{self.data["手当種類"].get()}":self.data["メインの交通費"].get()}
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
                       "更新": Renewal_data, "期間の定め": self.data["定めの期間の有無"].get(), "試用期間": self.data["試用期間"].get(), 
                       "雇用形態": self.data["雇用形態"].get(), "就業場所": self.data["就業場所"].get(),"等級": self.data["等級"].get(), 
                       "仕事内容":self.data["仕事内容"].get(),"勤務時間": Job_time_data,"残業": Over_time_data,"休日": self.data["休日"].get(),"主な交通費": Means_data, 
                       "サブ交通費": Sub_means_data, "備考欄": self.data["備考"].get(), "給与備考": self.data["給与備考"].get(), "在籍状況": "在籍中"}
        
        from staff_manegement_app.data.SQL_center import MySQL_New_Registration
        MySQL_New_Registration(Datail_list)
        

        

        
        
        
        
class Interim_update:
    def __init__(self, data,id_data):
        self.data = data
        self.id_data = id_data
        self.date_conversion()
        self.Data_Organization()
        
    def date_conversion(self):
        try:
            con_date = datetime.strptime(self.data["入社日"].get(), "%Y/%m/%d")
            self.joining_date = con_date.strftime("%Y-%m-%d")
            bir_date = datetime.strptime(self.data["生年月日"].get(), "%Y/%m/%d")
            self.birthday_date = bir_date.strftime("%Y-%m-%d")
            if self.data["更新の有無"].get() == "有":
                up_date = datetime.strptime(self.data["更新日"].get(), "%Y/%m/%d")
                self.update_date = up_date.strftime("%Y-%m-%d")
            else:
                self.update_date = ""
            
        except Exception as e:
            print(e)
            pass
    
    def Data_Organization(self):
        
        Mr_data = {"氏": self.data["f名字"].get(),"カナ": self.data["fカナ"].get()}
        Name = {"名":self.data["l名前"].get(),"カナ":self.data["lカナ"].get()}
        Staff_details = {"性別":self.data["性別"].get(),"生年月日":self.birthday_date,"携帯電話":self.data["携帯電話"].get(),"固定電話":self.data["固定電話"].get(),"郵便番号":self.data["郵便番号"].get(),"住所":self.data["住所"].get(),"住所カナ":self.data["住所カナ"].get()}
        Soc_details = {"有無":self.data["社会保険の有無"].get(),"番号":self.data["社会保険番号"].get()}
        Emp_details = {"有無":self.data["雇用保険の有無"].get(),"番号":self.data["雇用保険番号"].get()}
        Dependent_details = {"扶養":self.data["扶養"].get(),"人数":self.data["扶養の人数"].get()}
        Under1_details = {"名前":self.data["1名前"].get(),"続柄":self.data["1続柄"].get(),"電話番号":self.data["1電話番号"].get(),"勤務先":self.data["1勤務先"].get()}
        Under2_details = {"名前":self.data["2名前"].get(),"続柄":self.data["2続柄"].get(),"電話番号":self.data["2電話番号"].get(),"勤務先":self.data["2勤務先"].get()}
        Renewal_details = {"更新":self.data["更新の有無"].get(),"更新日":self.update_date}
        Job_time_details = {"出勤":self.data["出勤時間"].get(),"退勤":self.data["退勤時間"].get(),"休憩":self.data["休憩時間"].get(),"1週間":self.data["週の勤務時間"].get()}
        Over_time_details = {"有無":self.data["残業の有無"].get(),"開始":self.data["残業開始時間"].get(),"終了":self.data["残業終了時間"].get()}
        Means_details = {"通勤手段":self.data["通勤手段"].get(),f"通勤{self.data["手当種類"].get()}":self.data["メインの交通費"].get()}
        Sub_means_details = {self.data["サブ1店舗"].get():self.data["サブ1金額"].get(),self.data["サブ2店舗"].get():self.data["サブ2金額"].get(),
                             self.data["サブ3店舗"].get():self.data["サブ3金額"].get(),self.data["サブ4店舗"].get():self.data["サブ4金額"].get()}
        
        
        
        
        
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
                       "更新": Renewal_data, "期間の定め": self.data["定めの期間の有無"].get(), "試用期間": self.data["試用期間"].get(), 
                       "雇用形態": self.data["雇用形態"].get(), "就業場所": self.data["就業場所"].get(),"等級": self.data["等級"].get(), 
                       "仕事内容":self.data["仕事内容"].get(),"勤務時間": Job_time_data,"残業": Over_time_data,"休日": self.data["休日"].get(),"主な交通費": Means_data, 
                       "サブ交通費": Sub_means_data, "備考欄": self.data["備考"].get(), "給与備考": self.data["給与備考"].get(), "在籍状況": "在籍中"}
        
        from staff_manegement_app.data.SQL_center import MySQL_Staff_Update
        MySQL_Staff_Update(Datail_list,self.id_data)
        

        

        
        
        
        
