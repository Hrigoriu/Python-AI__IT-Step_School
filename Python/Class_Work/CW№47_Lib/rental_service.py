from datetime import datetime
from repository import UserRepository, BookRepository, RentalRepository

class RentalService:
    def __init__(self, user_repo: UserRepository, book_repo: BookRepository, rental_repo: RentalRepository):
        self.user_repo = user_repo
        self.book_repo = book_repo
        self.rental_repo = rental_repo

    def rent_book(self, user_id, book_id):
        user = self.user_repo.get_by_id(user_id)
        if not user:
            return 'Помилка: Користувача з таким ID не знайдено.'

        book = self.book_repo.get_by_id(book_id)

        if not book:
            return 'Помилка: Книгу не знайдено.'
        if not book.available:
            return 'Книга наразі недоступна для видачі.'

        try:
            self.book_repo.update(book.id, available=False)
            self.rental_repo.add(user_id=user_id, book_id=book_id, rental_date=datetime.now())
            return f'Книгу "{book.title}" успішно видано користувачу "{user.name}." '
        except Exception as e:
            return f'Сталася помилка: {e}'

    def return_book(self, user_id, book_id):
        user = self.user_repo.get_by_id(user_id)
        if not user:
            return 'Помилка: Користувача з таким ID не знайдено.'
        book = self.book_repo.get_by_id(book_id)
        if not book:
            return 'Помилка: Книгу не знайдено.'

        active_rental = self.rental_repo.find_active_rental(user_id, book_id)
        if not active_rental:
            return f'Помилка: Користувач з ID {user_id} не брав цю книгу, або вона вже повернута.'

        try:
            self.book_repo.update(book.id, available=True)
            self.rental_repo.update(active_rental.id, return_date=datetime.now())
            return f'Книгу "{book.title}" успішно повернуто користувачем "{user.name}." '
        except Exception as e:
            return f'Сталася помилка: {e}'