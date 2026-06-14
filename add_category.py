import sqlite3

conn = sqlite3.connect("database/olx.db")
cursor = conn.cursor()

# Check if category column already exists
cursor.execute("PRAGMA table_info(products)")
columns = cursor.fetchall()

column_names = [column[1] for column in columns]

if "category" not in column_names:
    cursor.execute("""
        ALTER TABLE products
        ADD COLUMN category TEXT DEFAULT 'Other'
    """)
    print("Category column added successfully!")
else:
    print("Category column already exists.")

conn.commit()
conn.close()