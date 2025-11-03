import random
import string


def test_func(a, b, *args, key_1=1, key_2=2, **kwargs):
    print(f'Позиційні: {a}, {b}')
    print(f'Нескінченні позиційні: {args}')
    print(f'Ключові: {key_1}, {key_2}')
    print(f'Нескінченні ключові: {kwargs}')


def mult_numbers(*numbers: int | float):
    result = 1

    for n in numbers:
        result *= n

    return result


def password_generator(password_len: int, include_punctuation=False):
    if password_len not in range(8, 31):
        return

    pattern = string.ascii_letters + string.digits
    if include_punctuation:
        pattern += string.punctuation

    return ''.join(random.choice(pattern) for _ in range(password_len))


# # Lambda-функції
# my_lambda = lambda x, y: x + y  # lambda <параметри>: <що повертаємо>
#
# print(my_lambda(10, 20))

def for_sort(el):
    return el[1]

# d = {
#     'string1': 10,
#     'string2': 25,
#     'string3': 1,
#     'string4': -4
# }
#
# print(dict(sorted(d.items(), key=lambda el: el[1])))

print(*map(lambda el: '!' + el + '!', 'HELLO'))
