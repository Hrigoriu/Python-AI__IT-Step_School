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

package(moduleA1(functionA1(), functionA2(), ...),moduleB2(functionB1(), functionB2(), ...),...)
""" 
Примітка: обидва файли повинні знаходитися в одній папці.
1.module.py
2.main.py (в середині файла написати: import module)
3. Автоматично створиться папка __pycache__
4. Всередині цієї папки є файл module.cpython-xy.pyc
x і y — це цифри, отримані з вашої версії Python
5. Пишемо в module.py 
print("I like to be a module.")

Потім пишено: 
print("I like to be a module.")
print(__name__)

Потім пишемо:
if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")

Потім пишемо:
counter = 0
   if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")
6. У файл main.py пишемо:
import module
print(module.counter)

"""

    #Рядки  string
"""
*однорядкові рядки: 'string' "string"
*багаторядкові рядки: 
'''
string
'''

"""
string
"""

"""
#----------------------
word = 'by'
print(len(word))#2

empty = ''
print(len(empty))#0

print(len("\n\n"))#2

i_am = 'I\'m'
print(len(i_am))#3

multiline = """Line #1
Line #2"""
print(len(multiline))#15
#-----------------------------------
str1 = 'a'
str2 = 'b'
print(str1 + str2)#ab
print(str2 + str1)#ba
print(5 * 'a')#aaaaa
print('b' * 4)#bbbb
#--------------------------------------
char_1 = 'a'
char_2 = ' '  # space пробіл
print(ord(char_1))#97   По системі ASCII/UNICODE
print(ord(char_2))#32   По системі ASCII/UNICODE
#------------------------------------------
""" 
chr(ord(character)) == character
ord(chr(codepoint)) == codepoint
"""
#-------------------------------------------
print(chr(97))#a    По системі ASCII/UNICODE - навпаки
print(chr(945))#α   По системі ASCII/UNICODE - навпаки
#---------------------------------------------
the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()#s i l l y   w a l k s

the_string = 'silly walks'
for ix in the_string:
    print(ix, end=' ')
print()#s i l l y   w a l k s
#--------------------------------------------------
alpha = "abdefg"
print(alpha[1:3])#bd
print(alpha[3:])#efg
print(alpha[:3])#abd
print(alpha[3:-2])#e
print(alpha[-3:4])#e
print(alpha[::2])#adf
print(alpha[1::2])#beg
#-----------------------------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)#True
print("F" in alphabet)#False
print("1" in alphabet)#False
print("ghi" in alphabet)#True
print("Xyz" in alphabet)#False

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" not in alphabet)#False
print("F" not in alphabet)#True
print("1" not in alphabet)#True
print("ghi" not in alphabet)#False
print("Xyz" not in alphabet)#True
#-------------------------------------------------------------
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)#abcdefghijklmnopqrstuvwxyz
#-------------------------------------------------------
print(min("aAbByYzZ"))#A

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')#[ ]

t = [0, 1, 2]
print(min(t))#0
#----------------------------------------------------
print(max("aAbByYzZ"))#z

t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')#[y]

t = [0, 1, 2]
print(max(t))#2
#---------------------------------------------------------
print("aAbByYzZaA".index("b"))#2
print("aAbByYzZaA".index("Z"))#7
print("aAbByYzZaA".index("A"))#1
#----------------------------------------------------
print(list("abcabc"))#['a', 'b', 'c', 'a', 'b', 'c']
#-----------------------------------------------------
            # .count()
print("abcabc".count("b"))#2
print('abcabc'.count("d"))#0

#=====================================================
            # .capitalize() змінює всі рядкові літери на великі
print("Alpha".capitalize())#Alpha
print('ALPHA'.capitalize())#Alpha
print(' Alpha'.capitalize())# alpha
print('123'.capitalize())#123
print("αβγδ".capitalize())#Αβγδ

print('[' + 'alpha'.center(10) + ']')#[  alpha   ]
print('[' + 'Beta'.center(2) + ']')#[Beta]
print('[' + 'Beta'.center(4) + ']')#[Beta]
print('[' + 'Beta'.center(6) + ']')#[ Beta ]
print('[' + 'gamma'.center(20, '*') + ']')#[*******gamma********]

#---------------------------------------------------------------------
            # .endswith()
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
#Видасть yes

t = "zeta"
print(t.endswith("a"))#True
print(t.endswith("A"))#False
print(t.endswith("et"))#False
print(t.endswith("eta"))#True
#----------------------------------------------------------
            # .startswith() є дзеркальним відображенням endswith() –
            # він перевіряє, чи починається заданий рядок із заданим підрядком
