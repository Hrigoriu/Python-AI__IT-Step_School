"""
Людина() -> Костянтин
Машина() -> BMW
"""
class Human:    # назву класу пишемо через CamelClass або CapWords
    def __init__(self, name: str, age:int, height: int | float): # метод-конструктор класу
        self.name = name
        self.age = age
        self.height = height

        self.is_alive = True

        self.money = 100 # Атрибут може приймати і статичне значення
    # age = 20
    # name = 'Bob'
    # height = 175

    def __str__(self):  # спрацьовує, коли об'єкт перетворюється на строку
        return f'Human {self.name}'

    def __len__(self):  # спрацьовує при функції len()
        return self.height

    def say_hi(self):   # метод say_hi
        return f'Hello! My name is: {self.name}! I`m {self.age} y.o.'

    def birthday(self, years: int): # метод, що буде збільшувати вік людини на вказану кількість
        self.age += years
        print(f'Людині {self.name} виповнилось {self.age} років!😁')

    def get_height(self):   # getter - просто повертає значення атрибуту
        return self.height

bob = Human('Bob', 27, 185)
alice = Human('Alice', 18, 161)

# bob = Human()   # ініціaлізація класу (створення екземпляру bob)
# alice = Human()

# !!! Так міняти атрибути не бажано! Це порушує одне з правил ООП
# alice.name = 'Alice'
# alice.age = 35
# alice.height =161

# print(bob.age)    #
# print(bob.name)
# print(bob.height)
#
# print(alice.age)  # звертаємось до атрибуту age, який знаходиться в об'єкту bob
# print(alice.name)
# print(alice.height)

print(bob.say_hi()) # метод насправді викликається: Human.say_hi(bob)
print(alice.say_hi())

#bob.age +=5 # поганий спосіб , щоб змінити атрибут

alice.birthday(10)
alice.birthday(5)
print(alice.say_hi())

print(bob)
print(alice)

print(len(bob))
print(len(alice))