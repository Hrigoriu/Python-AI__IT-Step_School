from abc import ABC, abstractmethod


# СТУКТУРНІ ПАТЕРНИ

# 1. Фасад (Facade)
# Суть патерну: дає спрощений інтерфейс до складної системи класів
#               (пов'язує класи всередині себе)


class Light:
    def __init__(self):
        self.light_on = False

    def activate(self):
        print('Свитло вимикається!' if self.light_on else 'Світло вмикається!')
        self.light_on = not self.light_on


class Thermostat:
    def __init__(self):
        self.temperature = 10

    def set_temp(self, new_temp):
        old = self.temperature
        self.temperature = new_temp

        print(f'Температуру встановлено з {old} C до {self.temperature} C!')


class Security:
    def arm(self):
        print('Сигналізацію активовано!')


class SmartHomeFacade:
    def __init__(self):
        self.light = Light()
        self.thermostat = Thermostat()
        self.security = Security()

    def leave_home(self):
        self.light.activate()
        self.thermostat.set_temp(16)
        self.security.arm()


# 2. Адаптер(Adapter)
# Суть патерну: призводить інтерфейс одного класа до потрібного (адаптує клас під потреби)

class MP3Player:
    def play_mp3(self, filename):
        print(f'Програється відео {filename}')


class AudioPlayer:
    def play(self, audio):
        print(f'Програється звук {audio}')


class MP3Adapter(AudioPlayer):
    def __init__(self, mp3_player: MP3Player):
        self.mp3 = mp3_player

    def play(self, audio):
        self.mp3.play_mp3(audio)


def interface(player: AudioPlayer, file):
    player.play(file)


player1 = AudioPlayer()

player2 = MP3Player()
player2 = MP3Adapter(player2)

interface(player2, 'Тестовий файл1')
interface(player2, 'Тестовий файл2')


# 3. Композит (Composite)
# Суть патерну: створення деревоподібної структури об'єктів з однаковим інтерфейсом

class SystemItem(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError


class File(SystemItem):  # Leaf (листя)
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f'-File: {self.name}')


class Folder(SystemItem):
    def __init__(self, name):
        self.name = name
        self.items: list[SystemItem] = []

    def add(self, item: SystemItem):
        self.items.append(item)

    def display(self):
        for item in self.items:
            item.display()


file_1 = File('Data.txt')
file_2 = File('Photo.jpg')
file_3 = File('main.py')

root_folder = Folder('root')

folder_1 = Folder('papka1')
folder_2 = Folder('papka2')
folder_3 = Folder('papka3')

folder_3.add(file_3)

folder_2.add(folder_3)
folder_2.add(file_2)

root_folder.add(folder_2)
root_folder.add(folder_1)
root_folder.add(file_1)

root_folder.display()


# 4. Декоратор(Decorator)
# Суть патерну: динамічно додає новий функціонал, зберігши старий

class Message(ABC):
    @abstractmethod
    def send(self):
        pass


class TextMessage(Message):
    def __init__(self, message_text):
        self.message_text = message_text

    def send(self):
        return f'Повідомлення: "{self.message_text}" відправлено'


class MessageWithPhoto(Message):
    def __init__(self, message_class: Message):
        self.message = message_class

    def send(self):
        return self.message.send() + ' з фото'


class MessageWithVideo(Message):
    def __init__(self, message_class: Message):
        self.message = message_class

    def send(self):
        return self.message.send() + ' з відео'


message = TextMessage("Привіт!")
print(message.send())
message = MessageWithPhoto(message)
print(message.send())
message = MessageWithVideo(message)
print(message.send())
