# Homepage.py
import streamlit as st
import sqlite3
from pages import Add_transaction, Insights, Your_transactions

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
    st.title("Personal Finance Tracker")
    
    st.write("""
    Welcome to Personal Finance Tracker app! This app helps you track your income and expenses.
    
    With this app, you can:
    - Add new transactions
    - View insights into your income and expenses
    - Explore your transaction history
    
    Get started now by adding your first transaction!
    """)

if __name__ == "__main__":
    main()

