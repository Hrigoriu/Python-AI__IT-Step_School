import telebot  # Імпортуємо pyTelegramBotAPI
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

shop_manager = ShopManager()    # Ініціалізатор магазину

# --- Функції для створення клавіатур ---

def create_main_reply_keyboard() -> types.ReplyKeyboardMarkup:
    """Метод, який створює головну Reply клавіатуру з основними пунктами меню."""
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_catalog = types.KeyboardButton('🛍️ Каталог')
    btn_cart = types.KeyboardButton('🛒 Кошик')
    btn_orders = types.KeyboardButton('📦 Мої замовлення')
    btn_help = types.KeyboardButton('ℹ️ Допомога')
    markup.add(btn_catalog, btn_cart, btn_orders, btn_help)
    return markup


def create_categories_markup() -> types.InlineKeyboardMarkup:
    """Метод, який створює Inline клавіатуру з категоріями товарів."""
    markup = types.InlineKeyboardMarkup()
    categories = shop_manager.get_categories()
    for category in categories:
        markup.add(types.InlineKeyboardButton(text=f'📄 {category}', callback_data=f'cat:{category}'))
    return markup

def create_products_markup(category_name: str) -> types.InlineKeyboardMarkup:
    """Метод, який створює Inline клавіатуру з товарами певної категорії."""
    markup = types.InlineKeyboardMarkup()
    products = shop_manager.get_products_by_category(category_name)

    if not products:
        markup.add(types.InlineKeyboardButton(text='Немає товарів у цій категорії.', callback_data='ignore'))
    else:
        for product in products:
             button_text = f'🛍️ "{product.name}" - {product.price:.2f} грн.'
             markup.add(types.InlineKeyboardButton(text=button_text, callback_data=f'prod:{product.id}'))

    markup.add(types.InlineKeyboardButton(text='← До категорій', callback_data='back_to_cats'))  # Кнопка "Назад до категорій"
    return markup

def create_product_details_markup(product_id: int) -> types.InlineKeyboardMarkup:
    """Метод, який створює Inline клавіатуру для сторінки товару (додати в кошик)."""
    markup = types.InlineKeyboardMarkup()
    product = shop_manager.get_product_by_id(product_id)
    if not product:
        markup.add(types.InlineKeyboardButton(text='Помилка: Товар не знайдено.', callback_data='ignore'))
        return markup

    markup.add(types.InlineKeyboardButton(text='🛒 Додати в кошик', callback_data=f'add:{product_id}'))
    markup.add(types.InlineKeyboardButton(text='← До каталогу', callback_data='back_to_cats'))
    return markup

def create_cart_markup(chat_id: int) -> types.InlineKeyboardMarkup:
    """Метод, який створює Inline клавіатуру для кошика (видалити, оформити)."""
    markup = types.InlineKeyboardMarkup()
    cart = shop_manager.get_cart(chat_id)

    if not cart.items:
        return markup

    markup.add(types.InlineKeyboardButton(text='--- Видалити товари ---', callback_data='ignore'))
    for item in cart.get_items():
        button_text = f'❌ "{item.product.name}" ({item.quantity} шт.)'
        markup.add(types.InlineKeyboardButton(text=button_text, callback_data=f'remove:{item.product.id}'))

    markup.add(types.InlineKeyboardButton(text='✅ Оформити замовлення', callback_data='checkout'))
    markup.add(types.InlineKeyboardButton(text='← До каталогу', callback_data='back_to_cats'))
    return markup

def get_welcome_message(user_name: str) -> str:
     """Метод, який формує текст привітального повідомлення."""
     return f"""
Привіт, {user_name}! Я бот-"Магазин".
Ти можеш переглянути наш каталог, додати товари в кошик та оформити замовлення.

Перед оформленням замовлення, будь ласка, зареєструйся:
register;Ім'я;Телефон;Адреса
(наприклад: `register;Іван;0991234567;Київ, вул. Тестова 1`)

Використовуй кнопки меню нижче, щоб керувати мною 👇
"""

# --- Обробники команд ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome_command(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'
    bot.send_message(chat_id, get_welcome_message(user_name), reply_markup=create_main_reply_keyboard(), parse_mode='Markdown')

@bot.message_handler(commands=['register'])
def register_user_command(message):
    chat_id = message.chat.id
    # Розбиваємо текст повідомлення: ігноруємо першу частину (команду), беремо решту.
    # Очікуємо формат: register;Ім'я;Телефон;Адреса
    # Якщо текст = "register", parts буде порожнім списком після [1:]
    parts = message.text.split(';')[1:]

    if len(parts) == 3:
        name, phone, address = [p.strip() for p in parts]
        if shop_manager.register_user(chat_id, name, phone, address):
            bot.send_message(chat_id, f'Вітаємо, {name}! Ти успішно зареєстрований.')
        else:
            bot.send_message(chat_id, 'Сталася помилка під час реєстрації. Спробуй ще раз.')
    else:
        bot.send_message(chat_id, 'Будь ласка, використовуй формат: `register;Ім\'я;Телефон;Адреса`', parse_mode='Markdown')
        bot.send_message(chat_id, 'Використовуй кнопки меню нижче:', reply_markup=create_main_reply_keyboard())


