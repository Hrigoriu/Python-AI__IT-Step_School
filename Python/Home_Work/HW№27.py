"""
Завдання 2: Менеджер пароля (складніше)
•	Створи клас PasswordManager:
•	Приватне поле  password (режим доступу private)
•	Метод set_password(pwd) — приймає новий пароль, якщо він довший за 6 символів.
•	Метод check_password(pwd) — перевіряє, чи співпадає переданий пароль з поточним. (режим доступу protected)
•	Метод change_password(old, new) — змінює пароль, якщо старий правильний і новий відповідає вимогам.
"""

class PasswordManager:  #Клас для безпечного керування паролем з валідацією та обмеженим доступом.
    def __init__(self): #Метод-конструктор класу.
        self.__password: str | None = None  #Показуємо приватність
        print('Менеджер паролів ініціалізовано. Пароль ще не встановлено.')

    def set_password(self, pwd: str):   # Метод для встановлення (або зміни) пароля.
        if not isinstance(pwd, str):
            print(f'!!!Помилка: Пароль має бути рядком, отримано {type(pwd).__name__}.')
            return
        if len(pwd) > 6:
            self.__password = pwd
            print('✅ Пароль успішно встановлено.')
        else:
            print('!!!❌ Помилка: Пароль має бути довшим за 6 символів.')

    def _check_password(self, pwd_to_check: str) -> bool:   # Метод для перевірки співпадіння паролів.
        if self.__password is None:
            print('!!! Помилка : Пароль ще не встановлено.')
            return False
        if not isinstance(pwd_to_check, str):
            print(f'!!!Помилка : Введений пароль має бути рядком, отримано {type(pwd_to_check).__name__}.')
            return False
        return self.__password == pwd_to_check

    def change_password(self, old_pwd: str, new_pwd: str):  # Метод для зміни пароля.
        print('\n- Спроба зміни пароля -')
        if self._check_password(old_pwd):
            print('Старий пароль правильний. Спроба встановити новий...')
            self.set_password(new_pwd)
        else:
            print('!!!❌ Помилка зміни пароля: Неправильний старий пароль.')

# --- Приклад використання ---
manager = PasswordManager()

print('\n-- Спроби встановити пароль --')
manager.set_password('Cat') # Помилка # Короткий пароль
manager.set_password(1234567890) # Помилка # Некоректний тип
manager.set_password('DonaldTramp2025') # Успіх

print('\n---- Спроби змінити пароль ----')
manager.change_password('QWERTY123456790', 'IlonMask02052025') # Помилка
manager.change_password('DonaldTramp2025', 'Dog') # Помилка
manager.change_password('DonaldTramp2025', 'IlonMask02052025') # Успіх
#=================================================================================

