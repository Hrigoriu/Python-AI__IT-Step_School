import telebot as tb
from telebot import types # окремо імпортуємо types
from bot_service import Service # сюди свій файл, де лежить Service
from bot_service import generate_password

TOKEN ='7917068514:AAF7-QdQQNg55_raHMDZN0_yI8ZNxkEfd-M' # ваш токен сюди :)
bot = tb.TeleBot(TOKEN)
#service = Service()

admin_id = 523793990

def send_password(message: types.Message):
    password_len = message.text
    password = generate_password(password_len)

    if not password:
        bot.send_message(message.chat.id, text='Довжина паролю невірна, або ви введи не число!')
        return
    bot.send_message(message.chat.id, text=f'Ваш пароль: {password}')

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    btn_1 = types.KeyboardButton('Генерація паролю😂')
    btn_2 = types.KeyboardButton('Відгуки👌')
    btn_3 = types.KeyboardButton('Вікторина😁')
    btn_4 = types.KeyboardButton('Цікаві сайти🙌')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    # markup - дошка для кнопки, яка надсилає їх користувачу
    markup.add(btn_1, btn_2)    #кожен add - один ряд
    markup.add(btn_3, btn_4)

    bot.send_message(message.chat.id,
                     text='Привіт! Я тестовий бот!😉',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_message(message: types.Message):
    message_text = message.text #дістаємо текст повідомлення
    chat_id = message.chat.id   #дістаємо айді чату (по якому будемо надсилати відповіді)
    print(chat_id)

    match message_text:
        case 'Генерація паролю😂':
            bot_message = bot.send_message(chat_id, text='OK! Надішли довжину паролю від 8 до 35')
            bot.register_next_step_handler(bot_message, send_password)

        case 'Відгуки👌':
            btn_5 = types.InlineKeyboardButton(text='5😍', callback_data=f'grade_5')
            btn_4 = types.InlineKeyboardButton(text='4😊', callback_data=f'grade_4')
            btn_3 = types.InlineKeyboardButton(text='3😓', callback_data=f'grade_3')
            btn_2 = types.InlineKeyboardButton(text='2🤢', callback_data=f'grade_2')
            btn_1 = types.InlineKeyboardButton(text='1🤮', callback_data=f'grade_1')

            markup = types.InlineKeyboardMarkup()
            markup.add(btn_5, btn_4, btn_3, btn_2, btn_1, row_width=1)
            bot.send_message(chat_id, text='Обери оцінку, яку поставиш мені:', reply_markup=markup)

        case 'Вікторина😁':
            pass
        case 'Цікаві сайти🙌':
            btn_1 = types.InlineKeyboardButton(text='Пакетний менeджер Python', url='https://pypi.org/')
            btn_2 = types.InlineKeyboardButton(text='Офіційний сайт Python', url='https://www.python.org/')

            markup = types.InlineKeyboardMarkup()   # Маркап для кнопок, що знаходяться у чаті (не клавіатурних)
            markup.add(btn_1, btn_2, row_width=1)
            bot.send_message(chat_id, text='Ось цікаві сайти для тебе:', reply_markup=markup)

        case _:
            bot.send_message(chat_id, text='Я тебе не розумію 😢')

@bot.callback_query_handler(func=lambda callback: callback.data.startswith('grade'))  #обробник callback`у від кнопки. func -
def get_grade(callback: types.CallbackQuery):
    grade = callback.data[-1]    #вміст самого колбеку (дані кнопки)
    username = callback.from_user.username
    call_id = callback.id   #id колбеку (треба для реєстрації відповіді від бота)

    bot.answer_callback_query(call_id, text='Дякую за оцінку!') #Офіційна відповідь від боту на колбек (закриває прогрузку кнопки)
    bot.edit_message_text(chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id,
                          text='Оцінку відправлено!',
                          reply_markup=None)


    bot.send_message(admin_id, text=f'{username} поставив тобі оцінку {grade}!')

bot.polling(none_stop=True)  # бот пінгує в нескінченному режимі