print("omega".startswith("meg"))#False
print("omega".startswith("om"))#True
#--------------------------------------------------------------------
            # .find()
print("Eta".find("ta"))#1
print("Eta".find("mma"))#-1
t = 'theta'
print(t.find('eta'))#2
print(t.find('et'))#2
print(t.find('the'))#0
print(t.find('ha'))#-1

print('kappa'.find('a', 1, 4))#1
print('kappa'.find('a', 2, 4))#-1
#--------------------------------------------------------------
            # .isalnum()    лише цифри або алфавітні символи (літери)
print('lambda30'.isalnum())#True
print('lambda'.isalnum())#True
print('30'.isalnum())#True
print('@'.isalnum())#False
print('lambda_30'.isalnum())#False
print(''.isalnum())#False
#------------------------------------------------------------------
            # .isalpha() лише літери
print("Moooo".isalpha())#True
print('Mu40'.isalpha())#False
#------------------------------------------------------------------
            # .islower() лише літери нижнього регістру
print("Moooo".islower())#False
print('moooo'.islower())#True
#------------------------------------------------------------------
            # .isdigit() лише цифри
print('2018'.isdigit())#True
print("Year2019".isdigit())#False
#-------------------------------------------------------------------
            # .isspace() лише пробіли
print(' \n '.isspace())#True
print(" ".isspace())#True
print("mooo mooo mooo".isspace())#False
#--------------------------------------------------------------------
            # .isupper()  лише лише на літерах верхнього регістру
print("Moooo".isupper())#False
print('moooo'.isupper())#False
print('MOOOO'.isupper())#True
#--------------------------------------------------------------------
            # .join() виконує об'єднання списків у рядок  list[]-->string()
print(",".join(["omicron", "pi", "rho"]))#omicron,pi,rho
#!!! якщо у списку не рядки, то буде TypeError
#... рядок, з якого був викликаний метод, використовується як роздільник, що ставиться серед рядків;
#аргумент join — це список, що містить три рядки;
#--------------------------------------------------------------------
            # .split()    розбиває рядок і будує список усіх виявлених підрядків string()-->list[]
print("phi       chi\npsi".split())#['phi', 'chi', 'psi']
#--------------------------------------------------------------------
            # .lower() замінює всі літери верхнього регістру на їх аналоги в нижньому регістрі
print("SiGmA=60".lower())#sigma=60
#--------------------------------------------------------------------
            #. lstrip()   видаляє спереді всe, що в дужках, в його аргументі (рядок)
print("[" + " tau ".lstrip() + "]")#[tau ]
print("www.cisco.com".lstrip("w."))#cisco.com
print("pythoninstitute.org".lstrip(".org"))#pythoninstitute.org
print("pythoninstitute.org".lstrip("pythoninstitute"))#.org
#--------------------------------------------------------------------
            # .rstrip()  видаляє заді всe, що в дужках, в його аргументі (рядок)
print("[" + " upsilon ".rstrip() + "]")#[ upsilon]
print("cisco.com".rstrip(".com"))#cis
#--------------------------------------------------------------------
            # .strip()  поєднує ефекти, спричинені rstrip() та lstrip() –
            # він створює новий рядок, у якому відсутні всі початкові та кінцеві пробіли
print("[" + "   aleph   ".strip() + "]")#[aleph]
#--------------------------------------------------------------------
            # .replace()  замінює, що в дужках, в його аргументі (старе на нове)
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))#www.pythoninstitute.org
print("This is it!".replace("is", "are"))#Thare are it!
print("Apple juice".replace("juice", ""))#Apple
print("This is it!".replace("is", "are", 1))#Thare is it!
print("This is it!".replace("is", "are", 2))#Thare are it!
#--------------------------------------------------------------------
            # .rfind()    починають свої пошуки з кінця рядка, а не з початку (звідси префікс r, що означає right)
print("tau tau tau".rfind("ta"))#8
print("tau tau tau".rfind("ta", 9))#-1
print("tau tau tau".rfind("ta", 3, 9))#4
#--------------------------------------------------------------------
            # .split()    розбиває рядок і будує список усіх виявлених підрядків string()-->list[]
print("phi       chi\npsi".split())#['phi', 'chi', 'psi']
#--------------------------------------------------------------------
            #swapcase() міняє символи, символи нижнього регістру стають великими літерами, і навпаки
