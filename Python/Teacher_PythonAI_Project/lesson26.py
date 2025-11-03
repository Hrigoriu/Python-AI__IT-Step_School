
# Наслідування
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return f'Привіт, я людина {self.name}! Мій вік: {self.age}'

    def birthday(self):
        self.age += 1


class Teacher(Human):
    # Все, що є в батьковському класі
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # спочатку викликаємо батьківський ініт

        self.subject = subject

    def say_hi(self):  # переназначаємо метод say_hi, щоб переробити його поведінку
        return f'Я вчитель! Мене звуть {self.name}, я викладаю предмет: {self.subject}'

    def teach(self):  # створюємо метод teach, що буде унікальним для вчителя
        return f'Я {self.name}, я зараз викладаю!'


class Policeman(Human):
    def __init__(self, name, age, rank):
        super().__init__(name, age)

        self.rank = rank

    def say_hi(self):
        return f'Я поліцейський {self.name} ({self.age})! Моє звання: {self.rank}'


def interface(human: Human):
    print(human.say_hi())


bob = Human('Боб', 15)
anna = Teacher("Анна", 35, "Математика")

john = Policeman('Джон', 29, "Сержант")

john.birthday()
john.birthday()

interface(bob)
interface(anna)
interface(john)
