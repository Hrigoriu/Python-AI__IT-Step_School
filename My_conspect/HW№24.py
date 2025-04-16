"""
Завдання №1
Створіть клас BankAccount (Банківський рахунок) з атрибутами account_number (номер рахунку)та
balance (баланс). Додайте методи deposit (внесення коштів) та withdraw (зняття коштів),які
змінюють баланс відповідним чином. Реалізуйте метод get_balance, який повертає поточний баланс.
"""


class BankAccount:  #Клас про банківський рахунок
    def __init__(self, account_number: str, initial_balance: int | float = 0):
        self.account_number: str = account_number # Атрибут: номер рахунку
        if initial_balance >= 0:
            self.balance: int | float = initial_balance
        else:
            print(f'Помилка: Початковий баланс ({initial_balance}) не може бути від`ємним.')
            self.balance: int | float = 0

    def __str__(self) -> str:   #Метод повертає рядкове представлення об'єкта BankAccount.
        try:
            formatted_balance = f'{float(self.balance):.2f}' # Формуємо баланс, щоб було 2 знаки після коми.
        except ValueError:
            formatted_balance = str(self.balance) # На випадок, якщо баланс не є числом
        return f'Банківський рахунок {self.account_number} (Баланс: {formatted_balance})'

    def deposit(self, amount: int | float): #Метод для внесення коштів на рахунок.
        if amount > 0:
            self.balance += amount
            print(f'Внесено {amount:.2f}. Новий баланс: {self.balance:.2f}')
        else:
            print('Помилка: Сума депозиту повинна бути позитивною.')

    def withdraw(self, amount: int | float):    #Метод для зняття коштів з рахунку.
        if amount <= 0:
            print('Помилка: Сума для зняття повинна бути позитивною.')
        elif amount > self.balance:
            print(f'Помилка: Недостатньо коштів. Баланс: {self.balance:.2f}, спроба зняти: {amount:.2f}')
        else:
            self.balance -= amount
            print(f'Знято {amount:.2f}. Новий баланс: {self.balance:.2f}')

    def get_balance(self) -> int | float:   #Метод для отримання поточного балансу.
        return self.balance


    def get_account_info(self) -> str:  # Метод, який повертає інформацію.
        return f'Інформація: Рахунок № {self.account_number}, Поточний баланс: {self.balance:.2f}'


# --- Приклад використання ---
print("--- Створення рахунків ---")
account1 = BankAccount('UA2001', 1500.50)
account2 = BankAccount('UA2002')
account3 = BankAccount('UA2003', -250)

print('\n--- Представлення об\'єктів (__str__) ---')
print(account1)
print(account2)
print(account3)

print('\n--- Операції з account1 ---')
current_balance_acc1 = account1.get_balance()
print(f'Початковий баланс account1: {current_balance_acc1:.2f}')
account1.deposit(350.25)
account1.withdraw(200)
# Отримуємо оновлений баланс
updated_balance_acc1 = account1.get_balance()
print(f'Баланс account1 після операцій (через getter): {updated_balance_acc1:.2f}')
# Використання нового методу get_account_info
print(account1.get_account_info())

print('\n--- Невдалі операції з account1 ---')
account1.withdraw(5000) # Недостатньо коштів
account1.deposit(-100)  # Некоректна сума

print('\n--- Операції з account2 ---')
print(account2)
account2.deposit(1000)
print(f'Баланс account2 (через getter): {account2.get_balance():.2f}')
print(account2)

#============================================================================
"""
Завдання №2
Реалізуйте клас Student (Студент) із атрибутами name (ім'я) та grades (оцінки). 
Додати метод average_grade, який обчислює середню оцінку студента.
"""


class Student:  #Клас для представлення студента та його оцінок.
    def __init__(self, name: str, initial_grades: list[int] | None = None):
        self.name: str = name
        if initial_grades is None:
            self.grades: list[int] = []
        else:
            self.grades: list[int] = list(initial_grades)
        print(f'Студента "{self.name}" створено.')

    def __str__(self) -> str:   # Метод повертає рядкове представлення об'єкта Student.
        grades_str = ', '.join(map(str, self.grades)) if self.grades else 'Ще немає оцінок'
        return f'Студент: {self.name} | Оцінки: [{grades_str}]'

    def add_grade(self, grade: int):    #Метод додає нову оцінку до списку оцінок студента
        self.grades.append(grade)
        print(f'Студенту {self.name} додано оцінку: {grade}.')

    def average_grade(self) -> float:   #Метод обчислює та повертає середню оцінку студента.
        if not self.grades:
            print(f'У студента {self.name} ще немає оцінок для розрахунку середнього балу.')
            return 0.0
        total_sum = sum(self.grades)
        count = len(self.grades)
        average = total_sum / count
        return average

