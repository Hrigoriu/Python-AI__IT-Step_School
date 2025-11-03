import telebot  # Імпортуємо pyTelegramBotAPI
from telebot import types  # Імпортуємо типи для клавіатур та кнопок
from chat_manager import ChatManager

TOKEN ='7810385962:AAFPvJYYSaytY030_Bs_S4jv91HrAnXwsAc' # мій токен :)
#name: «Анонімний чат»
#bot: @chat_incognito_HW_bot

if not TOKEN:
    print('Помилка: Не знайдено "@chat_incognito_HW_bot".')
    print('Будь ласка, встановіть її перед запуском.')
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Ініціалізуємо наш менеджер чатів
chat_manager = ChatManager()

# --- Функції для створення клавіатур ---

def create_main_reply_keyboard():
    """Створює головну Reply клавіатуру з кнопкою 'Знайти співрозмовника'."""
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    find_button = types.KeyboardButton('Знайти співрозмовника')
    markup.add(find_button)
    return markup

def create_waiting_inline_keyboard():
    """Створює Inline клавіатуру з кнопкою 'Відмінити пошук'."""
    markup = types.InlineKeyboardMarkup()
    cancel_button = types.InlineKeyboardButton('Відмінити пошук', callback_data='cancel_search')
    markup.add(cancel_button)
    return markup

def create_chat_inline_keyboard():
    """Створює Inline клавіатуру з кнопкою 'Зупинити чат'."""
    markup = types.InlineKeyboardMarkup()
    stop_button = types.InlineKeyboardButton('Зупинити чат', callback_data='stop_chat')
    markup.add(stop_button)
    return markup

# --- Обробники команд та повідомлень ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'
    welcome_message = f"""
Привіт, {user_name}! Я бот "Анонімний чат".
Зі мною ти можеш спілкуватися з випадковим співрозмовником анонімно.

Використовуй кнопку "Знайти співрозмовника", щоб почати пошук.
Якщо ти вже в чаті або очікуєш, ти побачиш відповідні опції.
"""
    # Надсилаємо привітання разом з головною Reply клавіатурою
    bot.send_message(chat_id, welcome_message, reply_markup=create_main_reply_keyboard())

# Обробник натискання кнопки "Знайти співрозмовника"
@bot.message_handler(commands=['find'])
@bot.message_handler(func=lambda message: message.text == 'Знайти співрозмовника', content_types=['text'])
def find_partner_action(message):
    chat_id = message.chat.id
    status = chat_manager.find_partner(chat_id)

    if status == 'Очікує':
        # Надсилаємо повідомлення про очікування з Inline кнопкою для скасування
        bot.send_message(chat_id, 'Шукаємо співрозмовника... Зачекайте, будь ласка.', reply_markup=create_waiting_inline_keyboard())
    elif status == 'в парі!':
        partner_id = chat_manager.get_partner(chat_id)
        # Надсилаємо повідомлення про знаходження партнера з Inline кнопкою для зупинки чату
        message_text = 'Знайдено співрозмовника! Можете почати спілкування.'
        bot.send_message(chat_id, message_text, reply_markup=create_chat_inline_keyboard())
        if partner_id:
            bot.send_message(partner_id, message_text, reply_markup=create_chat_inline_keyboard())
    elif status == 'В активному чаті:':
        bot.send_message(chat_id, 'Ви вже спілкуєтеся. Щоб знайти нового співрозмовника, спершу зупиніть поточний чат.', reply_markup=create_main_reply_keyboard())
    elif status == 'уже очікує':
        bot.send_message(chat_id, 'Ви вже в черзі на пошук співрозмовника. Зачекайте, будь ласка.', reply_markup=create_waiting_inline_keyboard())


