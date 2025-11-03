
class Human:  # назву класу пишемо через CamelCase або CapWords
    def __init__(self, name: str, age: int, height: int | float):  # init - метод-конструтор класу
        self.name = name
        self.age = age
        self.height = height

        self.money = 100  # атрибут може приймати і статичне значення

    def __str__(self):  # спрацьовує, коли об'єкт перетворюється на строку
        return f'Human {self.name}'

    def __len__(self):  # спрацьовує при функції len()
        return self.height

    def say_hi(self):  # метод say_hi
        return f'Hello! My name is: {self.name}! I`m {self.age} y.o.'

    def get_height(self):  # getter - просто повертає значення атрибуту
        return self.height

    def birthday(self, years: int):  # метод, що буде збільшувати вік на вказану кількість
        self.age += years
        print(f'Людині {self.name} виповнилось {self.age} років!🎉')


bob = Human('Bob', 27, 185)  # ініціалізація класу (створення екземпляру bob)
alice = Human('Alice', 18, 160)

# !!! Так міняти атрибути не бажано! Це порушує одне з правил ООП
# alice.name = 'Alice'
# alice.age = 35
# alice.height = 161

# print(alice.age)  # звертаємось до атрибуту age який знаходиться у об'єкту bob
# print(alice.name)
# print(alice.height)

print(bob.say_hi())  # Метод насправді викликається: Human.say_hi(bob)

alice.birthday(10)
alice.birthday(5)

print(alice.say_hi())

print(bob)
print(alice)

print(len(bob))
print(len(alice))
