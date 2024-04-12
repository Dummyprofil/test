# Homepage.py

import sqlite3

def create_table():
    conn = sqlite3.connect("transactions.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    Type TEXT,
                    Name TEXT,
                    Category TEXT,
                    Amount REAL,
                    Date TEXT
                 )''')
    conn.commit()
    conn.close()

def main():
    create_table()
    # Remaining code remains the same