print("I know that I know nothing.".swapcase())#i KNOW THAT i KNOW NOTHING.
#--------------------------------------------------------------------
            #title()    змінює першу літеру кожного слова на верхній регістр,
            # перетворюючи всі інші на малі.
print("I know that I know nothing. Part 1.".title())#I Know That I Know Nothing. Part 1
#--------------------------------------------------------------------
            #upper()    замінює всі літери нижнього регістру на їхні аналоги у верхньому регістрі
print("I know that I know nothing. Part 2.".upper())#I KNOW THAT I KNOW NOTHING. PART 2.
#--------------------------------------------------------------------
            #Підсумок
"""
 .capitalize() –    змінює всі рядкові літери на великі;
 .swapcase() –      міняє місцями регістри літер (нижні на верхні та навпаки)
 .title() –         робить першу літеру в кожному слові великою літерою;
 .lower() –         перетворює всі літери рядка на літери нижнього регістру;
 .upper() –         перетворює всі літери рядка на літери верхнього регістру.
 .center() –        центрує рядок всередині поля відомої довжини;
 .count() –         підраховує входження заданого символу;
 .join() –          об'єднує всі елементи кортежу/списку в один рядок;
 .lstrip() –        видаляє білі символи з початку рядка;
 .rstrip() –        видаляє кінцеві білі пробіли з кінця рядка;
 .strip() –         видаляє початкові та кінцеві білі пробіли;
 .replace() –       замінює заданий підрядок на інший;
 .rfind() –         знаходить підрядок, починаючи з кінця рядка;
 .split() –         розбиває рядок на підрядок за допомогою заданого роздільника;

 .startswith() –    чи починається рядок із заданого підрядка?
 .endswith() –      чи закінчується рядок заданим підрядком?
 .isalnum() –       рядок складається тільки з букв і цифр?
 .isalpha() –       рядок складається лише з літер?
 .islower() –       чи рядок складається лише з малих літер?
 .isupper() –       рядок складається лише з літер верхнього регістру?
 .isspace() –       чи рядок складається лише з білих пробілів?
"""
#=================================================================================
"""
== != > >= < <= 
"""
'alpha' == 'alpha'
'alpha' != 'Alpha'
'alpha' < 'alphabet'
'beta' > 'Beta'#
#Порівняння рядків завжди враховується за регістром
#(літери верхнього регістру сприймаються як менші, ніж літери нижнього регістру)
print('10' == '010')#False
print('10' > '010')#True
print('10' > '8')#False
print('20' < '8')#True
print('20' < '80')#True
#----------------------------------------------------------
          #sorted() сортує
          # .sort()
#variant#1
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)  #['omega', 'alpha', 'pi', 'gamma']
print(first_greek_2)#['alpha', 'gamma', 'omega', 'pi']
#variant#2
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)#['omega', 'alpha', 'pi', 'gamma']
second_greek.sort()
print(second_greek)#['alpha', 'gamma', 'omega', 'pi']
#------------------------------------------------------------
            #str-->int, float
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print(si + ' ' + sf)#13 1.3
#
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)
print(itg + flt)#14.3
#=============================================================================
            #Винятки
ValueError
ZeroDivisionError
IndexError
#var1
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")
print("THE END.")
#---------------------------------------------------------------
#var2
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")
print("THE END.")
"""Так саме ліпше
try:
    :
except:
    :
#-----------------------------------   
try:
    :
except exc1:
    :
except exc2:
    :
except:
    : 
#------------------------------------
try:
    :
except (exc1, exc2):
    :
#-----------------------------------
raise лише всередині except
#-----------------------------------
# The code that always runs smoothly.
:
try:
    :
    # Risky code.
    :
except:
    :
    # Crisis management takes place here.
    :
:
# Back to normal.
: 
#-------------------------------------------------
# The code that always runs smoothly.
:
try:
    :
    # Risky code.
    :
except Except_1:
    # Crisis management takes place here.
except Except_2:
    # We save the world here.
:
# Back to normal.
:
#-------------------------------------------
# The code that always runs smoothly.
:
try:
    :
    # Risky code.
    :
except Except_1:
    # Crisis management takes place here.
except Except_2:
    # We save the world here.
except:
    # All other issues fall here.
:
# Back to normal.
:   
#-----------------------------------------------------
Винятки ставити від меншого до більшого
try:
    # Risky code.
except IndexError:
    # Taking care of mistreated lists
except LookupError:
    # Dealing with other erroneous lookups
"""
#-----------------------------------------------------
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")
#--------------------------------------------
def bad_fun(n):
    raise ZeroDivisionError
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")
print("THE END.")
#---------------------------------------
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")
print("THE END.")
"""
#-----------------------------------
    raise лише всередині except
#-----------------------------------
 """
