
"""
Тема: Структури даних. Частина 1
Завдання
Користувач вводить з клавіатури набір чисел.
Отримані числа необхідно зберегти до списку
(тип списку оберіть в залежності від поставленого нижче завдання).
Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
1. Додати нове число до списку
(якщо таке число існує у списку, потрібно вивести повідомлення про це
користувачеві без додавання числа).
2. Видалити усі входження числа зі списку
(користувач вводить з клавіатури число для видалення)
3. Показати вміст списку
(залежно від вибору користувача, покажіть список з початку або з кінця)
4. Перевірити, чи є значення у списку
5. Замінити значення у списку
(користувач визначає, чи замінити тільки перше входження, чи всі)
Дія виконується залежно від вибору користувача,
після чого меню з’являється знову.
"""

def get_initial_numbers():
    while True:
        try:
            raw_input = input('Введіть набір чисел через пробіл: ')
            numbers = [int(x) for x in raw_input.split()]
            return numbers
        except ValueError:
            print('Помилка: Введені дані містять не числа. Спробуйте ще раз.')
        except Exception as e:
            print(f'Неочікувана помилка: {e}. Спробуйте ще раз.')

def get_integer_input(prompt_message):
    while True:
        try:
            num = int(input(prompt_message))
            return num
        except ValueError:
            print('Помилка: Будь ласка, введіть ціле число.')

def display_menu():
    print('\nМеню:')
    print('1. Додати нове число до списку')
    print('2. Видалити усі входження числа зі списку')
    print('3. Показати вміст списку')
    print('4. Перевірити, чи є значення у списку')
    print('5. Замінити значення у списку')
    print('0. Вийти')


def main():
    print('--- Структури даних. Частина 1 ---')
    data_list = get_initial_numbers()
    print(f'Початковий список: {data_list}')

    while True:
        display_menu()
        choice = input('Ваш вибір: ')

        if choice == '1':
            num_to_add = get_integer_input('Введіть число для додавання: ')
            if num_to_add in data_list:
                print(f'Число {num_to_add} вже існує у списку. Додавання не виконано.')
            else:
                data_list.append(num_to_add)
                print(f'Число {num_to_add} додано до списку.')

        elif choice == '2':
            if not data_list:
                print('Список порожній. Немає чого видаляти.')
                continue
            num_to_remove = get_integer_input('Введіть число для видалення: ')
            if num_to_remove not in data_list:
                print(f'Числа {num_to_remove} немає у списку.')
            else:
                initial_len = len(data_list)
                data_list = [x for x in data_list if x != num_to_remove]
                # Альтернативний спосіб
                # while num_to_remove in data_list:
                #     data_list.remove(num_to_remove)
                if len(data_list) < initial_len:
                    print(f'Усі входження числа {num_to_remove} видалено зі списку.')
                else:
                    print(f'Щось пішло не так при видаленні {num_to_remove}.')

        elif choice == '3':
            if not data_list:
                print('Список порожній.')
                continue
            while True:
                direction = input('Показати список з початку (напиши "п") чи з кінця (напиши "к")? : ').lower()
                if direction == 'п':
                    print(f'Вміст списку: {data_list}')
                    break
                elif direction == 'к':
                    print(f'Вміст списку (з кінця): {data_list[::-1]}')  # або list(reversed(data_list))
                    break
                else:
                    print('Щось пішло не так. Введіть "п" або "к".')

        elif choice == '4':
            if not data_list:
                print('Список порожній.')
                continue
            value_to_check = get_integer_input('Введіть значення для перевірки: ')
            if value_to_check in data_list:
                print(f'Значення {value_to_check} присутнє у списку.')
            else:
                print(f'Значення {value_to_check} відсутнє у списку.')

        elif choice == '5':
            if not data_list:
                print('Список порожній. Немає чого замінювати.')
                continue
            old_value = get_integer_input('Введіть значення, яке потрібно замінити: ')
            if old_value not in data_list:
                print(f'Значення {old_value} не знайдено у списку.')
                continue
            new_value = get_integer_input('Введіть нове значення: ')

            while True:
                replace_choice = input('Замінити перше входження (напиши "п") чи усі (напиши "у")? : ').lower()
                if replace_choice == 'п':
                    try:
                        index = data_list.index(old_value)
                        data_list[index] = new_value
                        print(f'Перше входження {old_value} замінено на {new_value}.')
                    except ValueError:
                        print(f'Значення {old_value} не знайдено для заміни.')
                    break
                elif replace_choice == 'у':
                    replaced_count = 0
                    for i in range(len(data_list)):
                        if data_list[i] == old_value:
                            data_list[i] = new_value
                            replaced_count += 1
                    if replaced_count > 0:
                        print(f'Усі {replaced_count} входження {old_value} замінено на {new_value}.')
                    break
                else:
                    print('Щось пішло не так. Введіть "п" або "у".')

        elif choice == '0':
            print('Дякуємо що були з нами! До побачення.')
            break
        else:
            print('Невірний вибір. Будь ласка, введіть число від 0 до 5.')

        if choice in ['1', '2', '5'] and data_list:
            print(f'Оновлений список: {data_list}')
        elif choice in ['1', '2', '5'] and not data_list:
            print('Список тепер порожній.')


if __name__ == "__main__":
    main()