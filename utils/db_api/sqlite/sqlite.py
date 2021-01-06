import sqlite3


class Database:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        if parameters:
            cursor.execute(sql, parameters)
        else:
            cursor.execute(sql)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += ' AND '.join([
            f'{item} = ${num}' for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    def create_table_users(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS Users (
        id INT NOT NULL,
        Name VARCHAR(255) NOT NULL,
        balance DECIMAL DEFAULT 0,
        PRIMARY KEY (id))
        """
        self.execute(sql, commit=True)

    def create_table_categories(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255))
        """
        self.execute(sql, commit=True)

    def create_table_products(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER REFERENCES categories(id),
        name VARCHAR(255),
        description VARCHAR(255),
        price DECIMAL,
        FOREIGN KEY(category_id) REFERENCES categories(id))
        """
        self.execute(sql, commit=True)

    def create_table_staff(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        staff VARCHAR(255),
        status INT DEFAULT 0,
        FOREIGN KEY(product_id) REFERENCES products(id))
        """
        self.execute(sql, commit=True)

    def create_table_orders(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        data VARCHAR(255),
        sum DECIMAL,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(product_id) REFERENCES products(id))
        """
        self.execute(sql, commit=True)

    def create_table_staff_in_orders(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS staff_in_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        staff_id INTEGER,
        FOREIGN KEY(order_id) REFERENCES orders(id),
        FOREIGN KEY(staff_id) REFERENCES staff(id))
        """
        self.execute(sql, commit=True)

    def create_table_payments(self):
        sql = """ 
        CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key VARCHAR(255),
        user_id INTEGER,
        sum DECIMAL,
        payment VARCHAR(255),
        FOREIGN KEY(user_id) REFERENCES users(id))
        """
        self.execute(sql, commit=True)

    def run(self):
        self.create_table_users()
        self.create_table_categories()
        self.create_table_products()
        self.create_table_orders()
        self.create_table_payments()
        self.create_table_staff()
        self.create_table_staff_in_orders()
