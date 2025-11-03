# Словники

'''
Ключ(key) - унікальний ідентифікатор, що вказує на значення
Значення(value) - значення ключа
Пара(item) - один елемент словнику (ключ-значення)
'''

# 1. Створення словнику
user = {
    'login': 'admin',
    'password': 'qwerty123',
    'age': 27,
    'name': 'Bob'
}  # item = key: value

# 2. Робота з ключами
print(user['name'])  # отримання значення за ключем

user['job'] = 'Google inc.'  # створення нової пари (user[key] = value)
user['name'] = 'Alice'  # перезапис ключа з новим значенням

del user['job']  # видалення пари по ключу

# 3. Методи словнику
# 3. 1. Розширення
user.update(name='John', country='Ukraine', age=20)  # оновлення/створення ключів
user.setdefault('new_key', 'new_value')  # якщо ключ існує - 0 реакції. Якщо не існує - створюється з значенням default

# 3. 2. Отримання
delete_value = user.pop('new_key')  # видаляє пару по ключу
print(delete_value)  # назад повертає видалене значення

delete_item = user.popitem()  # видаляє останню пару, повернувши кортеж (key, value)
print(delete_item[0], delete_item[1])  # 0 індекс - ключ, 1 індекс - значення

print(user.get('name', 'Ключа не існує!'))  # отримує значення ключа, якщо він існує
print(user.get('country', 'Ключа не існує!'))  # якщо ключа немає - повертає default

'''
Метод замінює конструкцію:

if key in dict:
    print(dict[key])
else:
    print("Ключа не існує!")
'''

# 3. 3. Стандартні методи
# user.clear()  # no comments
user_copy = user.copy()  # те саме, що і у list

# 4. Ітерація
for el in user:  # при будь-якій звичайній ітерації словник повертає ЛИШЕ КЛЮЧІ
    print(el)

print('==============')

for el in user.values():  # ітерація тільки значень
    print(el)

print('==============')
for key, value in user.items():  # ітерація пар (повертає кортеж(key, value))
    print(f'{key}: {value}')

# 5. Сортування
humans = {
    'Bob': 20,
    'Qwerty': 13,
    'John': 25,
    'Vi': 31,
    'Johann': 37
}  # {ім'я: вік}

sorted_name = dict(sorted(humans.items(), key=lambda el: len(el[0])))  # 0 ключ
sorted_age = dict(sorted(humans.items(), key=lambda el: el[1]))  # 1 значення

print(sorted_name)
print(sorted_age)
