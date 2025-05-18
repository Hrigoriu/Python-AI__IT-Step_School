from beverage import Beverage   # Витягуємо з файлу beverage.py клас Beverage

class Order:
    def __init__(self):
        self.__items: list[Beverage] = []   #режим private

    def add_beverage(self, beverage: Beverage): #Агрегація
        self.__items.append(beverage)

    def _get_total(self):   #   режим protected
        return sum(beverage.price for beverage in self.__items)

    def print_order(self):
        print('Order summery: ')
        for beverage in self.__items:
            print(beverage.get_description())
        print(f'Total: {self._get_total()}')