"""
Завдання №1.
Реалізуйте програму, яка створює кілька таймерів,
кожен із яких відлічує час до певної події
(наприклад, відправка повідомлення через 5 секунд, нагадування через 10 секунд тощо).
Використовуй для цього потоки, щоб усі таймери працювали одночасно, не блокуючи виконання програми.

"""

import threading
import time

def set_timer(delay_seconds: int, message: str):
    thread_name = threading.current_thread().name
    time.sleep(delay_seconds)
    print(f'!!! [ПОДІЯ] {message} (спрацював {thread_name}) !!!')

timers_to_set = [
    (2, 'Пора йти на обід!'),
    (5, 'Не забудь помити руки перед обідом.'),
    (8, 'Термінове нагадування: під час їжі випий свої ліки!'),
]

threads = []

print('Головна програма: запускаю всі таймери.')

for delay, msg in timers_to_set:
    timer_thread = threading.Thread(target=set_timer, args=(delay, msg), name=f'Таймер-{delay}с')
    threads.append(timer_thread)
    timer_thread.start()

for t in threads:
    t.join()    # Для того, щоб головний потік чекав завершення всіх дочірніх потоків

print('\nГоловна програма: Всі таймери спрацювали. Програма завершена.')
#----------------------------------------------------------------------------

"""
Завдання №2. 
При старті додатку запускаються три потоки. 
Перший потік заповнює список випадковими числами. 
Два інші потоки очікують на заповнення(метод join). 
Коли перелік заповнений, обидва потоки запускаються. 
Перший потік знаходить суму елементів списку, 
другий потік знаходить середнє арифметичне значення у списку. 
Отриманий список, сума та середнє арифметичне виводяться на екран.
"""
import threading
import time
import random

shared_list = []    #список, до якого матимуть доступ усі потоки
results = {}    # Словник для збереження результатів

def fill_list(data_list: list, count: int): #Потік 1: випадкові числа
    thread_name = threading.current_thread().name
    print(f'[{thread_name}] Починаю заповнювати список...')
    for _ in range(count):
        number = random.randint(1, 100)
        data_list.append(number)
        time.sleep(0.3) # Затримка
    print(f'[{thread_name}] Список заповнено! Зміст: {data_list}')

def calculate_sum(data_list: list, result_dict: dict):  #Потік 2: сума
    thread_name = threading.current_thread().name
    print(f'[{thread_name}] Очікую на дані... Отримав. Обмірковую обчислення суми.')
    list_sum = sum(data_list)
    result_dict['sum'] = list_sum
    print(f'[{thread_name}] Сума елементів: {list_sum}')

def calculate_average(data_list: list, result_dict: dict):  #Потік 3: середнє арифметичне
    thread_name = threading.current_thread().name
    print(f'\n[{thread_name}] Очікую на дані... Отримав. Обмірковую обчислення середнього.')
    if not data_list:
        avg = 0
    else:
        avg = sum(data_list) / len(data_list)
    result_dict['average'] = avg
    print(f'[{thread_name}] Середнє арифметичне: {avg:.2f}')

filler_thread = threading.Thread(target=fill_list, args=(shared_list, 10), name='Потік-випадкові числа')
sum_thread = threading.Thread(target=calculate_sum, args=(shared_list, results), name='Потік-сума')
average_thread = threading.Thread(target=calculate_average, args=(shared_list, results), name='Потік-середнє арифметичне')

filler_thread.start()
filler_thread.join()    #затримка, щоб завершився список
print('\nСписок успішно заповнено. Запускаю потоки для обчислень.')

sum_thread.start()
time.sleep(5)
average_thread.start()

sum_thread.join()   # затримка, щоб відбулися всі обчислення
average_thread.join()   # затримка, щоб відбулися всі обчислення
time.sleep(3)

print('\n--- ФІНАЛЬНІ РЕЗУЛЬТАТИ ---')
print(f'Згенерований список: {shared_list}')
print(f'Обчислена сума: {results.get("sum")}')
print(f'Середнє арифметичне: {results.get("average"):.2f}')
