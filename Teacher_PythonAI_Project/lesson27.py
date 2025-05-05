
class Human:
    __count = 0

    def __init__(self, name: str, age: int):
        self.__name = name  # _name = режим protected
        self.__age = age  # __name = режим private

        self.__add_counter()

    @classmethod  # класовий метод - метод, що працює на рівні класу, а не об'єкту
    def __add_counter(cls):  # cls - Human
        cls.__count += 1  # збільшуємо кількість людей на один

    @classmethod
    def get_humans_count(cls):
        return cls.__count

    @staticmethod
    def say_hi():
        return 'Hi!'

    def __str__(self):
        return f'Людина {self.__name}. {self.__age} років.'

    def __int__(self):
        return self.__age

    def __add__(self, other):  # спрацьовує при "+"
        if not isinstance(other, Human):
            raise ValueError('Додавати можна тільки людей!')

        return int(self) + int(other)

    def _get_name(self):
        return self.__name

    def _get_age(self):
        return self.__age


class Teacher(Human):
    def test_teacher(self):
        print(f'{self._get_name()}, {self._get_age()}')


class Auto:
    def __init__(self, name: str, max_passengers: int = 4):
        self.name = name
        self.max_passengers = max_passengers
        self.__passengers: list[Human] = []

    def add_passengers(self, *passengers: Human):
        for human in passengers:
            if not isinstance(human, Human):
                raise ValueError('Додавати можна тільки людей!')

            if len(self.__passengers) >= self.max_passengers:
                print(f'Авто {self.name} переповнене!')
                return

            self.__passengers.append(human)

    def print_all_passengers(self):
        print(f'Перелік пасажирів {self.name}: ')

        for index, human in enumerate(self.__passengers, start=1):
            print(f'{index}. {human}')


class Calculator:
    @staticmethod
    def plus(n1, n2):
        return n1 + n2

    @staticmethod
    def minus(n1, n2):
        return n1 - n2


bob = Human('Боб', 27)
alice = Human('Аліса', 35)
john = Teacher('Джон', 15)

print(bob.say_hi())
print(john.say_hi())

# print(john.get_humans_count())
#
# audi = Auto('Audi', 2)
#
# audi.add_passengers(bob, alice)
#
# audi.print_all_passengers()

calc = Calculator()

print(calc.plus(10, 20))
