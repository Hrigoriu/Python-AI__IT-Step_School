import json


'''
workers = [
    worker,
    worker
]

worker = {
    name: str,
    age: int
    job: str,
    skills: list[str]
}
'''


def add_worker(name: str, age: int, job: str, skills: list[str]):
    try:
        with open('files\\workers.json', 'r') as json_file:  # відкриємо на читання, щоб зберегти попередній зміст
            data = json.load(json_file)
    except FileNotFoundError:  # якщо попередньо файлу немає - створюємо порожній список
        data = []

    new_worker = {
        'name': name,
        'age': age,
        'job': job,
        'skills': skills
    }
    data.append(new_worker)

    with open('files\\workers.json', 'w') as file:
        json.dump(data, file, indent=4)


def print_workers():
    try:
        with open('files\\workers.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('Робітників немає! База порожня!')
        return

    for counter, worker in enumerate(data, start=1):
        print(f'{counter}. {worker['name']}, {worker['age']} років: ')
        print(f'\t-Місце роботи: {worker['job']};')
        print('\t-Навички: ')

        for skill in worker['skills']:
            print(f'\t\t-{skill}')


print_workers()