assert expression3  #коли вираз дорівнює нулю
#----------------------------------------
import math
x = float(input("Enter a number: "))
assert x >= 0.0
x = math.sqrt(x)
print(x)    #AssertionError якщо ввести <0
#----------------------------------------
""" 
           BaseException
                 ↑
     ____________|___________        
     ↑           ↑          ↑              
SystemExit  Exception KeyboardInterrupt 
                 ↑
    _____________|______________________________________________________ 
    ↑            ↑          ↑               ↑            ↑              ↑
ValueError LookupError ArithmeticError AssertionError MemoryError StandardError
               ↑            ↑                                           ↑
   ____________|_          _↑___________                                ↑
   ↑           ↑            ↑          ↑                                ↑
IndexError KeyError ZeroDivisionError OverflowError                ImportError
"""

BaseException ← KeyboardInterrupt
#користувач використовує комбінацію клавіш Ctrl-C
BaseException ← Exception ← AssertionError
#коли її аргумент має значення False, None, 0 або порожній рядок
BaseException ← Exception ← LookupError
#коли є неправильні посилання на різні колекції (списки, словники, кортежі тощо)
BaseException ← Exception ← LookupError ← IndexError
#при спробі отримати доступ до елемента неіснуючої послідовності (наприклад, елемента списку)
BaseException ← Exception ← LookupError ← KeyError
#коли ви намагаєтеся отримати доступ до неіснуючого елемента в колекції (наприклад, елемента словника)
BaseException ← Exception ← MemoryError
#коли операція не може бути завершена через брак вільної пам'яті
BaseException ← Exception ← ArithmeticError
#поділ на нуль або неприпустимий домен аргументу
BaseException ← Exception ← ArithmeticError ← OverflowError
#коли операція виробляє число, занадто велике для успішного зберігання
BaseException ← Exception ← StandardError ← ImportError
#коли операція імпорту не вдається виконати
#=============================================================
        #Об'єктно-Орієнтоване Програмування
"""       
Клас має сукупність Об'єктів
Об'єкт має атрибути(параметри) та методи(функції)
Об'єкт успадковує всі ознаки від суперкласу
Об'єкт і використовуєте:

Об'єкт має (щоб легше запам'ятати) має:
*іменник –      ви, ймовірно, визначаєте назву предмета;
*прикметник –   ви, мабуть, визначаєте властивість предмета;
*дієслово –     ви, мабуть, визначаєте діяльність предмета.
Рожевий Cadillac поїхав швидко.

Назва об'єкта = Cadillac
Home class = Колісні транспортні засоби
Властивість = Колір (рожевий)
Активність = Їхати (швидко)

A pink Cadillac went quickly.
Object name = Cadillac
Home class = Wheeled vehicles
Property = Color (pink)
Activity = Go (quickly)
#------------------------------
Рудольф – велика кішка, яка спить цілий день.
Ім'я об'єкта = Рудольф
Домашній клас = Кіт
Властивість = Розмір (великий)
Активність = Сон (весь день)

Rudolph is a large cat who sleeps all day.
Object name = Rudolph
Home class = Cat
Property = Size (large)
Activity = Sleep (all day)
"""
class TheSimplestClass: #Клас
    pass
my_first_object = TheSimplestClass()    #Об'єкт
#==========================================================

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")
stack_object = Stack()  # Instantiating the object.
#Видасть: Hi!
#------------------------------------------------------
class Stack:
    def __init__(self):
        self.stack_list = []
stack_object = Stack()
print(len(stack_object.stack_list))
#Видасть: 0
#--------------------------------------------------------
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())#1
print(stack_object.pop())#2
print(stack_object.pop())#3
#------------------------------------------------
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())
print(stack_object_2.pop())#3
#---------------------------------------------
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
#100
#------------------------------------------
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
#1
#dog
#False
#Queue error
#-----------------------------------------------------------
class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
#1
#dog
#False
#Queue empty
#------------------------------------------------------
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)#{'first': 1}
print(example_object_2.__dict__)#{'first': 2, 'second': 3}
print(example_object_3.__dict__)#{'first': 2, 'second': 3}
#--------------------------------------------------------------
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)#{'_ExampleClass__first': 1}
print(example_object_2.__dict__)#{'_ExampleClass__first': 2, '_ExampleClass__second': 3}
print(example_object_3.__dict__)#{'_ExampleClass__first': 4, '__third': 5}
#--------------------------------------------------------------------
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)#{'_ExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2.counter)#{'_ExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3.counter)#{'_ExampleClass__first': 4} 3
#------------------------------------------------------------------
class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)#{'_ExampleClass__first': 1} 3
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)#{'_ExampleClass__first': 2} 3
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)#{'_ExampleClass__first': 4} 3
#-----------------------------------------------------------------------------
class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val

