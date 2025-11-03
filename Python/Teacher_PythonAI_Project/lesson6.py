
# Цикли
# Ітерація - повторення одного порядку дій через якусь послідовність
# _iterable - властивість об'єктів, що дозволяють їм ітеруватись

# WHILE (ПОКИ)

number = 1

while number <= 100_000:  # ПОКИ <умова == Істина>: <код>
    print(number)   # крок циклу - 1 виконання всього його коду (1 ітерація)
    number += 1  # додає 1 до number

while True:  # while True - нескінченний цикл
    print(number)
    number += 1

    if number > 100_000:  # умова виходу
        break  # break - вихід з циклу


text = input('Text: ')
index = 0

while index < len(text):  # ітерація строки по індексу
    print(text[index])
    index += 1

# FOR (ДЛЯ)

for number in range(1, 100_001):  # ДЛЯ <частина> З <об'єкт>: <цикл>
    print(number)

text = input('Text: ')

for index in range(len(text)):
    print(text[index])

for char in text:  # ітерація строки (str)
    print(char)

# Задача: користувач вводить строку. Порахуйте кількість голосних літер

text = input('Text: ')
counter = 0

for char in text:
    if char in 'OIUYEAoiuyea':
        counter += 1

print(f'Кількість голосних літер: {counter}')
