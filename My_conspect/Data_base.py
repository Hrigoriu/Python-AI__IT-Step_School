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
#=============================================================
            #Ітератор#
"""            
__iter__() викликається один раз при створенні ітератора 
            і повертає сам об'єкт ітератора;
__next__() викликається для надання значення наступної ітерації 
    та викликає виняток StopIteration, коли ітерація добігає кінця.
"""
#-----------------------------------------------------
       #Генератори дуже часто називають ітераторами
for i in range(5):
print(i)
#---------------------------------------------------
def fun(n):
    for i in range(n):
        yield i
for v in fun(5):
    print(v)
"""
0
1
2
3
4
"""
#-------------------------------------------------------
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
for v in powers_of_2(8):
    print(v)
#-------------------------------------------------------------
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
t = list(powers_of_2(3))
print(t)#[1, 2, 4]
#----------------------------------------------------
list_1 = []
for ex in range(6):
    list_1.append(10 ** ex)
list_2 = [10 ** ex for ex in range(6)]
print(list_1)#[1, 10, 100, 1000, 10000, 100000]
print(list_2)#[1, 10, 100, 1000, 10000, 100000]
#----------------------------------------------------
the_list = []
for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)
print(the_list)#[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#----------------------------------------------------
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list)#[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#-----------------------------------------------
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
for v in the_list:
    print(v, end=" ")
print()#1 0 1 0 1 0 1 0 1 0

for v in the_generator:
    print(v, end=" ")
print()#1 0 1 0 1 0 1 0 1 0
#---------------------------------------------------
        #Лямбда-функція – це функція без назви
        # (її також можна назвати анонімною функцією)
"""
Лямбда-функція – це інструмент для створення анонімних функцій.
Ви можете назвати таку функцію, якщо вам дійсно потрібно, 
але, насправді, в багатьох випадках лямбда-функція 
може існувати і працювати, залишаючись при цьому повністю інкогніто.
"""
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
"""
4 4
1 1
0 0
1 1
4 4
"""
#--------------------------------------------------------
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')
print_function([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)
"""
f(-2)=18
f(-1)=8
f(0)=2
f(1)=0
f(2)=2
"""
#--------------------------------------------------------
map(function, list)
"""
Функція map(fun, list) створює копію аргументу list і застосовує функцію fun
до всіх його елементів, повертаючи генератор, який надає новий елемент вмісту списку.
"""
#--------------------------------------
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)#['Mython', 'Python', 'Fall', 'On', 'The', 'Floor']
#--------------------------------------
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)
for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
#[1, 2, 4, 8, 16]
#1 4 16 64 256
#-------------------------------------
        #filter (fun, list)
"""
Функція filter (fun, list) створює копію тих елементів списку, 
які змушують функцію fun повертати True. Результатом функції є генератор, 
який елемент за елементом надає новий контент списку.
"""
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)#['Python', 'Monty']
#-------------------------------------
from random import seed, randint
seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)#[8, 3, 5, -2, -6]
print(filtered)#[8]
#----------------------------------------
def outer(par):
    loc = par
    def inner():
        return loc
    return inner
var = 1
fun = outer(var)
print(fun())#1
#-----------------------------------------
            #Замикання# A closure
"""
Замикання - це техніка, яка дозволяє зберігати значення, 
незважаючи на те, що контексту, в якому вони були створені, більше не існує. 
"""
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]
    def inner(str):
        return tg + str + tg2
    return inner
b_tag = tag('<b>')
print(b_tag('Monty Python'))#<b>Monty Python</b>
#--------------------------------------------------------
def make_closure(par):
    loc = par
    def power(p):
        return p ** loc
    return power
fsqr = make_closure(2)
fcub = make_closure(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))
"""
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
"""
#===============================================================
        ##Доступ до файлів#
