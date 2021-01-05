from loader import db


async def add_product(category: int, name: str, description: str, price: int):
    sql = "INSERT INTO products (category_id, name, description, price) VALUES ($1, $2, $3, $4)"
    await db.pool.execute(sql, category, name, description, price)


async def get_products_from_category(category: int):
    sql = f"SELECT * FROM products WHERE category_id = {category}"
    return await db.pool.fetch(sql)


async def select_product(**kwargs):
    sql = "SELECT * FROM products WHERE "
    sql, parameters = db.formar_args(sql, kwargs)
    return await db.pool.fetchrow(sql, *parameters)


async def get_all_products():
    sql = "SELECT * FROM products"
    return await db.pool.fetch(sql)
