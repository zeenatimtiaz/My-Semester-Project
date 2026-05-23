import sqlite3

# Database connection
def connect():
    conn = sqlite3.connect("database/olx.db")
    return conn


# Add new product
def add_product(title, price, description, seller):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO products (title, price, description, seller)
    VALUES (?, ?, ?, ?)
    """, (title, price, description, seller))

    conn.commit()
    conn.close()


# Get all products
def get_products():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return products