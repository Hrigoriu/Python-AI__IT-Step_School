
"""
Завдання №1.
Створіть метаклас, що обмежує деякі назви атрибутів та методів(), забороняючи їх використання.
Перелік обмежених назв можна написати прямо у метакласі.
"""
class RestrictedNamesMeta(type):
    RESTRICTED_NAMES = ['restricted_attribute', 'forbidden_method', 'private', ' confidential_data']

    def __new__(cls, name: str, bases: tuple, dct: dict):
        print(f'Метаклас: Перевіряю клас "{name}" на заборонені назви...')
        for attr_name in dct:
            if attr_name in cls.RESTRICTED_NAMES:
                raise ValueError(f'Використано заборонену назву "{attr_name}" у класі "{name}".')
        return super().__new__(cls, name, bases, dct)

# --- Приклади використання ---
#1
print('--- Створення коректного класу (без забороненої назви) ---')
try:
    class ValidClass(metaclass=RestrictedNamesMeta):
        def __init__(self, data):
            self.data = data

        def allowed_method(self):
            print('Це дозволений метод.')

    print('Клас ValidClass успішно створено.')
    valid_obj = ValidClass(123)
    valid_obj.allowed_method()
    print(valid_obj.data)
except ValueError as e:
    print(f'Помилка при створенні класу ValidClass: {e}')

#2
print('\n--- Створення класу із забороненим атрибутом ---')
try:
    class InvalidAttributeClass(metaclass=RestrictedNamesMeta):
        def __init__(self):
            self.restricted_attribute = 'Секрет'

        def regular_method(self):
            pass

    print('Клас InvalidAttributeClass успішно створено.')
except ValueError as e:
    print(f'Помилка при створенні класу InvalidAttributeClass: {e}')

#3
print('\n--- Створення класу із забороненим методом ---')
try:
    class InvalidMethodClass(metaclass=RestrictedNamesMeta):
        def __init__(self):
            pass

        def forbidden_method(self):
            print('Цей метод заборонено!')
    print('Клас InvalidMethodClass успішно створено.')
except ValueError as e:
    print(f'Помилка при створенні класу InvalidMethodClass: {e}')

#4
print('\n--- Створення класу, що успадковує, але додає заборонену назву ---')
try:
    class ParentClass(metaclass=RestrictedNamesMeta):
        def __init__(self):
            self.parent_attr = 1

    class ChildClass(ParentClass):
        def __init__(self):
            super().__init__()
            self.child_attr = 2
            self.private = 'Приватне'
    print('Клас ChildClass успішно створено.')

except ValueError as e:
     print(f'Помилка при створенні класу ChildClass: {e}')

"""
Завдання №2.	
Реалізуйте метаклас, що забороняє спадкування(наслідування) від певних класів. 
Перелік можете написати прямо у метакласі.
"""
class NoInheritanceFromMeta(type):
    FORBIDDEN_BASE = ['ForbiddenBase', 'list', 'dict']
    def __new__(cls, name: str, bases: tuple, dct: dict):
        print(f'Метаклас: Перевірка базових класів для "{name}" ...')

        for base_class in bases:
            base_class_name = base_class.__name__

            if base_class_name in cls.FORBIDDEN_BASE:
                raise TypeError(f'Клас "{name}" не може успадковувати від забороненого базового класу "{base_class_name}" ')
        return super().__new__(cls, name, bases, dct)

# --- Приклади використання ---
#1
class ForbiddenBase:
    pass

class AllowedBase:
    pass

print('--- Створення коректного класу  ---')
try:
    class MyValidClass(AllowedBase, metaclass=NoInheritanceFromMeta):
        def __init__(self, data):
            self.data = data
    print('Клас MyValidClass успішно створено.')

    obj = MyValidClass(100)
    print(obj.data)
except TypeError as e:
    print(f'Помилка при створенні класу MyValidClass: {e}')

#2
print('\n--- Створення класу, що успадковує від забороненого класу ForbiddenBase ---')
try:
    class TryForbidden(ForbiddenBase, metaclass=NoInheritanceFromMeta):
        pass
    print('Клас TryForbidden успішно створено.')
except TypeError as e:
    print(f'Помилка при створенні класу TryForbidden: {e}')

#3
print('\n--- Створення класу, що успадковує від забороненого вбудованого типу (list) ---')
try:
    class MyForbiddenList(list, metaclass=NoInheritanceFromMeta):
        pass
    print('Клас MyForbiddenList успішно створено (цього не повинно статись).')
except TypeError as e:
    print(f'Помилка при створенні класу MyForbiddenList: {e}')

#4
print('\n--- Створення класу БЕЗ метакласу (успадковує від забороненого) ---')
class WithoutMeta(ForbiddenBase):
     pass
print('Клас WithoutMeta успішно створено, успадковує від ForbiddenBase.')
no_meta = WithoutMeta()


