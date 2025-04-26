import time


'''
Шаблон декоратора: 

def time_decorator(function):  # декоратор - це функція вищого порядку
    def wrapper(*args, **kwargs):
        # код до ВИКЛИКУ функції
        result = function(*args, **kwargs)
        # код після ВИКЛИКУ функції
        return result
    
    
    return wrapper
'''
def time_decorator(function):  # декоратор - це функція вищого порядку
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()

        print(f"Час роботи функції {function.__name__}: {end - start}")

        return result


    return wrapper


def powers(n: int):  # -> 1^2, 2^2, ... n
    for number in range(1, n + 1):
        yield number ** 2  # yield перетворює функцію на генератор


@time_decorator
def mult_numbers(*nums: int):
    result = 1

    for el in nums:
        result *= el

    return result

@time_decorator
def func():
    return 'Hi!'


print(mult_numbers(1, 2, 3, 4, 5))
# print(mult_numbers(*range(1, 10_000)))

print(func())