@bot.message_handler(commands=['stop'])
def end_chat_command(message):       #Метод, який завершує чат.
     chat_id = message.chat.id
     partner_id = chat_manager.end_chat(chat_id)

     if partner_id is not None:
         # Чат завершено
         bot.send_message(chat_id, 'Чат завершено. Щоб знайти нового співрозмовника, натисніть кнопку нижче.', reply_markup=create_main_reply_keyboard())
         bot.send_message(partner_id, 'Співрозмовник покинув чат. Щоб знайти нового, натисніть кнопку нижче.', reply_markup=create_main_reply_keyboard())
     elif chat_manager.waiting_user == chat_id:
         chat_manager.waiting_user = None
         bot.send_message(chat_id, 'Ви покинули чергу пошуку. Щоб знайти нового співрозмовника, натисніть кнопку нижче.', reply_markup=create_main_reply_keyboard())
     else:
         bot.send_message(chat_id, 'Ви зараз не в чаті і не очікуєте. Натисніть кнопку "Знайти співрозмовника", щоб розпочати.', reply_markup=create_main_reply_keyboard())


# Обробник Callback Query від Inline кнопок
@bot.callback_query_handler(func=lambda call: call.data in ['cancel_search', 'stop_chat'])
def callback_inline(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    callback_data = call.data

    # Відповідаємо на callback, щоб прибрати "годинник" з кнопки
    bot.answer_callback_query(call.id)

    if callback_data == "cancel_search":
        # Обробка натискання кнопки "Відмінити пошук"
        if chat_manager.waiting_user == chat_id:
            chat_manager.waiting_user = None
            print(f'Користувач {chat_id} скасував пошук через кнопку.')
            bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                  text='Пошук скасовано. Щоб знайти нового співрозмовника, натисніть кнопку нижче.',
                                  reply_markup=None)
            bot.send_message(chat_id, '...', reply_markup=create_main_reply_keyboard())

        else:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                  text="Ваш статус пошуку змінився.",
                                  reply_markup=None)

    elif callback_data == 'stop_chat':
        partner_id = chat_manager.end_chat(chat_id)

        if partner_id is not None:
            try:
                bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                      text='Чат завершено вами.', reply_markup=None)
            except Exception as e:
                 print(f'Помилка редагування повідомлення для {chat_id}: {e}')
                 bot.send_message(chat_id, 'Чат завершено.', reply_markup=None)

            try:
                 bot.send_message(partner_id, 'Співрозмовник покинув чат. Щоб знайти нового, натисніть кнопку нижче.', reply_markup=create_main_reply_keyboard())
            except Exception as e:
                 print(f'Помилка надсилання повідомлення партнеру {partner_id}: {e}')

            bot.send_message(chat_id, 'Щоб знайти нового співрозмовника, натисніть кнопку нижче.', reply_markup=create_main_reply_keyboard())

        else:
             bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                   text='Ви зараз не в активному чаті.',
                                   reply_markup=None) # Прибираємо Inline клавіатуру
             bot.send_message(chat_id, 'Щоб знайти співрозмовника, натисніть кнопку нижче.', reply_markup=create_main_reply_keyboard())


# Обробник будь-яких інших повідомлень (текст, стікери, медіа тощо)
@bot.message_handler(content_types=['text', 'sticker', 'photo', 'video', 'voice', 'audio', 'document'])
def handle_messages(message):
    chat_id = message.chat.id
    partner_id = chat_manager.get_partner(chat_id)

    if partner_id:
        try:
            bot.copy_message(partner_id, chat_id, message.message_id)
            print(f'Message from {chat_id} copied to {partner_id}.')
        except Exception as e:
            print(f'Error copying message from {chat_id} to {partner_id}: {e}')
            bot.send_message(chat_id, 'Не вдалося переслати повідомлення.')
    else:
        if message.text != 'Знайти співрозмовника':
             bot.send_message(chat_id, 'Ви не в активному чаті. Натисніть кнопку "Знайти співрозмовника", щоб знайти співрозмовника.', reply_markup=create_main_reply_keyboard())


# --- Запуск бота ---
print('Бот Анонімний чат запущено...')
bot.polling(none_stop=True, interval=0, timeout=20)