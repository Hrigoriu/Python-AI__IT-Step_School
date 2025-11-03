"""
Завдання №1.
Створіть клас Book з атрибутами, такими як назва книги та автор.
Створіть підкласи для різних жанрів книг,
наприклад, FictionBook, NonFictionBook, MysteryBook.
Додайте атрибути та методи, що характеризують кожен жанр
та можливо методи для роботи з книгами (наприклад, видача, повернення).
"""

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self) -> str:
        status = 'Доступна' if self.is_available else 'Видана'
        return f'Книга: "{self.title}" автора {self.author} ({status})'

    def issue_book(self):   #Метод для видачі книги
        if self.is_available:
            self.is_available = False
            print(f' Книга "{self.title}" видана.')
        else:
            print(f' Книга "{self.title}" вже видана.')

    def return_book(self):  #Метод для повернення книги
        if not self.is_available:
            self.is_available = True
            print(f' Книга "{self.title}" повернена.')
        else:
            print(f' Книга "{self.title}" вже доступна.')

    def get_genre_info(self) -> str:
        return 'Загальний жанр'


class FictionBook(Book):    #Клас для художньої літератури
    def __init__(self, title: str, author: str, series_name: str):
        super().__init__(title, author)
        self.series_name = series_name

    def __str__(self) -> str:
        base_info = super().__str__()
        series_info = f', Серія: "{self.series_name}"'
        return f'{base_info} [Жанр: Художня література{series_info}]'

    def get_genre_info(self) -> str:
        series_info = f', Серія: "{self.series_name}"'
        return f'Художня література{series_info}'

    def imagine_plot(self):
        print(f'У книзі "{self.title}" від {self.author} можна уявити захопливий сюжет!')


class NonFictionBook(Book):     #Клас для нехудожньої літератури
    def __init__(self, title: str, author: str, topic: str):
        super().__init__(title, author)
        self.topic = topic

    def __str__(self) -> str:
        base_info = super().__str__()
        return f'{base_info} [Жанр: Нехудожня література, Тема: {self.topic}]'

    def get_genre_info(self) -> str:
        return f'Нехудожня література, Тема: {self.topic}'

    def learn_from_book(self):
        print(f'Читаючи "{self.title}" від {self.author} на тему "{self.topic}", ви дізнаєтеся багато нового.')


class MysteryBook(Book):    #Клас для детективних книг
    def __init__(self, title: str, author: str, main_detective: str):
        super().__init__(title, author)
        self.main_detective = main_detective

    def __str__(self) -> str:
        base_info = super().__str__()
        detective_info = f', Головний детектив: {self.main_detective}'
        return f'{base_info} [Жанр: Детектив{detective_info}]'

    def get_genre_info(self) -> str:
        detective_info = f', Головний детектив: {self.main_detective}'
        return f'Детектив{detective_info}'

    def find_clues(self):
        print(f'У книзі "{self.title}" від {self.author} шукайте підказки, щоб розкрити таємницю!')


# --- Приклад використання ---
print('--- Створення книг різних жанрів ---')
book1 = FictionBook('Гаррі Поттер і Філософський камінь', 'Джоан Роулінг', 'Гаррі Поттер')
book2 = NonFictionBook('Коротка історія часу', 'Стівен Гокінг', 'Космологія')
book3 = MysteryBook('Вбивство у Східному експресі', 'Агата Крісті', 'Еркюль Пуаро')
book4 = FictionBook('1984', 'Джордж Орвелл', 'Класичні Антиутопії XX століття')
book5 = NonFictionBook('Чистий код', 'Роберт Мартін', 'Програмування')
book6 = MysteryBook('Дівчина з татуюванням дракона', 'Стіг Ларссон', 'Мікаеля Блумквіста')

print('\n--- Інформація про книги ---')
print(book1)
print(book2)
print(book3)
print(book4)
print(book5)
print(book6)

