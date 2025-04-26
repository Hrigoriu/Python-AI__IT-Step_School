# Типи даних

string = '10'  # str(строка) - текстовий літерал, або послідовність символів

integer = 10  # int - ціле число
float_ = 10.10  # float - дробове десятичне число

boolean = True  # bool - логічний тип даних: True(Істина, Так, 1); False(Брехня, Ні, 0)

none = None  # None - відстуній тип даних

# Перетворення

# на str (фактично майже завжди просто накладає лапки на об'єкт)
print(str(10) + '!')
print(str(True) + '.')

# на int
print(int('10') + 1)
# print(int('abc'))  # ValueError, бо таку строку не можна перетворити на число
print(int('10_000_000'))
# print(int('5354as.fbsa34'))  # ValueError

print(int(9.9999))  # 9, бо це НЕ округлення
print(int(False))

# на bool - True, якщо об'єкт НЕ порожній
print(bool(1))
print(bool(-5))
print(bool(0))

print(bool('False'))
print(bool(''))

print(bool(None))

# # Задача
num_1 = int(input('Введіть число 1: '))  # input() завжди повертає STR
num_2 = int(input('Введіть число 2: '))

sum_of_numbers = num_1 + num_2
print('Сума чисел: ' + str(sum_of_numbers))
print(f'Сума чисел: {sum_of_numbers}')

