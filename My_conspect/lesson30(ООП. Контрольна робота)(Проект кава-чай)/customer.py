from order import Order
from beverage import Beverage

class Customer: #Клас для Клієнта
    def __init__(self, name: str):
        self.name = name
        self.order = Order()    #композиція (замовлення створюється прямо в середині Клієнта)

    def add_to_order(self, beverage: Beverage):
        self.order.add_beverage(beverage)

    def checkout(self):
        print(f'---Customer: {self.name}---')
        self.order.print_order()