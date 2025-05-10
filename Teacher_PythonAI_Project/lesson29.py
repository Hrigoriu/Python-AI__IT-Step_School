
class MultClass:
    def __init__(self, number: int | float):
        self.__number = number

    def __call__(self, value: int | float):  # call перетворює клас на функтор
        self.__number *= value
        return self.__number

    def get_number(self):
        return self.__number


class Person:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):  # getter - спрацьовує під час отримання значення атрибуту
        return self.__name

    @name.setter  # setter - спрацьовує під час встановлення нового значення атрибуту
    def name(self, new_name: str):
        if not new_name:
            raise ValueError("Ім'я не може бути порожнім!")

        self.__name = new_name.capitalize()

    @name.deleter  # deleter - спрацьовує під час видалення атрибуту
    def name(self):
        raise ValueError('Атрибут не можна видалити!')

        # print('Викликається делітер')
        #
        # if len(self.__name) != 5:  # наше ім'я можна видалити лише, якщо воно довжиною 5 (не знаю навіщо)
        #     raise ValueError('Можна видалити тільки ім`я довжиною 5 літер!')
        #
        # del self.__name


class Person2:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not new_name:
            raise ValueError("Ім'я не може бути порожнім!")

        self.__name = new_name.capitalize()


class PointValidatorX:
    def __get__(self, obj, obj_type=None):
        print('Викликається дескриптор точки X!')
        print(obj_type)
        return obj.__x

    def __set__(self, obj, value):
        print("Викликається сеттер точки X!")
        if type(value) is not int:
            raise ValueError('Координата Х повинна бути цілим числом!')

        if value not in range(-50, 51):
            raise ValueError('Координата Х повинна бути в діапазоні від -50 до 50!')

        obj.__x = value


class PointValidatorY:
    def __get__(self, obj, obj_type=None):
        print('Викликається дескриптор точки Y!')
        print(obj_type)
        return obj.__y

    def __set__(self, obj, value):
        print("Викликається сеттер точки Y!")
        if type(value) is not int:
            raise ValueError('Координата Y повинна бути цілим числом!')

        if value not in range(-50, 51):
            raise ValueError('Координата Y повинна бути в діапазоні від -50 до 50!')

        obj.__y = value


# Є клас Точка(X, Y). Координати не можуть бути менше -50 та більше 50 та бути цілими числами
class Point:
    x = PointValidatorX()
    y = PointValidatorY()

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point (x: {self.x}, y: {self.y})'


point1 = Point(25, 25)
print(point1)
