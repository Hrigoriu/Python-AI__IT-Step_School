import asyncio
import aiohttp


urls = [
    'https://www.python.org',
    'https://example.com',
    'https://google.com',
    'https://httpbin.org/html'
]


async def fetch_and_save(session, url, index):
    try:
        async with session.get(url) as response:
            content = await response.text()
            file_name = f'sites\\site_{index}.html'

            with open(file_name, 'w', encoding='UTF-8') as f:
                f.write(content)

            print(f'{url} успішно збережено!')
    except Exception as exc:
        print(f'Помилка при завантаженні {url}: {exc}')


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save(session, url, index) for index, url in enumerate(urls)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
