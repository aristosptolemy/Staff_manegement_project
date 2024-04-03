import mysql.connector

config = {
    'host': '192.168.11.9',
    'user': 'STAFF_MANAGEMENT',
    'password': 'yoshi115STAFFMySQL',
    'database': 'yoshi_schema'
}

with mysql.connector.connect(**config) as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
                   select * from test where id = 5;''')
    
    result = cursor.fetchone()
    

    
    print(result)
    
    conn.commit()