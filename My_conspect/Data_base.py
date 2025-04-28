user_name = 'Bob'   = це присвоєння або створення змінної user_name з значенням 'Bob'
'Hello, ' + user_name + '!' # контамінація , склеювання слів , значок +
input - це ВВІД інформації в консоль

print(10 * 5)    # * -  множення
print(5 ** 3)    # ** - степінь
print(10 / 5)    # / -  ділення, покаже і після коми
print(11 // 3)   # // - цілочислене ділення - повертає тілу частку від ділення # покаже 3, нічого після коми (11/9=3)
print(10 % 3) # буде 1 (10-9=1)
print(11 % 3) # буде 2 (11-9=2)

print(text_2 + '20') #буде 1020, відбудеться склеювання, бо + для строк склеювання (contcatenate)

print(a, b, c, end='  |новий print|') # end - склеює цей рядок з наступним, тобто виведе рядок виводить -- 10 20 30  |новий print|a,b,c
print('a', 'b', 'c', sep=',') #/ виставить між аргументами коми
print('a', 'b', 'c', sep='') # sep - строка, яка ставиться МІЖ аргументами print
print('1\n2\n3\n4\n5')  # \n - перекидає на наступний абзац між аргументами
print(a, b, c, end='\n') # це по замовчуванню стоїть, але система не показує, система перекидає на новий рядок

print(number1)    # NameError - звертаємось до змінної, якої не існує
 print(number_1)   # IndentionError - зайвий абсзац або пробіл на початку рядка
print(number_1 + '!')  # TypeError - операція між різними типами даних (конфлікт типів даних)
var = 'Hi' = 5 # SyntaxError  - груба синтаксична помилка
text = 'Hello  # SyntaxError  - груба синтаксична помилка

#Типи даних
string = '10'    # str (строка) - текстовий літерал або послідовність символів
integer = 10     # int - ціле число
float_ = 10.10   # float - дробове десятичне число
boolean = True   # bool  - логічний тип даних: True(Істина, Так, 1); False(Брехня, Ні, 0)
none = None      # None  - відсутній тип даних

input() завжди повертає STR

#Перетворення
-на  str - (фактично майже завжди просто накладає лапки на об'єкт)
print(str(10) + '!')
print(str(True) + '.')
-на  int
print(int('10') + 1)
Виведе : 11
print(int('abc'))
Виведе  ValueError, бо таку строку не можна перетворити на число

int(input('Введіть число 2: ')) #- це перетворення на число int
str(sum_of_numbers) - це перетворення на строку str

# Порівняння чисел
print(20 > 10)  #True
print(20 < 10)  #False
print(20 >= 20) # більше або дорівнює
print(10 <= 20) # менше або дорівнює
print(10 == 10.0) #Виведе True #дорівнює (порівнювання, чи однакове?, нагадую, що = це присвоєння)
print(25 != 25.0) #Виведе False #не дорівнює

#Порівняння строк
print('abc' > 'ABC') #True # на > < строки порівнюються за unicode
print(ord('A')) #65
print(ord('a')) #97
print('hello' == ' hello') #False
print('hello' == 'hello')  #True
print('abc' == 'acb') #False  #== строки порівнюються на ідентичність
print('25' != '25.0')  #False

#Об'єднання порівнянь
i (and) потребує True всюди (зліва та справа)
print(True and True)   #True
print(False and False) #True
print(False and True)  #False

або (or) потребує True хоч десь
print(True or True)    #True
print(False or False)  #False
print(False or True)   #True
print(10 > 1 or 5 < 1) #True

#not - робить хибне твердження правдивим, повертає навпаки, розвертає твердження навпаки
print(not True) #False
print(not False) #True
print(not 10 >= 20) #True

Структура умови:
- 1 if:
- скільки завгодно elif (0 також): (Перевіряються по черзі)
- 0 або 1 else:

                #Умови
if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
    feed_the_sheepdogs()
===============================
if the_weather_is_good: # Якщо
    go_for_a_walk()
    have_fun()
else:                   # Якщо не виконується 1 умова, то
    go_to_a_theater()
    enjoy_the_movie()
    have_lunch()
===============================
if the_weather_is_good: # Якщо
    if nice_restaurant_is_found:
        have_lunch()
    else:               # Якщо не виконується 1 умова, то
        eat_a_sandwich()
else:                   # Якщо не виконується 1 умова, то
    if tickets_are_available:    # Якщо
        go_to_the_theater()
    else:                        # Якщо не виконується 1 умова, то
        go_shopping()
================================
if the_weather_is_good: # Якщо 1 умова
    go_for_a_walk()
elif tickets_are_available:  # Якщо 1 умова + 2 умова
    go_to_the_theater()
elif table_is_available:     # Якщо 1 умова + 2 умова + 3 умова
    go_for_lunch()
else:                  # В інших випадках
    play_chess_at_home()

            #WHILE (ПОКИ)
# ПОКИ <умова == Істина>: <код>
number = 1
while True:  #while True - нескінченний цикл
    print(number)
    number +=1
==============================
number = 1
while 10>1:  #while True - нескінченний цикл
    print(number)
    number +=1
    if number > 100_000:
        break # - вихід з циклу

        #цикл for та функція range
for i in range(10): #(перебирає від 0 до 9)
 print("Значення i зараз дорівнює", i)
================================================================
for i in range(2, 8, 3): #(перебирає від 2 до 8, з корком 3)
 print("Значення i зараз дорівнює", i)

        #функція break та continue
# приклад break
print("Інструкція break:")
for i in range(1, 6):
    if i == 3:
        break   # Зупиняє цикл і все
    print("Всередині циклу.", i)
print("За межами циклу.")
======================================
# приклад continue
print("Інструкція continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Всередині циклу.", i)
print("За межами циклу.")

"""
    Синтаксис range() має наступний вигляд: range(start, stop, step),де:
*start ‒ необов`язковий параметр, що задає початковий номер послідовності
        (за замовчуванням 0)
*stop ‒ необов`язковий параметр, що вказує на кінець згенерованої послідовності
        (не входить до складу),
*step ‒ необов`язковий параметр, що задає крок інтервалу між числами в послідовності
        (за замовчуванням ‒ 1).
"""
Ітерація - це повторення одного порядку дій через якусь послідовність.
_iterable - властивість об'єктів, що дозволяють їм ітеруватись
for char in text:  # ітерація строки (str)
    print(char)

n = int(input('Введіть число: '))
for n in range(1, n+1):  # range не включає останнє число
    print(n, '#' * n)

n = int(input('Введіть число: '))
for n in reversed(range(1, n+1)):  # range не включає останнє число
    print(n, '#' * n)

abs() Функція повертає додатній результат, навіть якщо різниця від'ємна.

    Функція: max() , min()
# Зчитайте три числа
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
number3 = int(input("Введіть третє число: "))
# Перевір, яке з чисел найбільше
# і передайте його largest_number variable.
largest_number = max(number1, number2, number3)
small_number = min(number1, number2, number3)
# Виведіть результат
print("Найбільше число це:", largest_number)
print("Найбільше число це:", small_number)

print(3E8) #Виведе: 100000000.0
print(0.0000000000000000000001) #Виведе: 1e-22

    Функція round(number, int), int округлить до числа після коми
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "миль це", round(miles_to_kilometers, 2), "кілометрів")
print(kilometers, "кілометрів це", round(kilometers_to_miles, 2), "миль")

""" 
    Комп`ютерна логіка
Різниця в роботі логічних і бітових операторів важлива: 
логічні оператори не проникають на бітовий рівень свого аргументу. 
Їх цікавить лише кінцеве ціле число.
    Логічні оператори
Оператор логічної кон`юнкції у мові Python є слово and
Оператор логічної диз`юнкції у мові Python є слово or
унарний оператор not
    Побітові оператори
& (амперсанд) ‒ побітова кон'юнкція;
| (риска) ‒     побітова диз'юнкція;
~ (тильда) ‒    побітове заперечення;
^ ( каретка ) ‒ побітове виключення або (xor).
& потрібно рівно дві 1,         щоб отримати в результаті 1;
| повинна мати хоча б одну 1,   щоб отримати в результаті 1;
^ повинна мати тільки одну 1,   щоб отримати в результаті 1;
Додамо важливе зауваження: аргументи цих операторів повинні бути цілими числами int,
тут не можна використовувати оператори з рухомою крапкою (float).
"""

    #Функція len()
length - довжина
len() - перевіряє поточну довжину списку [1, 2.0, 'dog'],
n = [1, 2.0, 'dog']
print(len(n))
# Видалення другого елементу зі списку, по індексу
del numbers[1]

Стандартний виклик функції може виглядати таким чином:
result = function(arg)
result = data.method(arg)
#Новий елемент можна додати до кінця існуючого списку
list.append(value)
#Новий елемент можна додати в будь-яке місце списку, а не тільки в кінець.
list.insert(location, value)
===============================
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
4
[111, 7, 2, 1]
###
numbers.append(4)
print(len(numbers))
print(numbers)
5
[111, 7, 2, 1, 4]
###
numbers.insert(0, 222)
print(len(numbers))
print(numbers)
6
[222, 111, 7, 2, 1, 4]
===========================
my_list = [] # Створення порожнього списку.
for i in range(5):
    my_list.append(i + 1)
print(my_list)
[1, 2, 3, 4, 5]
###
my_list = []  # Створення порожнього списку.
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)
[5, 4, 3, 2, 1]
### Заміна місцями аргументів по індексу
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)
[5, 3, 8, 1, 10]

    #list() Списки
