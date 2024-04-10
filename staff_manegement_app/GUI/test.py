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
    cursor.execute("SELECT * FROM staff_list_test WHERE id = 2;")
    result = cursor.fetchone()
    column_names = [i[0] for i in cursor.description]
    print(column_names)
    result_dict = dict(zip(column_names, result))

    # '主な交通費' カラムからJSON文字列を取得
    open_re = result_dict["主な交通費"]
    
    # JSON文字列を辞書に変換
    open_re_t = json.loads(open_re)
    
    # '通勤手当(日)' キーを使って値にアクセス
    print(open_re_t['通勤手当(日)'])
    
    # 仮にこれが結果辞書から取得したJSON文字列に対応する辞書だとします
    open_re_t = {"通勤手段": "公共交通機関", "通勤手当(日)": "700"}
    key_of_interest = "通勤手当"
    # キーと値を取り出す
    for key, value in open_re_t.items():
        print(f"{key}: {value}")
        if key_of_interest in open_re_t:
            print(f"{key_of_interest}: {open_re_t[key_of_interest]}")