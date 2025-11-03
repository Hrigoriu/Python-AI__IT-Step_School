
class Human:
    __count = 0

    def __init__(self, name: str, age: int):
        self.__name = name   #_name - режим protected
        self.__age = age

    @classmethod    # класовий метод - метод, що працює на рівні класу, а не об'єкту
    def __add_counter(cls):     #cls - Human
        cls.__count += 1    # збільшується кількість людей на один

    @classmethod
    def get_humans_count(cls):
        return cls.__count

    @staticmethod
    def say_hi():
        return "Hi"

    def __str__(self):
        return f'Людина {self.__name}.  {self.__age} років'

    def __int__(self):
        return self.__age

    def __add__(self, other:int):   # спрацьовує при "+"
        if not isinstance(other, Human):
            raise ValueError('Додавати можна тільки людей!')
        return int(self) + int(other)

    def _get_name_(self):
        return self.__name

    def _get_age_(self):
        return self.__age

class Teacher(Human):
    def test_teacher(self):
        print(f'{self._get_name()}, {self._get_age()}')


class Auto:
    def __init__(self, name: str, max_passengers: int = 4):
        self.name = name
        self.max_passengers = max_passengers
        self.passengers: list[Human] = []

    def add_passengers(self, *passengers: Human):
        for human in passengers:
            if not isinstance(human, Human):
                raise ValueError('Додавати можна тільки людей!')
            if len(self.passengers) >= self.max_passengers:
                print(f'Авто {self.name} переповнене!')
                return
            self.passengers.append(human)

    def print_all_passengers(self):
        print(f'Перелік пасажирів {self.name}: ')
        for index, human in enumerate(self.passengers, start=1):
            print(f'{index}. {human}')

class Calculator:
    @staticmethod
    def plus(n1, n2):
        return n1 + n2

    def minus(n1, n2):
        return n1 - n2

bob = Human('Боб', 27)
alice = Human('Аліса', 35)
john = Human('Джон', 15)

print(bob.say_hi())
print(alice.say_hi())

print(john.get_humans_count())

audi = Auto('Audi', 2)
audi.add_passengers(bob, alice)

audi.print_all_passengers()

calc = Calculator()
print(calc.plus(10, 20))
#================================================================
"""
Завдання 1: Температурний датчик
Створи клас TemperatureSensor, у якому:
Є приватне поле temperature (в градусах Цельсія). (режим private)
Метод get_temperature() повертає температуру в Цельсіях.
Метод get_temperature_fahrenheit() повертає температуру у Фаренгейтах.
Метод set_temperature(value), який дозволяє встановлювати значення тільки в межах від -100 до +100.
"""
class TemperatureSensor:
    def __init__(self, temperature: float = 0.0):
        self.__temperature = temperature

    def get_temperature(self) -> float:
        return self.__temperature

    def get_temperature_fahrenheit(self) -> float:
        fahrenheit = (self.__temperature * 9/5) + 32    # Формула: F = (C * 9/5) + 32
        return fahrenheit

    def set_temperature(self, value: float):
        if not isinstance(value, (int, float)):
            return
        if -100 <= value <= 100:
            self.__temperature = float(value)
            print(f'Температуру встановлено: {self.__temperature}°C.')
        else:
            print(f'Помилка: температура {value}°C поза діапазоном [-100, 100]. Температура не змінена.')

    def __str__(self) -> str:
        return (f'Датчик температури: {self.get_temperature()}°C'
                f'({self.get_temperature_fahrenheit()}°F)')

# --- Приклад використання ---
print('--- Створення датчика ---')
sensor1 = TemperatureSensor(25.0)
print(sensor1)

print('\n--- Зчитування температури ---')
celsius = sensor1.get_temperature()
print(f'Температура в Цельсіях: {celsius}°C')
fahrenheit = sensor1.get_temperature_fahrenheit()
print(f'Температура в Фаренгейтах: {fahrenheit}°F"')

print('\n--- Встановлення температури ---')
sensor1.set_temperature(95)
print(sensor1)

print('-'*10)
sensor1.set_temperature(110.0)
print(sensor1) # Температура не змінилася

sensor1.set_temperature(-150.0)
print(sensor1) # Температура не змінилася

