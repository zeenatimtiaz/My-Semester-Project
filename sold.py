import sqlite3

conn = sqlite3.connect("database/olx.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE products ADD COLUMN status TEXT DEFAULT 'available'
""")

conn.commit()
conn.close()
cursor.execute("PRAGMA table_info(products)")
print(cursor.fetchall())