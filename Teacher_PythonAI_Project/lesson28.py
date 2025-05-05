
print(type('HELLO'))
print(type([1, 2, 3]))

print(type(str))
print(type(list))

def method_b(self):
    return self.b


MyNewClass = type('NewClass',
                  (),
                  {'a': 100, 'b': 200, 'method_a': lambda self: self.a, 'method_b': method_b})  # name, bases, dict


test = MyNewClass()

print(test.method_a())
print(test.method_b())


# Задача1 - створіть метаклас, що перетворює всі публічні методи на uppercase()
class UpperAttrMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):  # __new__ - ініціалізатор класу (__init__ - ініціалізатор об'єкту)
        new_attrs = {}

        for attr_name, attr in dct.items():
            if not attr_name.startswith('__'):
                new_attrs[attr_name.upper()] = attr
            else:
                new_attrs[attr_name] = attr

        return super().__new__(cls, name, bases, new_attrs)


# 2. Зробіть метаклас, який перевіряє наявність методу test. Якщо його немає - помилка. Назва класу
# повинна закінчуватись на слово Test
class TestCheckMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        if not name.endswith('Test'):
            raise ValueError("Назва класу повинна закінчуватись на Test!")

        if 'test' not in dct:
            raise ValueError('У класі повинен бути метод з назвою test!')

        return super().__new__(cls, name, bases, dct)


class Human(metaclass=UpperAttrMeta):
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Привіт, я {self.name}! Мені {self.age} років!'


class NewTest(metaclass=TestCheckMeta):
    def test(self):
        pass
