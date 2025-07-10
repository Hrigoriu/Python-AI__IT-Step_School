"""
Завдання №1.
Запусти 3 процеси, кожен з яких виводить своє ім’я та затримується на 2 секунди.
Після цього основний процес має вивести "Усі завершились".
"""
#varian#1
import multiprocessing
import time

def worker_process():
    process_name = multiprocessing.current_process().name
    print(f'Процес "{process_name}" почав роботу.')
    time.sleep(3)
    print(f'Процес "{process_name}" завершив роботу.')

if __name__ == '__main__':
    processes = []
    for i in range(1, 4):
        p = multiprocessing.Process(target=worker_process, name=f'Worker-{i}')
        processes.append(p)
        p.start()
    print('Чекаю на завершення всіх дочірніх процесів...')
    for p in processes:
        p.join()
    print('\n Усі процеси завершились!')
#------------------------------------------------------------------------------
#varian#2
def mp_func():
    process_name = multiprocessing.current_process().name
    print(f'I... Am {process_name}!')
    time.sleep(2)

if __name__ == '__main__':
    for n in range(3):
        p = multiprocessing.Process(target=mp_func, name=f'Test Process {n}')
        p.start()
        p.join()
    print('Усі завершились')
#=============================================================================

"""
Завдання №2. 
Один процес чекає сигналу через Event, інший подає його через 3 секунди. 
Після сигналу вивести "Отримано дозвіл!".
"""
#variant №1
import multiprocessing
import time
import random

def waiter_process(event_object: multiprocessing.Event):
    process_name = multiprocessing.current_process().name
    print(f'[{process_name}] Я чекаю на сигнал (дозвіл)...')
    event_object.wait()  # Блокує процес, доки не буде викликано event
    print(f'[{process_name}] Отримано дозвіл!')

def sender_process(event_object: multiprocessing.Event):
    process_name = multiprocessing.current_process().name
    print(f'[{process_name}] Почекаю 3 секунди перед відправкою сигналу.')
    time.sleep(3)
    print(f'[{process_name}] Надсилаю сигнал!')
    event_object.set()

if __name__ == '__main__':
    event = multiprocessing.Event()
    waiter = multiprocessing.Process(target=waiter_process, args=(event,), name='Waiter')
    sender = multiprocessing.Process(target=sender_process, args=(event,), name='Sender')

    waiter.start()
    sender.start()

    waiter.join()
    sender.join()

    print('Обидва процеси (очікування та відправка) завершились.')
#------------------------------------------------------------------------------------------
#variant #2
def send_permission(conn, event):
    process_name = multiprocessing.current_process().name
    print(f'{process_name}: Даю дозвіл...')
    time.sleep(2)
    permission = random.choice([True, False])
    conn.send(permission)
    event.set()
    event.clear()

def check_permission(conn, event):
    process_name = multiprocessing.current_process().name
    print(f'{process_name}: Чекаю на дозвіл...')
    event.wait()
    permission = conn.recv()
    if permission:
        print(f'Отримано дозвіл {process_name}! ({permission})')
    else:
        print(f'Дозвіл не отримано {process_name}! ({permission})')

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    with multiprocessing.Manager() as manager:
        event = manager.Event()
        sender = multiprocessing.Process(target=send_permission, args=(parent_conn, event), name='Permission Sender Process')
        checker = multiprocessing.Process(target=check_permission, args=(child_conn, event), name='Permission Checker Process')

        sender.start()
        checker.start()

        sender.join()
        checker.join()