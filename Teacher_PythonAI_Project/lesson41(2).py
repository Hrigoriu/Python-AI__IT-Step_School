import multiprocessing
import threading
import random as rd
import time


number = 0
lock = threading.Lock()


def thread_adder():
    global number

    thread_name = threading.current_thread().name
    with lock:
        number += 1
        print(f'{thread_name}: {number}')


def task():
    global number

    number += 1

    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name

    print(f'Привіт з процесу {process_name} та потоку {thread_name}! Значення числа: {number}')

    for n in range(5):
        threading.Thread(target=thread_adder, name=f'Thread {n} ({process_name})').start()


def send_info(conn):
    time.sleep(5)

    random_number = rd.randint(1, 100)
    print(f'Я надсилаю інфу: {random_number}')

    conn.send(random_number)
    conn.close()


def check_info(conn):
    print('Я чекаю на інфу!')

    result = conn.recv()
    print(f'Я отримав нове число: {result}')


# - Запуск процесу
if __name__ == '__main__':
    for n in range(5):
        p = multiprocessing.Process(target=task, name=f'Process {n}')
        p.start()


# # Обмін інформацією між процесами
# if __name__ == "__main__":
#     parent_conn, child_conn = multiprocessing.Pipe()
#
#     multiprocessing.Process(target=send_info, args=(parent_conn, )).start()
#     multiprocessing.Process(target=check_info, args=(child_conn, )).start()
