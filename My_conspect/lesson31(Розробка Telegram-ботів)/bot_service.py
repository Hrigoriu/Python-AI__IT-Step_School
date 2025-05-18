import random as rd
import string

class Service:
    pass


def generate_password(message_len: str):
    message_len = message_len.strip()
    if not message_len.isdigit():
        return None

    message_len = int(message_len)
    if message_len not in range(8, 36):
        return None

    return ''.join(rd.choice(string.ascii_letters + string.digits) for _ in range(message_len))