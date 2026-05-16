import sqlite3 
 def connect():
     conn=sqlite3.connect("database/olx.db")
     return conn
def register_user(name,email,password):
   conn=connect()
   cursor=conn.cursor()
   cursor.execute("""
                  INSERT INTO users (name, email, password)
    VALUES (?, ?, ?)
    """, (name, email, password))

    conn.commit()
    conn.close()
def login_user(email,password)
  conn=connect()
  cursor=conn.cursor()
  cursor.execute("""
    SELECT * FROM users
    WHERE email = ? AND password = ?
    """, (email, password))

    user = cursor.fetchone() # if user exists fetchone() will return user details otherwise it will return None
    conn.close()

    return user