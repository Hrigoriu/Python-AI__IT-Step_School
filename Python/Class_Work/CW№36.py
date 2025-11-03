#Завдання№1
from abc import ABC, abstractmethod
"""
Завдання А: Паттерн "Адаптер"
Опис: У вас є система для роботи з різними платіжними методами 
(наприклад, PayPal та кредитні картки). 
Реалізуйте адаптер для інтеграції існуючого API платіжної системи з новим інтерфейсом.

Завдання В:
Створіть інтерфейс Payment, який міститиме метод pay(amount).
Реалізуйте класи PayPal та CreditCard з власними методами для обробки платежів.
Створіть адаптери для цих класів, щоб вони відповідали інтерфейсу Payment.
"""
# 1.
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# 2.
class PayPal:
    def __init__(self, email: str):
        self._email = email
        print(f'PayPal: створено для {self._email}')

    def submit_payment(self, total_amount: float):
        print(f'PayPal: Надсилання платежу на суму {total_amount:.2f} грн для користувача {self._email}.')
        print(f'PayPal: Платіж успішно оброблено.')

class CreditCard:
    def __init__(self, card_number: str, expiry_date: str):
        self._card_number_last_digits = card_number[-4:]
        self._expiry_date = expiry_date
        print(f'CreditCard: створено для карти ************{self._card_number_last_digits}')

    def process_transaction(self, amount_in_uah: float):
        print(f'CreditCard: Обробка транзакції на суму {amount_in_uah:.2f} грн для карти ************{self._card_number_last_digits}.')
        print(f'CreditCard: Транзакцію успішно виконано.')

# 3.
class PayPalAdapter(Payment):
    def __init__(self, paypal_adaptee: PayPal):
        self._paypal_adaptee = paypal_adaptee

    def pay(self, amount: float) -> None:
        print(f'PayPalAdapter: Виклик методу "pay" з сумою {amount:.2f} грн.')
        self._paypal_adaptee.submit_payment(total_amount=amount)

class CreditCardAdapter(Payment):
    def __init__(self, credit_card_adaptee: CreditCard):
        self._credit_card_adaptee = credit_card_adaptee

    def pay(self, amount: float) -> None:
        print(f'CreditCardAdapter: Виклик методу "pay" з сумою {amount:.2f} грн.')
        self._credit_card_adaptee.process_transaction(amount_in_uah=amount)

if __name__ == "__main__":
    paypal_account = PayPal(email='ilonn.mask@gmail.com')
    my_credit_card = CreditCard(card_number='7234-5678-9012-3456', expiry_date='12/27')

    print('\n' + '='*10 + ' Використання PayPal через адаптер ' + '='*10)
    paypal_payment_processor: Payment = PayPalAdapter(paypal_account)
    paypal_payment_processor.pay(150.75)

    print('\n' + '='*10 + ' Використання CreditCard через адаптер ' + '='*10)
    cc_payment_processor: Payment = CreditCardAdapter(my_credit_card)
    cc_payment_processor.pay(320.50)

    print('\n' + '='*10 + ' Демонстрація з функцією, що приймає Payment ' + '='*10)
    def execute_payment_process(payment_system: Payment, amount_to_pay: float):
        print(f'\nЗапуск процесу оплати на суму: {amount_to_pay:.2f} грн')
        payment_system.pay(amount_to_pay)
        print('Процес оплати завершено.')

    execute_payment_process(paypal_payment_processor, 55.00)
    execute_payment_process(cc_payment_processor, 99.99)

# --- Інтерактивна панель ---
    print('\n' + '='*10 + ' Інтерактивна панель вибору платіжної системи ' + '='*10)

    user_paypal = PayPal(email="bill.tramp@gmail.com")
    user_card = CreditCard(card_number='9876-5432-1098-7654', expiry_date='01/28')

    paypal_adapter_instance: Payment = PayPalAdapter(user_paypal)
    card_adapter_instance: Payment = CreditCardAdapter(user_card)


    while True:
        print('\nОберіть платіжну систему:')
        print('1 - PayPal')
        print('2 - Кредитна картка')
        print('0 - Вихід')

        choice = input('Ваш вибір: ')
        payment_system_to_use: Payment = None

        if choice == '1':
            payment_system_to_use = paypal_adapter_instance
            print('--- Обрано PayPal ---')
        elif choice == '2':
            payment_system_to_use = card_adapter_instance
            print('--- Обрано Кредитну картку ---')
        elif choice == '0':
            print('Дякуємо що ви з нами!')
            break
        else:
            print('Невірний вибір. Будь ласка, спробуйте ще раз.')
            continue

        if payment_system_to_use:
            try:
                amount_str = input('Введіть суму для оплати: ')
                amount_val = float(amount_str)
                if amount_val <= 0:
                    print('Сума повинна бути позитивною.')
                    continue
                execute_payment_process(payment_system_to_use, amount_val)
            except ValueError:
                print('Невірно введена сума. Будь ласка, введіть число.')
#--------------------------------------------------------------------------------------

#Завдання№2
"""
Уявіть, що при вході на сайт потрібно виконати кілька перевірок:
логін/пароль (клас, що зберігає логіни та паролі);
чи заблоковано користувача (клас що відповідно блокує);
чи включена двофакторна авторизація (клас, в якому зберігається унікальний код кожного користувача).
Кожна перевірка — це окрема система.
Користувач не повинен взаємодіяти з ними окремо — зроби фасад LoginFacade, який керує цим.
У фасаді повинен бути просто метод login та метод registation
"""

class LoginSystem:
    def __init__(self):
        self.users = {}  # login: password

    def add_user(self, login, password):
        self.users[login] = password

    def check_user(self, login, password):
        if login not in self.users:
            return False
        if self.users[login] != password:
            return False
        return True


class BlockSystem:
    def __init__(self):
        self.black_list = ['qwerty', 'admin']

    def check(self, login):
        if login in self.black_list:
            return True
        return False


class TwoFactorAuth:
    def __init__(self):
        self.users = {}

    def add_auth(self, login, code):
        self.users[login] = code

    def check_login(self, login):
        if login not in self.users:
            return False
        return True

    def check_code(self, login, code):
        if self.users[login] != code:
            return False
        return True


class LoginFacade:
    def __init__(self):
        self.login_system = LoginSystem()
        self.block_system = BlockSystem()
        self.two_factor = TwoFactorAuth()  # можна без цього (якщо складно)

    def login(self, login, password, auth_code=''):
        if self.block_system.check(login):
            print('Ви є у чорному списку!')
            return

        if not self.login_system.check_user(login, password):
            print('Невірний логін або пароль!')
            return

        if self.two_factor.check_login(login) and not self.two_factor.check_code(login, auth_code):
            print('Ви завалили двохфакторну аутентифікацію!')
            return
        print(f'Вітаю у програмі, {login}!')

    def registration(self, login, password, auth_code=''):
        if self.block_system.check(login):
            print('Ви є у чорному списку!')
            return
        self.login_system.add_user(login, password)
        if auth_code:
            self.two_factor.add_auth(login, password)
