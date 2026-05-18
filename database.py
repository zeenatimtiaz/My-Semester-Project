import sqlite3


# Connect to database
def connect():
    conn = sqlite3.connect("database/olx.db")
    return conn


# Create required tables
def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
        )
    """)

    # Products Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            description TEXT,
            seller TEXT
        )
    """)

    conn.commit()
    conn.close()


# Run table creation
create_tables()