
config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'port': '3306',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema',
    'auth_plugin': 'mysql_native_password',
}






"""
with mysql.connector.connect(**config) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff_list_test WHERE id = 4;")
    result = cursor.fetchone()
    
    column_names = [i[0] for i in cursor.description]
    result_dict = dict(zip(column_names, result))
    Decrypt_Data_Conversion(result_dict)
"""