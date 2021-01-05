from loader import db


async def add_payment(key: str, user_id: int, sum: int, payment: str):
    sql = "INSERT INTO payments (key, user_id, sum, payment) VALUES ($1, $2, $3, $4)"
    await db.pool.execute(sql, key, user_id, sum, payment)


async def update_payment(amount: int, key: str):
    print(key)
    sql = f"UPDATE payments SET sum = {amount} WHERE key = '{key}'"
    return await db.pool.execute(sql)


async def select_payment(**kwargs):
    sql = "SELECT * FROM payments WHERE "
    sql, parameters = db.formar_args(sql, kwargs)
    return await db.pool.fetchrow(sql, *parameters)


async def get_payments_from_user(user_id: int):
    sql = f"SELECT * FROM payments WHERE user_id = {user_id}"
    return await db.pool.fetch(sql)
