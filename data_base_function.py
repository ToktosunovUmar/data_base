import sqlite3


def connection():
    conn = None
    try:
        conn = sqlite3.connect('hw.db')
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR(200) NOT NULL,
        price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def add_products(conn):
    cursor = conn.cursor()
    products = [
        ("Жидкое мыло с запахом ванили", 10.0, 100),
        ("Мыло детское", 20.0, 200),
        ("Шампунь", 30.0, 300),
        ("Кондиционер для волос", 40.0, 400),
        ("Гель для душа", 50.0, 500),
        ("Пена для бритья", 60.0, 600),
        ("Лосьон после бритья", 70.0, 700),
        ("Крем для лица", 80.0, 800),
        ("Крем для рук", 90.0, 900),
        ("Зубная паста", 100.0, 1000),
        ("Зубная щетка", 110.0, 1100),
        ("Ополаскиватель для рта", 120.0, 1200),
        ("Гель для умывания", 130.0, 1300),
        ("Тоник для лица", 140.0, 1400),
        ("Маска для лица", 150.0, 1500),
    ]
    insert_query = "INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)"
    try:
        cursor.executemany(insert_query, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, product_id, new_quantity):
    cursor = conn.cursor()
    update_query = "UPDATE products SET quantity = ? WHERE id = ?"
    try:
        cursor.execute(update_query, (new_quantity, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(conn, product_id, new_price):
    cursor = conn.cursor()
    update_query = "UPDATE products SET price = ? WHERE id = ?"
    try:
        cursor.execute(update_query, (new_price, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, product_id):
    cursor = conn.cursor()
    delete_query = "DELETE FROM products WHERE id = ?"
    try:
        cursor.execute(delete_query, (product_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def get_all_products(conn):
    cursor = conn.cursor()
    select_query = "SELECT * FROM products"
    try:
        cursor.execute(select_query)
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print(e)


def get_products_by_price_and_quantity(conn):
    cursor = conn.cursor()
    select_query = """
    SELECT * FROM products
    WHERE price < 100 AND quantity > 5
    """
    try:
        cursor.execute(select_query)
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print(e)


def search_products_by_title(conn, search_term):
    cursor = conn.cursor()
    search_query = "SELECT * FROM products WHERE product_title LIKE ?"
    try:
        cursor.execute(search_query, ('%' + search_term + '%',))
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print(e)


conn = connection()
if conn is not None:
    create_table(conn)
    add_products(conn)
    update_quantity(conn, 1, 150)
    update_price(conn, 1, 15.0)
    delete_product(conn, 2)
    print("All Products:")
    get_all_products(conn)

    print("Products by Price and Quantity:")
    get_products_by_price_and_quantity(conn)

    print("Search Products by Title:")
    search_products_by_title(conn, "мыло")

    conn.close()
