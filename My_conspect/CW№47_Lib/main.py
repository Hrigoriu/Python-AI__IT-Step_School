from db import DB
from repository import UserRepository, BookRepository, RentalRepository
from rental_service import RentalService

def main():
    db = DB()
    user_repo = UserRepository(db)
    book_repo = BookRepository(db)
    rental_repo = RentalRepository(db)
    rental_service = RentalService(user_repo, book_repo, rental_repo)

    try:
        while True:
            print('\n===== Меню Бібліотеки =====')
            print('1. Додати користувача')
            print('2. Додати книгу')
            print('3. Переглянути всі книги')
            print('4. Взяти книгу')
            print('5. Повернути книгу')
            print('6. Переглянути всіх користувачів')
            print('7. Переглянути книги користувача')
            print('0. Вихід')

            choice = input('Оберіть опцію: ')
            match choice:
                case '1':
                    name = input('Ім\'я: ')
                    email = input('Email: ')
                    user_id = user_repo.add(name=name, email=email)
                    print(f'Користувача додано з ID {user_id}')
                case '2':
                    title = input('Назва книги: ')
                    author = input('Автор: ')
                    book_id = book_repo.add(title=title, author=author)
                    print(f'Книгу додано з ID {book_id}')
                case '3':
                    books = book_repo.list_all()
                    if not books:
                        print('У бібліотеці ще немає книг.')
                    for book in books:
                        status = 'Доступна' if book.available else 'Видана'
                        print(f'ID: {book.id}, Назва: "{book.title}", Автор: {book.author}, Статус: {status}')
                case '4':
                    user_id = input('ID користувача: ')
                    book_id = input('ID книги: ')
                    print(rental_service.rent_book(int(user_id), int(book_id)))
                case '5':
                    user_id = input('ID користувача: ')
                    book_id = input('ID книги: ')
                    print(rental_service.return_book(int(user_id), int(book_id)))
                case '6':
                    users = user_repo.list_all()
                    if not users:
                        print('У системі немає зареєстрованих користувачів.')
                    for user in users:
                        print(f'ID: {user.id}, Ім\'я: {user.name}, Email: {user.email}')
                case '7':
                    user_id = input('Введіть ID користувача: ')
                    user = user_repo.get_by_id(int(user_id))
                    if not user:
                        print('Користувача з таким ID не знайдено.')
                        continue

                    rented_books = book_repo.find_rented_by_user(int(user_id))
                    if not rented_books:
                        print(f'Користувач "{user.name}" наразі не має взятих книг.')
                    else:
                        print(f'Книги, взяті користувачем "{user.name}": ')
                        for book in rented_books:
                            print(f'- "{book.title}", автор: {book.author}')
                case '0':
                    break
                case _:
                    print('Щось пішло не так!')
    finally:
        db.close()


if __name__ == '__main__':
    main()