from loader import db


def add_user(id: int, name: str):
    sql = " INSERT INTO Users(id, name) VALUES(?, ?)"
    parameters = (id, name)
    db.execute(sql, parameters=parameters, commit=True)


def select_all_users():
    sql = "SELECT * FROM users"
    return db.execute(sql, fetchall=True)


def select_user(**kwargs):
    sql = "SELECT * FROM users WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def change_balance(user_id, new_balance):
    sql = f"UPDATE users SET balance = {new_balance} WHERE id = {user_id}"
    db.execute(sql, commit=True)


def add_balance(user_id, value):
    sql = f"UPDATE users SET balance = balance + {value} WHERE id = {user_id}"
    db.execute(sql, commit=True)
