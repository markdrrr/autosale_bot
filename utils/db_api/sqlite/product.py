from loader import db


def add_product(category: int, name: str, description: str, price: int):
    sql = "INSERT INTO products (category_id, name, description, price) VALUES (?, ?, ?, ?)"
    db.execute(sql, parameters=(category, name, description, price), commit=True)


def get_products_from_category(category: int):
    sql = f"SELECT * FROM products WHERE category_id = {category}"
    return db.execute(sql, fetchall=True)


def select_product(**kwargs):
    sql = "SELECT * FROM products WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def get_all_products():
    sql = "SELECT * FROM products"
    return db.execute(sql, fetchall=True)
