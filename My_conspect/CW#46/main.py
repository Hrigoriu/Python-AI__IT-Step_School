from db import Database
from auth import AuthManager
from workers import WorkerManager

def main():
    db = Database()
    db.init_db()
    db.close()

    auth = AuthManager()
    workers = WorkerManager()

    print('1 - Увійти\n2 - Зареєструватись\n3 - Змінити пароль')
    choice = input('Оберіть опцію: ')

    if choice == '1':
        login = input('Логін: ')
        password = input('Пароль: ')
        if auth.login_user(login, password):
            print('Успішний вхід!')
            while True:
                print('\nМеню:')
                print('1 - Переглянути всіх працівників')
                print('2 - Додати працівника')
                print('3 - Видалити працівника')
                print('4 - Знайти працівника за ім\'ям')
                print('5 - Сортувати працівників за зарплатою')
                print('6 - Змінити посаду працівника')
                print('7 - Вийти')

                action = input('Оберіть дію: ')

                if action == '1':
                    for row in workers.get_all_workers():
                        print(row)
                elif action == '2':
                    name = input('Ім\'я: ')
                    age = int(input('Вік: '))
                    salary = float(input('Зарплата: '))
                    position = input('Посада: ')
                    workers.add_worker(name, age, salary, position)
                elif action == '3':
                    worker_id = int(input('ID працівника: '))
                    workers.delete_worker(worker_id)
                elif action == '4':
                    name = input('Введіть ім\'я для пошуку: ')
                    results = workers.find_worker_by_name(name)
                    for row in results:
                        print(row)
                elif action == '5':
                    order = input('Сортувати за спаданням зарплати? (так/ні): ').strip().lower()
                    descending = (order == 'так')
                    for row in workers.get_workers_sorted_by_salary(descending):
                        print(row)
                elif action == '6':
                    worker_id = int(input('ID працівника: '))
                    new_position = input('Нова посада: ')
                    workers.update_worker_position(worker_id, new_position)
                    print('Посаду оновлено.')
                elif action == '7':
                    break
                else:
                    print('Невірна дія.')
        else:
            print('Невірний логін або пароль.')

    elif choice == '2':
        login = input('Новий логін: ')
        password = input('Пароль: ')
        code = input('Код відновлення (будь-яке слово): ')
        auth.register_user(login, password, code)

    elif choice == '3':
        login = input('Логін: ')
        code = input('Код відновлення: ')
        new_password = input('Новий пароль: ')
        auth.reset_password(login, code, new_password)

    auth.close()
    workers.close()

if __name__ == '__main__':
    main()
