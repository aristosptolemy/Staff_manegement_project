import mysql.connector
import pandas as pd
pd.set_option('future.no_silent_downcasting', True)



config = {
    'host': '192.168.0.43',
    'user': 'STAFF_MANAGEMENT',
    'port': '3306',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema'
}



My_SQL_table_Name = "staff_list"


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
        from data.encryption_conversion import Encryption_Data_Conversion
        self.Encryption_Conversion_data = Encryption_Data_Conversion(self.data)
        set_data = self.Encryption_Conversion_data.get_data()

        self.MySQL_insert(set_data)

        
    def MySQL_insert(self,data):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            #print(data)
            
            
            
            cursor.execute(f'''
                        INSERT INTO {My_SQL_table_Name} (氏,名,スタッフ詳細,社会保険,雇用保険,扶養,身元引受人１,身元引受人２,入社日,
                        更新,期間の定め,試用期間,雇用形態,就業場所,等級,仕事内容,勤務時間,休日,残業,主な交通費,サブ交通費,備考欄,給与備考,在籍状況) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',
                        (data["氏"],data["名"],data["スタッフ詳細"],data["社会保険"],data["雇用保険"],
                         data["扶養"],data["身元引受人1"],data["身元引受人2"],data["入社日"],
                         data["更新"],data["期間の定め"],data["試用期間"],data["雇用形態"],data["就業場所"],
                         data["等級"],data["仕事内容"],data["勤務時間"],data['休日'],data["残業"],data["主な交通費"],
                         data["サブ交通費"],data["備考欄"],data["給与備考"],data["在籍状況"]))
            
            conn.commit()


class MySQL_Staff_Update:
    def __init__(self,data,id_data):
        self.data = data
        self.id_data = id_data
        from data.encryption_conversion import Encryption_Data_Conversion
        self.Encryption_Conversion_data = Encryption_Data_Conversion(self.data)
        set_data = self.Encryption_Conversion_data.get_data()

        self.MySQL_update(set_data)

        
    def MySQL_update(self,data):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            #print(data)
            
            
            
            cursor.execute(f'''
                        UPDATE {My_SQL_table_Name} 
                        SET 氏 = %s ,名 = %s ,スタッフ詳細 = %s ,社会保険 = %s ,雇用保険 = %s ,扶養 = %s ,身元引受人１ = %s ,身元引受人２ = %s ,入社日 = %s ,
                        更新 = %s ,期間の定め = %s ,試用期間 = %s ,雇用形態 = %s ,就業場所 = %s ,等級 = %s ,仕事内容 = %s ,勤務時間 = %s ,休日 = %s ,残業 = %s ,
                        主な交通費 = %s ,サブ交通費 = %s ,備考欄 = %s ,給与備考 = %s ,在籍状況 = %s 
                        WHERE id = %s;''',
                        (data["氏"],data["名"],data["スタッフ詳細"],data["社会保険"],data["雇用保険"],
                         data["扶養"],data["身元引受人1"],data["身元引受人2"],data["入社日"],
                         data["更新"],data["期間の定め"],data["試用期間"],data["雇用形態"],data["就業場所"],
                         data["等級"],data["仕事内容"],data["勤務時間"],data['休日'],data["残業"],data["主な交通費"],
                         data["サブ交通費"],data["備考欄"],data["給与備考"],data["在籍状況"],self.id_data))
            
            conn.commit()







class MySQL_Staff_Search(object):
    def __init__(self, data, widget,number):
        self.data = data
        self.widget = widget
        self.number = number
        self.column_get()
        self.MySQL_search()
        
    def column_get(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'''
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = 'staff_list_test'
                    ORDER BY ORDINAL_POSITION;
                    '''
            cursor.execute(query)
            result = cursor.fetchall()
            
            self.column_names = []
            for i in result:
                self.column_names.append(i[0])
            
    def MySQL_search(self):
        
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            
            query = f'''SELECT * FROM {My_SQL_table_Name} WHERE 1=1'''
            params = []

            # 条件をチェックしてクエリとパラメータを組み立てる
            for key, value in self.data.items():
                if key == "就業場所":
                    if value:
                        query += f" AND {key} = %s"
                        params.append(value)
            
            if query == f'SELECT * FROM {My_SQL_table_Name} WHERE 1=1':
                query = f'SELECT * FROM {My_SQL_table_Name}'
                
            
            cursor.execute(query, params)
            results = cursor.fetchall()
            result_data = []
            
            for i in results:
                result_data.append(list(i))
            
            from GUI_Logic.staff_search_logic import Search_Staff_List_INSERT
            from data.encryption_conversion import Decrypt_Data_Conversion
            
            list_data = []
            count = 0
            for li in result_data:
                count = 0
                en_data = {}
                for i in li:
                    ap_key = self.column_names[count]
                    en_data[ap_key] = i
                    count += 1
                
                dec_data = Decrypt_Data_Conversion(en_data)
                list_data.append(dec_data.get_data())
            import json
            search_results_data = []
            for Data_for_one_person in list_data:
                judgement = 0
                for key,value in Data_for_one_person.items():
                    try:
                        d_value = json.loads(value)
                        if isinstance(d_value, dict):
                            for min_key, min_value in d_value.items():
                                search_word = self.data[key]
                                word = search_word[min_key]
                                if word != "":
                                    if min_value == word:
                                        judgement += 1
                                    else:
                                        pass
                                else:
                                    pass
                                
                                    
                        else:
                            search_word = self.data[key]
                            if d_value == search_word:
                                judgement += 1
                            else:
                                pass
                            
                            
                    except:
                        try:
                            search_word = self.data[key]
                            if value == search_word:
                                judgement += 1
                            else:
                                pass
                        except:
                            pass
                
                if judgement == self.number:
                    search_results_data.append(Data_for_one_person)
                    #print("検索結果に追加")
                else:
                    #print("追加無し")       
                    pass
            
            
            Search_Staff_List_INSERT(search_results_data,self.widget)
    
            

            
class MySQL_Select_Details(object):
    def __init__(self,data,widget):
        self.data = data
        self.widget = widget
        self.select_detail_search()
    
    def column_get(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'''
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = '{My_SQL_table_Name}'
                    ORDER BY ORDINAL_POSITION;
                    '''
            cursor.execute(query)
            result = cursor.fetchall()
            
            self.column_names = []
            for i in result:
                self.column_names.append(i[0])   
        
    def select_detail_search(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            #print(self.data[5])
            params = [self.data[5]]
            query = f'''SELECT * FROM {My_SQL_table_Name} WHERE id = %s'''
            
            cursor.execute(query,params)
            result = cursor.fetchall()
            from data.encryption_conversion import Decrypt_Data_Conversion
            from GUI.staff_details_GUI import Staff_Details_Display
            encrypted_data = []
            for i in result:
                ap = list(i)
                encrypted_data.append(ap)
            self.column_get()
            list_data = []
            count = 0
            for li in encrypted_data:
                count = 0
                en_data = {}
                for i in li:
                    ap_key = self.column_names[count]
                    en_data[ap_key] = i
                    count += 1
                
                dec_data = Decrypt_Data_Conversion(en_data)
                list_data.append(dec_data.get_data())
        
        Staff_Details_Display(list_data[0],self.widget)



        
        
        


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
    def __init__(self,main_rank,sub_rank,update_col,value,widget):
        self.main_rank = main_rank
        self.sub_rank = sub_rank
        self.update_col = update_col
        self.value = value
        self.widget = widget
        self.rank_value_update()
        
    def rank_value_update(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            table_name = ""
            if self.sub_rank == "総務担当":
                table_name = 'office_rank_list'
            else:
                table_name = 'rank_list'
            
            query = f'UPDATE {table_name} SET {self.update_col} = %s WHERE 等級 = %s AND サブランク = %s'
            
            cursor.execute(query,(self.value,self.main_rank,self.sub_rank))
            
            conn.commit()
            Rank_list_update(table_name,self.widget)
            


class Rank_details:
    def __init__(self,rank):
        self.details(rank)
        

    def details(self,rank):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            table_name = ""
            if len(rank) == 1:
                table_name = "office_rank_list"
                sub_rank = "総務担当"
                rank = rank
            elif "As" in rank:
                table_name = "rank_list"
                rank = 1
                sub_rank = "As"
            else:
                table_name = "rank_list"
                rank = rank[:-1]
                sub_rank = rank[-1]
            
            query = f'''SELECT * FROM {table_name} WHERE 等級 = %s AND サブランク = %s;'''
            cursor.execute(query,(rank,sub_rank))
            result = cursor.fetchall()
            
            self.rank_result = list(result[0])
           
            
            return self.rank_result
    
    def result_get(self):
        return self.rank_result



        
        
class setting_update:
    def __init__(self,name,setting_id):
        self.name = name
        self.setting_id = setting_id
        self.update()
    
    def update(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'''
            UPDATE setting_table SET setting_name = '{self.name}' WHERE id = {self.setting_id}'''
            
            cursor.execute(query)
            conn.commit()
            
            
            

class setting_select:
    def __init__(self,data):
        self.data = data
        self.select()
    
    def select(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                           SELECT setting_name FROM setting_table
                           WHERE id = {self.data};
                           ''')
            
            self.result = cursor.fetchall()
    
    def get_data(self):
        return self.result   
            





class Staff_printing_detail:
    def __init__(self,staff_id):
        self.Staff_detail_extraction(staff_id)
    
    def column_get(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            query = f'''
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = '{My_SQL_table_Name}'
                    ORDER BY ORDINAL_POSITION;
                    '''
            cursor.execute(query)
            result = cursor.fetchall()
            
            self.column_names = []
            for i in result:
                self.column_names.append(i[0])
        
    def Staff_detail_extraction(self,staff_id):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()

            query = f'''SELECT * FROM {My_SQL_table_Name} WHERE id = %s'''
            
            cursor.execute(query,(staff_id,))
            result = cursor.fetchall()
            from data.encryption_conversion import Decrypt_Data_Conversion
            encrypted_data = []
            for i in result:
                ap = list(i)
                encrypted_data.append(ap)
            self.column_get()
            self.list_data = []
            count = 0
            for li in encrypted_data:
                count = 0
                en_data = {}
                for i in li:
                    ap_key = self.column_names[count]
                    en_data[ap_key] = i
                    count += 1
                
                dec_data = Decrypt_Data_Conversion(en_data)
                self.list_data.append(dec_data.get_data())
        
        return self.list_data
    
    def get_data(self):
        return self.list_data[0]