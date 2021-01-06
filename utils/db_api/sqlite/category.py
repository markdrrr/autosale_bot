from loader import db


def add_category(name: str):
    sql = "INSERT INTO categories (name) VALUES (?)"
    db.execute(sql, parameters=(name, ), commit=True)


def get_category(**kwargs):
    sql = "SELECT * FROM categories WHERE "
    sql, parameters = db.format_args(sql, kwargs)
    return db.execute(sql, parameters, fetchone=True)


def get_all_categories():
    sql = "SELECT * FROM categories"
    return db.execute(sql, fetchall=True)