"""
Завдання 3: Система користувачів
•	Створи ієрархію класів:
•	Базовий клас User:
•	Приватні поля: __username, __password.
•	Метод check_password(pwd).
•	Метод get_username().
•	Метод change_password(old, new) — тільки якщо старий пароль правильний і новий > 6 символів.
•	Похідний клас Admin
•	Метод reset_password(user, new_password) — дозволяє змінити пароль іншого користувача (доступ до приватного поля через публічні методи базового класу).
•	Умови: Ніхто не має доступу до __password напряму.
"""
class User: # Клас користувача
    def __init__(self, username: str, password: str):   #Метод для зберігання логіну та пароля.
        self.__username: str = ""
        self.__password: str | None = None
        if not isinstance(username, str) or not username.strip():
             raise ValueError('Логін користувача має бути непустим рядком.')
        self.__username = username.strip()
        print(f'Створення користувача "{self.get_username()}". Встановлення початкового пароля...')
        self.set_password(password)
        if self.__password is None:
             raise ValueError('Помилка, щось пішло не так.')
        print(f'Користувача "{self.get_username()}" успішно створено.')

    def set_password(self, pwd: str):   # Метод для встановлення нового пароля (публічний метод).
        if not isinstance(pwd, str):
            print(f'❌ Помилка встановлення пароля: Пароль має бути рядком, отримано {type(pwd).__name__}.')
            return
        if len(pwd) > 6:
            self.__password = pwd
            print('✅ Пароль успішно встановлено.')
        else:
            print('❌ Помилка встановлення пароля: Пароль має бути довшим за 6 символів.')

    def check_password(self, pwd_to_check: str) -> bool:    # Метод для перевірки співпадіння паролів (публічний метод).
        if self.__password is None:
            print('🤷 Немає пароля для перевірки.')
            return False
        if not isinstance(pwd_to_check, str):
            print(f'Помилка перевірки: Введений пароль має бути рядком, отримано {type(pwd_to_check).__name__}.')
            return False
        return self.__password == pwd_to_check

    def get_username(self) -> str:  # Метод для отримання логіну користувача.
        return self.__username

    def change_password(self, old_pwd: str, new_pwd: str):  # Метод для зміни пароля користувачем.
        print(f'\n--- Користувач "{self.get_username()}" спробував змінити пароль ---')
        if self.check_password(old_pwd):
            print('Старий пароль правильний. Спроба встановити новий...')
            self.set_password(new_pwd)
        else:
            print('❌ Помилка зміни пароля: Неправильний старий пароль.')

    def __str__(self) -> str:
        return f'Користувач: {self.get_username()}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(username="{self.get_username()}", password="***")'


class Admin(User):  # Клас Admin
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
        print(f'Адміністратора "{self.get_username()}" успішно створено.')

    def reset_password(self, user: User, new_password: str):    # Метод для скидання пароля іншого користувача.
        print(f'\n--- Адмін "{self.get_username()}" спробував скинути пароль користувачу "{user.get_username()}" ---')
        if not isinstance(user, User):
            print(f'❌ Помилка скидання пароля: {user} не є користувачем системи.')
            return
        if user is self:
             print('⚠️ Увага: Адмін скидає пароль собі.')
        print(f'Адмін встановлює новий пароль для користувача "{user.get_username()}"...')
        user.set_password(new_password)

    def __str__(self) -> str:
        return f'Адміністратор: {self.get_username()}'

    def __repr__(self) -> str:
         return f'Admin(username="{self.get_username()}", password="***")'


# --- Приклад використання ---
print('--- Створення користувачів ---')
# Створюємо користувачів
try:
    user1 = User('Жан-Люк Пікар', 'USS-Enterprise') # Успіх
    user2 = User('Джеймс Т. Кірк', 'Ship') # Помилка
except ValueError as e:
    print(e)

print('----- Створення адміністраторів -----')
# Створюємо адміністратора
try:
    admin1 = Admin('admin_super', 'SuperAdmin0123456789!') # Валідний пароль для адміна
    admin2 = Admin('admin_light', 'cat') # Невалідний початковий пароль для адміна (викличе ValueError)
except ValueError as e:
     print(e)

# Перестворимо user2 та admin2 з валідними паролями для подальших прикладів
print('\n--- Перестворення користувачів з валідними паролями ---')
user2 = User('Джеймс Т. Кірк', 'Deep-Space')
admin2 = Admin('admin_light', 'TestAdminPwd987')

print('\n--- Демонстрація методів класу User ---')
print(user1.get_username())
print(user2.get_username())

print('\n--- Демонстрація методів класу Admin ---')
print(admin1.get_username())
print(admin2.get_username())

# Зміна пароля користувачем
user1.change_password('WrongOld', 'NewSecurePassword')  # Помилка
user1.change_password('USS-Enterprise', 'short')    # Помилка
user1.change_password('USS-Enterprise', 'Next-Generation!1987')  #Успіх

print('\n--- Демонстрація методу Admin.reset_password ---')
admin1.reset_password(user1, 'Star-Track')
admin1.reset_password(user2, 'short') # Помилка
admin2.reset_password(admin1, 'NewPassword_From_Admin2_ABC!')
admin1.reset_password(admin1, 'NewPassword_Myself_ABC!')
#=======================================================================================================

