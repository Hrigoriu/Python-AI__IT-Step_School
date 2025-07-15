from order_manager import OrderManager
from customer_manager import CustomerManager
from db import DB


def main():
    db = DB()

    customers = CustomerManager(db)
    orders = OrderManager(db)

    try:
        while True:
            print('--------Menu--------')
            print('1. Список клієнтів')
            print('2. Знайти клієнта по id')
            print('3. Замовлення клієнта')
            print('4. Вихід')

            choice = input('Оберіть опцію: ')

            match choice:
                case '1':
                    for customer_id, name, country in customers.list_customers():
                        print(f'{customer_id} | {name} | {country}')
                case '2':
                    customer_id = input('Введіть id клієнта: ')
                    customer = customers.get_customer_by_id(customer_id)

                    print(customer if customer else 'Клієнта не знайдено!')
                case '3':
                    customer_id = input('Введіть id клієнта: ')
                    result = orders.get_orders_by_customer(customer_id)

                    for row in result:
                        print(row)
                case '4':
                    break
                case _:
                    print('Невідома опція!')
    finally:
        db.close()


if __name__ == '__main__':
    main()