"""
#Windows
C:\directory\file
name = "\\dir\\file"
name = "/dir/file"
name = "c:/dir/file"
#Linux
/directory/files
name = "/dir/file"
"""
"""
На потоці виконуються дві основні операції:

*read зчитування з потоку: частини даних витягуються з файлу 
і поміщаються в область пам'яті, керовану програмою (наприклад, змінну);
*write запис у потік: у файл передаються частини даних з пам'яті (наприклад, змінна).

Для відкриття потоку використовуються три основні режими:
*read mode: Режим читання: потік, відкритий у цьому режимі, 
    дозволяє лише операції зчитування; спроба запису в потік викличе виняток 
    (виняток називається UnsupportedOperation, 
    який успадковує OSError і ValueError, і походить з модуля io);
write mode: Режим запису: потік, відкритий у цьому режимі, 
    дозволяє лише операції запису; спроба прочитати потік викличе виняток, 
    згаданий вище;
update mode:Режим оновлення: Відкритий у цьому режимі 
    потік дозволяє як записувати, так і читати.
"""
open(file_name, mode=open_mode, encoding=text_encoding)
stream = open(file, mode = 'r', encoding = None)
"""
*назва функції (open) говорить сама за себе; 
якщо відкриття пройшло успішно, функція повертає об'єкт потоку; 
в іншому випадку виникає виняток 
(наприклад, FileNotFoundError, якщо файл, який ви збираєтеся читати, не існує);
*перший параметр функції (file) вказує ім'я файлу, який буде пов'язаний з потоком;
*другий параметр (mode) визначає режим відкритості, який використовується для потоку; це рядок, заповнений послідовністю символів, і кожен з них має своє особливе значення (докладніше пізніше);
*третій параметр (кодування) визначає тип кодування 
(наприклад, UTF-8 при роботі з текстовими файлами)
"""
#r  Відкритий режим: читання (read)
#w  Відкритий режим: запис (write)
#a  Відкритий режим: додати (append)
#r+ Відкритий режим: читання та оновлення (read and update)
#w+ Відкритий режим: запис і оновлення (write and update)
"""
Якщо рядок режиму закінчується на букву b, 
це означає, що потік повинен бути відкритий в двійковому режимі.
Якщо рядок режиму закінчується на букву t, 
це означає, що потік відкривається в текстовому режимі.
"""
#------------------------------------------------------
try:
    stream = open("C:\Users\User\Desktopile.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
#-----------------------------------------------------------
import sys
    #Потоки
    #*sys.stdin зазвичай пов'язаний з клавіатурою
#Відома функція input() за замовчуванням зчитує дані зі Stdin
    #*sys.stdout зазвичай пов'язаний з екраном
#Відома функція print() виводить дані в потік stdout.
    #*sys.stderr зазвичай пов'язаний з екраном
#як стандартний вивід помилок
    #*stream.close() закриття потоку
"""    
errno.EACCES →  Permission denied
errno.EBADF →   Bad file number
errno.EEXIST →  File exists
errno.EFBIG →   File too large
errno.EISDIR →  Is a directory
errno.EMFILE →  Too many open files
errno.ENOENT →  No such file or directory
errno.ENOSPC →  No space left on device
"""
import errno
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
#The file doesn't exist.
#--------------------------------------------------------
from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
#The file could not be opened: No such file or directory
#=============================================================
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
#----------------------------------------------------------
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
#-----------------------------------------------------------
        #readline() прочитати повний рядок тексту з файлу
from os import strerror
try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file:     ", line_counter)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
#--------------------------------------------------------
        #readlines() прочитати весь вміст файлу та
            # повертає список рядків, по одному елементу на рядок файлу
from os import strerror
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
#-------------------------------------------------------------------
from os import strerror
try:
    ccnt = lcnt = 0
    for line in open('text.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
#----------------------------------------------------------------
        #write() очікує лише один аргумент – рядок, який буде передано у відкритий файл
from os import strerror
try:
    file = open('newtext.txt', 'wt')
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
#--------------------------------------------------------
        #bytearray() це масив, що містить (аморфні) байти
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 - i
for b in data:
    print(hex(b))
"""
0xa
0x9
0x8
0x7
0x6
0x5
0x4
0x3
0x2
0x1
"""
        #readinto()
#метод повертає кількість успішно прочитаних байтів
#метод намагається заповнити весь доступний простір всередині його аргументу
from os import strerror
data = bytearray(10)
try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
#------------------------------------------------------------------
"""
1. Для зчитування вмісту файлу можна використовувати такі методи потоку
read(number) –      зчитує числові символи/байти з файлу та повертає їх у вигляді рядка; вміє читати весь файл відразу;
readline() –        читає один рядок з текстового файлу;
readlines(number) – зчитує числові рядки з текстового файлу; вміє читати всі рядки відразу;
readinto(bytearray) – зчитує байти з файлу та заповнює ними масив байтів;
2. Для запису нового контенту у файл можна використовувати такі методи потоку:
write(string) –     записує рядок у текстовий файл;
write(bytearray) –  записує всі байти bytearray у файл
3. Метод open() повертає ітерабельний об'єкт, 
який можна використовувати для перебору всіх рядків файлу всередині циклу for. 
"""
#============================================================
    # Модуль os - дозволяє взаємодіяти з операційною системою
"""
uname - повертає об'єкт, який містить інформацію про поточну операційну систему
systemname — зберігає ім'я операційної системи;
nodename — зберігає ім'я машини у мережі;
release — зберігає реліз операційної системи;
version — зберігає версію операційної системи;
machine — зберігає ідентифікатор обладнання, наприклад, x86_64.
name - дозволяє розрізняти операційну систему:
    posix (ви отримаєте це ім'я, якщо використовуєте Unix)
    nt (ви отримаєте це ім'я, якщо використовуєте Windows)
    java (ви отримаєте це ім'я, якщо ваш код написаний на чомусь на кшталт Jython)
"""
"""
mkdir - функція, яка дозволяє створити директорію
chmod - змінює права доступу до каталогу
listdir - повертає список, що містить імена файлів і каталогів, 
        які знаходяться в шляху, переданому як аргумент
getcwd - показує в якій ти директорії
rmdir - функція, яка дозволяє видалити окремий каталог
removedirs - функція, яка дозволяє видалити каталог та його підкаталоги
my_first_directory — це відносний шлях, який створить 
    директорію my_first_directory у поточній робочій директорії;
./my_first_directory — це відносний шлях, який явно вказує 
    на поточну робочу директорію. Він має той самий ефект, що й наведений вище шлях;
.. /my_first_directory — це відносний шлях, який створить 
    my_first_directory директорію у батьківському каталозі поточної робочої директорії;
/python/my_first_directory — це абсолютний шлях, який створить 
    директорію my_first_directory, яка в свою чергу знаходиться 
    в директорії python в кореневій директорії.
"""
import os
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
#--------------------------------------------------------
import os
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
#---------------------------------------------------
import os
os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())
#-------------------------------------------------
import os
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())
#-------------------------------------------------
import os
returned_value = os.system("mkdir my_first_directory")
print(returned_value)
#===================================================================
        # datetime -робота з датою і часом