*Сортування:
-sort()
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)   #[2, 4, 6, 8, 10]
-reverse()
lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)  #  [4, 2, 1, 3, 5]

*Зріз
my_list[start:end]  від start до end - 1
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list) # [8, 6]
=========================
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) # [8, 6, 4]

#my_list[start:] == my_list[start:len(my_list)]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list  # [4, 2]
# del
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) #[10, 4, 2]


    ##Функції
def function_name():
    function_body
------------------------------------
def message():
    print("Введіть значення: ")
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
-------------------------------------
def hello(name):  # визначення функції
    print("Привіт,", name)  # тіло функції
name = input("Введіть своє ім'я: ")
hello(name)  # виклик функції


def message(what, number):
    print("Введіть", what, "число", number)
message("в телефоні", 11)
message("на ціннику", 5)
message("число", "число")

def introduction(first_name, last_name):
    print("Привіт, мене звати", first_name, last_name)
introduction("Люк", "Скайвокер")
introduction("Джессі", "Уілсон")
introduction("Кларк", "Кент")

def introduction(first_name="Джон", last_name="Сміт"):
    print("Привіт, мене звати", first_name, last_name)
introduction()
-------------------------------------------------------------
def my_function(a, b, c):
    print(a, b, c)
my_function(1, 2, 3)

