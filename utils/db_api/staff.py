# from loader import db
#
#
# async def add_staff(product_id: int, staff: str):
#     sql = "INSERT INTO staff (product_id, staff) VALUES ($1, $2)"
#     await db.pool.execute(sql, product_id, staff)
#
#
# async def add_staff_in_orders(order_id: int, staff_id: int):
#     sql = "INSERT INTO staff_in_orders (order_id, staff_id) VALUES ($1, $2)"
#     await db.pool.execute(sql, order_id, staff_id)
#
#
# async def select_staff(**kwargs):
#     sql = "SELECT * FROM staff WHERE "
#     sql, parameters = db.formar_args(sql, kwargs)
#     return await db.pool.fetchrow(sql, *parameters)
#
#
# async def select_staff_limit(product_id, status, count):
#     sql = f"SELECT * FROM staff WHERE product_id = {product_id} AND status = {status} LIMIT {count}"
#     return await db.pool.fetch(sql)
#
#
# async def get_count(**kwargs):
#     sql = "SELECT COUNT(*) FROM staff WHERE "
#     sql, parameters = db.formar_args(sql, kwargs)
#     return await db.pool.fetchval(sql, *parameters)
#
#
# async def change_status(staff_id, new_status):
#     sql = f"UPDATE staff SET status = {new_status} WHERE id = {staff_id}"
#     return await db.pool.execute(sql)
#
#
# async def get_all_staff():
#     sql = "SELECT * FROM staff"
#     return await db.pool.fetch(sql)