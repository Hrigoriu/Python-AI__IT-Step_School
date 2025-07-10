import asyncio
import random as rd

# Task 1
"""
Завдання №1. 
Асинхронний програвач нот
Опис:
Є список нот ["До", "Ре", "Мі", "Фа"], кожна триває 0.5 секунди. 
Програй їх у функції play_note(note):
 - послідовно (main1)
-  одночасно (main2)
"""
#variant#1
async def play_simultaneously(notes: list):
    print(', '.join(note for note in notes))

async def play_consistently(notes: list):
    for note in notes:
        await asyncio.sleep(0.5)
        print(note)

async def main():
    notes = ['До', 'Ре', 'Мі', 'Фа']
    await asyncio.gather(
        play_simultaneously(notes),
        play_consistently(notes)
    )
asyncio.run(main())
#----------------------------------------------------------------
#variant#2
import asyncio

notes = ['До', 'Ре', 'Мі', 'Фа']
async def play(note: str):
    await asyncio.sleep(0.5)
    print(note)

async def main1():
    for n in notes:
        await play(n)

async def main2():
    tasks = [play(n) for n in notes]
    await asyncio.gather(*tasks)
asyncio.run(main1())
asyncio.run(main2())
#=================================================================

# Task 2
"""
Завдання №2. 
Є список серверів: ["Server-A", "Server-B", "Server-C", ...].
Кожен сервер імітує відповідь із випадковою затримкою (0.1–2 сек).
Твоя задача:
Імітувати пінг кожного сервера з випадковою затримкою.
Дочекатися відповідей.
Визначити, хто відповів найпершим.
"""
import asyncio
import random as rd
servers_results = []

async def ping_server(server: str, delay: float):
    global servers_results
    print(f'{server} is up and running! Delay: {delay:.2f}')
    await asyncio.sleep(delay)
    print(f'The {server} has answered!')
    servers_results.append({'name': server, 'delay': delay})

async def main():
    servers = ['Server-A', 'Server-B', 'Server-C']
    tasks = [ping_server(server, rd.uniform(0.1, 2)) for server in servers]
    await asyncio.gather(*tasks)
    fastest = min(servers_results, key=lambda x: x['delay'])
    print(f'\nFastest server: {fastest["name"]} (delay: {fastest["delay"]:.2f} сек.)')

if __name__ == '__main__':
    asyncio.run(main())
