
# day = int(input('Введіть номер дня тижня(1-7): '))

# if day == 1:
#     print('Понеділок')
# elif day == 2:
#     print('Вівторок')
# elif day == 3:
#     print("Середа")
# elif day == 4:
#     print('Четвер')
# elif day == 5:
#     print("П'ятниця")
# elif day == 6:
#     print('Субота')
# elif day == 7:
#     print("Неділя")
# else:
#     print('Такого дня тижня не існує!')
#
# day = int(input('Введіть номер дня тижня(1-7): '))
#
# match day:
#     case 1:
#         print('Понеділок')
#     case 2:
#         print('Вівторок')
#     case 3:
#         print('Середа')
#     case 4:
#         print('Четвер')
#     case 5:
#         print("П'ятниця")
#     case 6:
#         print('Субота')
#     case 7:
#         print('Неділя')
#     case _:  # аналог else
#         print('Такого дня тижня не існує')


# login = input('Введіть логін: ')
# password = input('Введіть пароль: ')
#
# match login:
#     case 'admin' if password == 'qwerty123':  # login == 'admin' and password == 'qwerty123'
#         print('WELCOME')
#     case _:
#         print('Доступ заборонено!')


'''
Користувач вводить номер місяця (1-12)
Поверніть відповідну пору року (Зима, Літо, Осінь, Весна)
Виконайте завдання через match case
'''

month = int(input('Введіть номер місяця: '))

match month:
    case 12 | 1 | 2:  # | - or
        print('Зима')
    case 3 | 4 | 5:
        print('Весна')
    case 6 | 7 | 8:
        print('Літо')
    case 9 | 10 | 11:
        print('Осінь')
    case _:
        print('Такого місяця не існує')
