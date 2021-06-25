import sqlite3

connect = sqlite3.connect('clients.db')
cursor = connect.cursor()



def db_rec(phone_number: int, user_name: str, date: str, time: str) -> object:
    cursor.execute('INSERT INTO test (phone_number, user_name, date, time) VALUES (?, ?, ?, ?)',
                   (phone_number, user_name, date, time))
    conn.commit()

class User:
    def user_name(self, user_name):
        self.user_name = user_name
    def phone_number(self, phone_number):
        self.phone_number = phone_number
    def time(self,time):
        self.time = time
    def date(self, date):
        self.date = date