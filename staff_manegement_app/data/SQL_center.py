import mysql.connector
import pandas as pd
pd.set_option('future.no_silent_downcasting', True)


"""
config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'port': '3306',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema',
}

"""

config = {
    'host':'localhost',
    'user':'test_user',
    'port': '3306',
    'password':'password',
    'database':'test_schema'
}



My_SQL_table_Name = "staff_list_test"


class Rank_List_Manager():
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
        from .encryption_conversion import Encryption_Data_Conversion
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
            
            query = f'''SELECT * FROM {My_SQL_table_Name} WHERE 1=1'''
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
            from ..GUI_Logic.staff_search_logic import Search_Staff_List_INSERT
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
            query = f'''SELECT * FROM {My_SQL_table_Name} WHERE id = %s'''
            
            cursor.execute(query,params)
            result = cursor.fetchall()
            from staff_manegement_app.GUI.staff_details_GUI import Staff_Details_Display
            Staff_Details_Display(result)


        
        


class Rank_list_all:
    def __init__(self):
        
        
        self.rank_list =[]
        self.rank_table = "rank_list"
        self.rank_list_get(self.rank_table)
        self.column_names_get()
    
    def column_names_get(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'''
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = 'rank_list'
                    ORDER BY ORDINAL_POSITION;
                    '''
            cursor.execute(query)
            result = cursor.fetchall()
            
            self.column_names = []
            for i in result:
                self.column_names.append(i[0])
            
            
            
            
    def rank_list_get(self,rank_table):
        
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'SELECT * FROM {rank_table}'
            cursor.execute(query)
            result = cursor.fetchall()
            for app in result:
                ap = list(app)
                self.rank_list.append(ap)
            
            
    
    def get_data(self):
        rank_DF = pd.DataFrame(self.rank_list,columns=self.column_names)
        
        return rank_DF
    
    def column_get(self):
        return self.column_names
    

class Rank_list_update:
    def __init__(self,table_name,widget):
        self.table_name = table_name
        self.widget = widget
        self.rank_list =[]
        self.column_names_get()
        self.update(self.table_name)
        
    def update(self,rank_table):
        from pandastable import TableModel
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'SELECT * FROM {rank_table}'
            cursor.execute(query)
            result = cursor.fetchall()
            for app in result:
                ap = list(app)
                self.rank_list.append(ap)
            
            rank_DF = pd.DataFrame(self.rank_list,columns=self.column_names)
            rank_DF.fillna(0).infer_objects()
            def format_with_commas(x):
                if x in exclusion:
                    pass
                else:
                    if isinstance(x, (int, float)):
                        return ' ' + '{:,}'.format(x)
                    return x
            rank_DF = rank_DF.sort_values('総支給額見込', ascending=False)
            exclusion = ["等級","サブランク","能力"]
            for col in self.column_names:
                rank_DF[col] = rank_DF[col].apply(format_with_commas) 
            new_model = TableModel(rank_DF)
            self.widget.updateModel(new_model)
            self.widget.columnwidths["等級"] = 50
            self.widget.redraw()
            
            for colname in self.column_names:
                try:
                    if colname in exclusion:
                        pass
                    else:
                        self.widget.columnformats['alignment'][colname] = 'e'
                except KeyError:
                    print(f'Column {colname} does not exist.')
            
            
            
            
     
                
    

    def column_names_get(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'''
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = 'rank_list'
                    ORDER BY ORDINAL_POSITION;
                    '''
            cursor.execute(query)
            result = cursor.fetchall()
            
            self.column_names = []
            for i in result:
                self.column_names.append(i[0])
    


class Rank_Detail_update:
    def __init__(self,main_rank,sub_rank,update_col,value):
        self.main_rank = main_rank
        self.sub_rank = sub_rank
        self.update_col = update_col
        self.value = value
        
    def rank_value_update(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
        
        
        