import mysql.connector

config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema'
}
def MySQL_insert():
    with mysql.connector.connect(**config) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
                    INSERT INTO test (id,message) 
                    VALUES (?,?);''',())
        
        conn.commit()

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
    

