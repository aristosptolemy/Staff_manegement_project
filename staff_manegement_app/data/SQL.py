import mysql.connector

config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema'
}


class Rank_List_Manager:
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
        
        self.MySQL_insert_test()

        
    def MySQL_insert_test(self):
        with mysql.connector.connect(**config) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                        INSERT INTO staff_list_test (氏,名,スタッフ詳細,社会保険,雇用保険,扶養,身元引受人1,身元引受人2,入社日,
                        更新,期間の定め,勤務形態,所属店舗,等級,勤務時間,残業,主な交通費,サブ交通費,備考欄,給与備考,在籍状況) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',
                        (self.data["氏"],self.data["名"],self.data["スタッフ詳細"],self.data["社会保険"],self.data["雇用保険"],
                         self.data["扶養"],self.data["身元引受人1"],self.data["身元引受人2"],self.data["入社日"],
                         self.data["更新"],self.data["期間の定め"],self.data["試用期間"],self.data["勤務形態"],self.data["所属店舗"],
                         self.data["等級"],self.data["勤務時間"],self.data["残業"],self.data["主な交通費"],self.data["備考欄"],
                         self.data["給与備考"],self.data["在籍状況"]))
            
            conn.commit()




