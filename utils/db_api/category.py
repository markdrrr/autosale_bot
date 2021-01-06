# from loader import db
#
#
# async def add_category(name: str):
#     sql = "INSERT INTO categories (name) VALUES ($1)"
#     await db.pool.execute(sql, name)
#
#
# async def get_category(**kwargs):
#     sql = "SELECT * FROM categories WHERE "
#     sql, parameters = db.formar_args(sql, kwargs)
#     return await db.pool.fetchrow(sql, *parameters)
#
#
# async def get_all_categories():
#     sql = "SELECT * FROM categories"
#     return await db.pool.fetch(sql)