print('\n--- Робота з книгами: видача та повернення ---')
book1.issue_book() # Видаємо книгу Гаррі Поттер
book2.issue_book() # Видаємо книгу Коротка історія часу
book1.issue_book() # Спроба видати вже видану книгу
print('-'*20)
print(book1) # Перевіряємо статус Гаррі Поттера
print(book2) # Перевіряємо статус Коротка історія часу
print('-'*40)
book1.return_book() # Повертаємо Гаррі Поттера
book3.issue_book() # Видаємо Вбивство у Східному експресі
book3.issue_book() # Спроба видати вже видану книгу
print(book1)
print(book3)
print('-'*40)

print("\n--- Жанрово-специфічні дії ---")
book1.imagine_plot() # Унікальний метод для FictionBook
book4.imagine_plot() # Унікальний метод для FictionBook
book2.learn_from_book() # Унікальний метод для NonFictionBook
book5.learn_from_book() # Унікальний метод для NonFictionBook
book3.find_clues() # Унікальний метод для MysteryBook
book6.find_clues() # Унікальний метод для MysteryBook
print('-'*40)
#=================================================================

"""
Завдання №2.	
Створіть клас Library з методами для видачі та повернення книг. 
Використовуйте поліморфізм при створенні функції, яка може 
видачу та повернення книги, безперечно працюючи з об'єктами різних типів.
"""


class Book:
    def __init__(self, title: str, author: str):  # Базовий клас для всіх книг
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self) -> str:  # Метод рядкового представлення базової інформації про книгу.
        status = 'Доступна' if self.is_available else 'Видана'
        return f'Книга: "{self.title}" автора {self.author} ({status})'

    def issue_book(self):  # Метод для видачі книги
        if self.is_available:
            self.is_available = False
            print(f'✅ Книга "{self.title}" видана.')
        else:
            print(f'❌ Книга "{self.title}" вже видана.')

    def return_book(self):  # Метод для повернення книги
        if not self.is_available:
            self.is_available = True
            print(f'✅ Книга "{self.title}" повернена.')
        else:
            print(f'❌ Книга "{self.title}" вже доступна.')

    def __eq__(self, other) -> bool:  # Метод для коректного пошуку книги в списку бібліотеки
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))


class FictionBook(Book):  # Клас для художньої літератури
    def __init__(self, title: str, author: str, series_name: str | None = None):
        super().__init__(title, author)
        self.series_name = series_name

    def __str__(self) -> str:
        base_info = super().__str__()
        series_info = f', Серія: "{self.series_name}"' if self.series_name else ''
        return f'{base_info} [Жанр: Художня література{series_info}]'


class NonFictionBook(Book):  # Клас для нехудожньої літератури
    def __init__(self, title: str, author: str, topic: str):
        super().__init__(title, author)
        self.topic = topic

    def __str__(self) -> str:
        base_info = super().__str__()
        return f'{base_info} [Жанр: Нехудожня література, Тема: {self.topic}]'


class MysteryBook(Book):  # Клас для детективних книг
    def __init__(self, title: str, author: str, main_detective: str | None = None):
        super().__init__(title, author)
        self.main_detective = main_detective

    def __str__(self) -> str:
        base_info = super().__str__()
        detective_info = f', Головний детектив: {self.main_detective}' if self.main_detective else ''
        return f'{base_info} [Жанр: Детектив{detective_info}]'