print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)
#--------------------------------------------------------------
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
example_object = ExampleClass(1)
print(example_object.a)
try:
    print(example_object.b)
except AttributeError:
    pass
#Виведе: 1
#---------------------------------------------------------------
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2
example_object = ExampleClass()
print(hasattr(example_object, 'b'))#True
print(hasattr(example_object, 'a'))#True
print(hasattr(ExampleClass, 'b'))#False
print(hasattr(ExampleClass, 'a'))#True
#=======================================================================
class Classy:
    def method(self):
        print("method")
obj = Classy()
obj.method()
#method
#----------------------------------------------------------------
class Classy:
    def method(self, par):
        print("method:", par)
obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)
#method: 1
#method: 2
#method: 3
#-------------------------------------------------
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
obj = Classy()
obj.var = 3
obj.method()
#2 3
#------------------------------------------------------
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()
obj = Classy()
obj.method()
#method
#other
#------------------------------------------------------------
class Classy:
    def __init__(self, value):
        self.var = value
obj_1 = Classy("object")
print(obj_1.var)#object
#--------------------------------------------------------------
class Classy:
    def __init__(self, value = None):
        self.var = value
obj_1 = Classy("object")
obj_2 = Classy()
print(obj_1.var)#object
print(obj_2.var)#None
#-----------------------------------------------------------
class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")
obj = Classy()
obj.visible()
try:
    obj.__hidden()
except:
    print("failed")
obj._Classy__hidden()
#visible
#failed
#hidden
#------------------------------------------------------------------
class Classy:
    pass
print(Classy.__name__)#Classy
obj = Classy()
print(type(obj).__name__)#Classy
#---------------------------------------------------------------
class Classy:
    pass
print(Classy.__module__)#__main__
obj = Classy()
print(obj.__module__)#__main__
#----------------------------------------------------------------
class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls):
    print('( ', end='')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperOne)#( object )
printBases(SuperTwo)#( object )
printBases(Sub)#( SuperOne SuperTwo )
#----------------------------------------------------
class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)
print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
#{'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
#{'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}
#----------------------------------------------------------------
class Sample:
    def __init__(self):
        self.name = Sample.__name__

    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)
obj = Sample()
obj.myself()
#My name is Sample living in a __main__
#====================================================================
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

sun = Star("Sun", "Milky Way")
print(sun)#<__main__.Star object at 0x7fb67ee89a50>
#---------------------------------------------------
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):  #повертає рядок
        return self.name + ' in ' + self.galaxy
sun = Star("Sun", "Milky Way")
print(sun)#Sun in Milky Way
#--------------------------------------------------------
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
#True	False	False
#True	True	False
#True	True	True
#--------------------------------------------------------------
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
#True	False	False
#True	True	False
#True	True	True
#---------------------------------------------------------------
class SampleClass:
    def __init__(self, val):
        self.val = val

object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
#False
#False
#True
#1 2 1
#True False
#-------------------------------------------------------
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Andy")
print(obj)#My name is Andy.
#----------------------------------------------------------
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

obj = Sub("Andy")
print(obj)#My name is Andy.
#-----------------------------------------------------------
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()
print(obj.subVar)#2
print(obj.supVar)#1
#------------------------------------------------------------
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()
print(obj.subVar)#12
print(obj.supVar)#11
#--------------------------------------
class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102

