import telebot
from telebot import types
from shop_manager import ShopManager

TOKEN ='7054259200:AAFVaeLLmC4NtGv5aPbZawgRVYn0cHr1MWs' # мій токен :)
#name: «Магазин»
#bot: @magazin_HW_bot

if not TOKEN:
    print('Помилка: Не знайдено "@magazin_HW_bot".')
    print('Будь ласка, встановіть її перед запуском.')
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Ініціалізуємо наш менеджер магазину
shop_manager = ShopManager()

def create_categories_markup() -> types.InlineKeyboardMarkup:   # Метод, який створює клавіатуру з категоріями товарів.
    markup = types.InlineKeyboardMarkup()
    categories = shop_manager.get_categories()
    for category in categories:
        markup.add(types.InlineKeyboardButton(text=category, callback_data=f'cat:{category}'))
    return markup

def create_products_markup(category_name: str) -> types.InlineKeyboardMarkup:   # Метод, який створює клавіатуру з товарами певної категорії
    markup = types.InlineKeyboardMarkup()
    products = shop_manager.get_products_by_category(category_name)
    if not products:
        markup.add(types.InlineKeyboardButton(text='Немає товарів у цій категорії.', callback_data='ignore'))
        return markup

    for product in products:
        markup.add(types.InlineKeyboardButton(text=f' "{product.name}" - {product.price:.2f} грн.', callback_data=f'prod:{product.id}'))
    markup.add(types.InlineKeyboardButton(text='← Категорії', callback_data='back_to_cats'))  # Кнопка "Назад до категорій"
    return markup

def create_product_details_markup(product_id: int) -> types.InlineKeyboardMarkup:   # Метод, який cтворює клавіатуру для сторінки товару
    markup = types.InlineKeyboardMarkup()
    product = shop_manager.get_product_by_id(product_id)
    if not product:
        markup.add(types.InlineKeyboardButton(text='Помилка: Товар не знайдено.', callback_data='ignore'))
        return markup

    markup.add(types.InlineKeyboardButton(text='➕ Додати в кошик', callback_data=f'add:{product_id}'))  # Кнопка "Назад до товарів категорії"
    markup.add(types.InlineKeyboardButton(text="'← Назад'", callback_data='back_to_cats'))
    return markup

def create_cart_markup(chat_id: int) -> types.InlineKeyboardMarkup: # Метод, який cтворює клавіатуру для кошика (видалити, оформити).
    markup = types.InlineKeyboardMarkup()
    cart = shop_manager.get_cart(chat_id)

    if not cart.items:
        markup.add(types.InlineKeyboardButton(text='Кошик порожній.', callback_data='ignore'))
        return markup

    markup.add(types.InlineKeyboardButton(text='--- Видалити товари ---', callback_data='ignore'))    # Кнопки для видалення товарів (по одній на товар)
    for item in cart.get_items():
        markup.add(types.InlineKeyboardButton(text=f' "{item.product.name}" ({item.quantity} шт.) ❌', callback_data=f'remove:{item.product.id}'))
    markup.add(types.InlineKeyboardButton(text='✅ Оформити замовлення', callback_data='checkout'))
    return markup


# --- Обробники команд ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):  # Метод, який обробляє команди /start та /help.
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'
    welcome_message = f"""
Привіт, {user_name}! Я бот-"Магазин".
Ти можеш переглянути наш каталог, додати товари в кошик та оформити замовлення.

Перед оформленням замовлення, будь ласка, зареєструйся:
/register Ім'я;Телефон;Адреса
(наприклад: '/register Іван;0991234567;Київ, вул. Тестова 1')

Основні команди:
/catalog - Переглянути каталог товарів
/cart - Подивитись свій кошик
/orders - Мої замовлення
/help - Допомога
"""
    bot.send_message(chat_id, welcome_message)

@bot.message_handler(commands=['register'])
def register_user_command(message): # Метод, який обробляє команду /register.
    chat_id = message.chat.id
    parts = message.text.split(';')[1:] # Ігноруємо саму команду '/register'

    if len(parts) == 3:
        name, phone, address = [p.strip() for p in parts]
        if shop_manager.register_user(chat_id, name, phone, address):
            bot.send_message(chat_id, f'Вітаємо, {name}! Ти успішно зареєстрований.')
        else:
            bot.send_message(chat_id, 'Сталася помилка під час реєстрації. Спробуй ще раз.')
    else:
        bot.send_message(chat_id, 'Будь ласка, використовуй формат: /register Ім\'я;Телефон;Адреса')


