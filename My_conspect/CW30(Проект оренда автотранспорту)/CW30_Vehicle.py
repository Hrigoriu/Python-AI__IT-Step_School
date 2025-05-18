from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name: str, model: str, rental_price_per_day: int):
        self.name = name
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_rented: bool = False

    @abstractmethod
    def display_info(self):
        pass

    def calculate_rental_cost(self, num_days: int) -> int:
        return self.rental_price_per_day * num_days

    def __str__(self) -> str:
        status = 'Орендовано' if self.is_rented else 'Доступний'
        return f'{self.name} {self.model}, Ціна/день: {self.rental_price_per_day} грн, Статус: {status}'


class Motorcycle(Vehicle):
    def __init__(self, name: str, model: str, rental_price_per_day: int, top_speed: int):
        super().__init__(name, model, rental_price_per_day)
        self.top_speed = top_speed

    def display_info(self):
        print(f'- Мотоцикл: {self.name} {self.model}, Макс. швидкість: {self.top_speed} км/год, Ціна/день: {self.rental_price_per_day} грн, Статус: {"Орендовано" if self.is_rented else "Доступний"}')


class Car(Vehicle):
    def __init__(self, name: str, model: str, rental_price_per_day: int, num_doors: int):
        super().__init__(name, model, rental_price_per_day)
        self.num_doors = num_doors

    def display_info(self):
        print(f'- Автомобіль: {self.name} {self.model}, Дверей: {self.num_doors}, Ціна/день: {self.rental_price_per_day} грн, Статус: {"Орендовано" if self.is_rented else "Доступний"}')


class Truck(Vehicle):
    def __init__(self, name: str, model: str, rental_price_per_day: int, capacity: int):
        super().__init__(name, model, rental_price_per_day)
        self.capacity = capacity

    def display_info(self):
        print(f'- Вантажівка: {self.name} {self.model}, Вантажопідйомність: {self.capacity} кг, Ціна/день: {self.rental_price_per_day} грн, Статус: {"Орендовано" if self.is_rented else "Доступний"}')