def address(street, city, postal_code):
    print("Ваша адреса: ", postal_code, ", м. ", city, ", вул. ", street, sep = '')
s = input("Вулиця: ")
p_c = input("Поштовий індекс: ")
c = input("місто: ")
address(s, c, p_c)


def subtra(a, b):
    print(a - b)
subtra(5, b=2)  # виведе: 3
subtra(a=5, 2)  # Syntax Error

def add_numbers(a, b=2, c):
    print(a + b + c)
add_numbers(a=1, c=3)  # Syntax Error
-------------------------------------------------------------

def intro(a="Джеймс Бонд", b="Бонд"):
    print("Мене звати", b + ".", a + ".")
intro() # Мене звати Бонд. Джеймс Бонд.
===============================================================

    #Функція return
def happy_new_year(wishes=True):
    print("Три...")
    print("Два...")
    print("Один...")
    if not wishes:
        return
    print("Щасливого Нового року!")
happy_new_year()
"""
Цей урок цікавий!
Режим нудьги' УВІМКНЕНО.
Цей урок нудний...
"""

def boring_function():
    return 123
x = boring_function()
print("Функція boring_function повернула свій результат. Він:", x)
      #Функція boring_function повернула свій результат. Він: 123

def boring_function():
    return 'boy'
#x = boring_function()
print("Функція boring_function повернула свій результат. Він:", boring_function())
      #Функція boring_function повернула свій результат. Він: boy


