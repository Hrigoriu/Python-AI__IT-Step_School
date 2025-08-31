from db import DB
from user_manager import UserManager
from book_manager import BookManager
from rental_service import RentalManager


def main():
    db = DB()
    users = UserManager(db)
    books = BookManager(db)
    rentals = RentalManager(db)

    try:
        while True:
            print('\n===== Меню Бібліотеки =====')
            print('1. Додати користувача')
            print('2. Додати книгу')
            print('3. Переглянути книги')
            print('4. Взяти книгу')
            print('5. Повернути книгу')
            print('6. Вихід')

            choice = input('Оберіть опцію: ')
            match choice:
                case '1':
                    name = input('Ім\'я: ')
                    email = input('Email: ')
                    user_id = users.add_user(name, email)
                    print(f'Користувача додано з ID {user_id}')
                case '2':
                    title = input('Назва книги: ')
                    author = input('Автор: ')
                    book_id = books.add_book(title, author)
                    print(f'Книгу додано з ID {book_id}')
                case '3':
                    for book in books.list_books():
                        print(book)
                case '4':
                    user_id = input('ID користувача: ')
                    book_id = input('ID книги: ')
                    print(rentals.rent_book(user_id, book_id))
                case '5':
                    user_id = input('ID користувача: ')
                    book_id = input('ID книги: ')
                    print(rentals.return_book(user_id, book_id))
                case '6':
                    break
                case _:
                    print('Невідома опція!')
    finally:
        db.close()

if __name__ == '__main__':
    main()