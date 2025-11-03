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
        with lock:
            number += 1
            print(f'{threading.current_thread().name}: {number}')
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
# threading.Thread(target=waiter, name='Thread Waiter 1').start()
# # threading.Thread(target=waiter, name='Thread Waiter 2').start()
#
# threading.Thread(target=sender, name='Thread Sender').start()

# # ---- Очікування завершення потоків
# timer_thread = threading.Thread(target=timer, args=(5, ), name='Timer Thread')
# another_thread = threading.Thread(target=add_counter, name='Another Thread')
#
# timer_thread.start()
# timer_thread.join()  # очікує завершення потоку
#
# another_thread.start()


# ----Тест семафорів
# for n in range(10):
#     threading.Thread(target=semaphore_test, name=f'Test Semaphore {n}').start()

# ----Тест бар'єрів
for n in range(10):
    threading.Thread(target=barrier_test, name=f'Test Barrier {n}').start()