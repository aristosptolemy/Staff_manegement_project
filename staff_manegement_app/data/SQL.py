import mysql.connector
import json
"""
from staff_manegement_app.GUI.staff_details_GUI import Staff_Details_Display
from ..GUI_Logic.staff_search_logic import Search_Staff_List_INSERT

from staff_manegement_app.GUI.load_config import load_GUI_file
from staff_manegement_app.GUI.load_config import load_List_file

from .encryption_conversion import Encryption_Data_Conversion

GUI_lists = load_GUI_file()
select_lists = load_List_file()
"""

config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'port': '3306',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema',
    'auth_plugin': 'mysql_native_password',
}


My_SQL_table_Name = "staff_list_test"


class Rank_List_Manager(object):
    def __init__(self):
        
        self.rank_number_list_store_get()
    
    def rank_number_list_store_get(self):
        
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                            SELECT 等級,サブランク FROM rank_list
                            ;''')
            result = cursor.fetchall()
            rank_number = []
            for i,b in result:
                if b == "As":
                    insert = "ｱｼｽﾀﾝﾄ"
                else:
                    insert = b
                rank_number.append((i,insert))
            
            rank_ = sorted(rank_number, key=lambda x: (x[0], -ord(x[1][0]) if x[1][0].isalpha() else x[1]), reverse=True)
            rank_num_list = []
            for f1,s2 in rank_:
                if s2 == 'ｱｼｽﾀﾝﾄ':
                    insert = s2
                else:
                    insert = f'{f1}{s2}'
                rank_num_list.append(insert)
        print(rank_num_list)
        return rank_num_list
            

    def rank_number_list_office_get(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                            SELECT 等級,サブランク FROM office_rank_list
                            ;''')
            result = cursor.fetchall()
            rank_number = []
            for i,b in result:
                insert = i
                rank_number.append(insert)
            rank_num_list = sorted(rank_number, reverse=True)
        return rank_num_list
    

class MySQL_New_Registration(object):
    def __init__(self,data):
        self.data = data
        
        self.Encryption_Conversion_data = Encryption_Data_Conversion(self.data)
        set_data = self.Encryption_Conversion_data.get_data()

        self.MySQL_insert(set_data)

        
    def MySQL_insert(self,data):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            #print(data)
            
            
            
            cursor.execute(f'''
                        INSERT INTO {My_SQL_table_Name} (氏,名,スタッフ詳細,社会保険,雇用保険,扶養,身元引受人１,身元引受人２,入社日,
                        更新,期間の定め,試用期間,雇用形態,就業場所,等級,勤務時間,残業,主な交通費,サブ交通費,備考欄,給与備考,在籍状況) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',
                        (data["氏"],data["名"],data["スタッフ詳細"],data["社会保険"],data["雇用保険"],
                         data["扶養"],data["身元引受人1"],data["身元引受人2"],data["入社日"],
                         data["更新"],data["期間の定め"],data["試用期間"],data["雇用形態"],data["就業場所"],
                         data["等級"],data["勤務時間"],data["残業"],data["主な交通費"],data["サブ交通費"],
                         data["備考欄"],data["給与備考"],data["在籍状況"]))
            
            conn.commit()
            


class MySQL_Staff_Search(object):
    def __init__(self, data, widget):
        self.data = data
        self.widget = widget
        self.MySQL_search()

    def MySQL_search(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            
            query = f"""SELECT * FROM {My_SQL_table_Name} WHERE 1=1"""
            params = []

            # 条件をチェックしてクエリとパラメータを組み立てる
            for key, value in self.data.items():
                if isinstance(value, dict):  # ネストされた辞書の処理
                    for sub_key, sub_value in value.items():
                        if sub_value:  # 空の文字列でない場合に条件を追加

                            if key == "氏":
                                query += f''' AND JSON_EXTRACT(氏, '$."{sub_key}"') = %s'''
                                params.append(sub_value)
                            elif key == "名":
                                query += f''' AND JSON_EXTRACT(名, '$."{sub_key}"') = %s'''
                                params.append(sub_value)
                            elif key == "性別":
                                query += f''' AND JSON_EXTRACT(スタッフ詳細, '$."{sub_key}"') = %s'''
                                params.append(sub_value)
                elif value:  # ネストされていない直接の値の処理
                    query += f" AND {key} = %s"
                    params.append(value)
            
            cursor.execute(query, params)
            results = cursor.fetchall()
            
            Search_Staff_List_INSERT(results,self.widget)
            

            
class MySQL_Select_Details(object):
    def __init__(self,data):
        self.data = data
        self.select_detail_search()
        
        
    def select_detail_search(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            #print(self.data[5])
            params = [self.data[5]]
            query = f"""SELECT * FROM {My_SQL_table_Name} WHERE id = %s"""
            
            cursor.execute(query,params)
            result = cursor.fetchall()
            Staff_Details_Display(result)

Rank_List_Manager()
        
        
        

