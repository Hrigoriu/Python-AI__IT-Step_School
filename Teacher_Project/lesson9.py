
string = 'Hello, world!'

# Метод - "дія" об'єкта, направлена на його властивості чи атрибути
# Метод - функція, яка описана всередині класу

# ---Методи строк

# 1. case-методи
print(string.upper())  # призводить всі літеру у строці до великого кейсу
print(string.lower())  # призводить всі літеру у строці до маленького кейсу
print('hElLo, wOrlD!'.capitalize())  # першу літера - велика, всі інші - маленькі
print(string.swapcase())  # міняє кейс на протилежний

# 2. bool-методи (починаються з is) - створені для використання в умовах
print(' UPPER!!!123'.isupper())  # True, якщо всі ЛІТЕРИ(символи, що мають кейс) - великі
print('lower'.islower())  # True, якщо всі ЛІТЕРИ(символи, що мають кейс) - маленькі
print('100000'.isdigit())  # True, якщо ВСІ ЕЛЕМЕНТИ строки - цифри
print('qwertyфвіафівафів'.isalpha())  # True, якщо ВСІ ЕЛЕМЕНТИ строки - літери

print(string.startswith('Hello'))  # True, якщо строка ПОЧИНАЄТЬСЯ з вказаної підстроки
print(string.endswith('world!'))  # True, якщо строка ЗАКІНЧУЄТЬСЯ вказаною підстрокою

string = 'Hello, world!'
# 3. Робота з підстроками (підстрока(substring) - будь-яка частина строки)
print(string.index('world'))  # повертає індекс, з якого починається підстрока
# print(string.index('python'))  # якщо підстроки не існує - ValueError

print(string.find('world'))  # повертає індекс, з якого починається підстрока
print(string.find('python'))  # на відміну від index, повертає -1, якщо підстроки не існує

print(string.count('l'))  # повертає кількість входжень підстроки у строку (кількість елементів). Може бути 0

print(string.replace('l', '*'))  # заміняє всі __old на __new
print(string.replace('world', '$'))  # працює і з підстроками
print(string.replace('o', '[replace]'))
print(string.replace('l', ''))  # можна навіть видаляти елементи, міняючи їх на порожню строку

print('   Python        '.strip())  # "відрізає" пробіли з обох боків строки
print('   1 2 3 4 5 6 7       '.strip())
print('_-_-_1-_2-_3-_4-_5-_-_'.strip('-_'))  # якщо передати групу символів, відріже їх

# 4. split та join
numbers = '543 -3 6543 400 54 236'  # "розрізає" строку, поклавши всі елементи в список
print(numbers.split())

word = 'HELLO'  # задача: помістити між всіма літерами '|'

print('|'.join(word))
print(', '.join(str(number) for number in range(1, 101)))
print(' | '.join(numbers.split()))
print(''.join(str(number) for number in range(100)))
print('\n'.join(word))
