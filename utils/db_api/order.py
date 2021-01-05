from loader import db


async def select_all_users():
    sql = "SELECT * FROM orders"
    return await db.pool.fetch(sql)


async def select_order(**kwargs):
    sql = "SELECT * FROM orders WHERE "
    sql, parameters = db.formar_args(sql, kwargs)
    return await db.pool.fetchrow(sql, *parameters)


async def get_staff_in_order(**kwargs):
    sql = "SELECT * FROM staff_in_orders WHERE "
    sql, parameters = db.formar_args(sql, kwargs)
    return await db.pool.fetch(sql, *parameters)


async def select_orders_from_user(**kwargs):
    sql = "SELECT * FROM orders WHERE "
    sql, parameters = db.formar_args(sql, kwargs)
    return await db.pool.fetch(sql, *parameters)


async def count_order(**kwargs):
    sql = "SELECT COUNT(*) FROM orders WHERE "
    sql, parameters = db.formar_args(sql, kwargs)
    return await db.pool.fetchval(sql, *parameters)


async def add_order(user_id: int, product_id: int, data: str, sum: int):
    sql = "INSERT INTO orders (user_id, product_id, data, sum) VALUES ($1, $2, $3, $4)"
    await db.pool.execute(sql, user_id, product_id, data, sum)
