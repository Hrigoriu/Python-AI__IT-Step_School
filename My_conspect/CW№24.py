"""
Завдання № 1.
Створіть клас "Квадрат" з атрибутом - довжиною сторони.
Зробіть метод "Площа", що виводить площ квадрату та метод "Периметр"
"""
#variant№1
class Kvadrat:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
#        area = self.side_length ** 2
#        print(f'Площа квадрата зі стороною {self.side_length} дорівнює {area}.')
        return self.side_length ** 2

    def perimeter(self):
#        perimeter = 4 * self.side_length
#        print(f'Периметр квадрата зі стороною {self.side_length} дорівнює {perimeter}.')
        return 4 * self.side_length

my_kvadrat = Kvadrat(5)
# my_kvadrat.area()
# my_kvadrat.perimeter()

print(f'Площа: {my_kvadrat.area()}')
print(f'Периметр: {my_kvadrat.perimeter()}')

#==========================================================
#variant№2
class Square:
    def __init__ (self, a: int|float):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimetr(self):
        return self.a * 4

square_1 = Square(15)
square_2 = Square(15)
print(square_1.area())
print(square_2.perimetr())
#==================================================================
"""
Завдання № 2. 
Реалізуйте клас "Бібліотека" з методами для додавання та видалення книг, 
пошуку книги за автором або назвою та відображення списку доступних книг.
"""
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})
        return f'Книга "{title}" автора {author} додана до бібліотеки.'

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                return f'Книга "{title}" була видалена з бібліотеки.'
        return f'Книга "{title}" не знайдена.'

    def find_by_author(self, author):
        found = [book for book in self.books if book['author'] == author]
        return found

    def find_by_title(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None

    def show_books(self):
        return self.books if self.books else []

lib = Library()
print(lib.add_book('Фундація', 'Айзек Азімов'))
print(lib.add_book('Я, робот', 'Айзек Азімов'))
print(lib.add_book('Кінець Вічності', 'Айзек Азімов'))
print('='*40)
books_by_asimov = lib.find_by_author('Айзек Азімов')
for book in books_by_asimov:
    print(f'{book["title"]} (Автор: {book["author"]})')

print('='*40)
print(lib.remove_book('Я, робот'))
print('='*40)
for book in lib.show_books():
    print(f'{book["title"]} (Автор: {book["author"]})')
#=========================================================================
class Library:
    def __init__(self):
        self.books = {}  # автор: [книга, книга]

    def add_book(self, autor, title):
        if autor not in self.books:
            self.books[autor] = [title]
        else:
            self.books[autor].append(title)

    def find_book_by_title(self, title):
        for autor_name, autor_list in self.books.items():
            if title in autor_list:
                print(f'Книгу було знайдено у автора {autor_name}')
                return
        print(f'Книги у бібліотеці немає!')

    def print_all_books(self):
        for autor_name, autor_list in self.books.items():
            print(f'-----Автор: {autor_name}-----')
            print('\n'.join(autor_list))

my_library = Library()

my_library.add_book('С. Кінг', "Сяйво")
my_library.add_book("Д. Браун", "Джерело")
my_library.add_book('С. Кінг', "Воно")
my_library.add_book('Й. Гетте', "Фауст")
my_library.add_book("Д. Браун", "Код Да Вінчі")

my_library.find_book_by_title('Фауст')
my_library.find_book_by_title('Кобзар')

my_library.print_all_books()