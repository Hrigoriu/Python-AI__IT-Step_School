# main_bot.py
import os  # Імпортуємо os для безпечного зберігання токена та admin_id
import telebot as tb
from telebot import types

# Імпортуємо наш Service
from bot_service import Service

from functools import partial

# Використовуємо змінні середовища для токена та admin_id (рекомендовано)
# Наприклад, встановіть їх перед запуском скрипта:
# export TELEGRAM_BOT_TOKEN='<ВАШ_ТОКЕН>'
# export TELEGRAM_ADMIN_ID='<ВАШ_ID>'
# Якщо змінні середовища не встановлені, можна використовувати значення за замовчуванням (менш безпечно)
#TOKEN = os.getenv('TELEGRAM_BOT_TOKEN',
                  #'ТОКЕН_ЗА_ЗАМОВЧУВАННЯМ')  # Замініть на ваш токен або використовуйте змінну середовища
#ADMIN_ID_STR = os.getenv('TELEGRAM_ADMIN_ID', '0')  # Замініть на ваш ID або використовуйте змінну середовища
TOKEN ='7791357414:AAFnWP0c3lHIdjloUq8GD0ILL-EcXKOUAV4' # ваш токен сюди :)
bot = tb.TeleBot(TOKEN)
service = Service()

ADMIN_ID_STR = 523793990

try:
    ADMIN_ID = int(ADMIN_ID_STR)
except ValueError:
    print("Помилка: Неправильний формат ADMIN_ID. Встановіть коректне числове значення.")
    ADMIN_ID = 0  # За замовчуванням 0 або інше значення, яке не буде нічиїм chat_id






def send_question(user_id: int, username: str):
    """Надсилає користувачу поточне питання вікторини або завершує її."""
    question_data = service.send_question(user_id)

    if not question_data:
        # Питання закінчились, завершуємо вікторину
        score_result = service.end_quiz(user_id)  # Очікуємо рядок 'score/total'

        # Використання одинарних зовнішніх та подвійних внутрішніх лапок
        bot.send_message(user_id, text=f"'Вікторину закінчено! Ваш результат: {score_result}!'")
        # Використання одинарних зовнішніх та подвійних внутрішніх лапок
        bot.send_message(ADMIN_ID, text=f"'{username}' пройшов вікторину та отримав '{score_result}'!")
        return

    # Питання є, надсилаємо його
    markup = types.InlineKeyboardMarkup()

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок для тексту кнопок
    for index, option in enumerate(question_data['options']):
        # У callback_data передаємо тільки індекс відповіді, service.check_answer
        # використає цей індекс для отримання тексту відповіді
        markup.add(types.InlineKeyboardButton(text=f"'{option}'", callback_data=f'quizanswer_{index}'))

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок для тексту питання
    bot.send_message(user_id, text=f"'{question_data['question']}'", reply_markup=markup)


def send_password(message: types.Message):
    """Генерує та надсилає пароль за отриманою довжиною."""
    password_len_str = message.text  # Отримуємо рядок з довжиною
    password = service.generate_password(password_len_str)

    if password is None:  # Перевіряємо, чи генерація була успішною (повертає None при помилці)
        # Використання одинарних зовнішніх та подвійних внутрішніх лапок
        bot.send_message(message.chat.id, text="'Довжина паролю невірна, або ви ввели не число!'")
        return

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок для тексту паролю
    bot.send_message(message.chat.id, text=f"'Ваш пароль: {password}'")


