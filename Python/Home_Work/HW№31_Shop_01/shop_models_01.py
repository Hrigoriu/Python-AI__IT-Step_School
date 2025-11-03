from typing import Dict, List
import datetime

class Product:  #Клас, що представляє один товар.
    def __init__(self, product_id: int, name: str, category: str, price: float):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f' "{self.name}" - {self.price:.2f} грн.'

class CartItem: #Клас, що представляє товар у кошику з кількістю.
    def __init__(self, product: Product, quantity: int = 1):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f' "{self.product.name}" ({self.quantity} шт.) - {self.product.price * self.quantity:.2f} грн.'

class Cart: #Клас, що представляє кошик користувача.
    def __init__(self):
        self.items: Dict[int, CartItem] = {}    # Словник: key -> product_id, Item -> CartItem

    def add_item(self, product: Product, quantity: int = 1):    #Метод, який додає товар до кошика або збільшує кількість.
        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product, quantity)

    def remove_item(self, product_id: int): #Метод, який видаляє товар з кошика повністю.
        if product_id in self.items:
            del self.items[product_id]

    def get_items(self) -> List[CartItem]:  #метод, який повертає список всіх товарів у кошику.
        return list(self.items.values())

    def get_total(self) -> float:   #Метод, який розраховує загальну вартість товарів у кошику.
        return sum(item.product.price * item.quantity for item in self.items.values())

    def clear(self):    #Метод, який очищає кошик.
        self.items = {}

    def __str__(self):
        if not self.items:
            return 'Ваш кошик порожній.'
        items_str = '\n'.join(str(item) for item in self.items.values())
        return f'{items_str}\n---\nВсього: {self.get_total():.2f} грн.'


class User: #Клас, що представляє користувача бота.
    def __init__(self, chat_id: int):
        self.chat_id = chat_id
        self.name: str | None = None
        self.phone: str | None = None
        self.address: str | None = None
        self.cart = Cart()
        self.is_registered: bool = False

    def register(self, name: str, phone: str, address: str):    #Метод, який реєструє користувача, зберігаючи його дані.
        self.name = name
        self.phone = phone
        self.address = address
        self.is_registered = True

    def __str__(self):
        if self.is_registered:
             return f'{self.name}, {self.phone}, {self.address}'
        return 'Незареєстрований користувач.'


class Order:    #Клас, що представляє оформлене замовлення.
    def __init__(self, order_id: int, user: User, items: List[CartItem], total_price: float):
        self.id = order_id
        self.user = user
        self.items = [CartItem(item.product, item.quantity) for item in items]
        self.total_price = total_price
        self.timestamp = datetime.datetime.now()
        self.status = 'Pending'

    def __str__(self):
        items_str = '\n  '.join(str(item) for item in self.items)
        return (
            f'Замовлення №{self.id}\n'
            f'Дата: {self.timestamp.strftime("%Y-%m-%d %H:%M")}\n'
            f'Статус: {self.status}\n'
            f'Товари:\n  {items_str}\n'
            f'Всього: {self.total_price:.2f} грн.'
        )