"""
Завдання 4: Розробіть систему управління замовленнями таксі. 
Кожне замовлення має містити інформацію про клієнта, адресу, тип автомобіля та вартість. 
Реалізуйте методи для додавання нових замовлень, зміни адреси та типу автомобіля, а також видалення замовлення. 
Використайте інкапсуляцію для захисту вартості від неправильних змін. 
*Можете реалізувати інтерфейс для повноцінної взаємодії.
Перелік можливих класів для використання: Клієнт, Замовлення, Авто (Може бути Звичайний, Преміум…), 
*Інтерфейс(може бути функцією).
"""


class Client:   #Клас клієнта таксі.
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


class CarType:  #Клас типу автомобіля та коефіцієнт вартості.
    def __init__(self, name: str, cost_multiplier: float):
        self.name = name
        self.cost_multiplier = cost_multiplier

    def __str__(self) -> str:
        return self.name

CarType.STANDARD = CarType('Стандарт', 1.0)
CarType.PREMIUM = CarType('Преміум', 1.5)
CarType.VAN = CarType('Мінівен', 1.8)


class Order:    #Клас замовлення таксі.
    _next_order_id = 1 # Атрибут класу для генерації унікальних ID

    def __init__(self, client: Client, pickup_address: str, destination_address: str, car_type: CarType, base_rate: float):
        self.order_id = Order._next_order_id
        Order._next_order_id += 1

        self.client = client
        self.pickup_address = pickup_address
        self.destination_address = destination_address
        self.car_type = car_type
        self.status = 'Створено'
        self.__cost = 0.0   #Вартість
        self._calculate_cost(base_rate)

    def __str__(self) -> str:
        return (f'Замовлення #{self.order_id} ({self.status}): Клієнт: {self.client}, '
                f'Звідки: {self.pickup_address}, Куди: {self.destination_address}, '
                f'Авто: {self.car_type}, Вартість: {self.get_cost():.2f} грн')

    def _calculate_cost(self, base_rate: float):    # Метод для розрахунку вартості.
        try:
             distance_factor = (len(self.pickup_address) + len(self.destination_address)) / 10.0
             if distance_factor < 1: distance_factor = 1
             calculated_cost = base_rate * self.car_type.cost_multiplier * distance_factor
             self.__cost = round(calculated_cost, 2)
             print(f'(Вартість для #{self.order_id} розраховано: {self.__cost:.2f})')

        except Exception as e:
             print(f'Помилка при розрахунку вартості для замовлення #{self.order_id}: {e}')
             self.__cost = 0.0

    def get_cost(self) -> float:    # Метод для отримання вартості
        return self.__cost

    def set_address(self, new_pickup: str | None = None, new_destination: str | None = None):
        # Метод змінює адресу посадки або призначення.
        changed = False
        if new_pickup is not None and isinstance(new_pickup, str) and new_pickup.strip():
            self.pickup_address = new_pickup.strip()
            changed = True
            print(f'Адресу посадки для #{self.order_id} змінено на "{self.pickup_address}".')
        if new_destination is not None and isinstance(new_destination, str) and new_destination.strip():
            self.destination_address = new_destination.strip()
            changed = True
            print(f'Адресу призначення для #{self.order_id} змінено на "{self.destination_address}".')
        if not changed:
             print(f'Некоректні дані для зміни адреси замовлення #{self.order_id}.')

    def set_car_type(self, new_car_type: CarType, base_rate: float):
        # Метод для зміни типу автомобіля та перерахунку вартості.
        if not isinstance(new_car_type, CarType):
            print(f'Помилка: Некоректний тип автомобіля для замовлення #{self.order_id}.')
            return

        self.car_type = new_car_type
        print(f'Тип авто для #{self.order_id} змінено на {self.car_type}.')
        self._calculate_cost(base_rate)
        print(f'Нова вартість замовлення #{self.order_id}: {self.get_cost():.2f} грн')


