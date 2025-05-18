import telebot
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

# --- Обробники команд ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):  # Метод, який обробляє команди /start та /help.
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'
    welcome_message = f"""
Привіт, {user_name}! Я бот "Анонімний чат".
Зі мною ти можеш спілкуватися з випадковим співрозмовником анонімно.

Використовуй команду /find, щоб знайти співрозмовника.
Використовуй команду /stop, щоб завершити поточний чат.
"""
    bot.send_message(chat_id, welcome_message)

@bot.message_handler(commands=['find'])
def find_partner_command(message):  # Метод, який обробляє команду /find - шукає або ставить у чергу.
    chat_id = message.chat.id
    status = chat_manager.find_partner(chat_id)

    if status == 'Очікує':
        bot.send_message(chat_id, 'Шукаємо співрозмовника... Зачекайте, будь ласка.')
    elif status == 'в парі!':
        partner_id = chat_manager.get_partner(chat_id)
        bot.send_message(chat_id, 'Знайдено співрозмовника! Можете почати спілкування. Щоб зупинити чат, напишіть /stop.')
        if partner_id:
             bot.send_message(partner_id, 'Знайдено співрозмовника! Можете почати спілкування. Щоб зупинити чат, напишіть /stop.')
    elif status == 'В активному чаті:':
        bot.send_message(chat_id, 'Ви вже спілкуєтеся. Щоб знайти нового співрозмовника, спершу напишіть /stop.')
    elif status == 'уже очікує':
        bot.send_message(chat_id, 'Ви вже в черзі на пошук співрозмовника. Зачекайте, будь ласка.')


@bot.message_handler(commands=['stop'])
def end_chat_command(message):  # Метод, який обробляє команду /stop - завершує чат.
    chat_id = message.chat.id
    partner_id = chat_manager.end_chat(chat_id)

    if partner_id is not None:
        bot.send_message(chat_id, 'Чат завершено. Щоб знайти нового співрозмовника, напишіть /find.')
        bot.send_message(partner_id, 'Співрозмовник покинув чат. Щоб знайти нового, напишіть /find.')
    elif chat_manager.waiting_user != chat_id and partner_id is None:
        bot.send_message(chat_id, 'Ви зараз не в чаті і не очікуєте. Напишіть /find, щоб розпочати.')
    else:
        bot.send_message(chat_id, 'Ви покинули чергу пошуку.')


@bot.message_handler(content_types=['text', 'sticker', 'photo', 'video', 'voice', 'audio', 'document'])
def handle_messages(message):   # Метод, який обробляє будь-які повідомлення і пересилає їх співрозмовнику, якщо є активний чат.
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
        bot.send_message(chat_id, 'Ви не в активному чаті. Напиши /find, щоб знайти співрозмовника.')


# --- Запуск бота ---
print('Бот Анонімний чат запущено...')
bot.polling(none_stop=True)