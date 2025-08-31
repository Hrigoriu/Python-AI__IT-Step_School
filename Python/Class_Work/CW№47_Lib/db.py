import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

class DB:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            self.connection.autocommit = False
            self.cursor = self.connection.cursor()
            print('З\'єднання з базою даних успішне.')
        except psycopg2.OperationalError as e:
            print(f'Помилка з\'єднання з базою даних: {e}')
            exit()

    def execute(self, query, params=None, fetchone=False):
        self.cursor.execute(query, params or ())
        if fetchone:
            return self.cursor.fetchone()
        if self.cursor.description:
            return self.cursor.fetchall()
        return None

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
        print('З\'єднання з базою даних закрито.')