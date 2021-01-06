from loader import db


def add_payment(key: str, user_id: int, sum: int, payment: str):
    sql = "INSERT INTO payments (key, user_id, sum, payment) VALUES (?, ?, ?, ?)"
    db.execute(sql, parameters=(key, user_id, sum, payment), commit=True)


def update_payment(amount: int, key: str):
    sql = f"UPDATE payments SET sum = {amount} WHERE key = '{key}'"
    db.execute(sql, commit=True)


def select_payment(**kwargs):
    sql = "SELECT * FROM payments WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def get_payments_from_user(user_id: int):
    sql = f"SELECT * FROM payments WHERE user_id = {user_id}"
    return db.execute(sql, fetchall=True)
