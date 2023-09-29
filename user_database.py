import sqlite3

def connect_database():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT, password TEXT, email TEXT, phone TEXT, account_type TEXT)''')
    conn.commit()
    return conn, c

def close_database(conn):
    conn.close()

def insert_user(conn, c, username, password, email, phone, account_type):
    c.execute("INSERT INTO users (username, password, email, phone, account_type) VALUES (?, ?, ?, ?, ?, ?)", (username, password, email, phone, account_type))
    conn.commit()

def fetch_user(conn, c, email, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (email, password))
    return c.fetchone()