def send_admin_answer(message: types.Message, user_id: int):
    """Надсилає відповідь адміна користувачу."""
    # Використання одинарних зовнішніх та подвійних внутрішніх лапок для тексту відповіді
    bot.send_message(user_id,
                     text=f"'Відповідь адміна на твою оцінку: \"{message.text}\"'\n\n'Це повідомлення від адміністратора бота.'")


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    """Обробляє команду /start та надсилає головне меню."""
    btn_1 = types.KeyboardButton('Генерація паролю🧨')
    btn_2 = types.KeyboardButton('Відгуки😎')
    btn_3 = types.KeyboardButton('Вікторина🤓')
    btn_4 = types.KeyboardButton('Цікаві сайти😉')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(btn_1, btn_2)
    markup.add(btn_3, btn_4)

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок
    bot.send_message(message.chat.id,
                     text="'Привіт! Я тестовий бот!🤓'",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message: types.Message):
    """Обробляє текстові повідомлення від користувача (кнопки меню)."""
    message_text = message.text
    chat_id = message.chat.id
    # print(f"Received text message from {chat_id}: {message_text}") # Логування для відладки

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок для тексту в case
    match message_text:
        case 'Генерація паролю🧨':
            # Використання одинарних зовнішніх та подвійних внутрішніх лапок
            bot_message = bot.send_message(chat_id, text="'ОК! Надішли довжину паролю від 8 до 35😀'")
            bot.register_next_step_handler(bot_message, send_password)
        case 'Відгуки😎':
            btn_5 = types.InlineKeyboardButton(text="'5😍'", callback_data=f'grade_5')
            btn_4 = types.InlineKeyboardButton(text="'4😊'", callback_data=f'grade_4')
            btn_3 = types.InlineKeyboardButton(text="'3😓'", callback_data=f'grade_3')
            btn_2 = types.InlineKeyboardButton(text="'2🤢'", callback_data=f'grade_2')
            btn_1 = types.InlineKeyboardButton(text="'1🤮'", callback_data=f'grade_1')

            markup = types.InlineKeyboardMarkup()
            markup.add(btn_5, btn_4, btn_3, btn_2, btn_1, row_width=1)

            # Використання одинарних зовнішніх та подвійних внутрішніх лапок
            bot.send_message(chat_id, text="'Обери оцінку, яку поставиш мені:'", reply_markup=markup)
        case 'Вікторина🤓':
            markup = types.InlineKeyboardMarkup()
            titles = service.get_titles(chat_id)  # Отримуємо список назв вікторин

            if titles is None:
                # Використання одинарних зовнішніх та подвійних внутрішніх лапок
                bot.send_message(chat_id, "'Ти вже проходиш вікторину. Заверши поточну, перш ніж почати нову.'")
                return

            if not titles:  # Якщо список тем порожній (наприклад, помилка завантаження quiz_data.json)
                # Використання одинарних зовнішніх та подвійних внутрішніх лапок
                bot.send_message(chat_id, "'Наразі немає доступних вікторин. Спробуй пізніше.'")
                return

            # Використання одинарних зовнішніх та подвійних внутрішніх лапок для тексту кнопок з назвами вікторин
            for t in titles:
                markup.add(types.InlineKeyboardButton(text=f"'{t}'", callback_data=f'quizstart_{t}'))

            # Використання одинарних зовнішніх та подвійних внутрішніх лапок
            bot.send_message(chat_id, text="'Обери тему вікторини!'", reply_markup=markup)
        case 'Цікаві сайти😉':
            btn_1 = types.InlineKeyboardButton(text="'Пакетний менеджер Python'", url='https://pypi.org/')
            btn_2 = types.InlineKeyboardButton(text="'Офіційний сайт Python'", url='https://www.python.org/')

            markup = types.InlineKeyboardMarkup()
            markup.add(btn_1, btn_2, row_width=1)

            # Використання одинарних зовнішніх та подвійних внутрішніх лапок
            bot.send_message(chat_id, text="'Ось цікаві сайти для тебе:'", reply_markup=markup)
        case _:
            # Використання одинарних зовнішніх та подвійних внутрішніх лапок
            bot.send_message(chat_id, text="'Я тебе не розумію('")


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('grade'))
def get_grade(callback: types.CallbackQuery):
    """Обробляє натискання кнопки оцінки."""
    # Отримуємо оцінку (остання цифра в callback_data 'grade_X')
    grade = callback.data[-1]
    username = callback.from_user.username if callback.from_user.username else callback.from_user.first_name
    user_id = callback.from_user.id
    call_id = callback.id

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок
    bot.answer_callback_query(call_id, text="'Дякую за оцінку!'")

    # Редагуємо повідомлення з кнопками оцінки, прибираючи їх
    bot.edit_message_text(chat_id=callback.message.chat.id,
                          message_id=callback.message.id,
                          # Використання одинарних зовнішніх та подвійних внутрішніх лапок
                          text=f"'Оцінку {grade} відправлено!'",  # Можна показати оцінку
                          reply_markup=None)  # Прибираємо клавіатуру

    # Надсилаємо повідомлення адміну
    markup = types.InlineKeyboardMarkup()
    # Кнопка для адміна, щоб відповісти цьому користувачу
    markup.add(types.InlineKeyboardButton(text="'Відповісти:'", callback_data=f'adminanswer_{user_id}'))

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок для тексту повідомлення адміну
    bot.send_message(ADMIN_ID, text=f"'{username}' (ID: {user_id}) поставив тобі оцінку '{grade}'!",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('adminanswer'))
