"""
Створи дві таблиці:

Product (продукти) — з полями:
-id (Primary Key)
-name (назва продукту)
-price (ціна)
-category_id (зовнішній ключ на таблицю Category)

Category (категорії) — з полями:
-id (Primary Key)
-name (назва категорії)

Створи зв'язок One-to-Many між таблицями Category та Product (одна категорія може мати кілька продуктів).

Напиши методи:
Для Product: метод, який перевіряє, чи є продукт дорогим (ціна більше 100).

Для Category: метод, який повертає список всіх продуктів у категорії.

Створи кілька об'єктів:
Кілька категорій (наприклад, "Електроніка", "Одяг").
Кілька продуктів у цих категоріях.

Перевір, як працюють методи для пошуку всіх продуктів у категорії та перевірки, чи дорогий продукт.
"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///files/shop.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    products = relationship('Product', back_populates='category')

    def get_products(self):
        return self.products

    def __repr__(self):
        return f'<Категорія(назва="{self.name}")>'


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(600), nullable=False)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')

    def is_expensive(self):
        if self.price > 600:
            return True
        else:
            return False

    def __repr__(self):
        return f'<Продукт(назва="{self.name}", ціна={self.price})>'

Base.metadata.create_all(engine)

with Session() as session:
    if session.query(Category).first() is None:
        print('База даних порожня. Давайте створимо')

        category_electronics = Category(name='Електроніка')
        category_clothing = Category(name='Одяг')

        product1 = Product(name='Смартфон', price=15000, category=category_electronics)
        product2 = Product(name='Навушники', price=800, category=category_electronics)
        product3 = Product(name='Футболка', price=325, category=category_clothing)
        product4 = Product(name='Джинси', price=520, category=category_clothing)

        session.add_all([product1, product2, product3, product4])
        session.commit()
        print('Дані успішно збережено.')
    else:
        print('База даних вже містить дані.')


print('\n' + '=' * 50)
print('Перевірка роботи методів:')
print('=' * 50)

with Session() as session:
    print('\n--- Перевірка, чи є продукт дорогим (ціна > 600) ---')

    all_products = session.query(Product).all()
    for product in all_products:
        if product.is_expensive():
            result_text = 'Так'
        else:
            result_text = 'Ні'
        print(f'Продукт: "{product.name}", Ціна: {product.price}, Дорогий: {result_text}')


    print('\n--- Пошук всіх продуктів у кожній категорії ---')
    all_categories = session.query(Category).all()
    for category in all_categories:
        print(f'\nПродукти в категорії "{category.name}": ')

        products_in_category = category.get_products()
        if products_in_category:
            for product in products_in_category:
                print(f'  - {product.name} (Ціна: {product.price})')
        else:
            print('  (немає продуктів)')
