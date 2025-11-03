"""
Завдання №1.
Створіть дескриптор, який автоматично зберігає текст у верхньому регістрі.
У класі існує текстовий атрибут (наприклад, name).
Дескриптор при set повинен назначати йому значення у верхньому регістрі.
При заповненні атрибуту, також перевіряється тип (якщо не строка - помилка)
"""
class TextUpperDescriptor:
    def __get__(self, obj, obj_type=None):
        return obj.__text

    def __set__(self, obj, value: str):
        if type(value) is not str:
            raise ValueError('Можна тільки строку!')
        obj.__text = value.upper()

class Human:
    name = TextUpperDescriptor()

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

h = Human('боб')
print(h)

"""
Завдання №2.
Створіть клас Temperature, де:
- внутрішньо зберігається температура в Цельсіях (__celsius)
- через @property реалізований доступ до fahrenheit:
- getter повертає значення в Фаренгейтах
- setter дозволяє встановлювати значення в Фаренгейтах, автоматично перераховуючи в __celsius.
"""
class Temperature:
    def __init__(self, start_celsius):
        self.__celsius = start_celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * 5 / 9

temp = Temperature(10)
print(temp.fahrenheit)
temp.fahrenheit = 250
print(temp.fahrenheit)

"""
Завдання №3.
Зроби клас Circle, у якого:
- є атрибут radius
- властивість area обчислюється як π * r^2, але не дозволяє змінюватися (read-only)
"""

class Circle:
    #атрибут radius, area - property (p * radius *s )
    class Circle:
        def __init__(self, r):
            self._r = r

        @property
        def area(self):
            return self._r ** 2 * 3.14

        @area.setter
        def area(self, value):  # (???)
            raise ValueError('Площу неможливо назначити!')