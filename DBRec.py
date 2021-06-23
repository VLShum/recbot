import sqlite3

connect = sqlite3.connect('clients.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clients(client_id INT , client_name TEXT, date TEXT, time FLOAT)""")

connect.commit()

# clients_list = []
# cursor.execute('INSERT INTO clients VALUES(?, ?, ?, ?);', clients_list)