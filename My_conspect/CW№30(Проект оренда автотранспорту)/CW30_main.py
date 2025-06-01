from CW30_rental_service import RentalService

def main():
    print('=== Ласкаво просимо до Системи Оренди Транспорту! ===')

    rental_service = RentalService()
    rental_service.display_available_vehicles()

    while True:
        print('\n Оберіть дію:')
        print('1. Показати доступні ТЗ')
        print('2. Орендувати ТЗ')
        print('3. Повернути ТЗ')
        print('4. Показати весь автопарк')
        print('5. Вийти')

        choice = input('Ваш вибір: ')
        match choice:
            case '1':
                rental_service.display_available_vehicles()

            case '2':
                vehicle_type = input('Введіть тип ТЗ для оренди (Motorcycle, Car, Truck): ')
                try:
                    num_days_str = input('Введіть кількість днів оренди (ціле число): ')
                    num_days = int(num_days_str)
                    rental_service.rent_vehicle(vehicle_type, num_days)
                except ValueError:
                    print('❌ Некоректне введення кількості днів. Будь ласка, введіть ціле число.')
                except Exception as e:
                    print(f'❌ Сталася помилка під час оренди: {e}')

            case '3':
                vehicle_type = input('Введіть тип ТЗ для повернення (Motorcycle, Car, Truck): ')
                try:
                    rental_service.return_vehicle(vehicle_type)
                except Exception as e:
                     print(f'❌ Сталася помилка під час повернення: {e}')

            case '4':
                rental_service.display_all_vehicles()

            case '5':
                print('Дякуємо! До побачення.')
                break
            case _:
                print('Невірний вибір. Будь ласка, спробуйте ще раз.')

if __name__ == '__main__':
    main()


"""
Розробіть програму для управління системою оренди автомобілів, 
використовуючи основні принципи об’єктно-орієнтованого програмування: 
інкапсуляцію, успадкування, поліморфізм та абстракцію. 
Вимоги:
1.	Наявність абстрактного класу Vehicle, та його класів нащадків 
    (конкретні класи автомобілів для оренди).
2.	Наявність класу Service, що керує орендою.
3.	Приватні атрибути та методи, що обмежені в доступі.
4.	Виконання принципу поліморфізму для автомобілів.
"""
