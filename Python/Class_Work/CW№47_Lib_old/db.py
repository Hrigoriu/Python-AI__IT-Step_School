import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

class DB:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None, fetchone=False, commit=False):
        self.cursor.execute(query, params or ())
        if commit:
            self.connection.commit()
        if fetchone:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()