# --- Приклад використання ---
print('--- Створення студентів ---')
student1 = Student('Дональд Трамп', [11, 9, 8, 10])
student2 = Student('Ілон Маск')
student3 = Student('Леонід Кравчук', [8, 6, 10])

print('\n--- Початковий стан студентів (__str__) ---')
print(student1)
print(student2)
print(student3)

print('\n--- Додавання оцінок ---')
student1.add_grade(8)
student2.add_grade(5)
student2.add_grade(9)
student2.add_grade(12)
student3.add_grade(9)

print('\n--- Оновлений стан студентів ---')
print(student1)
print(student2)
print(student3)

print('\n--- Обчислення середньої оцінки ---')
avg1 = student1.average_grade()
print(f'Середня оцінка для {student1.name}: {avg1:.2f}')
avg2 = student2.average_grade()
print(f'Середня оцінка для {student2.name}: {avg2:.2f}')
avg3 = student3.average_grade()
print(f'Середня оцінка для {student3.name}: {avg3:.2f}')

print('\n--- Студент без оцінок ---')
student4 = Student('Юля Тимошенко')
print(student4)
avg4 = student4.average_grade()
print(f'Середня оцінка для {student4.name}: {avg4:.2f}')

#=================================================================
"""
Завдання №3
Створіть клас StudentGroup, що має атрибут students. 
Суть розробленого класу – мати можливість додавати клас Student(з минулого завдання) до атрибуту students. 
Клас повинен мати метод, що дозволяє вивести статистику самого успішного студента(по середньому балу). 
"""
class StudentGroup: #Клас для представлення групи студенті
    def __init__(self, group_name: str):
        self.group_name: str = group_name
        self.students: list[Student] = []
        print(f'Групу "{self.group_name}" створено.')

    def add_student(self, student: Student):    #Метод додає об студента до групи.
        if isinstance(student, Student):
            if student not in self.students:
                 self.students.append(student)
                 print(f'Студента {student.name} додано до групи {self.group_name}.')
            else:
                 print(f'Студент {student.name} вже є у групі {self.group_name}.')
        else:
            print(f'Якась помилка, ти щось зробив не так')

    def get_best_student_stats(self) -> Student | None: #Метод знаходить студента з найвищою середньою оцінкою в групі
        print(f'\n--- Пошук найкращого студента в групі {self.group_name} ---')
        if not self.students:
            print(f'Група {self.group_name} порожня. Немає студентів для аналізу.')
            return None
        try:
            best_student = max(self.students, key=lambda s: s.average_grade())
        except Exception as e:
            print(f'Помилка під час обчислення середніх балів або порівняння: {e}')
            return None

        best_average = best_student.average_grade()

        print(f'Найкращий студент у групі {self.group_name}:')
        print(f'  Ім\'я: {best_student.name}')
        print(f'  Середня оцінка: {best_average:.2f}')
        print(f'  Усі оцінки: {best_student.grades}')
        return best_student

    def __str__(self) -> str:   #Метод повертає рядкове представлення групи студентів.
        representation = f'Група: {self.group_name}\n'
        representation += f'Кількість студентів: {len(self.students)}\n'
        if self.students:
            representation += 'Список студентів:\n'
            for student in self.students:
                representation += f'  - {student}\n'
        else:
            representation += 'Студентів у групі немає.\n'
        return representation.strip()

# --- Приклад використання класів Student та StudentGroup ---
print('--- Етап 1: Створення Студентів  ---')
student1 = Student('Дональд Трамп', [11, 9, 8, 10])
student2 = Student('Ілон Маск')
student3 = Student('Леонід Кравчук', [8, 6, 10])
student4 = Student('Юля Тимошенко')
student5 = Student('Віктор Ющенко', [10, 12, 11, 10])

print('\n--- Етап 2: Додавання оцінок студентам ---')
student1.add_grade(8)
student2.add_grade(5)
student2.add_grade(9)
student2.add_grade(12)
student3.add_grade(9)
student4.add_grade(7)
student4.add_grade(8)

print('\n--- Етап 3: Створення та наповнення Груп Студентів ---')
programming_group = StudentGroup('Розробники ШІ')
history_group = StudentGroup('Історики')
programming_group.add_student(student1)
programming_group.add_student(student2)
programming_group.add_student(student5)

history_group.add_student(student3)
history_group.add_student(student4)
history_group.add_student(student1)
print('\n--- Перевірка помилок ---')
history_group.add_student("Викладач")
programming_group.add_student(student2)

print('\n--- Етап 4: Інформація про Групи (__str__) ---')
print(programming_group)
print('\n')
print(history_group)

print('\n--- Етап 5: Статистика найкращих студентів у Групах ---')
best_programmer = programming_group.get_best_student_stats()
print('\n')
best_historian = history_group.get_best_student_stats()

print('\n--- Етап 6: Тест з порожньою групою ---')
empty_group = StudentGroup('Майбутні генії')
print(empty_group)
result = empty_group.get_best_student_stats()
