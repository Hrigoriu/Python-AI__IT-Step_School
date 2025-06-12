# ПАТЕРНИ ПРОЕКТУВАННЯ
# Породжувальні патерни


# 1. Singleton(Одинак)
# Суть патерну: гарантує, що у класу буде тільки один екземпляр
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.counter = 0

        return cls._instance

    def add_counter(self):
        self.counter += 1

    def count(self):
        return self.counter


singleton_1 = Singleton()
singleton_2 = Singleton()

for _ in range(5):
    singleton_1.add_counter()

singleton_3 = Singleton()

print(singleton_3.count())

# 2. Фабричний метод(Factory Method)
# Суть патерну: реалізує інтерфейс створення об'єкта, але дозволяє підкласам вирішувати
# у "фабричному методі", який саме клас створювати


class Button:
    def click(self):
        pass


class WindowsButton(Button):
    def click(self):
        return 'Windows button clicked!'


class LinuxButton(Button):
    def click(self):
        return 'Linux button clicked!'


class Computer:
    def create_button(self) -> Button:
        raise NotImplementedError


class WindowsComputer(Computer):
    def create_button(self):
        return WindowsButton()


class LinuxComputer(Computer):
    def create_button(self):
        return LinuxButton()


def interface(comp: Computer):
    btn = comp.create_button()
    print(btn.click())


wind_comp = WindowsComputer()
linux_comp = LinuxComputer()

interface(wind_comp)
interface(linux_comp)

# 3. Абстрактна Фабрика (Abstract Factory)
# Суть патерну: реалізує інтерфейс для створення цілих семейств об'єктів


class Chair:
    def sit(self):
        pass


class Table:
    def dine(self):
        pass


class ModernChair(Chair):
    def sit(self):
        return 'Ти сидиш на сучасному стулі!'


class VictorianChair(Chair):
    def sit(self):
        return 'Ти сидиш на вікторианському стулі!'


class ModernTable(Table):
    def dine(self):
        return 'Ти вечеряєш за сучасним столом'


class VictorianTable(Table):
    def dine(self):
        return 'Ти вечеряєш за вікторианським столом'


class AbstractFactory:
    def create_table(self):
        return Table()

    def create_chair(self):
        return Chair()


class ModernFactory(AbstractFactory):
    def create_table(self):
        return ModernTable()

    def create_chair(self):
        return ModernChair()


class VictorianFactory(AbstractFactory):
    def create_table(self):
        return VictorianTable()

    def create_chair(self):
        return VictorianChair()


def interface(abst_factor: AbstractFactory):
    chair = abst_factor.create_chair()
    table = abst_factor.create_table()

    print(chair.sit())
    print(table.dine())


modern_factory = ModernFactory()
victorian_factory = VictorianFactory()

choice = input('Що бажаєш?\n1-Сучасний стиль\n2-Вікторианський стиль\nВибір: ')

match choice:
    case '1':
        interface(modern_factory)
    case '2':
        interface(victorian_factory)


# 4. Будівельник (Builder)
# Суть патерну: розділяє створення складного об'єкта від його представлення.
# Переносить логіку створення на клас-будівельник


class House:
    def __init__(self):
        self.walls = ''
        self.roof = ''
        self.door = ''

    def show(self):
        return f'Будинок: {self.walls}, {self.roof}, {self.door}.'


class WoodenHouseBuilder:
    def __init__(self):
        self.house = House()

    def _build_roof(self):
        self.house.roof = "Дерев'яна криша"

    def _build_door(self):
        self.house.door = "Дерев'яна дверь"

    def _build_walls(self):
        self.house.walls = "Дерев'яні стіни"

    def build(self):
        self._build_roof()
        self._build_door()
        self._build_walls()

    def get_house(self):
        return self.house


builder = WoodenHouseBuilder()
builder.build()

house = builder.get_house()

print(house.show())

# 5. Прототип (Prototype)
# Суть патерну: можна створювати об'єкти шляхом копіювання вже існуючих
import copy


class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f'{self.name}: {self.age}'

    def birthday(self):
        self.age += 1

    def clone(self):  # ось це фактично і являється патерном
        return copy.deepcopy(self)


bob = Human('Боб', 21)

bob.birthday()
bob.birthday()
bob.birthday()

bob_clone = bob.clone()

bob_clone.birthday()

print(bob)
print(bob_clone)


# ================== Будівельник Піцци (Factory Method, Builder)
class Pizza:  # БАЗОВА ПІЦЦА
    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        return f'Піцца з: {", ".join(self.ingredients)}'


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_dough(self):
        self.pizza.add('тісто')
        return self

    def add_sauce(self):
        self.pizza.add('томатний соус')
        return self

    def add_cheese(self):
        self.pizza.add('сир')
        return self

    def add_topping(self, topping):
        self.pizza.add(topping)
        return self

    def build(self):
        return self.pizza


class PizzaFactory:
    def create_pizza(self):
        raise NotImplementedError()


class MargaritaFactory(PizzaFactory):
    def create_pizza(self):
        return PizzaBuilder().add_dough().add_sauce().add_cheese().build()


class VIPFactory(PizzaFactory):
    def create_pizza(self):
        return PizzaBuilder().add_dough().add_sauce().add_topping('гриби').build()


def order_pizza(factory: PizzaFactory):
    pizza = factory.create_pizza()

    print(pizza.show())


if __name__ == '__main__':
    print('Оберіть піццу:')
    print('1-Маргарита')
    print('2-VIP')
    choice = input('Вибір: ')

    if choice == '1':
        order_pizza(MargaritaFactory())
    elif choice == '2':
        order_pizza(VIPFactory())
    else:
        print('Невірний вибір!')

