"""
Завдання 1. Асинхронний лічильник з Event (рівень: середній)
Інструмент: asyncio.Event
________________________________________
📄 Умова:
•	Одна корутина (watcher) чекає на сигнал від іншої (trigger).
•	Після сигналу лічильник починає рахувати до 5 з інтервалом 1 сек.
•	До події має виводитись Очікую сигналу...
________________________________________
🔧 Ціль:
•	асинхронна синхронізація між задачами.
"""
import asyncio

async def watcher(event: asyncio.Event):
    print('[Watcher] Очікую сигналу...')
    await event.wait()
    print('\n[Watcher] Сигнал отримано! Починаю відлік.')
    for i in range(1, 6):
        print(f'Лічильник: {i}')
        await asyncio.sleep(1)
    print('[Watcher] Відлік завершено.')

async def trigger(event: asyncio.Event, delay: int):
    print(f'[Trigger] Я надішлю сигнал через {delay} секунди.')
    await asyncio.sleep(delay)
    print('[Trigger] Надсилаю сигнал!')
    event.set()

async def main():
    signal_event = asyncio.Event()
    watcher_task = asyncio.create_task(watcher(signal_event))
    trigger_task = asyncio.create_task(trigger(signal_event, delay=3))
    await asyncio.gather(watcher_task, trigger_task)
    print('\n[Main] Мої вітання! Кінець.')

if __name__ == '__main__':
    asyncio.run(main())
#========================================================================

"""
Завдання 2. Обмежений завантажувач з Semaphore (рівень: середньо-складний)
Інструмент: asyncio.Semaphore
________________________________________
📄 Умова:
•	Є список сайтів (можна просто імена сайтів, без справжніх запитів).
•	Імітується "завантаження" кожного з них (через await asyncio.sleep(...)).
•	Не більше 3 сайти одночасно завантажуються.
________________________________________
🔧 Ціль:
•	обмеження кількості одночасних задач.
________________________________________
"""
import asyncio  #пишу тут, щоб вам можна було скопіювати з усім і провірити
import random

SITES = [
    'google.com',
    'facebook.com',
    'youtube.com',
    'twitter.com',
    'instagram.com',
    'linkedin.com',
    'github.com',
    'wikipedia.org',
    'reddit.com',
]

async def download_site(semaphore: asyncio.Semaphore, site: str):
    async with semaphore:
        print(f'[Download] ! Починаю завантаження [{site}] (Слот зайнято)')
        download_time = random.uniform(3, 8)
        await asyncio.sleep(download_time)
        print(f'    [Download] ### {site} завантажено! (Слот звільнено)')

async def main():
    semaphore = asyncio.Semaphore(3)
    print(f'Запускаю завантаження {len(SITES)} сайтів з обмеженням в 3 одночасних з\'єднання.\n')
    tasks = [asyncio.create_task(download_site(semaphore, site)) for site in SITES]
    await asyncio.gather(*tasks)
    print('\n[Main] Все успішно завантажено!')

if __name__ == "__main__":
    asyncio.run(main())
#=======================================================================================


"""
Завдання 3. Продюсер / Консюмер з Queue та cancel (рівень: складний)
Інструменти: asyncio.Queue, asyncio.create_task, cancel()
________________________________________
📄 Умова:
•	producer() — додає в чергу випадкові числа кожні 0.5 секунди.
•	consumer() — обробляє числа (імітація через sleep(1)).
•	Через 5 секунд система повинна зупинитись:
o	зупинити продюсера,
o	відмінити споживача,
o	завершити програму акуратно.
________________________________________
🔧 Ціль:
•	робота з чергою,
•	контроль виконання і відміна задач.
"""
import asyncio  #пишу тут, щоб вам можна було скопіювати з усім і провірити
import random

async def producer(queue: asyncio.Queue):
    print('[Producer] Почав роботу. Генерую числа...')
    try:
        while True:
            number = random.randint(1, 100)
            await queue.put(number)
            print(f'[Producer] --> Додав у чергу: {number}')
            await asyncio.sleep(2)
    except asyncio.CancelledError:
        print('[Producer] Мене зупинили! Завершую роботу.')

async def consumer(queue: asyncio.Queue):
    print('[Consumer] Почав роботу. Очікую на числа...')
    try:
        while True:
            number = await queue.get()
            print(f'  [Consumer] ! Отримав: {number}. Починаю обробку (1 сек)...')
            await asyncio.sleep(2)
            print(f'  [Consumer] ### {number} оброблено.')
            queue.task_done()
    except asyncio.CancelledError:
        print('[Consumer] Мене зупинили! Завершую роботу.')

async def main():
    shared_queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(shared_queue))
    consumer_task = asyncio.create_task(consumer(shared_queue))
    print('\n[Main] Система запущена. Працюємо 7 секунд...')
    await asyncio.sleep(7)
    print('\n[Main] Час вийшов! Починаю все зупиняти.')
    print('[Main] Скасовую задачу producer...')
    producer_task.cancel()
    print('[Main] Скасовую задачу consumer...')
    consumer_task.cancel()
    await asyncio.gather(producer_task, consumer_task, return_exceptions=True)
    print('\n[Main] Система успішно зупинена.')

if __name__ == '__main__':
    asyncio.run(main())
