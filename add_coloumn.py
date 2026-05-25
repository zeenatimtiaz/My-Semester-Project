import sqlite3

conn = sqlite3.connect("database/olx.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE products ADD COLUMN image TEXT")

conn.commit()
conn.close()

print("Image column added")