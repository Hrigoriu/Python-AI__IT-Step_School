"""
Завдання №1.
Реалізуйте програму, яка створює один процес,
який обчислює суму чисел від 1 до 10,
і два потоки в цьому процесі, які обчислюють добуток чисел
від 1 до 5 і від 6 до 10 відповідно.
Результати кожного обчислення виводяться на екран.
"""
import multiprocessing
import threading
import math
import time

def calculate_product(start: int, end: int):
    thread_name = threading.current_thread().name
    numbers_range = range(start, end + 1)
    product_result = math.prod(numbers_range)
    print(f'  [Потік: {thread_name}] Добуток чисел від {start} до {end} = {product_result}')

def process_task():
    process_name = multiprocessing.current_process().name
    print(f'[{process_name}] Почав роботу.')
    time.sleep(2)
    sum_result = sum(range(1, 11))
    print(f'[{process_name}] Сума чисел від 1 до 10 = {sum_result}')
    print(f'[{process_name}] Створюю два потоки для обчислення добутку...')

    thread1 = threading.Thread(target=calculate_product, args=(1, 5), name='Product-1-5')
    thread2 = threading.Thread(target=calculate_product, args=(6, 10), name='Product-6-10')

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'[{process_name}] Усі потоки завершили роботу. Процес завершується.')

if __name__ == '__main__':
    main_process = multiprocessing.Process(target=process_task, name='MainCalcProcess')

    main_process.start()
    main_process.join()

    print('\nПрограма завершила усі свої завдання.')
#--------------------------------------------------------------

"""
Завдання №2.	
Напишіть програму, яка запускає два процеси. 
Кожен процес створює два потоки. 
Перший поток виводить текстове повідомлення, 
а другий обчислює і виводить результат факторіала чисел 
від 1 до 5(для першого процесу) та від 6 до 10(для другого).
"""
import multiprocessing
import threading
import math
import time

def show_message():
    proc_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    print(f'  [{proc_name}][{thread_name}] Вітання від процесу!')
    time.sleep(1)

def calculate_factorials(start_num, end_num):
    proc_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    print(f'  [{proc_name}][{thread_name}] Починаю обчислення факторіалів...')
    time.sleep(2)
    for i in range(start_num, end_num + 1):
        result = math.factorial(i)
        print(f'    [{proc_name}][{thread_name}] Факторіал {i}! = {result}')
        time.sleep(2)
    print(f'  [{proc_name}][{thread_name}] Обчислення завершено.')
    time.sleep(3)

def process_container(factorial_start, factorial_end):
    proc_name = multiprocessing.current_process().name
    print(f'[{proc_name}] Створюю внутрішні потоки.')
    time.sleep(2)

    msg_thread = threading.Thread(target=show_message, name='MessageThread')
    fact_thread = threading.Thread(target=calculate_factorials, args=(factorial_start, factorial_end),
                                   name='FactorialThread')
    msg_thread.start()
    fact_thread.start()

    msg_thread.join()
    fact_thread.join()
    print(f'[{proc_name}] Завершив роботу.')
    time.sleep(1)

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=process_container, args=(1, 5), name='Process-A')
    process2 = multiprocessing.Process(target=process_container, args=(6, 10), name='Process-B')

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('\nВсі процеси завершили свою роботу.')