from db import DB

class RentalManager:
    def __init__(self, db: DB):
        self.db = db

    def rent_book(self, user_id, book_id):
        available = self.db.execute(
            'SELECT available FROM books WHERE id = %s;', (book_id,), fetchone=True
        )
        if not available or not available[0]:
            return 'Книга недоступна'
        self.db.execute(
            'INSERT INTO rentals (user_id, book_id) VALUES (%s, %s);',
            (user_id, book_id), commit=True
        )
        self.db.execute(
            'UPDATE books SET available = FALSE WHERE id = %s;', (book_id,), commit=True
        )
        return 'Книгу видано'

    def return_book(self, user_id, book_id):
        self.db.execute(
            'UPDATE rentals SET return_date = NOW() WHERE user_id = %s AND book_id = %s AND return_date IS NULL;',
            (user_id, book_id), commit=True
        )
        self.db.execute(
            'UPDATE books SET available = TRUE WHERE id = %s;', (book_id,), commit=True
        )
        return 'Книгу повернуто'