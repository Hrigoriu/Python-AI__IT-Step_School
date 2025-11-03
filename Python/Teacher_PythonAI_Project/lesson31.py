import telebot as tb
from telebot import types  # окремо імпортуємо types

from bot_service import Service  # сюди свій файл, де лежить Service

from functools import partial  # спеціальний "декоратор", що дозволяє передавати функцію та її аргументи окремо


TOKEN = ''  # ваш токен сюди, бо цей мій, він не спрацює :)

bot = tb.TeleBot(TOKEN)
service = Service()

admin_id = 0  # ваш id сюди


def send_question(user_id: int, username: str):
    question_data = service.send_question(user_id)

    if not question_data:
        score = service.end_quiz(user_id)

        bot.send_message(user_id, text=f'Вікторину закінчено! Ваш результат: {score}!')
        bot.send_message(admin_id, text=f'{username} пройшов вікторину та отримав {score}!')
        return

    markup = types.InlineKeyboardMarkup()

    for index, option in enumerate(question_data['options']):
        markup.add(types.InlineKeyboardButton(text=option, callback_data=f'quizanswer_{index}'))

    bot.send_message(user_id, text=question_data['question'], reply_markup=markup)


def send_password(message: types.Message):
    password_len = message.text
    password = service.generate_password(password_len)

    if not password:
        bot.send_message(message.chat.id, text='Довжина паролю невірна, або ви ввели не число!')
        return

    bot.send_message(message.chat.id, text=f'Ваш пароль: {password}')


def send_admin_answer(message: types.Message, user_id: int):
    bot.send_message(user_id, text=f'Відповідь адміна на твою оцінку: "{message.text}"')


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    btn_1 = types.KeyboardButton('Генерація паролю🧨')
    btn_2 = types.KeyboardButton('Відгуки😎')
    btn_3 = types.KeyboardButton('Вікторина🤓')
    btn_4 = types.KeyboardButton('Цікаві сайти😉')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # markup - дошка для кнопок, яка надсилає їх користувачу

    markup.add(btn_1, btn_2)  # кожен add - один ряд
    markup.add(btn_3, btn_4)

    bot.send_message(message.chat.id,
                     text='Привіт! Я тестовий бот!🤓',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message: types.Message):
    message_text = message.text  # дістаємо текст повідомлення
    chat_id = message.chat.id  # дістаємо айді чату (по якому будемо надсилати відповіді)
    print(chat_id)

    match message_text:
        case 'Генерація паролю🧨':
            bot_message = bot.send_message(chat_id, text='ОК! Надішли довжину паролю від 8 до 35😀')

            bot.register_next_step_handler(bot_message, send_password)
        case 'Відгуки😎':
            btn_5 = types.InlineKeyboardButton(text='5😍', callback_data=f'grade_5')
            btn_4 = types.InlineKeyboardButton(text='4😊', callback_data=f'grade_4')
            btn_3 = types.InlineKeyboardButton(text='3😓', callback_data=f'grade_3')
            btn_2 = types.InlineKeyboardButton(text='2🤢', callback_data=f'grade_2')
            btn_1 = types.InlineKeyboardButton(text='1🤮', callback_data=f'grade_1')

            markup = types.InlineKeyboardMarkup()
            markup.add(btn_5, btn_4, btn_3, btn_2, btn_1, row_width=1)

            bot.send_message(chat_id, text='Обери оцінку, яку поставиш мені:', reply_markup=markup)
        case 'Вікторина🤓':
            markup = types.InlineKeyboardMarkup()
            titles = service.get_titles(chat_id)

            for t in titles:
                markup.add(types.InlineKeyboardButton(text=t, callback_data=f'quizstart_{t}'))

            bot.send_message(chat_id, text='Обери тему вікторини!', reply_markup=markup)
        case 'Цікаві сайти😉':
            btn_1 = types.InlineKeyboardButton(text='Пакетний менеджер Python', url='https://pypi.org/')
            btn_2 = types.InlineKeyboardButton(text='Офіційний сайт Python', url='https://www.python.org/')

            markup = types.InlineKeyboardMarkup()  # маркап для кнопок, що знаходяться у чаті (не для клавіатурних)
            markup.add(btn_1, btn_2, row_width=1)

            bot.send_message(chat_id, text='Ось цікаві сайти для тебе:', reply_markup=markup)
        case _:
            bot.send_message(chat_id, text='Я тебе не розумію(')


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('grade'))  # обробник callback`у від кнопки. func -
def get_grade(callback: types.CallbackQuery):
    grade = callback.data[-1]   # вміст самого колбеку (дані кнопки)
    username = callback.from_user.username
    user_id = callback.from_user.id

    call_id = callback.id  # id колбеку (треба для реєстрації відповіді від бота)

    bot.answer_callback_query(call_id, text='Дякую за оцінку!')  # офіційна відповідь від боту на колбек (закриває прогрузку кнопки)
    bot.edit_message_text(chat_id=callback.message.chat.id,
                          message_id=callback.message.id,
                          text='Оцінку відправлено!',
                          reply_markup=types.InlineKeyboardMarkup())

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Відповісти: ', callback_data=f'adminanswer_{user_id}'))

    bot.send_message(admin_id, text=f'{username} поставив тобі оцінку {grade}!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('adminanswer'))  # обробник callback`у від кнопки. func -
def admin_answer(callback: types.CallbackQuery):
    user_id = int(callback.data.split('_')[1])
    call_id = callback.id

    bot.answer_callback_query(call_id, text='Пиши свою відповідь для користувача!')
    bot.edit_message_text(chat_id=callback.message.chat.id,
                              message_id=callback.message.id,
                              text='Пиши відповідь нижче!',
                              reply_markup=types.InlineKeyboardMarkup())

    bot.register_next_step_handler(callback.message, partial(send_admin_answer, user_id=user_id))


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('quizstart'))  # обробник callback`у від кнопки. func -
def start_quiz(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    quiz_name = callback.data.split('_')[1]

    bot.answer_callback_query(callback.id, text='Вікторину розпочато!')
    service.start_quiz(user_id, quiz_name)
    send_question(user_id, callback.from_user.username)  # велосипед, вибачте


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('quizanswer'))  # обробник callback`у від кнопки. func -
def check_answer(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_answer_index = int(callback.data.split('_')[1])

    bot.answer_callback_query(callback.id, text='Відповідь надіслано!')

    answer_result = service.check_answer(user_id, user_answer_index)
    bot.edit_message_text(chat_id=callback.message.chat.id,
                          message_id=callback.message.id,
                          text='Відповідь правильна!' if answer_result else 'Відповідь неправильна!',
                          reply_markup=types.InlineKeyboardMarkup())
    send_question(user_id, callback.from_user.username)  # велосипед, вибачте


bot.polling(none_stop=True)  # бот пінгує в нескінченному режимі

