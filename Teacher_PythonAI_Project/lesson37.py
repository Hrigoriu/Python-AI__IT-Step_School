from abc import ABC, abstractmethod


# ПОВЕДІНКОВІ ПАТЕРНИ

# 1. Ітератор (Iterator)
# Суть патерну: дає можливість послідовно обходити об'єкт по елементам

'''
for el in list:

1. Пайтон створює ітератор за допомогою iter(list)
2. Пайтон витягує елемент з ітератору за допомогою next(iterator)
3. Якщо елементи скінчились - StopIteration
'''


class Student:
    def __init__(self, name, *grades: int | float):
        self.name = name
        self.grades = list(grades)

    def __str__(self):
        return f'Студент {self.name}, оцінка: {', '.join(str(grade) for grade in self.grades)}'


class StudentGroupIterator:
    def __init__(self, students: list[Student]):
        self.index = 0
        self.students = students

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration

        student = self.students[self.index]
        self.index += 1

        return student


class StudentGroup:
    def __init__(self):
        self.students = []

    def __iter__(self):
        return StudentGroupIterator(self.students)

    def add_students(self, *students: Student):
        self.students.extend(students)


group = StudentGroup()

bob = Student('Боб', 10, 11, 12, 10)
alice = Student('Аліса', 9, 11, 9, 12)
john = Student('Джон', 4, 6, 8, 1)

group.add_students()
group.add_students(bob, alice, john)

for el in group:
    print(el)


# 2. Стан (State)
# Суть патерну: дозволяє об'єктам змінювати поведінку в залежності від свого стану.
# Стан являється окремим класом з своїми методами

class State(ABC):
    @abstractmethod
    def handle(self, cola_machine):
        pass


class MoneyState(State):
    def handle(self, cola_machine):
        print(f'{cola_machine.name} приймає гроші!')
        cola_machine.switch_state(GetDrinkState())


class GetDrinkState(State):
    def handle(self, cola_machine):
        print(f'{cola_machine.name} видає напой!')
        cola_machine.plus_counter()
        cola_machine.switch_state(ReloadState())


class ReloadState(State):
    def handle(self, cola_machine):
        print(f'{cola_machine.name} перезагружається!')
        cola_machine.switch_state(MoneyState())


class ColaMachine:
    def __init__(self, name):
        self.counter = 0
        self.name = name
        self.state = MoneyState()

    def plus_counter(self):
        self.counter += 1

    def switch_state(self, new_state: State):  # СТАНДАРТНИЙ СЕТТЕР
        self.state = new_state

    def activate(self):
        self.state.handle(self)


cola = ColaMachine('Автомат з колою')

for _ in range(10):
    cola.activate()

print(cola.counter)


# 3. Спостерігач (Observer)
# Суть патерну: дозволяє об'єктам спостерігати за іншим класом та реагувати на його події та методи

class Subscriber:  # Відповідно, він і являється спостерігачем
    def __init__(self, name):
        self.name = name
        self.view_counter = 0

    def notify(self, video_title: str):
        self.view_counter += 1
        print(f'{self.name} отримав сповіщення про відео {video_title} та переглянув! Кількість переглянутих відео: {self.view_counter}')


class YouTubeChannel:
    def __init__(self):
        self.subscribers: list[Subscriber] = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def new_video(self, video_title):
        for sub in self.subscribers:
            sub.notify(video_title)


my_channel = YouTubeChannel()

sub1 = Subscriber('Боб')
sub2 = Subscriber("Аліса")
sub3 = Subscriber("Джон")

my_channel.subscribe(sub1)
my_channel.new_video('Як створювати змінні в Python')
my_channel.new_video('Як писати умови в Python')

my_channel.subscribe(sub2)
my_channel.subscribe(sub3)
my_channel.new_video('Як робити цикли в Python')


# 4. Ланцюг обов'язків (Chain Of Responsibility)
# Суть патерну: передача "обов'язків" між класами, що з'єднані спільним ланцюгом
class Email:
    def __init__(self, subject, content):
        self.subject = subject
        self.content = content


class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, email: Email):  # логіка передачі обов'язків по ланцюгу
        if self.next_handler:
            self.next_handler.handle(email)


class SpamFilter(Handler):
    def handle(self, email):
        if 'купи' in email.content.lower():
            print(f'Спам був видалений: {email.subject}')
        else:
            super().handle(email)


class VirusScanner(Handler):
    def handle(self, email: Email):
        if '<script>' in email.content.lower():
            print(f'Вірус було заблоковано: {email.subject}')
        else:
            super().handle(email)


class ImportantFilter(Handler):
    def handle(self, email: Email):
        if 'важливо' in email.subject.lower():
            print(f'Повідомлення помічено як важливе: {email.subject}')
        else:
            super().handle(email)


class Inbox(Handler):
    def handle(self, email: Email):
        print(f'Стандартне повідомлення: {email.subject}')


chain = SpamFilter(VirusScanner(ImportantFilter(Inbox())))

emails = [
    Email('Купи зараз!!!!', 'Купи це зараз та отримуй знижку!'),
    Email('Привіт!', "Як справи?"),
    Email('I love you', '<script>'),
    Email('ВАЖЛИВО: Документи за місяць', "Треба до 18:00")
]

for email in emails:
    print('НОВЕ ПОВІДОМЛЕННЯ!')
    chain.handle(email)


# 5. Знімок(Memento)
# Суть патерну: дозволяє зберігати та відновлювати минуті стани об'єктів, не
# вдаваючись в їх реалізацію
class Memento:
    def __init__(self, text):
        self.text = text


class Editor:
    def __init__(self):
        self.text = ''

    def write(self, new_text):
        self.text += new_text

    def get_text(self):
        return self.text

    def save(self):
        return Memento(self.text)

    def restore(self, memento: Memento):  # відновити клас до якогось моменту
        self.text = memento.text


class History:
    def __init__(self):
        self.__history: list[Memento] = []

    def save(self, new_memento: Memento):
        self.__history.append(new_memento)

    def undo(self):
        if not self.__history:
            return

        return self.__history.pop()


editor = Editor()
history = History()

editor.write('Привіт! ')
editor.write('Привіт ще раз! ')

history.save(editor.save())

editor.write('Як справи?')

print(f'Поточний текст: {editor.get_text()}')
editor.restore(history.undo())
print(f'Поточний текст: {editor.get_text()}')
