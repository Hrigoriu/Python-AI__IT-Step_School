
# Складна задача 1
numbers = input('Введіть числа через пробіл: ') + " "

even_count = 0  # парні
odd_count = 0  # непарні

memory = ''
for char in numbers:
    if char != ' ':
        memory += char
    else:  # якщо char - пробіл
        if not memory:  # if memory == '' (якщо змінна порожня)
            continue
        if int(memory) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        memory = ''

print(f'Кількість парних: {even_count}')
print(f'Кількість непарних: {odd_count}')

# Бонусний варіант:
numbers = list(map(int, input('Введіть числа через пробіл: ').split()))
print(f'Кількість парних: {sum(1 for number in numbers if number % 2 == 0)}')
print(f'Кількість непарних: {sum(1 for number in numbers if number % 2 != 0)}')

# Складна задача 2
find_len = int(input('Введіть шукому довжину слова: '))
text = 'Привіт, як твої справи? У мене все ок.'
counter = 0

word = ''
for char in text:
    if char in '!?.,:; ()':  # якщо символ - знак пунктуації
        if len(word) == find_len:
            counter += 1

        word = ''
    else:  # якщо символ - НЕ знак пунктуації
        word += char

print(f'Результат: {counter}')
