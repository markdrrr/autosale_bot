from loader import db


async def create_table_users():
    sql = """ 
    CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    balance DECIMAL DEFAULT 0,
    PRIMARY KEY (id))
    """
    await db.pool.execute(sql)


async def create_table_categories():
    sql = """ 
    CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255))
    """
    await db.pool.execute(sql)


async def create_table_products():
    sql = """ 
    CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(id),
    name VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL)
    """
    await db.pool.execute(sql)


async def create_table_staff():
    sql = """ 
    CREATE TABLE IF NOT EXISTS staff (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    staff VARCHAR(255),
    status INT DEFAULT 0)
    """
    await db.pool.execute(sql)


async def create_table_orders():
    sql = """ 
    CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    data VARCHAR(255),
    sum DECIMAL)
    """
    await db.pool.execute(sql)


async def create_table_staff_in_orders():
    sql = """ 
    CREATE TABLE IF NOT EXISTS staff_in_orders (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    staff_id INTEGER REFERENCES staff(id))
    """
    await db.pool.execute(sql)


async def create_table_payments():
    sql = """ 
    CREATE TABLE IF NOT EXISTS payments (
    id SERIAL PRIMARY KEY,
    key VARCHAR(255),
    user_id INTEGER REFERENCES users(id),
    sum DECIMAL,
    payment VARCHAR(255))
    """
    await db.pool.execute(sql)


async def run():
    await create_table_users()
    await create_table_categories()
    await create_table_products()
    await create_table_orders()
    await create_table_payments()
    await create_table_staff()
    await create_table_staff_in_orders()