#Клас date - дата, що складається з року, місяця і дня
from datetime import date

today = date.today()
print("Today:", today)      #Today: 2025-05-31
print("Year:", today.year)  #Year: 2025
print("Month:", today.month)#Month: 5
print("Day:", today.day)    #Day: 31
#-----------------------------------------------
"""
В Unix часова позначка виражає кількість секунд 
з 00:00:00 (UTC) з 1 січня 1970 року. 
Цю дату називають епохою Unix, тому що саме тоді 
почався відлік часу в системах Unix.
"""
#------------------------------------------------
""" 
time() - функція, пов'язана з часом
fromtimestamp() - часова позначка Unix
    # - яка повертає кількість секунд
    # з 1 січня 1970 року до поточного моменту
    # у вигляді числа з плаваючою комою
fromisoformat() - бере дату в форматі РРРР-ММ-ДД,
                # що відповідає стандарту ISO 8601
replace() - якщо потрібно замінити рік, місяць або день на інше значення
weekday() - повертає день тижня у вигляді цілого числа, 
          де 0 — понеділок, а 6 — неділя
isoweekday - повертає день тижня як ціле число, 
          але 1 — це понеділок, а 7 — неділя     
time(hour, minute, second, microsecond, tzinfo, fold)
представляє час          
ctime() - перетворює час у секундах з 1 січня 1970 року (епоха Unix) у рядок     
datetime() - дата і час можуть бути представлені як окремі об'єкти, 
            так і як один об'єкт          
datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)          
today() — повертає поточну локальну дату та час з атрибутом tzinfo, 
            встановленим у значення None.;
now() — повертає поточну локальну дату та час так само, як і метод today, 
        якщо ми не передаємо йому необов'язковий аргумент tz. 
        Аргументом цього методу повинен бути об'єкт підкласу tzinfo;
utcnow() — повертає поточну дату та час UTC зі встановленим атрибутом 
        tzinfo у значення None.          
timestamp() - часова позначка          
         повертає число з плаваючою точкою, що виражає кількість секунд, 
         що минули між датою та часом, вказаними об'єктом datetime, 
         і 1 січня 1970 року, 00:00:00 (UTC)      
strftime() - дозволяє нам повернути дату і час у вказаному нами форматі        
timedelta() - це метод для віднімання об'єктів date або datetime 
sleep() - призупиняє виконання команди print на задану кількість секунд                   
"""
#--------------------------------------------
from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)      #Timestamp: 1748682665.7633297
d = date.fromtimestamp(timestamp)
print("Date:", d)                   #Date: 2025-05-31
#-------------------------------------------------
from datetime import date