class Library:  # Клас, що представляє бібліотеку
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):  # Метод для додавання книг
        if not isinstance(book, Book):
            print('Це не книга')
            return
        if book not in self.books:  # Перевірка на дублікати завдяки __eq__ та __hash__ в Book
            self.books.append(book)
            print(f'📘 Книга \"{book.title}\" автора {book.author} додана до бібліотеки.')
        else:
            print(f"❌ Книга \"{book.title}\" автора {book.author} вже є в бібліотеці. Не додано.")

    def _find_book(self,
                   book_to_find: Book) -> Book | None:  # Метод для пошуку книги за об'єктом (необхідний для issue/return)
        if not isinstance(book_to_find, Book):
            return None
        for book in self.books:
            if book == book_to_find:  # Використовуємо Book.__eq__
                return book
        return None

    def issue_book(self, book_to_issue: Book):  # Метод для видачі книги
        if not isinstance(book_to_issue, Book):
            print('❌ Неможливо видати: об\'єкт не є Книгою.')
            return

        found_book = self._find_book(book_to_issue)

        if found_book:
            print(f'\n>>> Спроба видати книгу: \"{found_book.title}\"')
            found_book.issue_book()
        else:
            print(f'\n❌ Книга \"{book_to_issue.title}\" автора {book_to_issue.author} не знайдена в цій бібліотеці.')

    def return_book(self, book_to_return: Book):  # Метод для повернення книги
        if not isinstance(book_to_return, Book):
            print('❌ Неможливо повернути: об\'єкт не є Книгою.')
            return

        found_book = self._find_book(book_to_return)

        if found_book:
            print(f'\n>>> Спроба повернути книгу: \"{found_book.title}\"')
            found_book.return_book()
        else:
            print(f'\n❌ Книга \"{book_to_return.title}\" автора {book_to_return.author} не належить цій бібліотеці.')

    def display_all_books(self) -> str:  # Метод, який дає інформацією про всі книги в бібліотеці
        if not self.books:
            return 'Бібліотека порожня.'
        return '\n'.join(f'{index}. {book}' for index, book in enumerate(self.books, start=1))


# --- Приклад використання ---
print('--- Створення книг різних жанрів ---')
book1 = FictionBook('Гаррі Поттер і Філософський камінь', 'Джоан Роулінг', series_name='Гаррі Поттер')
book2 = NonFictionBook('Коротка історія часу', 'Стівен Гокінг', topic='Космологія')
book3 = MysteryBook('Вбивство у Східному експресі', 'Агата Крісті', main_detective='Еркюль Пуаро')
book4 = FictionBook('1984', 'Джордж Орвелл')  # Без вказання серії
book5 = NonFictionBook('Чистий код', 'Роберт Мартін', topic='Програмування')
book6 = MysteryBook('Дівчина з татуюванням дракона', 'Стіг Ларссон')  # Без вказання детектива

my_library = Library()

print("\n--- Додавання книг до бібліотеки ---")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)
my_library.add_book(book6)
my_library.add_book(FictionBook('Гаррі Поттер і Філософський камінь', 'Джоан Роулінг',
                                series_name='Гаррі Поттер'))  # Спроба додати дублікат

print('\n----- Каталог Бібліотеки -----')
print(my_library.display_all_books())

print('\n--- Процес видачі та повернення книг ---')
my_library.issue_book(book1)  # Видаємо книгу Гаррі Поттер
my_library.issue_book(book5)  # Видаємо книгу Чистий код
my_library.issue_book(book1)  # Спроба видати вже видану книгу
# Створимо об'єкт книги, якої немає в бібліотеці, для демонстрації
temp_book_not_in_lib = Book('Незвідана книга', 'Невідомий автор')
my_library.issue_book(temp_book_not_in_lib)  # Спроба видати книгу, якої немає в бібліотеці

print('\n----- Каталог Бібліотеки після видачі -----')
print(my_library.display_all_books())
my_library.return_book(book5)  # Повертаємо книгу Чистий код
my_library.return_book(book1)  # Повертаємо книгу Гаррі Поттер
my_library.return_book(book2)  # Спроба повернути книгу, яка не була видана (наприклад, Коротка історія часу - book2)
my_library.return_book(temp_book_not_in_lib)  # Спроба повернути книгу, якої немає в бібліотеці

print('\n----- Каталог Бібліотеки після повернення -----')
print(my_library.display_all_books())