import telebot  # Імпортуємо pyTelegramBotAPI
from telebot import types  # Імпортуємо типи для клавіатур та кнопок
from guess_game import GuessGame

TOKEN ='7620696692:AAGd8Uik3jjGGoTo42aBKeagsI47E1N4P6k' # мій токен :)
#name: «Вгадай число»
#bot: @Guess_the_number_HW_bot

if not TOKEN:
    print('Помилка: Не знайдено "@Guess_the_number_HW_bot".')
    print('Будь ласка, встановіть перед запуском.')
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Словник для зберігання активних ігор для кожного користувача.
user_games: dict[int, GuessGame] = {}
"""
'key'-chat_id: 'item1'-об'єкт GuessGame
"""

# --- Функція для створення Reply клавіатури ---

def create_main_reply_keyboard():
    """Створює головну Reply клавіатуру з кнопкою 'Нова гра'."""
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    new_game_button = types.KeyboardButton('Нова гра')
    markup.add(new_game_button)
    return markup

# --- Обробники команд та повідомлень ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'

    welcome_message = f"""
Привіт, {user_name}! Я бот 'Вгадай число'.
Я загадаю число від 1 до 100, а ти маєш його вгадати.

Щоб почати гру, просто натисни кнопку 'Нова гра' нижче.
Якщо ти вже граєш, надсилай мені числа, щоб зробити спробу.
"""
    bot.send_message(chat_id, welcome_message, reply_markup=create_main_reply_keyboard())

# Функція для початку нової гри (викликається з обробників)
def _start_game_for_user(chat_id):
    """Внутрішня функція для логіки початку нової гри."""
    try:
        new_game = GuessGame(1, 100)
        user_games[chat_id] = new_game
        min_num, max_num = new_game.get_range()
        bot.send_message(chat_id, f'Я загадав нове число від {min_num} до {max_num}. Спробуй вгадати!\n\nВводь числа прямо тут:', reply_markup=types.ReplyKeyboardRemove())
    except ValueError as e:
        bot.send_message(chat_id, f'Сталася помилка при створенні гри: {e}', reply_markup=create_main_reply_keyboard())

# Обробник команди newgame
@bot.message_handler(commands=['newgame'])
def start_new_game_command(message):
    chat_id = message.chat.id
    if chat_id in user_games:
         bot.send_message(chat_id, 'Ви вже граєте. Починаємо нову гру.')
         del user_games[chat_id] # Закінчуємо попередню гру, якщо вона була
    _start_game_for_user(chat_id)

# Обробник натискання кнопки "Нова гра"
@bot.message_handler(func=lambda message: message.text == 'Нова гра' and message.content_type == 'text')
def start_new_game_button(message):
    chat_id = message.chat.id
    if chat_id in user_games:
         bot.send_message(chat_id, 'Ви вже граєте. Починаємо нову гру.')
         del user_games[chat_id] # Закінчуємо попередню гру, якщо вона була
    _start_game_for_user(chat_id)


# Обробник команди stopgame
@bot.message_handler(commands=['stopgame'])
def stop_game(message):
    chat_id = message.chat.id
    if chat_id in user_games:
        del user_games[chat_id]
        bot.send_message(chat_id, 'Гра зупинена.', reply_markup=create_main_reply_keyboard())
    else:
        bot.send_message(chat_id, 'Ви зараз не в грі.', reply_markup=create_main_reply_keyboard())


# Обробник будь-яких інших текстових повідомлень (спроб вгадати число)
@bot.message_handler(content_types=['text'])
def handle_guess(message):
    chat_id = message.chat.id
    user_text = message.text

    if user_text.startswith('/') or user_text == 'Нова гра':
         return

    if chat_id not in user_games:
        bot.send_message(chat_id, 'Ти ще не розпочав гру. Натисни кнопку "Нова гра", щоб почати!', reply_markup=create_main_reply_keyboard())
        return

    current_game = user_games[chat_id]

    try:
        guess = int(user_text)
    except ValueError:
        bot.send_message(chat_id, 'Це не схоже на число😉. Будь ласка, надсилай мені тільки числа!')
        return

    min_num, max_num = current_game.get_range()
    if not (min_num <= guess <= max_num):
        bot.send_message(chat_id, f'Будь ласка, введіть число в діапазоні від {min_num} до {max_num}.')
        return

    result = current_game.make_guess(guess)
    attempts = current_game.get_attempts()

    if result == 'correct':
        bot.send_message(chat_id, f'🎉 Чудово! Ти вгадав число ({current_game.secret_number}) за {attempts} спроб!')
        del user_games[chat_id] # Видаляємо гру після завершення
        bot.send_message(chat_id, 'Натисни кнопку "Нова гра", щоб зіграти ще раз!', reply_markup=create_main_reply_keyboard())
    elif result == 'high':
        bot.send_message(chat_id, 'Занадто високо! Спробуй ще.')
    elif result == 'low':
        bot.send_message(chat_id, 'Занадто низько! Спробуй ще.')


# --- Запуск бота ---
print('Бот Вгадай число запущено...')
bot.polling(none_stop=True, interval=0, timeout=20)