"""
Напиши функцію, для сортування рядка слів,
розділених пропусками за довжиною слів в порядку зменшення.
Вхідні дані: Ruby Python Go JavaScript Java
Очікуваний результат: JavaScript Python Java Ruby Go
"""
def sort_word(string):
    words = string.split()
    words.sort(key=len, reverse=True)
    return ' '.join(words)

input_words = "Ruby Python Go JavaScript Java"
result = sort_word(input_words)
print(result)

"""
Напишіть рекурсивну функцію для обчислення суми списку цілих чисел
Вхідні дані:
1 4 7 90 45 23 16
Вихідні дані: 186
"""
def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + recursive_sum(numbers[1:])

input_list = [1, 4, 7, 90, 45, 23, 16]
result = recursive_sum(input_list)
print(result)