@bot.message_handler(commands=['catalog'])
def show_catalog(message):  # Метод, який обробляє команду /catalog - показує категорії.
    chat_id = message.chat.id
    markup = create_categories_markup()
    bot.send_message(chat_id, 'Обери категорію товарів:', reply_markup=markup)

@bot.message_handler(commands=['cart'])
def show_cart(message): # Метод, який обробляє команду /cart - показує вміст кошика.
    chat_id = message.chat.id
    cart = shop_manager.get_cart(chat_id)
    markup = create_cart_markup(chat_id)

    if not cart.items:
        bot.send_message(chat_id, 'Ваш кошик порожній. Додай щось з /catalog!')
    else:
        bot.send_message(chat_id, f'Ваш кошик:\n{cart}', reply_markup=markup)

@bot.message_handler(commands=['orders'])
def show_orders(message):   # Метод, який обробляє команду /orders - показує історію замовлень.
    chat_id = message.chat.id
    orders = shop_manager.get_user_orders(chat_id)

    if not orders:
        bot.send_message(chat_id, 'У вас ще немає замовлень.')
    else:
        orders_text =' "Ваші замовлення:"\n\n' + '\n---\n'.join(str(order) for order in orders)
        bot.send_message(chat_id, orders_text)


# --- Обробник натискання кнопок (Callback Query) ---

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):    # Метод, який обробляє натискання Inline кнопок.
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    callback_data = call.data

    def answer(ansr: str):
        bot.answer_callback_query(call.id, ansr)

    if callback_data == 'ignore':   # Ігноруємо технічні колбеки
        answer('Дія недоступна.')
        return

    if callback_data.startswith('cat:'):    # Обробка навігації
        category_name = callback_data.split(':')[1]
        markup = create_products_markup(category_name)
        products_in_cat = shop_manager.get_products_by_category(category_name)
        text = f'Товари в категорії \"{category_name}\":'
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup)
        answer('Показано товари категорії.')

    elif callback_data.startswith('prod:'):
        try:
            product_id = int(callback_data.split(':')[1])
            product = shop_manager.get_product_by_id(product_id)
            if product:
                markup = create_product_details_markup(product_id)
                text = f' "{product.name}"\nКатегорія: "{product.category}"\nЦіна: {product.price:.2f} грн.'
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup)
                answer('Деталі товару.')
            else:
                 bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Помилка: Товар не знайдено.')
                 answer('Помилка.')
        except (ValueError, IndexError):
             answer('Помилка при виборі товару.')

    elif callback_data == 'back_to_cats':
        markup = create_categories_markup()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Обери категорію товарів:', reply_markup=markup)
        answer('Повернуто до категорій.')

    elif callback_data.startswith('add:'):  # Обробка дій з кошиком
        try:
            product_id = int(callback_data.split(':')[1])
            added_product = shop_manager.add_to_cart(chat_id, product_id, quantity=1) # Додаємо 1 шт
            if added_product:
                answer(f'Товар \"{added_product.name}\" додано до кошика.')
            else:
                answer('Помилка при додаванні товару.')
        except (ValueError, IndexError):
             answer('Помилка при додаванні.')

    elif callback_data.startswith('remove:'):
        try:
            product_id = int(callback_data.split(':')[1])
            removed_product = shop_manager.remove_from_cart(chat_id, product_id)
            if removed_product:
                answer(f'Товар \"{removed_product.name}\" видалено з кошика.')
                cart = shop_manager.get_cart(chat_id)   # Оновлюємо повідомлення з кошиком
                markup = create_cart_markup(chat_id)
                text = f'Ваш кошик:\n{cart}' if cart.items else 'Ваш кошик порожній. Додай щось з /catalog!'
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup)
            else:
                answer('Помилка при видаленні товару.')
        except (ValueError, IndexError):
            answer('Помилка при видаленні.')

    elif callback_data == 'checkout':
        user = shop_manager.get_user(chat_id)
        if not user.is_registered:
            answer('Будь ласка, зареєструйтесь (/register) перед оформленням замовлення.')
            return

        order = shop_manager.place_order(chat_id)

        if order:
            answer(f'Замовлення №{order.id} успішно оформлено!')
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Замовлення №{order.id} успішно оформлено!\n{order}') # Редагуємо повідомлення кошика на підтвердження замовлення
        else:
            answer('Не вдалося оформити замовлення. Можливо, кошик порожній?') # Або користувач не зареєстрований


@bot.message_handler(func=lambda message: True)
def handle_other_messages(message): # Метод інших текстових повідомлень
     chat_id = message.chat.id
     bot.send_message(chat_id, 'Я бот-магазин. Використовуй команди: /catalog, /cart, /orders, /register, /help.')


# --- Запуск бота ---
print('Бот Магазин запущено...')
bot.polling(none_stop=True)