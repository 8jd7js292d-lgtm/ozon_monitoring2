import sqlite3


DB_NAME = "ozon.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT UNIQUE,
        name TEXT,
        price REAL,
        updated TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_product(url, name, price):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO products
    (url, name, price, updated)
    VALUES (?, ?, ?, datetime('now'))
    """,
    (url, name, price))

    conn.commit()
    conn.close()


def get_products():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT url, name, price
    FROM products
    """)

    data = cur.fetchall()

    conn.close()

    return data


def update_price(url, price):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    UPDATE products
    SET price = ?, updated = datetime('now')
    WHERE url = ?
    """,
    (price, url))

    conn.commit()
    conn.close()