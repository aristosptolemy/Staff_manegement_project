import mysql.connector

config = {
    'host': '192.168.11.9',
    'user': 'testuser',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema'
}


with mysql.connector.connect(**config) as conn:
    cursor = conn.cursor()
    
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
        print(rank_number)
        rank_ = sorted(rank_number, key=lambda x: (x[0], -ord(x[1][0]) if x[1][0].isalpha() else x[1]), reverse=False)
        print(rank_)
        rank_num_list = []
        for f1,s2 in rank_:
            if s2 == 'As':
                insert = 'ｱｼｽﾀﾝﾄ'
            else:
                insert = f'{f1}{s2}'
            rank_num_list.append(insert)
        
    
        
    

        



