from CW30_Vehicle import Vehicle, Motorcycle, Car, Truck

class RentalService:
    def __init__(self):
        self._vehicles: list[Vehicle] = [
            Motorcycle('Yamaha', 'MT-07', 500, 200),
            Car('Toyota', 'Camry', 800, 4),
            Truck('Ford', 'F-150', 1200, 3500)
        ]
        print('Сервіс оренди ініціалізовано з автопарком.')
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

        if vehicle and not vehicle.is_rented:
            vehicle.is_rented = True
            total_cost = vehicle.calculate_rental_cost(num_days)
            print(f'✅ Успіх: {vehicle.name} {vehicle.model} орендовано. Вартість: {total_cost} грн.')
        elif vehicle and vehicle.is_rented:
            print(f'❌ Помилка: {vehicle.name} {vehicle.model} вже орендовано.')
        else:
             print(f'❌ Помилка: Тип транспортного засобу "{vehicle_type}" не знайдено в автопарку.')
        print('-----------------------------------')

    def return_vehicle(self, vehicle_type: str):
        print(f'\n--- Спроба повернути "{vehicle_type}" ---')
        vehicle = self._find_vehicle(vehicle_type)

        if vehicle and vehicle.is_rented:
            vehicle.is_rented = False
            print(f'✅ Успіх: {vehicle.name} {vehicle.model} повернено.')
        elif vehicle and not vehicle.is_rented:
            print(f'❌ Помилка: {vehicle.name} {vehicle.model} не був орендований.')
        else:
             print(f'❌ Помилка: Тип транспортного засобу "{vehicle_type}" не знайдено в автопарку.')
        print('-----------------------------------')

    def display_all_vehicles(self):
        print('\n--- Весь автопарк ---')
        if not self._vehicles:
            print('Автопарк порожній.')
            return
        for vehicle in self._vehicles:
            print(vehicle)
        print('-----------------------------------')
