from db import DB

class BookManager:
    def __init__(self, db: DB):
        self.db = db

    def add_book(self, title, author):
        query = 'INSERT INTO books (title, author) VALUES (%s, %s) RETURNING id;'
        return self.db.execute(query, (title, author), fetchone=True)[0]

    def list_books(self):
        return self.db.execute('SELECT id, title, author, available FROM books;')