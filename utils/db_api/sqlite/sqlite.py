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
        print(parameters)
        print(type(parameters))
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