# --- Обробники кнопок Reply Keyboard ---

@bot.message_handler(func=lambda message: message.text == '🛍️ Каталог' and message.content_type == 'text')
def show_catalog_button(message):
    chat_id = message.chat.id
    markup = create_categories_markup()
    bot.send_message(chat_id, 'Обери категорію товарів:', reply_markup=markup) # Надсилаємо Inline клавіатуру, Reply автоматично приховується

@bot.message_handler(func=lambda message: message.text == '🛒 Кошик' and message.content_type == 'text')
def show_cart_button(message):
    chat_id = message.chat.id
    cart = shop_manager.get_cart(chat_id)
    markup = create_cart_markup(chat_id) # Це Inline клавіатура кошика

    if not cart.items:
        # Якщо кошик порожній, надсилаємо повідомлення і повертаємо головну Reply клавіатуру
        bot.send_message(chat_id, 'Ваш кошик порожній. Додай щось з Каталогу!', reply_markup=create_main_reply_keyboard())
    else:
        # Якщо кошик не порожній, надсилаємо вміст з Inline клавіатурою кошика
        bot.send_message(chat_id, f'Ваш кошик:\n{cart}', reply_markup=markup) # Надсилаємо Inline клавіатуру, Reply автоматично приховується

@bot.message_handler(func=lambda message: message.text == '📦 Мої замовлення' and message.content_type == 'text')
def show_orders_button(message):
    chat_id = message.chat.id
    orders = shop_manager.get_user_orders(chat_id)

    if not orders:
        bot.send_message(chat_id, 'У вас ще немає замовлень.', reply_markup=create_main_reply_keyboard()) # Повертаємо головну клавіатуру
    else:
        orders_text = '📦 "Ваші замовлення:"\n\n' + '\n---\n'.join(str(order) for order in orders)
        bot.send_message(chat_id, orders_text, reply_markup=create_main_reply_keyboard()) # Повертаємо головну клавіатуру

