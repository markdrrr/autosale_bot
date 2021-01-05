from loader import db


async def select_all_users():
    sql = "SELECT * FROM users"
    return await db.pool.fetch(sql)


async def select_user(**kwargs):
    sql = "SELECT * FROM users WHERE "
    sql, parameters = db.formar_args(sql, kwargs)
    return await db.pool.fetchrow(sql, *parameters)


async def change_balance(user_id, new_balance):
    sql = f"UPDATE users SET balance = {new_balance} WHERE id = {user_id}"
    return await db.pool.execute(sql)


async def add_balance(user_id, value):
    sql = f"UPDATE users SET balance = balance + {value} WHERE id = {user_id}"
    return await db.pool.execute(sql)
