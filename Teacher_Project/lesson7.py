
# end = int(input('Кінцеве число діапазону: '))
#
# for number in range(1, end + 1):
#     print(number)  # 135
#
#     if number >= 500:
#         print('Діапазон перебільшено!')
#         break
# else:  # виконується, якщо цикл не був перерваний оператором break
#     print('ELSE')

# end = int(input('Кінцеве число діапазону: '))
# number = 1
#
# while number <= end:
#     print(number)
#
#     if number >= 500:
#         print('Діапазон перебільшено!')
#         break
#
#     number += 1
# else:
#     print('ELSE')

# for number in range(1, 100_001):
#     if number % 2 != 0:
#         continue  # continue перекидає цикл на наступний крок (ітерацію)
#
#     print(number)

'''
Завдання 1
Користувач вводить текст та якийсь символ. Замініть всі ці символи у тексті на "*"
Наприклад: "Hello, world", "l" -> "He**o, wor*d"
'''

# text = input('Введіть текст: ')
# find_char = input('Введіть символ для заміни на зірочку: ')
# result = ''
#
# for char in text:
#     if char != find_char:
#         result += char
#     else:
#         result += '*'
#
# print(result)

# text = input(': ')
#
# for char in text:
#     if char in '0123456789':
#         print(f'У тексті знайдена цифра: {char}')
#         break
# else:
#     print('У тексті немає цифр')


for x in range(1, 11):  # зовнішній
    print('x=', x)
    print('---------------------')
    for y in range(1, 11):  # вкладений
        print('y=', y)



