
def create_hashtag(string: str):
    return '#' + ''.join(word.capitalize() for word in string.split())


def move_zeros(l: list):
    for el in l:
        if el == 0:
            l.remove(0)
            l.append(0)

    return l


print('Hello, world!')
print(move_zeros([1, 2, 0, 0, 3, 0, 4]))
print(move_zeros([1, 5, 0, 0, 5, 45, 6, 0]))
print(move_zeros([]))
