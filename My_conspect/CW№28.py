"""
#Завдання 1. Реалізуйте метаклас, який буде автоматично
додавати всі створені класи у глобальний реєстр
(наприклад, глобальный словник registry).

registry = {} #name: class
"""
#variant №1
registry = {}
class RegistryMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict):
        created_class = super().__new__(cls, name, bases, dct)
        registry[name] = created_class
        print(f'Клас "{name}" зареєстровано.')
        return created_class

class MyRightHand(object, metaclass=RegistryMeta):
    def __init__(self, value: str):
        self.value = value

    def greet(self):
        print(f'Моя MyRightHand : {self.value}')

class MyLeftHand(object, metaclass=RegistryMeta):
     def process(self, data):
         print(f'Моя MyLeftHand : {data}')

class MyRightLeg:
     def info(self):
         print('Це клас, що недобавлений до словника.')

print('Вміст словника registry:', registry)

print('\n--- Приклад зареєстрованих класів ---')
Class1 = registry.get('MyRightHand')
Class2 = registry.get('MyLeftHand')
Class3 = registry.get('MyRightLeg')

if Class1:
    obj1 = Class1('махає')
    obj1.greet()

if Class2:
    obj2 = Class2()
    obj2.process('в кишені')

if Class3:
     print('Помилка: MyRightLeg не зареєстрований, але знайдений в registry.')
else:
     print('MyRightLeg не знайдений в registry .')

#variant №2
"""
#Завдання 2. Створіть метаклас, який автоматично генерує 
метод repr для класу, якщо він не реалізований. 
У методі мають відображатися всі змінні екземпляра.

#Відображення користувача
__str__     для читача
__repr__    для технічного
"""
registry = {}
class AutoRegistryMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        new_class = super().__new__(cls, name, bases, dct)
        registry[name] = new_class
        return new_class

class AutoReprMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        if '__repr__' not in dct:
            def __repr__(self):
                return f'Name: {name}. Methods: {', '.join(f'{k}={v}' for k, v in dct.items())}'
            dct['__repr__'] = __repr__
        return super().__new__(cls, name, bases, dct)

class CounterMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        dct['counter'] = 0
        class_init = dct['__init__']
        def __init__(self, *args, **kwargs):
            self.__class__.counter += 1
            class_init(self, *args, **kwargs)
        dct['__init__'] = __init__
        return super().__new__(cls, name, bases, dct)

class Human(metaclass=CounterMeta):
    def __init__(self, age):
        self.age = age

h1 = Human(20)
h2 = Human(20)
h3 = Human(20)
h4 = Human(20)
print(Human.counter)
#=====================================================================

"""
#Завдання 3. Створіть метаклас, який додає до класу
лічильник створених екземплярів.
(Як у попередньому занятті)
"""

registry = {}
class AutoRegistryMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        new_class = super().__new__(cls, name, bases, dct)

        registry[name] = new_class
        return new_class

class AutoReprMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        if '__repr__' not in dct:
            def __repr__(self):
                return f'Name: {name}. Methods: {', '.join(f'{k}={v}' for k, v in dct.items())}'
            dct['__repr__'] = __repr__
        return super().__new__(cls, name, bases, dct)

class CounterMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict[str, object]):
        dct['counter'] = 0
        class_init = dct['__init__']

        def __init__(self, *args, **kwargs):
            self.__class__.counter += 1
            class_init(self, *args, **kwargs)
        dct['__init__'] = __init__
        return super().__new__(cls, name, bases, dct)

class Human(metaclass=CounterMeta):
    def __init__(self, age):
        self.age = age

h1 = Human(20)
h2 = Human(20)
h3 = Human(20)
h4 = Human(20)

print(Human.counter)






