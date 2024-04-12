import mysql.connector
import json  

from staff_manegement_app.data.encryption_conversion import Decrypt_Data_Conversion


config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema'
}

with mysql.connector.connect(**config) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff_list_test WHERE id = 4;")
    result = cursor.fetchone()
    
    column_names = [i[0] for i in cursor.description]
    print(column_names)
    result_dict = dict(zip(column_names, result))
    Decrypt_Data_Conversion(result_dict)
    