from typing import Dict, List, Optional
from shop_models import Product, User, Order, Cart

class ShopManager:  #Клас, що керує каталогом товарів, користувачами, їхніми кошиками та замовленнями.
    def __init__(self):
        self._products: List[Product] = []
        self._load_sample_products()
        self._users: Dict[int, User] = {}   # Словник для зберігання користувачів: key -> chat_id,Item -> User object
        self._orders: List[Order] = []  # Список для зберігання всіх замовлень
        self._next_order_id = 1 # Лічильник для ID замовлень

    def _load_sample_products(self):    #Метод, який завантажує товари.
        self._products = [
            Product(1, 'Смартфон "Model X"', 'Електроніка', 15500.00),
            Product(2, 'Ноутбук "LiteBook Air"', 'Електроніка', 28000.00),
            Product(3, 'Навушники "SoundBlast"', 'Електроніка', 2500.00),
            Product(4, 'Футболка "Python Lover"', 'Одяг', 450.00),
            Product(5, 'Джинси "Code Style"', 'Одяг', 1200.00),
            Product(6, 'Шкарпетки "Binary Socks"', 'Одяг', 150.00),
            Product(7, 'Книга "Clean Code"', 'Книги', 800.00),
            Product(8, 'Книга "Effective Python"', 'Книги', 950.00),
        ]

    def get_categories(self) -> List[str]:  #Метод, який повертає список унікальних категорій.
        return sorted(list(set(p.category for p in self._products)))

    def get_products_by_category(self, category_name: str) -> List[Product]:    #Метод, який повертає список товарів за назвою категорії.
        return [p for p in self._products if p.category == category_name]

    def get_product_by_id(self, product_id: int) -> Optional[Product]:  #Метод, який повертає товар за його ID.
        for p in self._products:
            if p.id == product_id:
                return p
        return None

    def get_user(self, chat_id: int) -> User:   #Метод, який повертає користувача за chat_id. Якщо не існує, створює нового.
        if chat_id not in self._users:
            self._users[chat_id] = User(chat_id)
        return self._users[chat_id]

    def register_user(self, chat_id: int, name: str, phone: str, address: str) -> bool: #Метод, який реєструє користувача або оновлює його дані.
        user = self.get_user(chat_id)
        user.register(name, phone, address)
        return True

    def add_to_cart(self, chat_id: int, product_id: int, quantity: int = 1) -> Optional[Product]:   #Метод, який додає товар до кошика користувача.
        user = self.get_user(chat_id)
        product = self.get_product_by_id(product_id)
        if product:
            user.cart.add_item(product, quantity)
            return product
        return None

    def remove_from_cart(self, chat_id: int, product_id: int) -> Optional[Product]: #Метод, який видаляє товар з кошика користувача.
        user = self.get_user(chat_id)
        product = self.get_product_by_id(product_id)
        if product:
            user.cart.remove_item(product_id)
            return product
        return None


    def get_cart(self, chat_id: int) -> Cart:   #Метод, який повертає кошик користувача.
        user = self.get_user(chat_id)
        return user.cart

    def place_order(self, chat_id: int) -> Optional[Order]: #Метод, який оформлює замовлення з кошика користувача.
        user = self.get_user(chat_id)
        if not user.cart.items:
            return None
        if not user.is_registered:  # Перевіряємо, чи користувач зареєстрований перед оформленням
             return None # Користувач не зареєстрований

        order_items_copy = user.cart.get_items() # Отримуємо копію товарів
        total_price = user.cart.get_total()

        if not order_items_copy:
            return None

        order = Order(self._next_order_id, user, order_items_copy, total_price)
        self._orders.append(order)
        self._next_order_id += 1

        user.cart.clear() # Очищаємо кошик після оформлення замовлення

        return order

    def get_user_orders(self, chat_id: int) -> List[Order]: #Метод, який повертає список замовлень користувача.
        return [order for order in self._orders if order.user.chat_id == chat_id]
