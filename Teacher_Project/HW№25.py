"""
Завдання №1
Реалізуйте клас Shop (магазин), у який можна додавати товари (клас Product).
Товар має назву та ціну у якості атрибутів.
Магазин повинен мати:
*методи для друку всіх наявних товарів,
*перевірки наявності товару (через магічний метод __contains__),
*додавання товару.
"""

class Product:
    def __init__(self, name: str, price: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Назва товару має бути непустим рядком.')
        if not isinstance(price, (int, float)) or price < 0:
             raise ValueError('Ціна товару має бути невід\'ємним числом.')

        self.name = name.strip()
        self.price = float(price)

    def __str__(self) -> str:
        return f'{self.name} - {self.price:.2f} грн'

class Shop:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError('До магазину можна додати лише об\'єкти класу Product.')
        self.products.append(product)
        print(f'Товар "{product.name}" додано до магазину.')

    def print_all_products(self):
        print('--- Товари в магазині ---')
        if not self.products:
            print('Наразі товарів немає.')
            return
        for product in self.products:
            print(product)
        print('-------------------------')

    def __contains__(self, item: str) -> bool:
        if not isinstance(item, str):
            return False
        for product in self.products:
            if product.name.lower() == item.lower():
                return True
        return False

# --- Приклад використання ---

# Створюємо об'єкти товарів
product1 = Product('Ноутбук', 25000.50)
product2 = Product('Мишка', 500.00)
product3 = Product('Клавіатура', 1200.75)
product4 = Product('Монітор', 8000.00)

my_shop = Shop()

print('--- Додавання товарів ---')
my_shop.add_product(product1)
my_shop.add_product(product2)
my_shop.add_product(product3)
my_shop.add_product(product4)

print('-' * 40)
my_shop.print_all_products()
print('-' * 40)

print('--- Перевірка наявності товару (\"in\") ---')
print(f'В магазині є "Мишка"? {"Мишка" in my_shop}') #  True
print(f'В магазині є "Навушники"? {"Навушники" in my_shop}') # False
print(f'В магазині є "ноутбук" ? {"ноутбук" in my_shop}') # True
print(f'В магазині є об\'єкт product1? {product1 in my_shop}') # False, бо __contains__ перевіряє рядок, а не об`єкт

#===========================================================================
"""
Завдання №2
Реалізуйте класи Auto та Human. 
Автомобіль(Auto) повинен мати атрибути: 
*назву та максимальну кількість пасажирів. 
Людина(Human) повинна мати: ім’я та вік. 
Реалізуйте можливість додавання людей до авто (якщо воно ще не переповнене), 
можливість подивитись кількість пасажирів (len) 
та вивід всіх пасажирів авто(кожен пасажир авто повинен привітатись). 
Людина повинна мати метод hi(привітання), 
що виводить її атрибути в будь-якому форматі.
"""

class Human:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Ім\'я людини має бути непустим рядком.')
        if not isinstance(age, int) or age <= 0:
            raise ValueError('Вік людини має бути додатним цілим числом.')

        self.name = name.strip()
        self.age = age

    def hi(self):
        print(f'Привіт! Я {self.name}, мені {self.age} років.')

    def __str__(self) -> str:
        return f'Людина: {self.name} - ({self.age} років)'

class Auto:
    def __init__(self, name: str, max_passengers: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Назва авто має бути непустим рядком.')
        if not isinstance(max_passengers, int) or max_passengers <= 0:
             raise ValueError('Максимальна кількість пасажирів має бути додатним цілим числом.')

        self.name = name.strip()
        self.max_passengers = max_passengers
        self.passengers: list[Human] = []

    def add_passenger(self, human: Human):
        if not isinstance(human, Human):
            print(f'Помилка: {human} - це не Людина. Додати неможливо.')
            return
        if len(self.passengers) >= self.max_passengers:
            print(f'Помилка: Авто "{self.name}" вже повне (макс {self.max_passengers} пасажирів). Неможливо додати {human.name}.')
            return
        self.passengers.append(human)
        print(f'{human.name} сів(ла) в авто "{self.name}".')

    def __len__(self) -> int:
        return len(self.passengers)

    def all_passengers(self):
        print(f'--- Пасажири авто "{self.name}" кажуть привіт: ---')
        if not self.passengers:
            print('В авто нікого немає.')
            return
        for passenger in self.passengers:
            passenger.hi()
        print('-----------------------------------------------')

    def __str__(self) -> str:
        return f'Авто "{self.name}" (макс. пасажирів: {self.max_passengers}, зараз: {len(self)}).'


# --- Приклад використання ---

# Створюємо об'єкти людей
human1 = Human('Олег', 30)
human2 = Human('Ірина', 25)
human3 = Human('Петро', 45)
human4 = Human('Олена', 22)
human5 = Human('Василь', 50)

print('------- Привітання людей -------')
human1.hi()
human4.hi()
print('-' * 40)

# Створюємо об'єкт авто з максимальною кількістю пасажирів 2-6
car1 = Auto('Купе', 2)
car2 = Auto('Седан', 4)
car3 = Auto('Мінівен', 6)

print('------- Стан авто -------')
print(car1)
print(car2)
print(car3)
print('-' * 40)

print('------- Додавання пасажирів в Седан -------')
car2.add_passenger(human1)
car2.add_passenger(human2)
car2.add_passenger(human3)
car2.add_passenger(human4)
car2.add_passenger(human5) # Василь намагається сісти (авто вже повне)
print('-' * 40)

print('------- Перевірка кількості пасажирів (len) -------')
print(f'Кількість пасажирів в авто "{car1.name}": {len(car1)}')
print(f'Кількість пасажирів в авто "{car2.name}": {len(car2)}')
print(f'Кількість пасажирів в авто "{car3.name}": {len(car3)}')
print('-' * 40)

print('------- Пасажири авто вітаються -------')
car1.all_passengers()
car2.all_passengers()
print('-' * 40)

print('------- Додавання пасажирів в Мінівен -------')
car3.add_passenger(human1)
car3.add_passenger(human3)
car3.add_passenger(human5)
print('-' * 40)

print(car3)
car3.all_passengers()

# Спроба додати щось інше в авто
car1.add_passenger('Собака') # Виведе помилку