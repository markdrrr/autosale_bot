from loader import db


def add_staff(product_id: int, staff: str):
    sql = "INSERT INTO staff (product_id, staff) VALUES (?, ?)"
    db.execute(sql, parameters=(product_id, staff), commit=True)


def add_staff_in_orders(order_id: int, staff_id: int):
    sql = "INSERT INTO staff_in_orders (order_id, staff_id) VALUES (?, ?)"
    db.execute(sql, parameters=(order_id, staff_id), commit=True)


def select_staff(**kwargs):
    sql = "SELECT * FROM staff WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def select_staff_limit(product_id, status, count):
    sql = f"SELECT * FROM staff WHERE product_id = {product_id} AND status = {status} LIMIT {count}"
    return db.execute(sql, fetchall=True)


def get_count(**kwargs):
    sql = "SELECT COUNT(*) FROM staff WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def change_status(staff_id, new_status):
    sql = f"UPDATE staff SET status = {new_status} WHERE id = {staff_id}"
    return db.execute(sql, commit=True)


def get_all_staff():
    sql = "SELECT * FROM staff"
    return db.execute(sql, fetchall=True)
