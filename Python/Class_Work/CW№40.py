"""
Завдання №1. Створіть два потоки.
Один повинен друкувати числа від 1 до 10,
другий — літери від 'a' до 'j'.
Обидва потоки повинні працювати одночасно.
"""
import threading
import time

def print_numbers():    # 1 потік
    thread_name = threading.current_thread().name
    print(f'Потік "{thread_name}" почав роботу.')
    for i in range(1, 11):
        print(f'Число: {i}')
        time.sleep(0.3)  # затримка
    print(f'Потік "{thread_name}" завершив роботу.')

def print_letters():    # 2 потік
    thread_name = threading.current_thread().name
    print(f'Потік "{thread_name}" почав роботу.')
    letters = 'abcdefghij'
    for letter in letters:
        print(f'Літера: {letter}')
        time.sleep(0.5) # затримка
    print(f'Потік "{thread_name}" завершив роботу.')

thread1 = threading.Thread(target=print_numbers, name='Потік-цифри',daemon=True)
thread2 = threading.Thread(target=print_letters, name='Потік-літер')

thread1.start()
thread2.start()
#-----------------------------------------------------------------------------------

"""
Завдання №2. 
Створи потік, який щосекунди виводить поточний час протягом 5 секунд. 
Головний поток просто працює в while True, поки користувач його не закриє. 
Коли закривається головний поток, замірювач часу теж припинє роботу.
"""
import threading
import time

print('Потік з часом буде працювати, поки ви не зупините програму (Ctrl+C).')
def show_current_time():    # Потік виводу часу
    thread_name = threading.current_thread().name
    print(f'Потік "{thread_name}" запущено.')
    while True:
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f'Поточний час: {current_time}')
        time.sleep(1)    # затримка

time_thread = threading.Thread(target=show_current_time, name='Потік-час', daemon=True)
time_thread.start()

try:
    while True:
        time.sleep(0.5)    # затримка
except KeyboardInterrupt:
    print('\n Ура!!! Ти сам зупинив програму.')
#--------------------------------------------------------------------------------------------
"""
Завдання №3. 
Створи демон-потік, який вічно виводить "Я працюю..." кожні 2 секунди. 
Основна програма повинна завершитися через 5 секунд.
"""
import threading
import time

def worker_daemon():    # 1 потік
    while True:
        print('Демон-потік: Я працюю...')
        time.sleep(2)# затримка

daemon = threading.Thread(target=worker_daemon, name='Демон-потік', daemon=True)
daemon.start()

print('Програма почала роботу і працюватиме 5 секунд.')
time.sleep(5)
print('Програма завершує роботу. Демон-потік буде зупинено.')
