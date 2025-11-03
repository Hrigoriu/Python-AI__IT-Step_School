import asyncio  # модуль для роботи з асинхронністю
import time

async def say_hello():  # створення асинхронної функції
    print('Привіт!')
    #time.sleep(5)
    await asyncio.sleep(5)
    print('Бувай!')

async def main():
    await say_hello()
asyncio.run(main())


# ========= 1-й приклад
async def complete_task(task: str, delay: int):  # створення асинхронної функції
    print(f'Почала виконуватись задача: {task}!')
    await asyncio.sleep(delay)
    print(f'Задача {task} була виконана!')

async def main():
    await asyncio.gather(
        complete_task('Задача 1', 5),
        complete_task('Задача 2', 3),
        complete_task("Задача 3", 6)
    )
asyncio.run(main())


# ========= 2-й приклад (Асинхронний повідомлення)
import asyncio
async def remind(sec: int, message: str):
    await asyncio.sleep(sec)
    print(f'Нагадка: {message}')

async def main():
    await asyncio.gather(
        remind(3, 'Випипти води'),
        remind(5, 'Підйом'),
        remind(7, 'Працювати')
    )
asyncio.run(main())
# ========= 3-й приклад (Асинхронний таймер)
import asyncio
seconds = [5, 3, 2, 6, 3, 7, 2]
async def remind(sec: int, message: str):
    await asyncio.sleep(sec)
    print(f'Нагадка: {message}')

async def main():
    functions = [remind(s, f'Задача на {s} секунд') for s in seconds]
    await asyncio.gather(*functions)
asyncio.run(main())


# ========= 4-й приклад (Асинхронний прогрес бар)
import asyncio
async def progress_bar(name: str, duration: int):
    for number in range(1, duration + 1):
        print(f'({name}) | {number}/{duration}')
        await asyncio.sleep(1)
    print(f'{name} зевершено!')

async def main():
    await asyncio.gather(
        progress_bar('Задача 1', 5),
        progress_bar('Задача 2', 3),
        progress_bar('Задача 3', 10)
    )
asyncio.run(main())