def multiply(a, b):
    return a * b
print(multiply(3, 4))  # виведе: 12

def multiply(a, b):
    return
print(multiply(3, 4))  # виведе: None


# приклад 1
def wishes():
    print("Мої побажання")
    return "З Днем народження"
wishes()  # виведе: Мої побажання

# приклад 2
def wishes():
    print("Мої побажання")
    return "З Днем народження"
print(wishes())
# виведе:   Мої побажання
#           З Днем народження
-------------------------------------------------------------------
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print(list_sum([5, 4, 3]))  #12

def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
print(strange_list_fun(5))  #[4, 3, 2, 1, 0]

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end="---")
print() #2---3---5---7---11---13---17---19---


def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))    #[1, 4, 9, 16, 25]
-------------------------------------------------

    #global
def my_function():
    print("Чи знаю я цю змінну?", var)
var = 1
my_function()
print(var)
"""
Видасть:
Чи знаю я цю змінну? 1
1
"""

def my_function():
   global var       # слово global робить змінну і всередині та зовні однаковою
   var = 2
   print("Чи знаю я цю змінну?", var)
var = 1
my_function()
print(var)
"""
Видасть:
Чи знаю я цю змінну? 2
2
"""
========================================================================

def bmi(weight, height):
    return weight / height ** 2
print(bmi(92.4, 1.82))  #27.895181741335588

def lb_to_kg(lb):
    return lb * 0.45359237  # 1 фунт = 0.45359237 кг
print(lb_to_kg(1))

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254  # 1 фут = 0.3048 м, 1 дюйм = 2.54 см = 0.0254 м
print(ft_and_inch_to_m(1, 1))


def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254
def lb_to_kg(lb):
    return lb * 0.4535923
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7))) #27.56520982857069


def is_a_triangle(a, b, c): #Чи можна побудувати трикутник?
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
print(is_a_triangle(1, 1, 1))   #True
print(is_a_triangle(1, 1, 3))   #False

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


def is_a_triangle(a, b, c): # теоремa Піфагора c2 = a2 + b2
    return a + b > c and b + c > a and c + a > b
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        if a > b and a > c:
            return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
print(area_of_triangle(1., 1., 2. ** .5))

    ##Рекурсія##
#Рекурсія це техніка, в якій функція викликає сама себе.
#числа Фібоначчі Fibi = Fibi-1 + Fibi-2
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
n = int(input('Введіть число: '))
print(n, "->", factorial_function(n))


# Рекурсивна реалізація функції факторіала.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input('Введіть число: '))
print(factorial(n))  # n = 5/ 5 * 4 * 3 * 2 * 1 = 120
======================================================

            #Список це тип змінної послідовності
    empty_list = []
list_1 = [1, 2, 4, 8]
print(list_1)
my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)
-------------------------------------------------------------------------
            #Кортеж це тип незмінної послідовності
    empty_tuple = ()
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_tuple_1 = 1,
print(type(my_tuple_1))     # виведе: <class 'tuple'>
my_tuple_2 = 1              # Це не кортеж.
print(type(my_tuple_2))     # виведе: <class 'int'>

