import sqlite3

def connect():
    conn = sqlite3.connect("database/olx.db")
    return conn

def setup_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            email TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def register_user(name, email, password):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, password))
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False  # email already exists

def login_user(email, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM users
        WHERE email = ? AND password = ?
    """, (email, password))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None

# run once to create table
setup_db()