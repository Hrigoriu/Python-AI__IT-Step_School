"""
Завдання 1: Клас «Книга»
Створіть клас Book, який має такі атрибути:
title (назва), author (автор), pages (кількість сторінок)
І реалізуйте магічні методи:
str – повертайте гарно відформатований рядок з інформацією про книгу.
len – повертайте кількість сторінок.
eq – книги вважаються однаковими, якщо в них однакові назва й автор.
"""
#var№1
class Book:
    def __init__(self, name: str, autor: str, pages: int):
        self.name = name
        self.autor = autor
        self.pages = pages

    def __str__(self):
        return f'Книга {self.name} - {self.autor} ({self.pages} сторінок)'

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if type(other) is Book:
            return False
        return self.name == other.name and self.autor == other.autor
book1 = Book('Я робот', 'Айзек Азімов', 350)

#-------------------------------------------------------------------------------------
#var№2
class Book:
    def __init__(self, name: str, autor: str, pages: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Назва книги має бути непустим рядком.')
        if not isinstance(autor, str) or not autor.strip():
            raise ValueError('Ім\'я автора має бути непустим рядком.')
        if not isinstance(pages, int) or pages <= 0:
             raise ValueError('Кількість сторінок має бути додатним цілим числом.')

        self.name = name.strip()
        self.autor = autor.strip()
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}" - {self.autor} ({self.pages} сторінок)'

    def __len__(self) -> int:
        return self.pages

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self.name == other.name and self.autor == other.autor

# --- Приклад використання класу Book ---

book1 = Book('Гаррі Поттер і Філософський камінь', 'Джоан Роулінг', 320)
book2 = Book('Маленький принц', 'Антуан де Сент-Екзюпері', 96)
book3 = Book('Гаррі Поттер і Філософський камінь', "Джоан Роулінг", 350)
book4 = Book('Гаррі Поттер і Таємна кімната', 'Джоан Роулінг', 384)

print('--- Інформація про книги ---')
print(book1)
print(book2)
print(book3)
print(book4)

print('-' * 40)

print('--- Кількість сторінок ---')
print(f"Кількість сторінок у '{book1.name}': {len(book1)}")
print(f"Кількість сторінок у '{book2.name}': {len(book2)}")
print(f"Кількість сторінок у '{book3.name}': {len(book3)}")
print(f"Кількість сторінок у '{book4.name}': {len(book4)}")

print('-' * 40)

print('--- Порівняння книг ---')
print(f"Книга 1 ('{book1.name}') дорівнює Книзі 3 ('{book3.name}')? {book1 == book3}") # Назва і автор однакові -> True
print(f"Книга 1 ('{book1.name}') дорівнює Книзі 2 ('{book2.name}')? {book1 == book2}") # Назва і автор різні -> False
print(f"Книга 1 ('{book1.name}') дорівнює Книзі 4 ('{book4.name}')? {book1 == book4}") # Назва різна -> False

"""
Завдання 2: Клас «Кошик покупок»
Створи клас ShoppingCart, який:
Зберігає список товарів (кожен товар — це кортеж: (назва, ціна)).
Має метод add_item(name, price) — додає товар.
Має метод total() — повертає загальну вартість.
Реалізуй магічні методи:
len — кількість товарів.
str — список товарів у вигляді рядка.
add — об'єднання двох кошиків. (резульатом повертаєтсья новий кошик)
"""
#var№1
class ShoppingCart:
    def __init__(self, start_cart=None):
        self.cart = [] if not start_cart else start_cart

    def __add__(self, other):
        if type(other) is not ShoppingCart:
            return ValueError('Додавати можна тільки корзини')
        return ShoppingCart(start_cart=self.cart + other.cart)

    def add_item(self, name: str, price: int | float):
        self.cart.append((name, price))  # price - 1 index

    def total(self):
        return sum(el[1] for el in self.cart)  # el - tuple(name, price)

sh1 = ShoppingCart()
sh2 = ShoppingCart()

sh1.add_item('Яблуко', 10)
sh2.add_item('Груша', 20)
sh3 = sh1 + sh2
print(sh3.cart)

#-------------------------------------------------------------------------------------
#var№2
class ShoppingCart:
    def __init__(self):
        self.items: list[tuple[str, float]] = []

    def add_item(self, name: str, price: float): # Метод для додавання нового товару до кошика
        self.items.append((name, price))
        print(f'Товар "{name}" додано до кошика.')

    def total(self) -> float:   # Метод для розрахунку загальної вартості товарів у кошику.
        return sum(item[1] for item in self.items)

    def __len__(self) -> int:   # Метод для розрахунку кількості елементів у списку items
        return len(self.items)

    def __str__(self) -> str:   # Метод для предявлення у вигляді рядка
        if not self.items:
            return 'Кошик порожній.'
        result = '--- Вміст кошика ---'
        for name, price in self.items:
            result += f'\n- {name}: {price:.2f} грн'
        result += f'\n--------------------'
        result += f'\nЗагальна вартість: {self.total():.2f} грн'
        return result

    def __add__(self, other):
        if not isinstance(other, ShoppingCart):
            raise TypeError('Можна додавати тільки об\'єкти типу ShoppingCart.')
        new_cart = ShoppingCart()
        new_cart.items.extend(self.items)
        new_cart.items.extend(other.items)
        return new_cart

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_item('Ноутбук', 25000.50)
cart1.add_item('Мишка', 500.00)
cart1.add_item('Клавіатура', 1200.75)