d = date(1991, 2, 5)
print(d)    #1991-02-05
d = d.replace(year=1992, month=1, day=16)
print(d)    #1992-01-16
#------------------------------------------------
from datetime import date

d = date(2019, 11, 4)
print(d.weekday())#0
#------------------------------------------------
from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())#1
#------------------------------------------------
from datetime import time

t = time(14, 53, 20, 1)
print("Time:", t)                   #Time: 14:53:20.000001
print("Hour:", t.hour)              #Hour: 14
print("Minute:", t.minute)          #Minute: 53
print("Second:", t.second)          #Second: 20
print("Microsecond:", t.microsecond)#Microsecond: 1
#------------------------------------------------
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")
student = Student()
student.take_nap(5)
"""
I'm very tired. I have to take a nap. See you later.
5 сек затримка
I slept well! I feel great!
"""
#------------------------------------------------
from datetime import datetime

print("today:", datetime.today())   #today:  2025-05-31 12:10:55.801230
print("now:", datetime.now())       #now:    2025-05-31 12:10:55.803666
print("utcnow:", datetime.utcnow()) #utcnow: 2025-05-31 12:10:55.804528
#---------------------------------------------
from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())  ##Timestamp: 1601823300.0
#----------------------------------------------------------------
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))   #2020/01/04
#-----------------------------------------------------------------
from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))   #14:53:00

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S")) #20/November/04 14:53:00
#-------------------------------------------------------------------
from datetime import date
from datetime import datetime
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)  #366 days, 0:00:00

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)    #365 days, 9:07:00
#---------------------------------------------------------------
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)    #16 days, 3:00:00
#--------------------------------------------------
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)                  #Days: 16
print("Seconds:", delta.seconds)            #Seconds: 10800
print("Microseconds:", delta.microseconds)  #Microseconds: 0
#----------------------------------------------
from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)    #16 days, 2:00:00

delta2 = delta * 2
print(delta2)   #32 days, 4:00:00

