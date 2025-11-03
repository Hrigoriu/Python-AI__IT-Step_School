
'''
Алгоритм ітерації об'єкту:
1. Пайтон створює ітератор об'єкту за допомогою iter()
2. Пайтон витягує елемент з ітератору за допомогою next()
3. Як тільки у ітератора закінчуються елементи, він видає StopIteration
'''


class Student:
    def __init__(self, name: str, *grades: int | float):  # __init__ - функція-конструктор
        self.name = name
        self.grades = list(grades)

    def __str__(self):
        return f'Я студент {self.name}. Мій середній бал: {self.average_grade()}'

    def __gt__(self, other):  # магічний метод, що спрацьовує при Student > other
        if type(other) is not Student:
            raise ValueError('Порівнювати студента можна тільки з іншим студентом!')

        return self.average_grade() > other.average_grade()

    def __add__(self, other):  # магічний метод, що спрацьовує при Student + other
        if type(other) is not Student:
            raise ValueError('Порівнювати студента можна тільки з іншим студентом!')

        return sum(self.grades) + sum(other.grades)

    def add_grade(self, new_grade: int | float):
        self.grades.append(new_grade)

    def average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)


class StudentGroup:
    def __init__(self, name: str):
        self.name = name
        self.students: list[Student] = []

        self.iterator_index = 0

    def __len__(self):
        return len(self.students)

    def __iter__(self):  # спрацьовує, коли пайтону треба ітератор нашого об'єкту
        self.iterator_index = 0  # скидаємо на стартову позначку індекс ітератора
        return self  # в якості ітератора, просто повертаємо наш об'єкт

    def __next__(self):  # спрацьовує, коли пайтону треба наступний елемент для ітерації
        if self.iterator_index >= len(self.students):
            raise StopIteration  # помилка, яку чекає пайтон, щоб зупинити ітерацію

        student = self.students[self.iterator_index]

        self.iterator_index += 1
        return student

    def add_student(self, student: Student):
        if type(student) is not Student:
            raise ValueError('До групи можна додати тільки студента!')

        self.students.append(student)

    def get_best_student(self):  # обчислити студента з самим великим середнім балом
        return max(self.students, key=lambda student: student.average_grade())


bob = Student('Bob', 10, 9, 5, 7, 10, 6)
alice = Student('Alice', 10, 8, 7, 8, 10, 10, 7)
john = Student('John', 9, 9, 8, 10, 4, 5)

jason = Student('Jason', 10, 10, 10, 1)

python_ai = StudentGroup('PythonAI')
math_group = StudentGroup('Math')

python_ai.add_student(bob)
python_ai.add_student(alice)
python_ai.add_student(john)

math_group.add_student(jason)

# print(python_ai.get_best_student())

print(alice < bob)
print(alice + bob)
print(len(python_ai))

print('Всі студенти групи Python AI: ')
for el in python_ai:
    print(el)

print('Всі студенти групи Math: ')
for el in math_group:
    print(el)
