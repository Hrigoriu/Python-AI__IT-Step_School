
print(type('HELLO'))#<class 'str'>
print(type([1, 2, 3]))#<class 'list'>

print(type(str))#<class 'type'>
print(type(list))#<class 'type'>

def method_b(self):
    return self.b

MyNewClass = type('NewClass',
                  (),
                  {'a':100, 'b':200, 'method_a':lambda self : self.a, 'method_b': method_b}) #name, bases, dict
test = MyNewClass()
print(test.method_a())
print(test.method_b())
#=========================================================
# Задача №1: Створити метаклас, що перетворює всі публічні методи

class UpperAttrMeta(type):
    def __new__(cls, name: str, bases: tuple, dct:dict):    # __new__ - ініціатор класу (__init__ - ініціалізатор об'єкту)
        # print(f'Створився клас: {name}')
        # print(f'Його базові: {bases} ')
        # print(f'Його отрибути: {dict}')
        new_attrs = {}
        for attr_name, attr in dct.items():
            if not attr_name.startswith('__'):
                new_attrs[attr_name.upper()] = attr
            else:
                new_attrs[attr_name] = attr
        return super().__new__(cls, name, bases, new_attrs)


class Human(metaclass=UpperAttrMeta):
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Привіт я {self.name}! Мені {self.age} років'
    
olga = Human('Ольга',26)
print(olga.SAY_HELLO())

""" 
Задача №2
Зробіть метаклас, який що перетворює наявність методу test.Якщо його немає - помилка.
Назва класу повинна закінчуватися на слово test
"""
class TestCheckMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        if not name.endswith('Test'):
            raise ValueError('Назва класу повинна закінчуватися на Test!')

        if 'test' not in dct:
            raise ValueError(f'У класі повинно бути метод під назвою Test')
        return super.__new__(cls, name, bases, dct)

class NewTest(metaclass=TestCheckMeta):
    def test(self):
        pass