my_list = ["машина", "Форд", "квітка", "Тюльпан"]   #Список
t = tuple(my_list)  #Перетворює список в кортеж
print(t)            #('машина', 'Форд', 'квітка', 'Тюльпан')

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
print(tuple_1)
print(tuple_2)
"""
Кортеж - Ви не зможете ні додати до нього елемент, ні вилучити 
з нього будь-який елемент. Це означає, що додавання елемента 
в кінець списку вимагатиме створення нового списку з нуля.
"""

my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3
print(len(t2))  #9
print(t1)       #(1, 10, 100, 1000, 10000)
print(t2)       #(1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple)       #True
print(-10 not in my_tuple)  #True

my_tuple = (1, 2.0, "string", [3, 4], (5,), True)
print(my_tuple[3])  # виведе: [3, 4]

---------------------------------------------------------------------------
            #Словник це тип змінної впорядкованої послідовності
            #Cловник — це набір пар ключ-значення
dictionary = {'key1': 'item1', 'key2': 'item2', 'key3': 'item3'}

my_dictionary = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)     #Перетворює кортеж в словник
print(colors_dictionary)             #{'green': '#008000', 'blue': '#0000FF'}

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']    #list
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
else:
    print(word, "немає в словнику")
"""
cat -> chat
lion немає в словнику
horse -> cheval
"""

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key in dictionary.keys():
    print(key, "->", dictionary[key])
"""
cat -> chat
dog -> chien
horse -> cheval
"""

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for english, french in dictionary.items():
    print(english, "->", french)
"""
cat -> chat
dog -> chien
horse -> cheval
"""

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.update({"duck": "canard"})
print(dictionary)   #{'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'duck': 'canard'}

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
del dictionary['dog']
print(dictionary)   #{'cat': 'chat', 'horse': 'cheval'}

ukr_eng_dictionary = {"квітка": "flower"}
ukr_eng_dictionary.update({"ґрунт": "soil"})    #додає ключ:значення
print(ukr_eng_dictionary)  # виведе: {'квітка': 'flower', 'ґрунт': 'soil'}
ukr_eng_dictionary.popitem()    #Видаляє останній ключ:значення
print(ukr_eng_dictionary)  # виведе: {'квітка': 'flower'}

school_class = {}
while True:
    name = input("Введіть ім'я студента: ")
    if name == '':
        break
    score = int(input("Введіть оцінку студента (0-10): "))
    if score not in range(0, 11):
        break
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)


    #Помилки - Винятки#
#  У світі Python існує правило, яке звучить так:
# "Краще просити вибачення, ніж просити дозволу".
# "Краще виправити помилку, коли вона сталася, ніж намагатися її уникнути"

try:
  value = int(input('Введіть натуральне число: '))
  print('Обернене число для', value, 'дорівнює', 1/value)
except:
  print('Я не знаю, що робити.')
--------------------------------------------------------
try:
  value = int(input('Введіть натуральне число: '))
  print('Обернене число для', value, 'дорівнює', 1/value)
except ValueError:
  print('Я не знаю, що робити.')
except ZeroDivisionError:
  print('Ділення на нуль у нашому Всесвіті не допускається.')
#кількість except не обмежена
------------------------------------------------------------
try:
  value = int(input('Введіть натуральне число: '))
  print('Обернене число для', value, 'дорівнює', 1/value)
except ValueError:
  print('Я не знаю, що робити.')
except ZeroDivisionError:
  print('Ділення на нуль у нашому Всесвіті не допускається.')
except:
  print('Тут сталося щось дивне... Вибачте!')
        #except за замовчуванням (тобто такий, що не має назви)
        #           повинна бути останньою гілкою except. Завжди!
        #           Cлід розміщувати в нижній гілці
