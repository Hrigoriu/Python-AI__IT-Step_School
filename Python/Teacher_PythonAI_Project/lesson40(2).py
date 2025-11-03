import threading


def new_thread(data):
    thread_name = threading.current_thread().name

    for counter in range(1, data + 1):
        print(f'{thread_name}: {counter}')


# daemon - поток, який існує тільки поки існує головний поток (або інший поток без daemon=True)
threading.Thread(target=new_thread, args=(100, ), name='New Thread 1(DAEMON)', daemon=True).start()  # запускаємо поток з циклом на 1000

threading.Thread(target=new_thread, args=(50, ), name='New Thread 2').start()  # запускаємо поток з циклом на 1000

new_thread(15)