d = date(2019, 10, 4) + delta2
print(d)    #2019-11-05

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)   #2019-11-05 18:53:00
#----------------------------------------------
from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)
print(my_date.strftime("%Y/%m/%d %H:%M:%S"))    #2020/11/04 14:53:00
print(my_date.strftime("%y/%B/%d %H:%M:%S %p")) #20/November/04 14:53:00 PM
print(my_date.strftime("%a, %Y %b %d"))         #Wed, 2020 Nov 04
print(my_date.strftime("%A, %Y %B %d"))         #Wednesday, 2020 November 04
print(my_date.strftime("Weekday: %w"))          #Weekday: 3
print(my_date.strftime("Day of the year: %j"))  #Day of the year: 309
print(my_date.strftime("Week number of the year: %W"))#Week number of the year: 44
#-------------------------------------------------------------------------------
import time

time.sleep(10)
print("Hello world!") # This text will be displayed after 10 seconds.
#------------------------------------------------------------------------
from datetime import datetime

dt = datetime(2020, 9, 29, 13, 51)
print("Datetime:", dt)  # Datetime: 2020-09-29 13:51:00
#------------------------------------------------------------------------
from datetime import date

d = date(2020, 9, 29)
print(d.strftime('%Y/%m/%d')) #2020/09/29
#=========================================================================
        ##calendar##
"""
відображаються дні тижня з понеділка по неділю. 
Кожен день тижня має своє представлення у вигляді цілого числа, 
де перший день тижня (понеділок) представлений значенням 0, 
а останній день тижня (неділя) – значенням 6.
"""

import calendar
print(calendar.calendar(2020))
#------------------------------------------------------------------------
import calendar
calendar.prcal(2020)
#------------------------------------------------------------------------
import calendar
print(calendar.month(2020, 11))
#------------------------------------------------------------------------
import calendar
calendar.prmonth(2020, 11)
#------------------------------------------------------------------------
import calendar
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)
#Дозволяє змінити перший день тижня.
#Він приймає значення від 0 до 6, де 0 – неділя, а 6 – субота.
#------------------------------------------------------------------------
import calendar
print(calendar.weekday(2020, 12, 24))#3-четвер
#------------------------------------------------------------------------
import calendar
print(calendar.weekheader(1))##M T W T F S S
print(calendar.weekheader(3))#Mon Tue Wed Thu Fri Sat Sun
#повертає назви днів тижня в скороченому вигляді
#------------------------------------------------------------------------
import calendar
print(calendar.isleap(2020))#True   Виявити чи високосний рік
print(calendar.leapdays(2010, 2021))
#дозволяє перевірити, чи є рік високосним чи ні
#------------------------------------------------------------------------
import calendar
c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ")
#6 0 1 2 3 4 5
#------------------------------------------------------------------------
import calendar
c = calendar.Calendar()
for date in c.itermonthdates(2019, 11):
    print(date, end=" ")#повертаються всі дні в зазначеному місяці і році
#------------------------------------------------------------------------
import calendar
c = calendar.Calendar()
for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")#
#------------------------------------------------------------------------
import calendar
c = calendar.Calendar()
for data in c.monthdays2calendar(2020, 12):
    print(data)
# ------------------------------------------------------------------------

#------------------------------------------------------------------------
"""
calendar.Calendar – надає методи підготовки даних календаря до форматування;
calendar.TextCalendar – використовується для створення звичайних текстових календарів;
calendar. HTMLCalendar – використовується для створення HTML-календарів;
calendar. LocalTextCalendar – є підкласом календаря. Клас TextCalendar. 
    Конструктор цього класу приймає параметр locale, який використовується для повернення 
    відповідних назв місяців та днів тижня.
calendar. LocalHTMLCalendar – це підклас календаря. Клас HTMLCalendar. 
    Конструктор цього класу приймає параметр locale, який використовується для повернення 
    відповідних назв місяців та днів тижня.
itermonthdates2 – повертає дні у вигляді кортежів, 
    що складаються з дня номера місяця та номера дня тижня;
itermonthdates3 – повертає дні у вигляді кортежів, 
    що складаються з чисел року, місяця та дня місяця. 
itermonthdates4 – повертає дні у вигляді кортежів, 
    що складаються з чисел року, місяця, дня місяця та дня тижня. 
    
"""