"""
Створіть систему для управління витратами.
Клас Витрати повинен мати атрибути для зберігання суми витрат та категорії витрат.
Використайте дескриптори для забезпечення обмежень на введені дані:
1.	Дескриптор для суми витрат (СумаВитрат):
•	Сума витрат не може бути від'ємною.
•	Сума витрат не може перевищувати заданий ліміт за місяць.
2.	Дескриптор для категорії витрат (КатегоріяВитрат):
•	Категорія витрат повинна бути однією з попередньо визначених категорій
(наприклад, "Їжа", "Транспорт", "Розваги" і т. д.).
"""


class AmountDescriptor: #Клас дескриптор рахунку
    def __init__(self, month_limit: float): #Метод ініціалізації
        self.month_limit = month_limit
        self._name = None

    def __set_name__(self, owner, name):    #Метод дескриптор, щоб присвоїти значення атрибуту об'єкта
        self._name = name

    def __set__(self, instance, value: float):  #Метод дескриптор, щоб присвоїти значення атрибуту об'єкта
        if value < 0:
            raise ValueError(f'{self._name} не може бути негативним.')
        if value > self.month_limit:
            raise ValueError(f'{self._name} ({value:.2f}) перевищує місячний ліміт ({self.month_limit:.2f}).')

        instance.__dict__[self._name] = value

    def __get__(self, instance, owner): #Метод дескриптор, щоб отримати значення атрибуту об'єкта
        if instance is not None:
            return instance.__dict__.get(self._name)
        return self


class CategoryDescriptor:   #Клас дескриптор категорії
    CATEGORIES = ['Їжа', 'Транспорт', 'Розваги', 'Одяг', 'Комунальні послуги', 'Інше']

    def __init__(self): #Метод ініціалізації
        self._name = None

    def __set_name__(self, owner, name):    #Метод дескриптор, щоб присвоїти значення атрибуту об'єкта
        self._name = name

    def __set__(self, instance, value: str):    #Метод дескриптор, щоб присвоїти значення атрибуту об'єкта
        if value not in self.CATEGORIES:
            raise ValueError(f'Помилка {self._name}: "{value}". Дозволені: {", ".join(self.CATEGORIES)}')

        instance.__dict__[self._name] = value

    def __get__(self, instance, owner): #Метод дескриптор, щоб отримати значення атрибуту об'єкта
        if instance is not None:
            return instance.__dict__.get(self._name)
        return self


class Expense: #Клас Витрат #
    amount = AmountDescriptor(month_limit=10000.0) # Місячний ліміт 10000
    category = CategoryDescriptor()

    def __init__(self, amount: float, category: str):   #Метод ініціалізації
        self.amount = amount
        self.category = category

    def __str__(self) -> str:   #Метод, який перетворює об'єкт на рядок
        return f'Витрати: {self.amount:.2f} грн | Категорія: {self.category}'


#================ Приклад використання ================================================================

print('--- Створення валідних об\'єктів витрат ---')
try:
    expense1 = Expense(150.50, 'Їжа')
    print(expense1)
    expense2 = Expense(5000, 'Транспорт')
    print(expense2)
except ValueError as e:
    print(f'Помилка, при створенні валідних об\'єктів: {e}')


print('\n--- Створення не валідних об\'єктів витрат---')
#1
try:
    print('Спроба: Витрат(-50, "Їжа")')
    invalid_expense1 = Expense(-50, 'Їжа')
except ValueError as e:
    print(f'Помилка, від\'ємна сума: {e}')
#2
try:
    print('Спроба: Витрат(11000, "Одяг")')
    invalid_expense2 = Expense(11000, 'Одяг')
except ValueError as e:
    print(f'Помилка, сума вище місячного ліміту: {e}')
#3
try:
    print('Спроба: Витрат(200, "Косметика")')
    invalid_expense3 = Expense(200, 'Косметика')
except ValueError as e:
    print(f'Помилка, недопустима категорія: {e}')


print('\n--- Спроби змінити атрибути (валідація дескриптором) ---')
print(f'Поточні витрати: {expense1}')
#1
try:
    print('Спроба - змінити витрати: -10')
    expense1.amount = -10
except ValueError as e:
    print(f'Помилка, спроба змінити суму на від\'ємну: {e}')
#2
try:
    print('Спроба - змінити витрати: 300.75')
    expense1.amount = 300.75
    print(f'Змінена витрат {expense1}')
except ValueError as e:
    print(f'Помилка : {e}')
#3
try:    #Змінити категорію на недопустиму
    print('Спроба - змінити витрати: "Відпустка" ')
    expense1.category = 'Відпустка'
except ValueError as e:
    print(f'Помилка, спроба змінити на недопустиму категорію: {e}')

