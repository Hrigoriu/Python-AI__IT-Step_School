
def counter(n: int):
    if n <= 0:
        return

    print(n)

    counter(n - 1)


def factorial_recursive(n: int):
    if n <= 0:
        return 1

    return n * factorial_recursive(n - 1)


