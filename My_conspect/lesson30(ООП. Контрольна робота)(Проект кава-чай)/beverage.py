from abc import ABC, abstractmethod

class Beverage(ABC):    #Абстрактний клас для напою
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod  #Абстрактний метод ОБОВ'ЯЗКОВО треба назначити в дочірніх класах
    def get_description(self) -> str:
        pass


class Coffee(Beverage):  # Кава (наслідує Напой)
    def __init__(self, size: str):
        price = {'small': 2.5, 'medium': 3.0, 'large': 3.5}.get(size, 3.0)
        name = f'{size.capitalize()} Coffee'
        super().__init__(name, price)

    def get_description(self) -> str:
        return f'{self.name}: {self.price} $'


class Tea(Beverage):  # Чай (наслідує Напой)
    def __int__(self, flavor: str):
        price = 2.5
        name = f'{flavor.capitalize()} Tea'
        super().__init__(name, price)

    def get_description(self) -> str:
        return f'{self.name}: {self.price} $'
