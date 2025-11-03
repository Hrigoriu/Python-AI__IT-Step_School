import sqlite3

name = 'Alica'
age = 25

# name = 'John'
# age = 31
"""
1. Створюємо підключення до бази (connection)
2. Створюємо з підключення курсор (cursor)
3. За допомогою методів курсору витягуємо інформацію та робимо запити
4. Закриваємо connection
"""

connection = sqlite3.connect('files/db.sl3')   #Або відкриває або створює
cursor = connection.cursor()    # з підключення повертає курсор для роботи з БД

cursor.execute('''
    CREATE TABLE IF NOT EXISTS humans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER)
''')    # Завдання: спробувати позбутися, коли таблиця вже існує

cursor.execute("INSERT INTO humans (name, age) VALUES ('Bob', 25)")
#cursor.execute(f"INSERT INTO humans (name, age) VALUES ('{name}', {age})")
#cursor.execute('INSERT INTO humans (name, age) VALUES (?, ?)', ('John',62))
#connection.commit() #commit фіксує зміни в базі даних
cursor.execute('SELECT * FROM humans')
data = cursor.fetchall()    # витягує результат селектів, які були зроблені в execute
print(data)
connection.close()
print('Інформація з БД (1-й варіант):')
for row in data:
    print(row)

print('Інформація з БД (2-й варіант):')
for human_id, human_name, human_age in data:
    print(f'{human_id}. Імя:{human_name}, вік: {human_age}')
#=========================================================================
