from abc import ABC, abstractmethod

#1.
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.configuration_details = []  # Список для збереження деталей конфігурації

    def add_component(self, component_type: str, component_detail: str):
        setattr(self, component_type.lower(), component_detail)
        self.configuration_details.append(f'{component_type.capitalize()}: {component_detail}')

    def show_config(self):
        print('Конфігурація комп\'ютера:')
        if not self.configuration_details:
            print('Не має ще компонентів для конфігурації.')
            return
        for detail in self.configuration_details:
            print(f'  - {detail}')
        print('-' * 30)


#2.
class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()

    def reset(self):
        self.computer = Computer()

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def build_gpu(self):
        pass

    def get_computer(self) -> Computer:
        product = self.computer
        self.reset()
        return product


#3.
class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.add_component('cpu', 'Intel Core i9 (14th Gen)')
        return self

    def build_ram(self):
        self.computer.add_component('ram', '32GB DDR5 6000MHz')
        return self

    def build_storage(self):
        self.computer.add_component('storage', '2TB NVMe SSD PCIe 4.0')
        return self

    def build_gpu(self):
        self.computer.add_component('gpu', 'NVIDIA GeForce RTX 4090')
        return self


class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.add_component('cpu', 'Intel Core i5 (13th Gen)')
        return self

    def build_ram(self):
        self.computer.add_component('ram', '16GB DDR4 3200MHz')
        return self

    def build_storage(self):
        self.computer.add_component('storage', '512GB SATA SSD')
        return self

    def build_gpu(self):
        self.computer.add_component('gpu', 'Integrated Intel UHD Graphics 770')
        return self


class ServerComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.add_component('cpu', 'Intel Xeon Scalable (Gold)')
        return self

    def build_ram(self):
        self.computer.add_component('ram', '128GB ECC DDR5 RAM')
        return self

    def build_storage(self):
        self.computer.add_component('storage', '4TB SAS HDD RAID 10 Array')
        return self

    def build_gpu(self):
        self.computer.add_component('gpu', 'Basic VGA Adapter (для управління сервером)')
        return self


#4.
class Director:
    def __init__(self):
        self._builder = None

    def set_builder(self, builder: ComputerBuilder):
        self._builder = builder

    def construct_full_computer(self):
        if not self._builder:
            raise ValueError('Щось пішло не так. Перевір все!')
        self._builder.build_cpu()
        self._builder.build_ram()
        self._builder.build_storage()
        self._builder.build_gpu()

    def construct_computer_without_gpu(self):
        if not self._builder:
            raise ValueError('Щось пішло не так. Перевір все!')
        self._builder.build_cpu()
        self._builder.build_ram()
        self._builder.build_storage()


#5.
if __name__ == '__main__':
    director = Director()

    while True:
        print('\nОберіть тип комп\'ютера для побудови:')
        print('1 - Ігровий комп\'ютер')
        print('2 - Офісний комп\'ютер')
        print('3 - Серверний комп\'ютер')
        print('0 - Вихід')

        choice = input('Ваш вибір: ')

        builder = None

        if choice == '1':
            builder = GamingComputerBuilder()
            print('\n--- Будуємо Ігровий Комп\'ютер ---')
        elif choice == '2':
            builder = OfficeComputerBuilder()
            print('\n--- Будуємо Офісний Комп\'ютер ---')
        elif choice == '3':
            builder = ServerComputerBuilder()
            print('\n--- Будуємо Серверний Комп\'ютер ---')
        elif choice == '0':
            print('Дякуємо за використання програми!')
            break
        else:
            print('Невірний вибір. Будь ласка, спробуйте ще раз.')
            continue

        if builder:
            director.set_builder(builder)
            director.construct_full_computer()
            computer = builder.get_computer()
            computer.show_config()


#5.
""" 
if __name__ == '__main__':
    director = Director()

    print('Побудова ігрового комп\'ютера:')
    gaming_builder = GamingComputerBuilder()
    director.set_builder(gaming_builder)
    director.construct_full_computer()
    gaming_computer = gaming_builder.get_computer()
    gaming_computer.show_config()

    print('Побудова офісного комп\'ютера:')
    office_builder = OfficeComputerBuilder()
    director.set_builder(office_builder)
    director.construct_full_computer()
    office_computer = office_builder.get_computer()
    office_computer.show_config()

    print('Побудова серверного комп\'ютера (без GPU):')
    server_builder = ServerComputerBuilder()
    director.set_builder(server_builder)
    director.construct_full_computer()
    server_computer_full = server_builder.get_computer()
    server_computer_full.show_config()

    print('Побудова комп\'ютера без Директора (клієнт керує будівельником):')
    custom_gaming_builder = GamingComputerBuilder()
    custom_computer = (custom_gaming_builder
                       .build_cpu()
                       .build_ram()
                       .build_storage()
                       .get_computer())
    custom_computer.show_config()

    print('Створення офісного комп\'ютера (тільки процесор і оперативна пам\'ять) вручну:')
    minimal_office_builder = OfficeComputerBuilder()
    minimal_office_computer = (minimal_office_builder
                               .build_cpu()
                               .build_ram()
                               .get_computer())
    minimal_office_computer.show_config()

    print('Очікування скидання:')
    another_computer_from_minimal_builder = minimal_office_builder.get_computer()
    another_computer_from_minimal_builder.show_config()
"""
