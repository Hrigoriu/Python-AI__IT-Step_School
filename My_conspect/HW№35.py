from abc import ABC, abstractmethod

#1.
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

#2.
class Car(Vehicle):
    def move(self):
        return "Автомобіль їде по дорозі."

class Motorcycle(Vehicle):
    def move(self):
        return "Мотоцикл мчить по шосе."

class Bicycle(Vehicle):
    def move(self):
        return "Велосипед їде по велодоріжці."

#3.
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

#4.
class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Car:
        return Car()

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self) -> Motorcycle:
        return Motorcycle()

class BicycleFactory(VehicleFactory):
    def create_vehicle(self) -> Bicycle:
        return Bicycle()

#5.
class Client:
    def __init__(self, factory: VehicleFactory):
        self._factory = factory

    def use_vehicle(self):
        vehicle = self._factory.create_vehicle()
        print(f'Клієнт: Да почнеться дійство!!!.')
        print(f'Клієнт: Цей: {vehicle.move()}')


#6.
if __name__ == "__main__":

    while True:
        print('\nОберіть тип транспортного засобу для створення:')
        print('1 - Автомобіль')
        print('2 - Мотоцикл')
        print('3 - Велосипед')
        print('0 - Вихід')

        choice = input('Ваш вибір: ')

        factory = None

        if choice == '1':
            factory = CarFactory()
            print('\n--- Створюємо Автомобіль ---')
        elif choice == '2':
            factory = MotorcycleFactory()
            print('\n--- Створюємо Мотоцикл ---')
        elif choice == '3':
            factory = BicycleFactory()
            print('\n--- Створюємо Велосипед ---')
        elif choice == '0':
            print('Дякуємо що скористалися нашими послугами!')
            break
        else:
            print('Невірний вибір. Будь ласка, спробуйте ще раз.')
            continue

        if factory:
            client_instance = Client(factory)
            client_instance.use_vehicle()

            vehicle = factory.create_vehicle()
            print(f'Створено: {vehicle.__class__.__name__}')
            print(f'Дія: {vehicle.move()}')

#6.
""" 
if __name__ == "__main__":
    print('Демонстрація з CarFactory:')
    car_client = Client(CarFactory())
    car_client.use_vehicle()
    print("-" * 30)

    print('Демонстрація з MotorcycleFactory:')
    motorcycle_client = Client(MotorcycleFactory())
    motorcycle_client.use_vehicle()
    print("-" * 30)

    print('Демонстрація з BicycleFactory:')
    bicycle_client = Client(BicycleFactory())
    bicycle_client.use_vehicle()
    print("-" * 30)

    def operate_vehicle_with_factory(factory: VehicleFactory):
        print(f'Робота з {factory.__class__.__name__}:')
        vehicle = factory.create_vehicle()
        print(f'  Тип транспортного засобу: {vehicle.__class__.__name__}')
        print(f'  Дія: {vehicle.move()}')

    print('Типи транспортних засобів та їх дії у різних фабриках:')
    operate_vehicle_with_factory(CarFactory())
    operate_vehicle_with_factory(MotorcycleFactory())
    operate_vehicle_with_factory(BicycleFactory())
"""