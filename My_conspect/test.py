
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