class OrderManager: # Клас Менеджера замовлень
    def __init__(self, base_rate: float):
        self.orders: dict[int, Order] = {}
        self._base_rate = float(base_rate)

    def add_order(self, client: Client, pickup_address: str, destination_address: str, car_type: CarType):
        # Метод створює та додає нове замовлення та повертає створене замовлення.
        order = Order(client, pickup_address, destination_address, car_type, self._base_rate)
        self.orders[order.order_id] = order
        print(f'✔️ Додано нове замовлення #{order.order_id}.')
        return order

    def find_order(self, order_id: int) -> Order | None:    # Метод шукає замовлення за ID.
        if not isinstance(order_id, int) or order_id <= 0:
             print('❌ Некоректний ID замовлення для пошуку.')
             return None
        return self.orders.get(order_id)

    def change_order(self, order_id: int, new_pickup: str | None = None, new_destination: str | None = None, new_car_type: CarType | None = None):
        # Метод змінює дані існуючого замовлення (адресу або тип авто).
        order = self.find_order(order_id)
        if order:
            print(f'\n--- Зміна замовлення #{order_id} ---')
            if new_pickup is not None or new_destination is not None:
                order.set_address(new_pickup, new_destination)
            if new_car_type is not None:
                order.set_car_type(new_car_type, self._base_rate)
            if new_pickup is None and new_destination is None and new_car_type is None:
                print('Не вказано параметри для зміни замовлення.')
        else:
            print(f'❌ Замовлення з ID {order_id} не знайдено.')

    def delete_order(self, order_id: int):  # Метод видаляє замовлення за ID.
        if order_id in self.orders:
            deleted_order = self.orders.pop(order_id)
            print(f'🗑️ Замовлення #{order_id} видалено.')
        else:
            print(f'❌ Замовлення з ID {order_id} не знайдено. Видалення неможливе.')

    def display_all_orders(self):   # Метод який виводить інформацію про всі замовлення.
        print('\n--- Список замовлень ---')
        if not self.orders:
            print('Замовлень немає.')
            return
        for order in self.orders.values():
            print(order)
        print("\n----------------------")

    def get_order_cost(self, order_id: int) -> float | None:    # Метод менеджера для отримання вартості замовлення за ID.
        order = self.find_order(order_id)
        if order:
            return order.get_cost()
        else:
            print(f'❌ Замовлення з ID {order_id} не знайдено для отримання вартості.')
            return None

# --- Приклад використання
print('--- Почнемо)) ---')
taxi_system = OrderManager(base_rate=50.0)

client1 = Client('Дональд Трамп')
client2 = Client('Ілон Маск')

print('\n--- Додавання замовлень ---')
order1 = taxi_system.add_order(client1, 'Вул. Свободи, 10', 'Пр. Перемоги, 5', CarType.STANDARD)
order2 = taxi_system.add_order(client2, 'Майдан Незалежності', 'Вул. Хрещатик, 25', CarType.PREMIUM)
order3 = taxi_system.add_order(client1, 'Залізничний вокзал', 'Аеропорт Бориспіль', CarType.VAN)
taxi_system.display_all_orders()

print('\n--- Доступ до вартості (через менеджер або об\'єкт замовлення) ---')
print(f'Вартість Замовлення #{order1.order_id} (з об\'єкта): {order1.get_cost():.2f} грн')
print(f'Вартість Замовлення #{order2.order_id} (з менеджера): {taxi_system.get_order_cost(order2.order_id):.2f} грн')

print('\n--- Зміна замовлення ---')
taxi_system.change_order(order1.order_id, new_destination='Вул. Шевченка, 1')
taxi_system.change_order(order2.order_id, new_car_type=CarType.VAN)
taxi_system.change_order(99, new_pickup='Бажана, 7')
taxi_system.display_all_orders()

print('\n--- Видалення замовлення ---')
taxi_system.delete_order(order3.order_id)
taxi_system.delete_order(99)
taxi_system.display_all_orders()