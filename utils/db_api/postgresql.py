# import asyncio
# import asyncpg
#
# from data import config
#
#
# class Database:
#     def __init__(self, loop: asyncio.AbstractEventLoop):
#         self.pool = loop.run_until_complete(
#             asyncpg.create_pool(
#                 user=config.PGUSER,
#                 password=config.PGPASSWORD,
#                 host='db',
#                 port='5432'
#             )
#         )
#
#     @staticmethod
#     def formar_args(sql, parameters: dict):
#         sql += ' AND '.join([
#             f'{item} = ${num}' for num, item in enumerate(parameters, start=1)
#         ])
#         return sql, tuple(parameters.values())
#
#     async def add_user(self, id: int, name: str):
#         sql = " INSERT INTO users (id, name) VALUES ($1, $2)"
#         await self.pool.execute(sql, id, name)
#
#     async def get_balance_user(self, **kwargs):
#         sql = "SELECT balance FROM users WHERE "
#         sql, parameters = self.formar_args(sql, kwargs)
#         return await self.pool.fetchval(sql, *parameters)
#
#     async def select_all_users(self):
#         sql = "SELECT * FROM users"
#         return await self.pool.fetch(sql)
#
#     async def select_user(self, **kwargs):
#         sql = "SELECT * FROM users WHERE "
#         sql, parameters = self.formar_args(sql, kwargs)
#         return await self.pool.fetchrow(sql, *parameters)
#
#     async def count_users(self):
#         return await self.pool.fetchval("SELECT COUNT(*) FROM users")
#
#     async def update_user_email(self, email, id):
#         sql = "UPDATE users SET email = $1 WHERE id = $2"
#         return await self.pool.execute(sql, email, id)
#
#     async def delete_users(self):
#         await self.pool.execute("DELETE FROM users WHERE True")
#
#     async def get_count_order(self, **kwargs):
#         sql = "SELECT COUNT(*) FROM orders WHERE "
#         sql, parameters = self.formar_args(sql, kwargs)
#         return await self.pool.fetchval(sql, *parameters)
#
#     async def get_orders(self, **kwargs):
#         sql = "SELECT * FROM orders WHERE "
#         sql, parameters = self.formar_args(sql, kwargs)
#         return await self.pool.fetch(sql, *parameters)
#
#     async def get_count_refill(self, **kwargs):
#         sql = "SELECT COUNT(sum) FROM refill WHERE "
#         sql, parameters = self.formar_args(sql, kwargs)
#         return await self.pool.fetchval(sql, *parameters)