def admin_answer_prompt(callback: types.CallbackQuery):
    """Обробляє натискання кнопки 'Відповісти' адміном."""
    user_id_to_reply = int(callback.data.split('_')[1])
    call_id = callback.id

    # Використання одинарних зовнішніх та подвійних внутрішніх лапок
    bot.answer_callback_query(call_id, text="'Пиши свою відповідь для користувача!'")

    # Редагуємо повідомлення для адміна
    bot.edit_message_text(chat_id=callback.message.chat.id,
                          message_id=callback.message.id,
                          # Використання одинарних зовнішніх та подвійних внутрішніх лапок
                          text=f"'Пиши відповідь для користувача з ID {user_id_to_reply} нижче:'",
                          reply_markup=None)  # Прибираємо клавіатуру

    # Реєструємо наступний крок: очікуємо текст відповіді від адміна
    bot.register_next_step_handler(callback.message, partial(send_admin_answer, user_id=user_id_to_reply))


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('quizstart'))
def start_quiz_callback(callback: types.CallbackQuery):
    """Обробляє натискання кнопки 'Почати вікторину'."""
    user_id = callback.from_user.id
    quiz_name = callback.data.split('_')[1]

    bot.answer_callback_query(callback.id, text="'Вікторину розпочато!'")

    # Спробуємо почати вікторину в service
    if service.start_quiz(user_id, quiz_name):
        # Редагуємо повідомлення з вибором теми
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              message_id=callback.message.id,
                              # Використання одинарних зовнішніх та подвійних внутрішніх лапок
                              text=f"'Вікторина \"{quiz_name}\" розпочата!'",  # Можна показати назву теми
                              reply_markup=None)  # Прибираємо клавіатуру

        # Надсилаємо перше питання
        # Передаємо username для використання в повідомленні адміну в send_question
        send_question(user_id,
                      callback.from_user.username if callback.from_user.username else callback.from_user.first_name)
    else:
        # Вікторина не розпочалась (можливо, вже активна або тема не знайдена)
        # Використання одинарних зовнішніх та подвійних внутрішніх лапок
        bot.edit_message_text(chat_id=callback.message.chat.id,
                              message_id=callback.message.id,
                              text="'Не вдалося розпочати вікторину. Спробуй ще раз або обери іншу тему.'",
                              reply_markup=None)  # Прибираємо клавіатуру
        # Можна також надіслати окреме повідомлення, якщо користувач вже в грі, замість редагування


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('quizanswer'))
def check_answer_callback(callback: types.CallbackQuery):
    """Обробляє натискання кнопки відповіді на питання вікторини."""
    user_id = callback.from_user.id
    # Отримуємо індекс відповіді з callback_data
    user_answer_index = int(callback.data.split('_')[1])
    call_id = callback.id

    # Відповідаємо на callback
    bot.answer_callback_query(call_id, text="'Відповідь надіслано!'")

    # Перевіряємо відповідь в service
    answer_result = service.check_answer(user_id, user_answer_index)  # Очікуємо True/False або None

    # Редагуємо повідомлення з питанням, щоб показати результат відповіді
    if answer_result is not None:
        # Використання одинарних зовнішніх та подвійних внутрішніх лапок
        edit_text = "'Відповідь правильна! ✅'" if answer_result else "'Відповідь неправильна! ❌'"
        try:
            bot.edit_message_text(chat_id=callback.message.chat.id,
                                  message_id=callback.message.id,
                                  text=edit_text,
                                  reply_markup=None)  # Прибираємо кнопки після відповіді
        except Exception as e:
            print(f"Error editing message {callback.message.id} for user {user_id}: {e}")
            # Якщо не вдалося редагувати (наприклад, повідомлення занадто старе або видалене),
            # можна просто надіслати нове повідомлення про результат відповіді.
            # bot.send_message(user_id, text=edit_text)

        # Надсилаємо наступне питання (або завершуємо вікторину)
        # Передаємо username для використання в повідомленні адміну
        send_question(user_id,
                      callback.from_user.username if callback.from_user.username else callback.from_user.first_name)

    else:
        # Якщо answer_result None, значить користувач не в активній вікторині
        # Це може статися, якщо він натиснув кнопку старого питання
        # Використання одинарних зовнішніх та подвійних внутрішніх лапок
        bot.send_message(user_id,
                         "'Ця вікторина вже неактивна або сталася помилка. Спробуй почати нову вікторину / Вікторина🤓.'")


# --- Обробник інших повідомлень (опціонально) ---
# Додаємо обробник для будь-якого тексту, що не є командою або кнопкою меню
@bot.message_handler(
    func=lambda message: message.text not in ['Генерація паролю🧨', 'Відгуки😎', 'Вікторина🤓', 'Цікаві сайти😉'] and
                         message.text[0] != '/')
def handle_other_text(message: types.Message):
    chat_id = message.chat.id
    # Використання одинарних зовнішніх та подвійних внутрішніх лапок
    bot.send_message(chat_id, "'Я не розумію твого повідомлення. Будь ласка, використовуй кнопки меню або команди.'")


# --- Запуск бота ---

print("Бот запущено...")
bot.polling(none_stop=True)