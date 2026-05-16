import sqlite3
     # connect and create a new database file in this every user login and the products data is store     # connect and create a new database file in this every user login and the products data is store
def connect()
    conn= sqlite3.connect("database/olx.db")
    return conn

def create_tables()
    conn=connect()       # open the database file in this function to use 
    cursor=conn.cursor() # creates worker --> cursor : runs commands 

# Users Table 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT
   """" ) 
    )
# Produccts Table 
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        description TEXT,
        seller TEXT
    )
    """)
    conn.commit() # save all our work
    conn.close()  # close the file

    create_tables()
    # file  completed