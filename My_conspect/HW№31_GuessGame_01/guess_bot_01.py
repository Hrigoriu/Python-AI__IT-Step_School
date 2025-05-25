import telebot  # Імпортуємо pyTelegramBotAPI
from guess_game_01 import GuessGame  # Імпортуємо наш клас гри

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

# --- Обробники команд ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):  #Метод, який починає старт
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'

    welcome_message = f"""
Привіт, {user_name}! Я бот 'Вгадай число'.
Я загадаю число від 1 до 100, а ти маєш його вгадати.
Використовуй команду /newgame, щоб почати нову гру.
Просто надсилай мені числа, щоб зробити спробу.

Бажаю успіхів!
"""
    bot.send_message(chat_id, welcome_message)


@bot.message_handler(commands=['newgame'])
def start_new_game(message):    #Метод для початку нової гри
    chat_id = message.chat.id

    try:
        new_game = GuessGame(1, 100)
        user_games[chat_id] = new_game
        min_num, max_num = new_game.get_range()
        bot.send_message(chat_id, f'Я загадав нове число від {min_num} до {max_num}. Спробуй вгадати!')
    except ValueError as e:
        bot.send_message(chat_id, f'Сталася помилка при створенні гри: {e}')

@bot.message_handler(func=lambda message: True)
def handle_guess(message):  #Метод для обробки повідомлень коли вгадуєш число
    chat_id = message.chat.id
    user_text = message.text

    if chat_id not in user_games:
        bot.send_message(chat_id, 'Ти ще не розпочав гру. Натисни або напиши /newgame, щоб почати!')
        return

    current_game = user_games[chat_id]

    try:
        guess = int(user_text)
    except ValueError:
        bot.send_message(chat_id, 'Помилка. Це не схоже на число😉. Будь ласка, надсилай мені тільки числа!')
        return
    result = current_game.make_guess(guess)
    attempts = current_game.get_attempts()

    if result == 'correct':
        bot.send_message(chat_id, f'🎉 Чудово! Ти вгадав число ({current_game.secret_number}) за {attempts} спроб!')
        del user_games[chat_id]
        bot.send_message(chat_id, 'Натисни або напиши /newgame, щоб зіграти ще раз!')
    elif result == 'high':
        bot.send_message(chat_id, 'Занадто високо! Спробуй ще.')
    elif result == 'low':
        bot.send_message(chat_id, 'Занадто низько! Спробуй ще.')


# --- Запуск бота ---
print('Бот запущено...')
bot.polling(none_stop=True)