class Level2(Level1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202

class Level3(Level2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302

obj = Level3()
print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
#100 101 102
#200 201 202
#300 301 302
#-----------------------------------------------------------
class SuperA:
    var_a = 10

    def fun_a(self):
        return 11

class SuperB:
    var_b = 20

    def fun_b(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()
print(obj.var_a, obj.fun_a())#10 11
print(obj.var_b, obj.fun_b())#20 21
#----------------------------------------------------
class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()
print(obj.var, obj.fun())#200 201
#--------------------------------------------------------
class Left:
    var = "L"
    var_left = "LL"

    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right = "RR"

    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass

obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())#L LL RR Left
#-------------------------------------------------------------------
class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it from Two")

one = One()
two = Two()
one.doanything()#do_it from One
two.doanything()#do_it from Two
#-------------------------------------------------
import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
#wheels:  True True
#wheels:  True False
#tracks:  False True
#tracks:  False False
#------------------------------------------------------------
                #Про успадовуваність: суперклас-->клас-->підклас
class Top:
    def m_top(self):
        print("top")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")

class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")

class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
#bottom
#middle_left
#top
#------------------------------------------------
"""
1. Метод з іменем __str__() відповідає за перетворення вмісту об'єкта 
в (більш-менш) читабельний рядок.
2. Функція з іменем issubclass(Class_1, Class_2) здатна визначити, 
чи є Class_1 підкласом Class_2. 
3. Функція з іменем isinstance(Object, Class) перевіряє, 
чи походить об'єкт з вказаного класу. 
4. Оператор is перевіряє, 
чи дві змінні посилаються на один і той самий об'єкт.
5. Безпараметрична функція з іменем super() повертає посилання 
на найближчий суперклас класу.
6. Методи, а також змінні екземпляра та класу, визначені в суперкласі, 
автоматично успадковуються їх підкласами.
7. Для того, щоб знайти будь-яку властивість об'єкта/класу, 
Python шукає її всередині:
*сам об'єкт;
*всі класи, що беруть участь у лінії успадкування об'єкту знизу вгору;
*якщо на певному шляху успадкування є більше одного класу, Python сканує їх зліва направо;
*якщо обидва з перерахованих вище не допомагають, виникає виняток AttributeError.
8. Якщо будь-який з підкласів визначає метод/змінну класу/змінну-екземпляр 
з таким же іменем, як існує в суперкласі, нове ім'я має пріоритет 
над будь-яким з попередніх екземплярів імені.
"""
#===============================================================
"""
BaseException
   +---Exception
   |   +---TypeError
   |   +---StopAsyncIteration
   |   +---StopIteration
   |   +---ImportError
   |   |   +---ModuleNotFoundError
   |   |   +---ZipImportError
   |   +---OSError
   |   |   +---ConnectionError
   |   |   |   +---BrokenPipeError
   |   |   |   +---ConnectionAbortedError
   |   |   |   +---ConnectionRefusedError
   |   |   |   +---ConnectionResetError
   |   |   +---BlockingIOError
   |   |   +---ChildProcessError
   |   |   +---FileExistsError
   |   |   +---FileNotFoundError
   |   |   +---IsADirectoryError
   |   |   +---NotADirectoryError
   |   |   +---InterruptedError
   |   |   +---PermissionError
   |   |   +---ProcessLookupError
   |   |   +---TimeoutError
   |   |   +---UnsupportedOperation
   |   |   +---ItimerError
   |   +---EOFError
   |   +---RuntimeError
   |   |   +---RecursionError
   |   |   +---NotImplementedError
   |   |   +---_DeadlockError
   |   +---NameError
   |   |   +---UnboundLocalError
   |   +---AttributeError
   |   +---SyntaxError
   |   |   +---IndentationError
   |   |   |   +---TabError
   |   +---LookupError
   |   |   +---IndexError
   |   |   +---KeyError
   |   |   +---CodecRegistryError
   |   +---ValueError
   |   |   +---UnicodeError
   |   |   |   +---UnicodeEncodeError
   |   |   |   +---UnicodeDecodeError
   |   |   |   +---UnicodeTranslateError
   |   |   +---UnsupportedOperation
   |   +---AssertionError
   |   +---ArithmeticError
   |   |   +---FloatingPointError
   |   |   +---OverflowError
   |   |   +---ZeroDivisionError
   |   +---SystemError
   |   |   +---CodecRegistryError
   |   +---ReferenceError
   |   +---MemoryError
   |   +---BufferError
   |   +---Warning
   |   |   +---UserWarning
   |   |   +---DeprecationWarning
   |   |   +---PendingDeprecationWarning
   |   |   +---SyntaxWarning
   |   |   +---RuntimeWarning
   |   |   +---FutureWarning
   |   |   +---ImportWarning
   |   |   +---UnicodeWarning
   |   |   +---BytesWarning
   |   |   +---ResourceWarning
   |   +---Error
   +---GeneratorExit
   +---SystemExit
   +---KeyboardInterrupt
"""


