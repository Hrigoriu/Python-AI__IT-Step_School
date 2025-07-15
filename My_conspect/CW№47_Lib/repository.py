from abc import ABC, abstractmethod
from models import User, Book, Rental

class BaseRepository(ABC):
    def __init__(self, db_connection):
        self.db = db_connection

    @property
    @abstractmethod
    def _table_name(self):
        pass

    @property
    @abstractmethod
    def _model(self):
        pass

    def _map_row_to_model(self, row):
        if not row:
            return None
        columns = [desc[0] for desc in self.db.cursor.description]
        row_dict = dict(zip(columns, row))
        return self._model(**row_dict)

    def get_by_id(self, item_id):
        query = f'SELECT * FROM {self._table_name} WHERE id = %s;'
        row = self.db.execute(query, (item_id,), fetchone=True)
        return self._map_row_to_model(row)

    def list_all(self):
        query = f'SELECT * FROM {self._table_name};'
        rows = self.db.execute(query)
        return [self._map_row_to_model(row) for row in rows]

    def add(self, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['%s'] * len(kwargs))
        values = tuple(kwargs.values())

        query = f'INSERT INTO {self._table_name} ({columns}) VALUES ({placeholders}) RETURNING id;'
        item_id = self.db.execute(query, values, fetchone=True)[0]
        self.db.commit()
        return item_id

    def update(self, item_id, **kwargs):
        set_clause = ', '.join([f'{key} = %s' for key in kwargs.keys()])
        values = tuple(kwargs.values()) + (item_id,)

        query = f'UPDATE {self._table_name} SET {set_clause} WHERE id = %s;'
        self.db.execute(query, values)
        self.db.commit()


class UserRepository(BaseRepository):
    _table_name = 'users'
    _model = User


class BookRepository(BaseRepository):
    _table_name = 'books'
    _model = Book

    def find_rented_by_user(self, user_id):
        query = '''
            SELECT b.* FROM books b
            JOIN rentals r ON b.id = r.book_id
            WHERE r.user_id = %s AND r.return_date IS NULL;
        '''
        rows = self.db.execute(query, (user_id,))
        return [self._map_row_to_model(row) for row in rows]


class RentalRepository(BaseRepository):
    _table_name = 'rentals'
    _model = Rental

    def find_active_rental(self, user_id, book_id):
        query = f'SELECT * FROM {self._table_name} WHERE user_id = %s AND book_id = %s AND return_date IS NULL;'
        row = self.db.execute(query, (user_id, book_id), fetchone=True)
        return self._map_row_to_model(row)