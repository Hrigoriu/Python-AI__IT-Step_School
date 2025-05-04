
# Наслідування
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return f'Привіт, я людина {self.name}! Мій вік: {self.age}'

    def birthday(self):
        self.age += 1

class Teacher(Human):
    # Все, що є в батьковському класі
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # спочатку викликаємо батьківський ініт
        self.subject = subject

    def say_hi(self):  # переназначаємо метод say_hi, щоб переробити його поведінку
        return f'Я вчитель! Мене звуть {self.name}, я викладаю предмет: {self.subject}'

    def teach(self):  # створюємо метод teach, що буде унікальним для вчителя
        return f'Я {self.name}, я зараз викладаю!'

class Policeman(Human):
    def __init__(self, name, age, rank):
        super().__init__(name, age)
        self.rank = rank

    def say_hi(self):
        return f'Я поліцейський {self.name} ({self.age})! Моє звання: {self.rank}'

def interface(human: Human):
    print(human.say_hi())

bob = Human('Боб', 15)
anna = Teacher('Анна', 35, 'Математика')
john = Policeman('Джон', 29, 'Сержант')
#print(anna.say_hi())

john.birthday()
john.birthday()

interface(bob)
interface(anna)
interface(john)
#===========================================================
from abc import ABC, abstractmethod

class Figure(ABC):  # ABC - абстрактний клас
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod  # абстрактний метод - метод, який треба ОБОВ'ЯЗКОВО переназначити у дочірніх класах
    def move(self):
        print("Абстрактна фігура ходить!")

class Knight(Figure):
    def move(self):
        print('Конь ходить!')
#============================================================

#Завдання 1:
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def S(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def get_color(self) -> str:
        return self.color

class Circle(Shape):
    def __init__(self, color: str, radius: int):
        super().__init__(color)
        self.radius = int(radius)

    def S(self) -> int:
        return math.pi * (self.radius ** 2) # Формула площі кола: π * R^2

    def __str__(self) -> str:
        return f'Коло (Колір: {self.color}, Радіус: {self.radius})'

class Square(Shape):
    def __init__(self, color: str, side_length: int):
        super().__init__(color)
        self.side_length = int(side_length)

    def S(self) -> int:
        return self.side_length ** 2 # Формула площі квадрата: сторона ^ 2

    def __str__(self) -> str:
        return f'Квадрат (Колір: {self.color}, Сторона: {self.side_length})'

class Triangle(Shape):
    def __init__(self, color: str, base: int, height: int):
        super().__init__(color)
        self.base = int(base)
        self.height = int(height)

    def S(self) -> int:
        return 0.5 * self.base * self.height # Формула площі трикутника: 0.5 * основа * висота

    def __str__(self) -> str:
        return f'Трикутник (Колір: {self.color}, Основа: {self.base}, Висота: {self.height})'

circle1 = Circle('Синій', 5)
square1 = Square('Червоний', 4)
triangle1 = Triangle('Зелений', 6, 3)
circle2 = Circle('Жовтий', 2)

print('--- Інформація про фігури ---')

print(circle1)
print(square1)
print(triangle1)
print(circle2)

print('--- Обчислення площі ---')

print(f'Площа {circle1.get_color()} {circle1.__class__.__name__}: {circle1.S()}')
print(f'Площа {square1.get_color()} {square1.__class__.__name__}: {square1.S()}')
print(f'Площа {triangle1.get_color()} {triangle1.__class__.__name__}: {triangle1.S()}')
print(f'Площа {circle2.get_color()} {circle2.__class__.__name__}: {circle2.S()}')
#============================================================

#Завдання 2:
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def special_action(self):
        pass

class Lion(Animal):
    def __str__(self):
        return f'Я - {self.name}, і мені {self.age} років!'

    def make_sound(self):
        return f'{self.name} видає такий звук: рик'

    def special_action(self):
        return f'{self.name} полює.'

class Monkey(Animal):
    def __str__(self):
        return f'Я - {self.name}, і мені {self.age} років!'

    def make_sound(self):
        return f'{self.name} видає такий звук: уу-аа'

    def special_action(self):
        return f"{self.name} лазить по деревах."

class Elephant(Animal):
    def __str__(self):
        return f'Я - {self.name}, і мені {self.age} років!'

    def make_sound(self):
        return f'{self.name} видає такий звук: трубний звук'

    def special_action(self):
        return f'{self.name} бризкає водою.'

# Завдання 3:
class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise ValueError('Не тварина!')
        self.animals.append(animal)

    def all_sounds(self):
        for animal in self.animals:
            print(animal.make_sound())
            print(animal.special_action())

    def __str__(self) -> str:
        if not self.animals:
            return 'Зоопарк порожній.'
        animal_names = [animal.name for animal in self.animals]
        return f'Зоопарк містить {len(self.animals)} тварин: {", ".join(animal_names)}'

lion = Lion('Сімба', 5)
monkey = Monkey('Чічі', 3)
elephant = Elephant('Дамбо', 10)
another_monkey = Monkey('Коко', 4)

print('--- Інформація про тварин ---')
print(lion)
print(monkey)
print(elephant)
print('-' * 40)

# Створюємо об'єкт зоопарку
my_zoo = Zoo()

print('--- Додавання тварин до зоопарку ---')
# Додаємо тварин до зоопарку
my_zoo.add_animal(lion)
my_zoo.add_animal(monkey)
my_zoo.add_animal(elephant)
my_zoo.add_animal(another_monkey)
print(my_zoo)
my_zoo.all_sounds()

