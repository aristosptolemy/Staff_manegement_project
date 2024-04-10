import mysql.connector
import json  

config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema'
}

with mysql.connector.connect(**config) as conn:
    cursor = conn.cursor()
    
    query = '''SELECT * FROM staff_list_test WHERE JSON_EXTRACT(氏, "$.カナ") = "スミヨシ"'''
    # cursor.execute(query) を使用し、params を使わない
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)  # 結果を出力して確認
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

