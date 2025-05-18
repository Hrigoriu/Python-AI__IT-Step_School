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

#=====================================================================================================

class Motorcycle(Vehicle):
    def __init__(self, name: str, model: str, rental_price_per_day: int, top_speed: int):
        super().__init__(name, model, rental_price_per_day)
        self.top_speed = top_speed

    def display_info(self):
        print(f"- Мотоцикл: {self.name} {self.model}, Макс. швидкість: {self.top_speed} км/год, Ціна/день: {self.rental_price_per_day} грн, Статус: {'Орендовано' if self.is_rented else 'Доступний'}")


class Car(Vehicle):
    def __init__(self, name: str, model: str, rental_price_per_day: int, num_doors: int):
        super().__init__(name, model, rental_price_per_day)
        self.num_doors = num_doors

    def display_info(self):
        print(f"- Автомобіль: {self.name} {self.model}, Дверей: {self.num_doors}, Ціна/день: {self.rental_price_per_day} грн, Статус: {'Орендовано' if self.is_rented else 'Доступний'}")


class Truck(Vehicle):
    def __init__(self, name: str, model: str, rental_price_per_day: int, capacity: int):
        super().__init__(name, model, rental_price_per_day)
        self.capacity = capacity

    def display_info(self):
        print(f"- Вантажівка: {self.name} {self.model}, Вантажопідйомність: {self.capacity} кг, Ціна/день: {self.rental_price_per_day} грн, Статус: {'Орендовано' if self.is_rented else 'Доступний'}")

#===============================================================================================================
class RentalService:
    def __init__(self):
        self._vehicles: list[Vehicle] = [
            Motorcycle('Yamaha', 'MT-07', 500, 200),
            Car('Toyota', 'Camry', 800,  4),
            Truck('Ford', 'F-150', 1200,  3500)
        ]
        print('-----------------------------------')
    def _find_vehicle(self, vehicle_type: str) -> Vehicle | None:
        target_class_name = vehicle_type.lower()
        for vehicle in self._vehicles:
            if vehicle.__class__.__name__.lower() == target_class_name:
                return vehicle
        return None

    def display_available_vehicles(self):
        print('\n--- Доступні транспортні засоби ---')
        available_found = False
        for vehicle in self._vehicles:
            if not vehicle.is_rented:
                vehicle.display_info()
                available_found = True
        if not available_found:
             print('Наразі немає доступних транспортних засобів для оренди.')
        print('-----------------------------------')

    def rent_vehicle(self, vehicle_type: str, num_days: int):
        print(f'\n--- Спроба орендувати "{vehicle_type}" на {num_days} днів ---')
        vehicle = self._find_vehicle(vehicle_type)

        if not vehicle.is_rented:
            vehicle.is_rented = True
            total_cost = vehicle.calculate_rental_cost(num_days)
            print(f' Успіх: {vehicle.name} {vehicle.model} орендовано. Вартість: {total_cost} грн.')
        else:
            print(f' Помилка: {vehicle.name} {vehicle.model} вже орендовано.')
        print('-----------------------------------')

    def return_vehicle(self, vehicle_type: str):
        print(f'\n--- Спроба повернути "{vehicle_type}" ---')
        vehicle = self._find_vehicle(vehicle_type)

        if vehicle.is_rented:
            vehicle.is_rented = False
            print(f' Успіх: {vehicle.name} {vehicle.model} повернено.')
        else:
            print(f' Помилка: {vehicle.name} {vehicle.model} не був орендований.')
        print('-----------------------------------')

    def display_all_vehicles(self):
        print('\n--- Весь автопарк ---')
        if not self._vehicles:
            print('Автопарк порожній.')
            return
        for vehicle in self._vehicles:
            print(vehicle)
        print('-----------------------------------')


rental_service = RentalService()
rental_service.display_available_vehicles()

rental_service.rent_vehicle('Motorcycle', 1)
rental_service.rent_vehicle('Car', 3)
rental_service.rent_vehicle('Car', 2)
rental_service.rent_vehicle('Truck', 5)
rental_service.display_available_vehicles()

rental_service.return_vehicle('Motorcycle')
rental_service.return_vehicle('Car')
rental_service.return_vehicle('Truck')
rental_service.display_available_vehicles()

print('\n--- Весь автопарк після оренди та повернення ---')
rental_service.display_all_vehicles()