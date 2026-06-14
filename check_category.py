import sqlite3

conn = sqlite3.connect("database/olx.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(products)")
columns = cursor.fetchall()

for column in columns:
    print(column)

conn.close()