"""
import threading
import time
import random as rd

number = 0
def add_counter():
    global number
    while True:
        number += 1
        print(f'{threading.current_thread().name}: {number}')
        time.sleep(1)
#add_counter()
for i in range(10):
    threading.Thread(target=add_counter, name=f'Thread {i}').start()
"""

import threading
import time
import random as rd

number = 0

lock = threading.Lock()  # блокує доступ до коду, якщо там знаходиться інший поток
event = threading.Event()  # блокує доступ до коду, поки не з'явиться сигнал в іншому потоці
semaphore = threading.Semaphore(3)  # обмежує кількість потоків, які можуть використовуватись одначасно
barrier = threading.Barrier(10)  # очікує, поки всі потоки не досягнуть однієї точки, щоб продовжити разом

def add_counter():
    global number
    while True:
        #lock.acquire()
        with lock:
            number += 1
            print(f'{threading.current_thread().name}: {number}')
        #lock.release()
        time.sleep(1)

def waiter():
    thread_name = threading.current_thread().name
    while True:
        print(f'Я ({thread_name}) чекаю сигнал')
        event.wait()  # очікування прийому сигналу
        print(f'Я спіймав сигнал! {thread_name}')
        time.sleep(1)

def sender():
    thread_name = threading.current_thread().name
    while True:
        print(f'Я ({thread_name}) відправляю сигнал')
        time.sleep(rd.randint(3, 5))
        event.set()  # надсилання сигналу (відкриває бар'єр)
        print('Сигнал надіслано!')
        event.clear()  # закриває бар'єр назад (для нового сигналу)

def timer(n: int):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)

def semaphore_test():
    thread_name = threading.current_thread().name
    with semaphore:
        print(f'{thread_name} почав роботу!')
        time.sleep(6)
        print(f'{thread_name} закінчив роботу!')

def barrier_test():
    random_sleep = rd.randint(1, 6)
    thread_name = threading.current_thread().name
    print(f'Я {thread_name} і я буду спати {random_sleep} секунд!')
    time.sleep(random_sleep)
    barrier.wait()  # поток займає бар'єр та чекає інших
    print(f'Я {thread_name} поспав!')

# # ---- Локери
# for i in range(10):
#     threading.Thread(target=add_counter, name=f'Thread {i}').start()

# # ---- Сигнали
threading.Thread(target=waiter, name='Thread Waiter 1').start()
threading.Thread(target=waiter, name='Thread Waiter 2').start()
threading.Thread(target=sender, name='Thread Sender').start()

# # ---- Очікування завершення потоків
timer_thread = threading.Thread(target=timer, args=(5, ), name='Timer Thread')
another_thread = threading.Thread(target=add_counter, name='Another Thread')

timer_thread.start()
timer_thread.join()  # очікує завершення потоку
another_thread.start()

# ----Тест семафорів
for n in range(10):
    threading.Thread(target=semaphore_test, name=f'Test Semaphore {n}').start()

# ----Тест бар'єрів
for n in range(10):
    threading.Thread(target=barrier_test, name=f'Test Barrier {n}').start()
#=======================================================================================

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
if __name__ == '__main__':  #рекурсія
    for n in range(5):
        p = multiprocessing.Process(target=task, name=f'Process {n}')
        p.start()


# # Обмін інформацією між процесами
if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    multiprocessing.Process(target=send_info, args=(parent_conn, )).start()
    multiprocessing.Process(target=check_info, args=(child_conn, )).start()
