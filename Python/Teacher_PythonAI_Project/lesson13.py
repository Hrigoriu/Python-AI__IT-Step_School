import random as rd
import string


def hello():  # def <назва>(<параметри>): <код>
    print('Привіт, світ!')


def hello_for_name(name: str):  # параметр - локальна змінна, яка створюється в момент виклику
    print(f'Привіт, {name.capitalize()}!')


def sum_two_numbers(a: int | float, b: int | float):
    return a + b  # return - повернути значення (якщо функція не має return, вона по дефолту повертає None)


def counter(n: int):
    for number in range(1, n + 1):
        return number  # return одразу закриває функцію


def password_generator(password_len: int):
    if password_len not in range(8, 31):
        return  # фактично буде return None

    # password = ''
    # for _ in range(password_len):
    #     password += rd.choice(string.ascii_letters + string.digits)
    #
    # return password

    return ''.join(rd.choice(string.ascii_letters + string.digits) for _ in range(password_len))


print(password_generator(-5))
print(password_generator(5))
print(password_generator(10_000_000))

print(password_generator(8))
print(password_generator(12))
print(password_generator(25))