@bot.message_handler(func=lambda message: message.text == 'ℹ️ Допомога' and message.content_type == 'text')
def send_help_button(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'
    bot.send_message(chat_id, get_welcome_message(user_name), reply_markup=create_main_reply_keyboard(), parse_mode='Markdown')


# --- Обробник натискання кнопок (Callback Query) ---

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id # ID повідомлення, до якого прив'язана кнопка
    callback_data = call.data

    # Функція для зручного відповіді на callback
    def answer_callback(text: str = None, show_alert: bool = False):
        try:
            bot.answer_callback_query(call.id, text=text, show_alert=show_alert)
        except Exception as e:
            print(f'Помилка при відповіді на callback query {call.id}: {e}')


    if callback_data == 'ignore':
        answer_callback('Дія недоступна.')
        return

    # Обробка навігації по каталогу
    if callback_data.startswith('cat:'):
        category_name = callback_data.split(':', 1)[1]
        markup = create_products_markup(category_name)
        text = f'Товари в категорії "{category_name}":'
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup)
            answer_callback()
        except telebot.apihelper.ApiTelegramException as e:
             print(f'Помилка редагування повідомлення {message_id} для {chat_id}: {e}')
             answer_callback('Не вдалося оновити. Спробуйте знову через меню.')
             bot.send_message(chat_id, 'Обери категорію товарів:', reply_markup=create_categories_markup())


    elif callback_data.startswith('prod:'):
        try:
            product_id = int(callback_data.split(':', 1)[1])
            product = shop_manager.get_product_by_id(product_id)
            if product:
                markup = create_product_details_markup(product_id)
                text = f'🛍️ "{product.name}"\nКатегорія: "{product.category}"\nЦіна: {product.price:.2f} грн.'
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup)
                answer_callback()
            else:
                 bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Помилка: Товар не знайдено.')
                 answer_callback('Помилка: Товар не знайдено.')
        except (ValueError, IndexError) as e:
             print(f'Помилка при обробці prod callback {callback_data}: {e}')
             answer_callback('Помилка при виборі товару.')
        except telebot.apihelper.ApiTelegramException as e:
             print(f'Помилка редагування повідомлення {message_id} для {chat_id}: {e}')
             answer_callback('Не вдалося оновити. Спробуйте знову через меню.')


    elif callback_data == 'back_to_cats':
        markup = create_categories_markup()
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Обери категорію товарів:', reply_markup=markup)
            answer_callback() # Відповідаємо без повідомлення
        except telebot.apihelper.ApiTelegramException as e:
             print(f'Помилка редагування повідомлення {message_id} для {chat_id}: {e}')
             answer_callback('Не вдалося повернутись. Спробуйте знову через меню.')
             bot.send_message(chat_id, 'Обери категорію товарів:', reply_markup=create_categories_markup())


    # Обробка дій з кошиком
    elif callback_data.startswith('add:'):
        try:
            product_id = int(callback_data.split(':', 1)[1])
            added_product = shop_manager.add_to_cart(chat_id, product_id, quantity=1)
            if added_product:
                answer_callback(f'🎉 Товар "{added_product.name}" додано до кошика.')
            else:
                answer_callback('Помилка при додаванні товару.', show_alert=True)
        except (ValueError, IndexError) as e:
             print(f'Помилка при обробці add callback {callback_data}: {e}')
             answer_callback('Помилка при додаванні.', show_alert=True)

    elif callback_data.startswith('remove:'):
        try:
            product_id = int(callback_data.split(':', 1)[1])
            removed_product = shop_manager.remove_from_cart(chat_id, product_id)
            if removed_product:
                answer_callback(f'🗑️ Товар "{removed_product.name}" видалено з кошика.')

                cart = shop_manager.get_cart(chat_id)
                markup = create_cart_markup(chat_id)

                # Перевіряємо, чи кошик став порожнім
                if not cart.items:
                    # Якщо кошик став порожнім, редагуємо повідомлення і прибираємо Inline клавіатуру
                    text = 'Ваш кошик порожній. Додай щось з Каталогу!'
                    try:
                         bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=None)
                         bot.send_message(chat_id, 'Використовуй кнопки меню нижче:', reply_markup=create_main_reply_keyboard())
                    except telebot.apihelper.ApiTelegramException as e:
                         print(f'Помилка редагування повідомлення кошика {message_id} для {chat_id}: {e}')
                         bot.send_message(chat_id, text, reply_markup=create_main_reply_keyboard())

                else:
                    text = f'Ваш кошик:\n{cart}'
                    try:
                        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup)
                    except telebot.apihelper.ApiTelegramException as e:
                        print(f'Помилка редагування повідомлення кошика {message_id} для {chat_id}: {e}')
                        bot.send_message(chat_id, text, reply_markup=markup)

            else:
                answer_callback('Помилка при видаленні товару.', show_alert=True)
        except (ValueError, IndexError) as e:
             print(f'Помилка при обробці remove callback {callback_data}: {e}')
             answer_callback('Помилка при видаленні.', show_alert=True)


    elif callback_data == 'checkout':
        user = shop_manager.get_user(chat_id)

        if not user.is_registered:
            answer_callback('Будь ласка, зареєструйтесь (register) перед оформленням замовлення.', show_alert=True)
            bot.send_message(chat_id, 'Для оформлення замовлення потрібно зареєструватись. Використовуйте команду: `register;Ім\'я;Телефон;Адреса`', parse_mode='Markdown')
            return

        cart = shop_manager.get_cart(chat_id)
        if not cart.items:
             answer_callback('Ваш кошик порожній. Додайте товари перед оформленням.', show_alert=True)
             try:
                 bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Ваш кошик порожній. Додай щось з Каталогу!', reply_markup=None)
             except Exception:
                 pass
             bot.send_message(chat_id, 'Використовуй кнопки меню нижче:', reply_markup=create_main_reply_keyboard())
             return

        order = shop_manager.place_order(chat_id) # Оформлюємо замовлення та очищаємо кошик

        if order:
            answer_callback(f'Замовлення №{order.id} успішно оформлено!')

            # Редагуємо повідомлення кошика на підтвердження замовлення
            confirmation_text = f'🎉 Замовлення №{order.id} успішно оформлено!\n\n{order}'
            try:
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=confirmation_text, reply_markup=None) # Прибираємо Inline клавіатуру кошика
            except telebot.apihelper.ApiTelegramException as e:
                 print(f'Помилка редагування повідомлення кошика {message_id} для {chat_id} після оформлення: {e}')
                 bot.send_message(chat_id, confirmation_text, reply_markup=None)

            bot.send_message(chat_id, 'Дякуємо за замовлення!\nВикористовуй кнопки меню нижче 👇', reply_markup=create_main_reply_keyboard())

        else:
            answer_callback('Не вдалося оформити замовлення.', show_alert=True)


# --- Обробник інших текстових повідомлень ---
@bot.message_handler(func=lambda message: message.content_type == 'text' and
                                         message.text not in ['🛍️ Каталог', '🛒 Кошик', '📦 Мої замовлення', 'ℹ️ Допомога'] and
                                         not message.text.startswith('/') # Ігноруємо команди, вони обробляються іншими хендлерами
)
def handle_other_messages(message):
     chat_id = message.chat.id
     bot.send_message(chat_id, 'Я бот-магазин. Використовуй кнопки меню нижче 👇', reply_markup=create_main_reply_keyboard())


# --- Запуск бота ---
print('Бот Магазин запущено...')
bot.polling(none_stop=True)