print('-' * 40)
cart2.add_item('Монітор', 8000.00)
cart2.add_item('Вебкамера', 750.20)

print('-' * 40)
print('Вміст першого кошика:')
print(cart1)
print('-' * 40)
print(f'Кількість товарів у першому кошику: {len(cart1)}')
print(f'Загальна вартість товарів у першому кошику: {cart1.total():.2f} грн')

print('-' * 40)
combined_cart = cart1 + cart2
print('Вміст об\'єднаного кошика:')
print(combined_cart)
print('-' * 40)
print(f'Кількість товарів в об\'єднаному кошику: {len(combined_cart)}')
print(f'Загальна вартість товарів в об\'єднаному кошику: {combined_cart.total():.2f} грн')

#=============================================================================================
"""
Завдання3: Клас BankAccount:
Атрибути: ім’я власника, баланс.
Методи: deposit(), withdraw()
Магічні методи:
str — форматований баланс
add — об'єднання рахунків (сума балансів)
lt, eq — порівняння за балансом
"""
#var№1
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        new_name = f'Спільний акаунт: {self.owner} + {other.owner}'
        new_balance = self.balance + other.balance

        return BankAccount(new_name, new_balance)

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance - value >= 0:
            self.balance -= value

#-------------------------------------------------------------------------------------
#var№2
class BankAccount:
    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        if not isinstance(owner_name, str) or not owner_name.strip():
            raise ValueError('Ім\'я власника має бути непустим рядком.')
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
             raise ValueError('Початковий баланс має бути невід\'ємним числом.')
        self.owner_name = owner_name.strip()
        self.balance = float(initial_balance)

    def deposit(self, amount: float):   # Метод для поповнення рахунку.
        if not isinstance(amount, (int, float)) or amount <= 0:
            print('Помилка: Сума поповнення має бути додатнім числом.')
            return
        self.balance += amount
        print(f'Рахунок {self.owner_name} поповнено на {amount:.2f} грн. Новий баланс: {self.balance:.2f} грн.')

    def withdraw(self, amount: float):  # Метод для зняття коштів з рахунку.
        if not isinstance(amount, (int, float)) or amount <= 0:
            print('Помилка: Сума зняття має бути додатнім числом.')
            return
        if amount > self.balance:
            print(f'Помилка: Недостатньо коштів на рахунку {self.owner_name}. Доступно: {self.balance:.2f} грн.')
            return
        self.balance -= amount
        print(f'З рахунку {self.owner_name} знято {amount:.2f} грн. Новий баланс: {self.balance:.2f} грн.')

    def __str__(self) -> str:   # Метод для того, щоб представити об'єкт у вигляді рядка.
        return f'Баланс рахунку {self.owner_name}: {self.balance:.2f} грн'

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance < other.balance

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
             return NotImplemented
        return self.balance == other.balance

account1 = BankAccount('Олександр', 1000.0)
account2 = BankAccount('Марія', 500.50)
account3 = BankAccount('Петро') # Рахунок з початковим балансом 0

print('--- Початковий стан ---')
print(account1)
print(account2)
print(account3)
print('-' * 40)

account1.deposit(200.0)
account2.withdraw(100.0)
account3.deposit(50.75)
print('-' * 40)

print('--- Стан після операцій ---')
print(account1)
print(account2)
print(account3)

print('-' * 40)
# Спроби викликати помилки
account1.deposit(-50)
account2.withdraw(1000.0)
print('-' * 40)
print('--- Стан після некоректних операцій ---')
print(account1)
print(account2)
print('-' * 40)

total_balance_alex_maria = account1 + account2
print(f'Сума балансів рахунків Олександра та Марії: {total_balance_alex_maria:.2f} грн')

total_balance_maria_petro = account2 + account3
print(f'Сума балансів рахунків Марії та Петра: {total_balance_maria_petro:.2f} грн')
print('-' * 40)

print(f'Баланс Олександра менший за баланс Марії? {account1 < account2}')
print(f'Баланс Марії менший за баланс Олександра? {account2 < account1}')
print(f'Баланс Олександра дорівнює балансу Петра? {account1 == account3}')

account4 = BankAccount('Ірина', account2.balance)
print(f'Баланс Марії дорівнює балансу Ірини? {account2 == account4}')
print('-' * 40)