"""
ZeroDivisionError
/, //, and % на 0
print(1/0)
TypeError
коли ви намагаєтесь застосувати дані, тип яких не відповідає поточному контексту
AttributeError
коли ви намагаєтеся активувати метод, який не існує в об'єкті, з яким ви взаємодієте
SyntaxError
коли елемент управління доходить до рядка коду, 
в якому порушується граматика мови Python
print("Привіт, Світ!)
"""
while True:
    try:
        number = int(input("Введіть ціле число: "))
        print(5 / number)
        break
    except (ValueError, ZeroDivisionError):
        print("Неправильне значення або порушено правило ділення на нуль.")
    except:
        print("Вибачте, щось пішло не так...")

#=======================================================================================
        #import#
import math
import sys

import math, sys

import math
print(math.sin(math.pi/2))  #1.0

import math
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
pi = 3.14
print(sin(pi/2))            #0.99999999
print(math.sin(math.pi/2))  #1.0

from math import sin, pi
print(sin(pi/2))    #1.0

from module import *    #* - означає, що імпортує всі модулі по типу sin, pi, ...
#Така інструкція імпортує всі сутності з вказаного модуля.

"""
Можна змінити назву модуля як тобі подобається за допомогою --as--
після успішного виконання імпорту псевдоніма оригінальне ім'я модуля 
стає недоступним і не повинно використовуватися.
"""
import module as alias

import math as m
print(m.sin(m.pi / 2))

from module import name as alias
from module import n as a, m as b, o as c

from math import pi as PI, sin as sine
print(sine(PI / 2))

dir(module)
#Функція повертає відсортований за алфавітом список,
#що містить всі доступні в модулі імена сутностей,
#ідентифіковані іменем, переданим у функцію як аргумент:

import math
dir(math)

from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar = radians(ad)
ad = degrees(ar)
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

random()
#генерує псевдовипадкові числа
seed()
#здатна безпосередньо встановлювати початкове число генератора
#встановлює seed з поточним часом
seed(int_value)
#встановлює seed з цілочисельним значенням int_value

from random import random, seed
seed(0)
for i in range(5):
    print(random())

#Якщо вам потрібні цілі випадкові значення,
#краще підійде одна з наступних функцій:
randrange(end)
randrange(beg, end)
randrange(beg, end, step)
randint(left, right)

#Перші три виклики згенерують ціле число,
#взяте (псевдовипадково) з діапазону (відповідно):
range(end)
range(beg, end)
range(beg, end, step)

from random import randint
for i in range(10):
    print(randint(1, 10), end=',')

choice(sequence)
#вибирає «випадковий» елемент з вхідної послідовності і повертає його
sample(sequence, elements_to_choose)
#будує список (зразок), що складається з elements_to_choose елемента,
#«намальованого» з вхідної послідовності

from random import choice, sample
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))
"""
4
[3, 1, 8, 9, 10]
[10, 8, 5, 1, 6, 4, 3, 9, 7, 2]
"""

platform()
#дозволяє отримати доступ до даних базової платформи,
#тобто до інформації про версію апаратного забезпечення,
#операційної системи та інтерпретатора.

from platform import platform
print(platform())   #Windows-11-10.0.22631-SP0
print(platform(1))  #Windows-11-10.0.22631-SP0
print(platform(0, 1))   #Windows-11

machine()
#ім'я процесора, який запускає вашу ОС разом із Python
from platform import machine
print(machine())    #AMD64

processor()
#повертає рядок, заповнений справжнім іменем процесора
from platform import processor
print(processor())  #Intel64 Family 6 Model 140 Stepping 1, GenuineIntel

system()
#повертає загальне ім'я ОС у вигляді рядка
from platform import system
print(system()) #Windows

version()
#Версія ОС у вигляді рядка
from platform import version
print(version())    #10.0.22631

python_implementation() #повертає рядок, що позначає реалізацію Python

python_version_tuple()
"""
повертає кортеж із трьох елементів, заповнений:
основна частина версії Python;
другорядна частина;
номер рівня патча.
"""
from platform import python_implementation, python_version_tuple
print(python_implementation())  #CPython
print(python_version_tuple())   #('3', '13', '3')
for atr in python_version_tuple():
    print(atr)
#3
#13
#3


