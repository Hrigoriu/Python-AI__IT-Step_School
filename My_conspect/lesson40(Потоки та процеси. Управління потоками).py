import threading  # для роботи з потоками
import time
import random as rd
import queue


def run_thread(data: int):  # data = target
    thread_name = threading.current_thread().name
    print(f'Поток: {thread_name}')

    for thr_number in range(1, data + 1):
        print(f'{thread_name}: {thr_number}')  # поток: число потоку
#run_thread(10)

# for n in range(1, 11):
#     new_thread = threading.Thread(target=run_thread, args=(10, ), name=f'New thread {n}')
#     new_thread.start()

# =======------ Міні-бот -------========
user_inputs = queue.Queue()  # сюди будуть залітати запити

def bot_response():  # відповідь бота на запит
    global user_inputs
    print('Bot say: hello!')
    while True:
        if user_inputs.empty():  # якщо черга порожня
            time.sleep(1)
            continue

        time.sleep(2.5)

        while not user_inputs.empty():  # поки черга НЕ порожня
            user_text = user_inputs.get().lower()
            if user_text == 'привіт':
                print('\nBot: і тобі привіт!')
            elif user_text == 'передбачування':
                print(f'\nBot: Ваше передбачування: {rd.choice(["Тобі сьогодні пощастить!", "Краще не виходь сьогодні з дому!"])}')
            else:
                print('\nBot: Я тебе не розумію!')

def user_request():  # робити запит
    global user_inputs
    while True:
        user_text = input('\nUser input: ')
        if user_text:
            user_inputs.put(user_text)

threading.Thread(target=user_request, name='User Thread').start()
threading.Thread(target=bot_response, name='Bot Thread').start()
"""
ser input: Bot say: hello!
Привіт

User input: 
Bot: і тобі привіт!
передбачування

User input: 
Bot: Ваше передбачування: Краще не виходь сьогодні з дому!
"""
#===================================================================
import threading

def new_thread(data):
    thread_name = threading.current_thread().name
    for counter in range(1, data + 1):
        print(f'{thread_name}: {counter}')

# daemon - поток, який існує тільки поки існує головний поток (або інший поток без daemon=True)
threading.Thread(target=new_thread, args=(1000, ), name='New Thread 1(DAEMON)', daemon=True).start()  # запускаємо поток з циклом на 1000
threading.Thread(target=new_thread, args=(50, ), name='New Thread 2').start()  # запускаємо поток з циклом на 1000

new_thread(15)