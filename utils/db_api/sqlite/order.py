from loader import db


def select_all_orders():
    sql = "SELECT * FROM orders"
    return db.execute(sql, fetchall=True)


def select_order(**kwargs):
    sql = "SELECT * FROM orders WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def get_staff_in_order(**kwargs):
    sql = "SELECT * FROM staff_in_orders WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchall=True)


def select_orders_from_user(**kwargs):
    sql = "SELECT * FROM orders WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchall=True)


def count_orders(**kwargs):
    sql = "SELECT COUNT(*) FROM orders WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def add_order(user_id: int, product_id: int, data: str, sum: int):
    sql = "INSERT INTO orders (user_id, product_id, data, sum) VALUES (?, ?, ?, ?)"
    db.execute(sql, parameters=(user_id, product_id, data, sum), commit=True)
