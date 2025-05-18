import os
import logging
import telebot as tb
from telebot import types # Для типів клавіатур тощо

# Імпортуємо класи та функції з наших файлів
from constants import DATABASE_FILE, EMPLOYEE_LEVELS, MONTHS # Імпортуємо константи
from salary_manager import SalaryManager # Імпортуємо менеджер
from utils import format_salary, validate_month_format, LOCALE_SETUP_MESSAGE # Імпортуємо утиліти

# --- Налаштування ---

# Використовуємо токен напряму, як було вказано в запиті
TOKEN = '7917068514:AAF7-QdQQNg55_raHMDZN0_yI8ZNxkEfd-M'
#name: Salary
#name_bot: Salary_AI_bot

# ID адміністратора для надсилання відгуків або інших повідомлень
ADMIN_ID = 523793990 # Замініть на реальний ID

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Ініціалізація бота
bot = tb.TeleBot(TOKEN)

# Ініціалізація менеджера даних
manager = SalaryManager(DATABASE_FILE)
logger.info(f"Статус завантаження даних: {manager._load_data()}")
logger.info(LOCALE_SETUP_MESSAGE) # Логуємо статус налаштування локалі


# --- Словники для управління станами розмови (ручна реалізація для pyTelegramBotAPI) ---
# Зберігаємо стан розмови та дані для кожного чату (chat_id)
user_states = {}
user_data = {} # Для збереження тимчасових даних в процесі розмови

# Константы станів для різних діалогів
STATE_IDLE = 0 # Бот очікує команду або натискання кнопки головного меню
STATE_ADD_NAME = 1
STATE_ADD_MONTH = 2
STATE_ADD_LEVEL = 3
STATE_ADD_HOURS = 4
STATE_ADD_TASKS = 5
STATE_ADD_USD = 6
STATE_ADD_EUR = 7
STATE_EDIT_ID = 8
STATE_EDIT_FIELD = 9
STATE_EDIT_VALUE = 10
STATE_DELETE_ID_CONFIRM = 11 # Видалення: очікуємо ID
STATE_REPORT_MONTH_INPUT = 12 # Звіти: очікуємо Місяць Рік
STATE_REPORT_YEAR_INPUT = 13 # Звіти: очікуємо Рік
STATE_FEEDBACK_GRADE = 14 # Стан для отримання оцінки
STATE_FEEDBACK_COMMENT = 15 # Стан для отримання коментаря до відгуку

# Функція для отримання поточного стану користувача
def get_user_state(chat_id):
    return user_states.get(chat_id, STATE_IDLE)

# Функція для встановлення стану користувача
def set_user_state(chat_id, state):
    user_states[chat_id] = state

# Функція для очищення стану та даних користувача
def reset_user_state(chat_id):
    user_states.pop(chat_id, None)
    user_data.pop(chat_id, None)
    # Також очищаємо register_next_step_handler на всякий випадок
    bot.clear_step_handler(chat_id)


# --- Допоміжна функція для головного меню ReplyKeyboardMarkup ---
def get_main_menu_markup():
    """Створює ReplyKeyboardMarkup для головного меню."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Використовуємо назви кнопок, які будемо обробляти в message_handler
    btn_add = types.KeyboardButton('➕ Додати запис')
    btn_list = types.KeyboardButton('📋 Список записів')
    btn_reports = types.KeyboardButton('📊 Звіти')
    btn_settings = types.KeyboardButton('⚙️ Налаштування')
    btn_feedback = types.KeyboardButton('🗣️ Відгуки') # Кнопка відгуків за прикладом
    btn_sites = types.KeyboardButton('🔗 Цікаві сайти') # Кнопка сайтів за прикладом

    # Розташовуємо кнопки в рядах
    markup.add(btn_add, btn_list)
    markup.add(btn_reports, btn_settings)
    markup.add(btn_feedback, btn_sites) # Додаємо кнопки відгуків та сайтів

    return markup

# --- Обробники команд ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Обробляє команди /start та /help. Показує головне меню."""
    chat_id = message.chat.id
    reset_user_state(chat_id) # Скасовуємо будь-яку поточну розмову

    welcome_text = (
        f"Привіт, {message.from_user.first_name}! Я бот для обліку зарплат.\n"
        "Використовуйте кнопки меню нижче або надсилайте команди (деякі з них вимагають параметрів, напр. /month Січень 2024):\n"
        "/list, /month, /year_total, /year_avg, /settings, /settings_edit, /details, /add, /edit, /delete\n"
        "Натисніть /cancel, щоб скасувати поточну дію."
    )
    bot.send_message(chat_id, welcome_text, reply_markup=get_main_menu_markup())

@bot.message_handler(commands=['cancel'])
def cancel_action(message):
    """Обробляє команду /cancel."""
    chat_id = message.chat.id
    current_state = get_user_state(chat_id)
    reset_user_state(chat_id) # Скидаємо стан та handler
    if current_state != STATE_IDLE:
        bot.send_message(chat_id, "Дію скасовано.", reply_markup=get_main_menu_markup())
    else:
        bot.send_message(chat_id, "Немає активної дії для скасування.", reply_markup=get_main_menu_markup())


@bot.message_handler(commands=['list'])
def list_records_command(message):
    """Показує всі записи про зарплату (сортовані за місяцем)."""
    chat_id = message.chat.id
    reset_user_state(chat_id) # Скасовуємо будь-яку поточну розмову

    records = manager.get_all_salary_records(sort_by='month')

    if not records:
        bot.send_message(chat_id, "Дані відсутні.")
        return

    report_parts = ["--- Усі записи про зарплату (за місяцем) ---"]
    for record in records:
        report_parts.append(manager.get_record_details_string(record))
    report_parts.append("--- Кінець списку ---")

    # Telegram має ліміт на довжину повідомлення (4096 символів).
    # Розділяємо звіт на частини, якщо він занадто довгий.
    full_report = "\n".join(report_parts)
    for i in range(0, len(full_report), 4000):
         bot.send_message(chat_id, full_report[i:i+4000])


@bot.message_handler(commands=['month'])
def report_by_month_command_inline(message):
    """Обробляє команду /month <Місяць Рік> (альтернативно до кнопки Звіти)."""
    chat_id = message.chat.id
    reset_user_state(chat_id) # Скасовуємо будь-яку поточну розмову

    args = message.text.split()[1:] # Беремо аргументи після команди
    if not args:
        # Якщо аргументів немає, переводимо в стан очікування місяця і реєструємо next_step
        set_user_state(chat_id, STATE_REPORT_MONTH_INPUT)
        bot.send_message(chat_id, "Будь ласка, вкажіть місяць після команди (наприклад, '/month Січень 2024') або введіть його окремо:")
        bot.register_next_step_handler(message, process_report_month_input)
        return

    # Якщо аргументи є, обробляємо одразу
    month_year_input = " ".join(args)
    result = manager.get_salary_report_by_month(month_year_input)

    if isinstance(result, str): # Повідомлення про помилку або відсутність даних
        bot.send_message(chat_id, result)
    else: # Список об'єктів MonthlySalaryRecord
        report_parts = [f"--- Записи за {result[0].month_year} ---"] # result[0] безпечно, бо список не порожній
        for record in result:
             report_parts.append(manager.get_record_details_string(record))
        report_parts.append("--- Кінець списку за місяць ---")
        full_report = "\n".join(report_parts)
        for i in range(0, len(full_report), 4000):
            bot.send_message(chat_id, full_report[i:i+4000])


@bot.message_handler(commands=['year_total'])
def report_year_total_command_inline(message):
    """Обробляє команду /year_total <Рік>."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    args = message.text.split()[1:]
    if not args:
        # Якщо аргументів немає, переводимо в стан очікування року і реєструємо next_step
        set_user_state(chat_id, STATE_REPORT_YEAR_INPUT)
        user_data[chat_id] = {'report_type': 'year_total'} # Зберігаємо тип звіту
        bot.send_message(chat_id, "Будь ласка, вкажіть рік після команди (наприклад, '/year_total 2024') або введіть його окремо:")
        bot.register_next_step_handler(message, process_report_year_input)
        return

    # Якщо аргументи є, обробляємо одразу
    year_input = args[0]
    result = manager.get_total_salary_report_by_year(year_input)

    if isinstance(result, str):
         bot.send_message(chat_id, result)
    else: # Словник
         report_text = (
             f"--- Загальна зарплата за {result['year']} рік ---\n"
             f"Всього записів за рік: {result['record_count']}\n"
             f"Загальна сума: {result['formatted_total']}\n"
             "------------------------------"
         )
         bot.send_message(chat_id, report_text)


@bot.message_handler(commands=['year_avg'])
def report_year_avg_command_inline(message):
    """Обробляє команду /year_avg <Рік>."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    args = message.text.split()[1:]
    if not args:
        # Якщо аргументів немає, переводимо в стан очікування року і реєструємо next_step
        set_user_state(chat_id, STATE_REPORT_YEAR_INPUT)
        user_data[chat_id] = {'report_type': 'year_avg'} # Зберігаємо тип звіту
        bot.send_message(chat_id, "Будь ласка, вкажіть рік після команди (наприклад, '/year_avg 2024') або введіть його окремо:")
        bot.register_next_step_handler(message, process_report_year_input)
        return

    # Якщо аргументи є, обробляємо одразу
    year_input = args[0]
    result = manager.get_average_salary_report_by_year(year_input)

    if isinstance(result, str):
         bot.send_message(chat_id, result)
    else: # Словник
         report_text = (
             f"--- Середня зарплата за місяць у {result['year']} році ---\n"
             f"Розраховано на основі {result['record_count']} записів.\n"
             f"Середня сума: {result['formatted_average']}\n"
             "------------------------------"
         )
         bot.send_message(chat_id, report_text)


@bot.message_handler(commands=['settings'])
def show_settings_command(message):
    """Показує поточні налаштування розрахунку зарплати."""
    chat_id = message.chat.id
    reset_user_state(chat_id)
    settings_string = manager.get_settings_string()
    bot.send_message(chat_id, settings_string)

@bot.message_handler(commands=['settings_edit'])
def settings_edit_command(message):
    """Обробляє команду редагування налаштувань за параметрами."""
    chat_id = message.chat.id
    reset_user_state(chat_id) # На всякий випадок скидаємо стан

    args = message.text.split()[1:]
    if not args:
        help_text = (
            "Редагування налаштувань. Використовуйте наступні формати команд:\n"
            "`/settings_edit base\\_amount Рівень Значення` (напр. `/settings\\_edit base\\_amount Junior 15000`)\n" # Екрануємо символи для MarkdownV2
            "`/settings\\_edit coefficient Рівень Значення` (напр. `/settings\\_edit coefficient Middle 1\\.6`)\n"
            "`/settings\\_edit task\\_cost Назва Вартість` (напр. `/settings\\_edit task\\_cost Complex 700`)\n"
            "`/settings\\_edit task\\_delete Назва` (напр. `/settings\\_edit task\\_delete Simple`)\n"
            "`/settings\\_edit hours Значення` (напр. `/settings\\_edit hours 160`)\n"
            "`/settings\\_edit rates USD_Значення EUR_Значення` (напр. `/settings\\_edit rates 42\\.5 45\\.0`)\n"
            "Натисніть /settings щоб побачити поточні значення."
        )
        # pyTelegramBotAPI підтримує MarkdownV2 та HTML. HTML простіший для форматування
        bot.send_message(chat_id, "<b>Як редагувати налаштування:</b>\n" + help_text.replace('`', '').replace('\\', ''), parse_mode="HTML") # Просто виводимо текст без спеціального форматування
        return

    setting_type = args[0].lower()
    result = "Невірний формат команди або недостатньо параметрів. Використовуйте `/settings_edit` для довідки." # Дефолтне повідомлення про помилку

    # Перевіряємо та викликаємо відповідний метод менеджера
    if setting_type == 'base_amount' and len(args) == 3:
        level = args[1]
        value = args[2]
        result = manager.edit_base_amount_setting(level, value)
    elif setting_type == 'coefficient' and len(args) == 3:
        level = args[1]
        value = args[2]
        result = manager.edit_coefficient_setting(level, value)
    elif setting_type == 'task_cost' and len(args) >= 3: # Назва може містити пробіли
         task_name_parts = args[1:-1]
         task_name = " ".join(task_name_parts)
         cost = args[-1]
         result = manager.edit_task_cost_setting(task_name, cost)
    elif setting_type == 'task_delete' and len(args) >= 2:
         task_name_parts = args[1:]
         task_name = " ".join(task_name_parts)
         result = manager.delete_task_cost_setting(task_name)
    elif setting_type == 'hours' and len(args) == 2:
        value = args[1]
        result = manager.edit_standard_hours_setting(value)
    elif setting_type == 'rates' and len(args) == 3:
        usd_value = args[1]
        eur_value = args[2]
        result = manager.edit_default_rates_setting(usd_value, eur_value)

    # Відправляємо результат операції
    bot.send_message(chat_id, result)

@bot.message_handler(commands=['details'])
def show_record_details_command(message):
    """Обробляє команду /details <ID>."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    args = message.text.split()[1:]
    if not args:
        bot.send_message(chat_id, "Будь ласка, вкажіть ID запису після команди (наприклад, '/details 123').")
        return

    record_id_input = args[0]
    record = manager.find_record_by_id(record_id_input)

    if not record:
        bot.send_message(chat_id, f"Запис із ID '{record_id_input}' не знайдено.")
        return

    # Отримуємо форматовані деталі запису
    details_text = manager.get_record_details_string(record)

    # Додаємо Inline кнопки для редагування та видалення
    action_markup = types.InlineKeyboardMarkup(row_width=2)
    btn_edit = types.InlineKeyboardButton('✍️ Редагувати', callback_data=f'edit_rec_{record.id}')
    btn_delete = types.InlineKeyboardButton('🗑️ Видалити', callback_data=f'delete_rec_{record.id}')
    action_markup.add(btn_edit, btn_delete)

    bot.send_message(chat_id, details_text, reply_markup=action_markup)


# --- Обробник головного меню ReplyKeyboardMarkup та інших текстових повідомлень ---
# Цей обробник має йти ПІСЛЯ ВСІХ CommandHandler-ів, але ПЕРЕД register_next_step_handler
# (хоча register_next_step_handler має вищий пріоритет).
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    """
    Обробляє текстові повідомлення, які не є командами.
    Використовується для обробки натискань кнопок головного меню або невідомого тексту.
    """
    chat_id = message.chat.id
    message_text = message.text.strip()
    current_state = get_user_state(chat_id)

    # Якщо бот очікує відповідь у багатоетапній розмові, це повідомлення буде
    # перехоплено register_next_step_handler.
    # Якщо воно сюди потрапило в стані, відмінному від IDLE, це може бути команда,
    # введена під час очікування (CommandHandlers мають вищий пріоритет),
    # або невідомий текст, який не обробив register_next_step_handler.
    # В даній реалізації, якщо register_next_step_handler не спрацював, і ми не в IDLE,
    # це означає, що користувач ввів щось не те. Краще скинути стан.

    if current_state != STATE_IDLE:
        # Якщо ми тут, це означає, що register_next_step_handler не спрацював
        # (наприклад, користувач ввів команду, яка перехопилася CommandHandler-ом раніше,
        # або була якась внутрішня помилка).
        # Найбезпечніше - повідомити користувача і скинути стан.
        bot.send_message(chat_id, "❌ Поточну операцію перервано або виникла помилка. Спробуйте ще раз або натисніть /cancel.", reply_markup=get_main_menu_markup())
        reset_user_state(chat_id)
        return # Зупиняємо обробку тут

    # Бот в стані IDLE, обробляємо текст як команду з головного меню
    match message_text:
        case '➕ Додати запис':
            add_start(message) # Переходимо до функції початку додавання
        case '📋 Список записів':
            list_records_command(message) # Переходимо до функції списку
        case '📊 Звіти':
            # Надсилаємо Inline клавіатуру для вибору типу звіту
            report_markup = types.InlineKeyboardMarkup()
            btn_month_report = types.InlineKeyboardButton('Звіт за місяць', callback_data='report_type_month')
            btn_year_total = types.InlineKeyboardButton('Загальний за рік', callback_data='report_type_year_total')
            btn_year_avg = types.InlineKeyboardButton('Середній за рік', callback_data='report_type_year_avg')
            report_markup.add(btn_month_report, btn_year_total, btn_year_avg, row_width=1)
            bot.send_message(chat_id, "Оберіть тип звіту:", reply_markup=report_markup)
        case '⚙️ Налаштування':
            # Надсилаємо Inline клавіатуру для вибору дії з налаштуваннями
            settings_markup = types.InlineKeyboardMarkup()
            btn_show_settings = types.InlineKeyboardButton('Показати поточні', callback_data='settings_show')
            btn_edit_settings_help = types.InlineKeyboardButton('Як редагувати', callback_data='settings_edit_help')
            settings_markup.add(btn_show_settings, btn_edit_settings_help, row_width=1)
            bot.send_message(chat_id, "Оберіть дію з налаштуваннями:", reply_markup=settings_markup)
        case '🗣️ Відгуки': # Обробка кнопки Відгуки
             send_feedback_start(message) # Переходимо до початку діалогу відгуків
        case '🔗 Цікаві сайти': # Обробка кнопки Сайти
            send_sites(message) # Переходимо до функції надсилання сайтів
        case _:
            # Це невідомий текст, коли бот в IDLE
            bot.send_message(chat_id, "Невідома команда або текст. Використовуйте кнопки меню або команди.", reply_markup=get_main_menu_markup())


# --- Обробник Inline клавіатур ---
@bot.callback_query_handler(func=lambda call: call.data.startswith(('report_type_', 'settings_', 'edit_rec_', 'delete_rec_', 'grade_')))
def handle_inline_buttons(call):
    """Обробляє натискання Inline кнопок."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    callback_data = call.data

    # Обов'язкова відповідь на callback, щоб прибрати "годинник" на кнопці
    bot.answer_callback_query(call.id, text='ОК')

    # --- Обробка кнопок "Звіти" ---
    if callback_data.startswith('report_type_'):
        report_type = callback_data.split('_')[2] # report_type_month -> month

        # Видаляємо або редагуємо повідомлення з Inline клавіатурою, щоб прибрати її
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Оберіть тип звіту:', reply_markup=None)
        except Exception as e: # Може виникнути помилка, якщо повідомлення старе або вже змінене
             logger.error(f"Помилка при редагуванні повідомлення {message_id} в чаті {chat_id}: {e}")
             pass # Продовжуємо без редагування повідомлення

        if report_type == 'month':
            set_user_state(chat_id, STATE_REPORT_MONTH_INPUT)
            bot.send_message(chat_id, "Введіть місяць для звіту (наприклад, 'Січень 2024'):")
            # Реєструємо наступний крок. Якщо користувач введе щось інше, handle_text_messages скине стан.
            bot.register_next_step_handler(call.message, process_report_month_input)
        elif report_type in ['year_total', 'year_avg']:
             user_data[chat_id] = {'report_type': report_type} # Зберігаємо тип звіту
             set_user_state(chat_id, STATE_REPORT_YEAR_INPUT)
             bot.send_message(chat_id, "Введіть рік для звіту (наприклад, '2024'):")
             bot.register_next_step_handler(call.message, process_report_year_input)

    # --- Обробка кнопок "Налаштування" ---
    elif callback_data.startswith('settings_'):
        action = callback_data.split('_')[1] # settings_show -> show
        # Видаляємо клавіатуру
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Оберіть дію з налаштуваннями:', reply_markup=None)
        except Exception as e:
             logger.error(f"Помилка при редагуванні повідомлення {message_id} в чаті {chat_id}: {e}")
             pass

        if action == 'show':
            bot.send_message(chat_id, manager.get_settings_string())
        elif action == 'edit_help':
             help_text = (
                "Редагування налаштувань. Використовуйте наступні формати команд:\n"
                "`/settings_edit base_amount Рівень Значення` (напр. `/settings_edit base_amount Junior 15000`)\n"
                "`/settings_edit coefficient Рівень Значення` (напр. `/settings_edit coefficient Middle 1.6`)\n"
                "`/settings_edit task_cost Назва Вартість` (напр. `/settings_edit task_cost Complex 700`)\n"
                "`/settings_edit task_delete Назва` (напр. `/settings_edit task_delete Simple`)\n"
                "`/settings_edit hours Значення` (напр. `/settings_edit hours 160`)\n"
                "`/settings_edit rates USD_Значення EUR_Значення` (напр. `/settings_edit rates 42.5 45.0`)\n"
                "Натисніть /settings щоб побачити поточні значення."
            )
             # HTML формат для зручності читання в Telegram
             formatted_help_text = "<b>Як редагувати налаштування:</b>\n" + help_text.replace('`', '<code>').replace('\n', '<br>')
             bot.send_message(chat_id, formatted_help_text, parse_mode="HTML")


    # --- Обробка кнопок дій над записом ("Редагувати", "Видалити") ---
    elif callback_data.startswith(('edit_rec_', 'delete_rec_')):
         parts = callback_data.split('_')
         action = parts[0] # edit або delete
         try:
             record_id = int(parts[2]) # edit_rec_123 -> 123

             # Видаляємо Inline клавіатуру з повідомлення деталей
             try:
                  bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=call.message.text, reply_markup=None)
             except Exception as e:
                  logger.error(f"Помилка при редагуванні повідомлення деталей {message_id} в чаті {chat_id}: {e}")
                  pass # Продовжуємо без редагування

             if action == 'delete' :
                  result = manager.delete_salary_record(record_id)
                  if isinstance(result, manager.MonthlySalaryRecord):
                       bot.send_message(chat_id, f"✅ Запис #{record_id} успішно видалено!")
                  else:
                       bot.send_message(chat_id, f"❌ Помилка видалення запису #{record_id}: {result}")
             elif action == 'edit':
                  # Переводимо користувача в діалог редагування, передаючи ID
                  # Починаємо діалог редагування з першого кроку (введення ID)
                  # Можна відразу передати ID в перший крок, щоб не запитувати його повторно
                  bot.send_message(chat_id, f"ОК. Починаю редагування запису #{record_id}.")
                  # Ініціюємо діалог редагування. Передаємо ID для автоматичного переходу.
                  edit_start(call.message, record_id=record_id) # Викликаємо стартову функцію редагування

         except (ValueError, IndexError) as e:
             logger.error(f"Помилка парсингу callback_data '{callback_data}': {e}")
             bot.send_message(chat_id, "Помилка: Невірний формат даних для редагування/видалення.")

    # --- Обробка кнопок оцінки ("Відгуки") ---
    elif callback_data.startswith('grade_'):
        grade = callback_data.split('_')[1] # grade_5 -> 5
        username = call.from_user.username
        user_id = call.from_user.id # Використовуємо ID, він завжди є

        # Редагуємо повідомлення, прибираючи кнопки
        try:
            bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text='Оцінку відправлено!',
                                reply_markup=None)
        except Exception as e:
             logger.error(f"Помилка при редагуванні повідомлення оцінки {message_id} в чаті {chat_id}: {e}")
             pass

        # Надсилаємо повідомлення адміністратору
        admin_message = f'Користувач @{username} (ID: {user_id}) поставив тобі оцінку {grade}!' if username else f'Користувач з ID {user_id} поставив тобі оцінку {grade}!'
        try:
            bot.send_message(ADMIN_ID, admin_message)
            # Можна запитати коментар після оцінки
            set_user_state(chat_id, STATE_FEEDBACK_COMMENT)
            user_data[chat_id] = {'grade': grade, 'username': username, 'user_id': user_id}
            bot.send_message(chat_id, "Дякую за оцінку! Якщо хочете, можете написати короткий коментар або надішліть /skip.", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(call.message, process_feedback_comment)

        except Exception as e:
            logger.error(f"Помилка при надсиланні повідомлення адміну {ADMIN_ID} або запиті коментаря: {e}")
            bot.send_message(chat_id, "Дякую за оцінку!") # Просто дякуємо, якщо не вийшло відправити адміну чи запитати коментар
            reset_user_state(chat_id) # Скидаємо стан, якщо не вдалося почати діалог коментаря


# --- Обробка введених даних для звітів (кроки після вибору типу звіту) ---
def process_report_month_input(message):
    """Крок 1 звіту за місяць: введення Місяць Рік."""
    chat_id = message.chat.id
    # Перевірка на /cancel
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    # Перевірка стану (хоча register_next_step_handler мав би спрацювати тільки в правильному стані)
    if get_user_state(chat_id) != STATE_REPORT_MONTH_INPUT:
         bot.send_message(chat_id, "Неочікуване повідомлення. Операцію скасовано.", reply_markup=get_main_menu_markup())
         reset_user_state(chat_id)
         return


    month_year_input = message.text.strip()
    result = manager.get_salary_report_by_month(month_year_input)

    if isinstance(result, str): # Повідомлення про помилку або відсутність даних
        bot.send_message(chat_id, f"❌ Помилка або дані не знайдено: {result}\nСпробуйте ще раз або /cancel.")
        bot.register_next_step_handler(message, process_report_month_input) # Залишаємось на цьому кроці
    else: # Список об'єктів MonthlySalaryRecord
        report_parts = [f"--- Записи за {result[0].month_year} ---"] if result else [f"Дані за {month_year_input} не знайдено (хоча формат вірний)."]
        for record in result:
             report_parts.append(manager.get_record_details_string(record))
        if result:
            report_parts.append("--- Кінець списку за місяць ---")
        full_report = "\n".join(report_parts)
        # Розділяємо на частини, якщо звіт довгий
        for i in range(0, len(full_report), 4000):
            bot.send_message(chat_id, full_report[i:i+4000])

        reset_user_state(chat_id) # Завершуємо розмову


def process_report_year_input(message):
    """Крок 1 звіту за рік: введення Рік."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_REPORT_YEAR_INPUT:
         bot.send_message(chat_id, "Неочікуване повідомлення. Операцію скасовано.", reply_markup=get_main_menu_markup())
         reset_user_state(chat_id)
         return

    year_input = message.text.strip()
    report_type = user_data[chat_id].get('report_type') # Отримуємо збережений тип звіту

    if report_type == 'year_total':
        result = manager.get_total_salary_report_by_year(year_input)
    elif report_type == 'year_avg':
        result = manager.get_average_salary_report_by_year(year_input)
    else:
        result = "Внутрішня помилка: Невідомий тип звіту." # На всякий випадок

    if isinstance(result, str):
         bot.send_message(chat_id, f"❌ Помилка або дані не знайдено: {result}\nСпробуйте ще раз або /cancel.")
         bot.register_next_step_handler(message, process_report_year_input) # Залишаємось
    else: # Словник з результатом
         if report_type == 'year_total':
              report_text = (
                 f"--- Загальна зарплата за {result['year']} рік ---\n"
                 f"Всього записів за рік: {result['record_count']}\n"
                 f"Загальна сума: {result['formatted_total']}\n"
                 "------------------------------"
              )
         elif report_type == 'year_avg':
              report_text = (
                 f"--- Середня зарплата за місяць у {result['year']} році ---\n"
                 f"Розраховано на основі {result['record_count']} записів.\n"
                 f"Середня сума: {result['formatted_average']}\n"
                 "------------------------------"
              )
         else:
              report_text = result # Виведе повідомлення про внутрішню помилку
         bot.send_message(chat_id, report_text)

         reset_user_state(chat_id) # Завершуємо розмову


# --- Реалізація діалогу відгуків (/feedback) ---
def send_feedback_start(message):
    """Починає процес відгуку."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    feedback_markup = types.InlineKeyboardMarkup()
    btn_5 = types.InlineKeyboardButton(text='5😍', callback_data=f'grade_5')
    btn_4 = types.InlineKeyboardButton(text='4😊', callback_data=f'grade_4')
    btn_3 = types.InlineKeyboardButton(text='3😓', callback_data=f'grade_3')
    btn_2 = types.InlineKeyboardButton(text='2🤢', callback_data=f'grade_2')
    btn_1 = types.InlineKeyboardButton(text='1🤮', callback_data=f'grade_1')
    feedback_markup.add(btn_5, btn_4, btn_3, btn_2, btn_1, row_width=1)

    # Стан STATE_FEEDBACK_GRADE встановлюється в handle_inline_buttons після вибору оцінки
    bot.send_message(chat_id, 'Обери оцінку, яку поставиш мені:', reply_markup=feedback_markup)


def process_feedback_comment(message):
    """Крок 2 відгуку: введення коментаря."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_FEEDBACK_COMMENT:
         bot.send_message(chat_id, "Неочікуване повідомлення. Операцію скасовано.", reply_markup=get_main_menu_markup())
         reset_user_state(chat_id)
         return

    comment = message.text.strip()
    grade = user_data[chat_id].get('grade', 'N/A')
    username = user_data[chat_id].get('username', 'N/A')
    user_id = user_data[chat_id].get('user_id', 'N/A')

    if comment.lower() == '/skip':
        comment = "(Коментар пропущено)"
        bot.send_message(chat_id, "Дякую за відгук!", reply_markup=get_main_menu_markup())
    else:
        bot.send_message(chat_id, "Дякую за відгук та коментар!", reply_markup=get_main_menu_markup())

    # Надсилаємо коментар адміну
    comment_admin_message = f'Коментар до оцінки {grade} від @{username} (ID: {user_id}):\n{comment}' if username else f'Коментар до оцінки {grade} від користувача ID {user_id}:\n{comment}'
    try:
        bot.send_message(ADMIN_ID, comment_admin_message)
    except Exception as e:
         logger.error(f"Помилка при надсиланні коментаря адміну {ADMIN_ID}: {e}")


    reset_user_state(chat_id)

# --- Реалізація функції "Цікаві сайти" ---
def send_sites(message):
    """Надсилає повідомлення з Inline кнопками-посиланнями."""
    chat_id = message.chat.id
    reset_user_state(chat_id) # Скидаємо стан

    sites_markup = types.InlineKeyboardMarkup()   # Маркап для кнопок, що знаходяться у чаті (не клавіатурних)
    btn_pypi = types.InlineKeyboardButton(text='Пакетний менеджер Python', url='https://pypi.org/')
    btn_python_org = types.InlineKeyboardButton(text='Офіційний сайт Python', url='https://www.python.org/')

    sites_markup.add(btn_pypi, btn_python_org, row_width=1)
    bot.send_message(chat_id, text='Ось цікаві сайти для тебе:', reply_markup=sites_markup)


# --- Реалізація багатоетапних діалогів (/add, /edit, /delete) ---
# Ці функції реалізуються аналогічно, як у попередньому прикладі tictactoe_bot.py
# на pyTelegramBotAPI, використовуючи register_next_step_handler та user_data/user_states.
# Важливо:
# 1. На початку кожного _step функції перевіряти на /cancel: if message.text and message.text.strip() == '/cancel': cancel_action(message); return
# 2. На початку кожного _step функції перевіряти поточний стан: if get_user_state(chat_id) != STATE_EXPECTED: ... return
# 3. У функціях *початку* діалогів (/add, /edit, /delete) викликати reset_user_state(chat_id)
#    та встановити set_user_state(chat_id, STATE_FIRST_STEP). Очистити ReplyKeyboardRemove.
# 4. У *кінцевих* функціях діалогів викликати reset_user_state(chat_id). Можна повернути головне меню.
# 5. У всіх _step функціях, які очікують введення, викликати bot.register_next_step_handler(message, next_step_function).

# Приклад початку додавання (прив'язано до кнопки меню):
def add_start(message):
    """Починає процес додавання запису."""
    chat_id = message.chat.id
    reset_user_state(chat_id)
    set_user_state(chat_id, STATE_ADD_NAME)
    user_data[chat_id] = {}
    bot.send_message(chat_id, "Додавання нового запису про зарплату. Введіть ім'я працівника:", reply_markup=types.ReplyKeyboardRemove()) # Прибираємо меню
    bot.register_next_step_handler(message, add_name_step)

# ... (додайте сюди функції add_name_step, add_month_step, ..., add_eur_rate_step - КОД НИЖЧЕ)
# ... (додайте сюди функції edit_start, edit_id_step, ..., edit_value_step - КОД НИЖЧЕ)
# ... (додайте сюди функції delete_start, delete_id_step - КОД НИЖЧЕ)


# --- Основна функція запуску бота ---
def main() -> None:
    """Запускає бота."""
    logger.info("Бот запущено. Натисніть Ctrl+C для зупинки.")
    # Використовуємо infinity_polling для постійного отримання оновлень
    # skip_pending=True пропустить старі повідомлення, які бот міг отримати поки був офлайн
    # clean_update_queue=True очистить чергу оновлень при старті
    bot.infinity_polling(skip_pending=True, clean_update_queue=True)


# Точка входу для бота
if __name__ == "__main__":
    # Додаємо сюди реалізації step-функцій для /add, /edit, /delete
    # Це місце зручне, бо вони використовуватимуть змінні з зовнішньої області видимості (bot, manager, user_states, user_data, constants)

    # --- Функції кроків для додавання запису (/add) ---
    # add_start оголошена вище, вона викликається з handle_text_messages
    def add_name_step(message):
        """Крок 1 додавання: Ім'я працівника."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        # Перевірка типу повідомлення (очікуємо текст)
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть ім'я працівника текстом:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, add_name_step); return
        if get_user_state(chat_id) != STATE_ADD_NAME: return # Перевірка стану

        name = message.text.strip()
        if not name:
            bot.send_message(chat_id, "Ім'я не може бути порожнім. Введіть ім'я працівника:")
            bot.register_next_step_handler(message, add_name_step)
            return

        user_data[chat_id]['employee_name'] = name
        set_user_state(chat_id, STATE_ADD_MONTH)
        bot.send_message(chat_id, "Введіть місяць (наприклад, 'Січень 2024'):")
        bot.register_next_step_handler(message, add_month_step)

    def add_month_step(message):
        """Крок 2 додавання: Місяць."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть місяць текстом:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, add_month_step); return
        if get_user_state(chat_id) != STATE_ADD_MONTH: return

        month_year = message.text
        is_valid, result = validate_month_format(month_year)
        if not is_valid:
            bot.send_message(chat_id, f"Помилка: {result}\nВведіть місяць ще раз (наприклад, 'Січень 2024'):")
            bot.register_next_step_handler(message, add_month_step)
            return

        user_data[chat_id]['month_year'] = result

        # Перевірка унікальності запису
        employee_name = user_data[chat_id].get('employee_name')
        if employee_name is None: # Внутрішня помилка
             bot.send_message(chat_id, "❌ Внутрішня помилка: Відсутнє ім'я працівника. Спробуйте почати з /add ще раз.")
             reset_user_state(chat_id)
             return

        if any(r.employee_name.lower() == employee_name.lower() and r.month_year.lower() == result.lower() for r in manager.monthly_records):
             bot.send_message(chat_id, f"Помилка: Дані за {result} для працівника {employee_name} уже існують! Використовуйте команду /edit для зміни.\nДодавання скасовано.")
             reset_user_state(chat_id)
             return

        set_user_state(chat_id, STATE_ADD_LEVEL)
        level_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for level in EMPLOYEE_LEVELS:
            level_keyboard.add(types.KeyboardButton(level))
        bot.send_message(chat_id, f"Введіть рівень працівника. Допустимі: {', '.join(EMPLOYEE_LEVELS)}:", reply_markup=level_keyboard)
        bot.register_next_step_handler(message, add_level_step)

    def add_level_step(message):
        """Крок 3 додавання: Рівень."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть рівень текстом або виберіть кнопку:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, add_level_step); return
        if get_user_state(chat_id) != STATE_ADD_LEVEL: return

        level = message.text.strip()
        if level not in EMPLOYEE_LEVELS:
            level_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            for level_opt in EMPLOYEE_LEVELS:
                 level_keyboard.add(types.KeyboardButton(level_opt))
            bot.send_message(chat_id, f"Невірний рівень '{level}'. Виберіть зі списку: {', '.join(EMPLOYEE_LEVELS)}:", reply_markup=level_keyboard)
            bot.register_next_step_handler(message, add_level_step)
            return

        user_data[chat_id]['level'] = level
        set_user_state(chat_id, STATE_ADD_HOURS)
        bot.send_message(chat_id, "Введіть фактично відпрацьовані години (число):", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, add_hours_step)

    def add_hours_step(message):
        """Крок 4 додавання: Години."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть відпрацьовані години числом:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, add_hours_step); return
        if get_user_state(chat_id) != STATE_ADD_HOURS: return

        try:
            hours = float(message.text)
            if hours < 0:
                bot.send_message(chat_id, "Відпрацьовані години не можуть бути від'ємними. Введіть число годин:")
                bot.register_next_step_handler(message, add_hours_step)
                return
            user_data[chat_id]['actual_hours'] = hours
            set_user_state(chat_id, STATE_ADD_TASKS)
            bot.send_message(chat_id, f"Введіть загальну вартість виконаних завдань за місяць (число). Наприклад, {manager.settings.task_costs.get('Simple', 100.0):.2f} за Simple задачу:")
            bot.register_next_step_handler(message, add_tasks_step)
        except (ValueError, TypeError):
            bot.send_message(chat_id, "Будь ласка, введіть коректне числове значення для годин:")
            bot.register_next_step_handler(message, add_hours_step)

    def add_tasks_step(message):
        """Крок 5 додавання: Вартість завдань."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть вартість завдань числом:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, add_tasks_step); return
        if get_user_state(chat_id) != STATE_ADD_TASKS: return

        try:
            tasks_value = float(message.text)
            if tasks_value < 0:
                bot.send_message(chat_id, "Вартість завдань не може бути від'ємною. Введіть число:")
                bot.register_next_step_handler(message, add_tasks_step)
                return
            user_data[chat_id]['tasks_completed_value'] = tasks_value
            set_user_state(chat_id, STATE_ADD_USD)

            last_record = next(iter(reversed(manager.monthly_records)), None)
            default_usd = last_record.usd_rate if last_record else manager.settings.default_rates.get("USD", 40.0)

            bot.send_message(chat_id, f"Введіть курс долара (USD) за місяць (наприклад, {default_usd:.2f}). Надішліть Enter, щоб використати це значення:")
            bot.register_next_step_handler(message, add_usd_rate_step)

        except (ValueError, TypeError):
            bot.send_message(chat_id, "Будь ласка, введіть коректне числове значення для вартості завдань:")
            bot.register_next_step_handler(message, add_tasks_step)

    def add_usd_rate_step(message):
        """Крок 6 додавання: Курс USD."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        # Дозволяємо порожнє повідомлення для використання дефолту
        if get_user_state(chat_id) != STATE_ADD_USD: return

        usd_input = message.text.strip()
        last_record = next(iter(reversed(manager.monthly_records)), None)
        default_usd = last_record.usd_rate if last_record else manager.settings.default_rates.get("USD", 40.0)
        usd_rate = default_usd

        if usd_input: # Якщо щось ввели
            try:
                usd_rate = float(usd_input)
                if usd_rate <= 0:
                    bot.send_message(chat_id, "Курс долара має бути більше нуля. Введіть число або залиште поле порожнім:")
                    bot.register_next_step_handler(message, add_usd_rate_step)
                    return
                # М'яка валідація (попередження)
                if usd_rate < 10 or usd_rate > 200:
                     bot.send_message(chat_id, f"⚠️ Увага: Введений курс долара ({usd_rate:.2f}) виглядає незвично.")
            except (ValueError, TypeError):
                bot.send_message(chat_id, "Будь ласка, введіть коректне числове значення для курсу долара або залиште поле порожнім:")
                bot.register_next_step_handler(message, add_usd_rate_step)
                return

        user_data[chat_id]['usd_rate'] = usd_rate
        set_user_state(chat_id, STATE_ADD_EUR)

        default_eur = last_record.eur_rate if last_record else manager.settings.default_rates.get("EUR", 43.0)

        bot.send_message(chat_id, f"Введіть курс євро (EUR) за місяць (наприклад, {default_eur:.2f}). Надішліть Enter, щоб використати це значення:")
        bot.register_next_step_handler(message, add_eur_rate_step)


    def add_eur_rate_step(message):
        """Крок 7 додавання: Курс EUR та завершення."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        # Дозволяємо порожнє повідомлення
        if get_user_state(chat_id) != STATE_ADD_EUR: return

        eur_input = message.text.strip()
        last_record = next(iter(reversed(manager.monthly_records)), None)
        default_eur = last_record.eur_rate if last_record else manager.settings.default_rates.get("EUR", 43.0)
        eur_rate = default_eur

        if eur_input: # Якщо щось ввели
            try:
                eur_rate = float(eur_input)
                if eur_rate <= 0:
                    bot.send_message(chat_id, "Курс євро має бути більше нуля. Введіть число або залиште поле порожнім:")
                    bot.register_next_step_handler(message, add_eur_rate_step)
                    return
                # М'яка валідація (попередження)
                if eur_rate < 10 or eur_rate > 200:
                    bot.send_message(chat_id, f"⚠️ Увага: Введений курс євро ({eur_rate:.2f}) виглядає незвично.")
            except (ValueError, TypeError):
                bot.send_message(chat_id, "Будь ласка, введіть коректне числове значення для курсу євро або залиште поле порожнім:")
                bot.register_next_step_handler(message, add_eur_rate_step)
                return

        user_data[chat_id]['eur_rate'] = eur_rate

        # Збираємо всі дані та викликаємо менеджер
        name = user_data[chat_id].get('employee_name')
        month = user_data[chat_id].get('month_year')
        level = user_data[chat_id].get('level')
        hours = user_data[chat_id].get('actual_hours')
        tasks = user_data[chat_id].get('tasks_completed_value')
        usd = user_data[chat_id].get('usd_rate')
        eur = user_data[chat_id].get('eur_rate')

        # Фінальна перевірка на None (хоча попередні кроки мали б це гарантувати)
        if None in [name, month, level, hours, tasks, usd, eur]:
             logger.error(f"Внутрішня помилка: Неповні дані для додавання запису в чаті {chat_id}. Дані: {user_data.get(chat_id)}")
             bot.send_message(chat_id, "❌ Внутрішня помилка: Не всі дані були зібрані. Спробуйте ще раз /add.", reply_markup=get_main_menu_markup())
        else:
            result = manager.add_salary_record(name, month, level, hours, tasks, usd, eur)

            if isinstance(result, manager.MonthlySalaryRecord):
                bot.send_message(chat_id,
                    f"✅ Запис #{result.id} за {result.month_year} для {result.employee_name} успішно додано!\n"
                    f"Розрахована зарплата: {format_salary(result.calculated_salary_uah, result.usd_rate, result.eur_rate)}",
                    reply_markup=get_main_menu_markup() # Повертаємо головне меню
                )
            else:
                bot.send_message(chat_id, f"❌ Помилка при додаванні запису: {result}", reply_markup=get_main_menu_markup()) # Повертаємо головне меню

        reset_user_state(chat_id)


    # --- Функції кроків для редагування запису (/edit) ---
    # edit_start оголошена вище (може приймати record_id як аргумент)
    def edit_start(message, record_id=None):
        """Починає процес редагування запису."""
        chat_id = message.chat.id
        reset_user_state(chat_id)
        set_user_state(chat_id, STATE_EDIT_ID)
        user_data[chat_id] = {}

        if record_id is not None:
             # Якщо ID передано (наприклад, з Inline кнопки), одразу переходимо до перевірки ID
             message.text = str(record_id) # Імітуємо повідомлення з текстом ID
             bot.send_message(chat_id, f"Редагування запису #{record_id}. Перевіряю ID...", reply_markup=types.ReplyKeyboardRemove())
             edit_id_step(message) # Викликаємо наступний крок з цим ID
        else:
            # Якщо ID не передано (наприклад, команда /edit без аргументів), запитуємо його
            bot.send_message(chat_id, "Редагування запису. Введіть ID запису, який потрібно редагувати (натисніть /cancel для скасування):", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, edit_id_step)

    def edit_id_step(message):
        """Крок 1 редагування: Введення ID."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть ID запису числом:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, edit_id_step); return
        if get_user_state(chat_id) != STATE_EDIT_ID: return

        record_id_input = message.text.strip()
        record_to_edit = manager.find_record_by_id(record_id_input)

        if not record_to_edit:
            bot.send_message(chat_id, f"Запис із ID '{record_id_input}' не знайдено. Будь ласка, введіть коректний ID або /cancel:")
            bot.register_next_step_handler(message, edit_id_step)
            return

        user_data[chat_id]['record_id_to_edit'] = record_to_edit.id
        user_data[chat_id]['record_data'] = record_to_edit.to_dict() # Зберігаємо поточні дані

        details_string = manager.get_record_details_string(record_to_edit)

        set_user_state(chat_id, STATE_EDIT_FIELD)
        bot.send_message(chat_id, f"Знайдено запис:\n{details_string}\n"
                                        "Яке поле хочете редагувати? (employee_name, month_year, level, actual_hours, tasks_completed_value, usd_rate, eur_rate)\n"
                                        "Натисніть /cancel для скасування.")
        bot.register_next_step_handler(message, edit_field_step)


    def edit_field_step(message):
        """Крок 2 редагування: Введення назви поля."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть назву поля текстом:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, edit_field_step); return
        if get_user_state(chat_id) != STATE_EDIT_FIELD: return

        field_name = message.text.strip().lower()
        valid_fields = ['employee_name', 'month_year', 'level', 'actual_hours', 'tasks_completed_value', 'usd_rate', 'eur_rate']

        if field_name not in valid_fields:
            bot.send_message(chat_id, f"Невідоме поле '{field_name}'. Будь ласка, введіть одне з наступних: {', '.join(valid_fields)}\n"
                                            "Натисніть /cancel для скасування.")
            bot.register_next_step_handler(message, edit_field_step)
            return

        user_data[chat_id]['field_to_edit'] = field_name
        current_value = user_data[chat_id]['record_data'].get(field_name, 'N/A') # Отримуємо поточне значення для підказки

        set_user_state(chat_id, STATE_EDIT_VALUE)
        # Додаємо специфічні підказки/клавіатури для певних полів
        reply_markup = types.ReplyKeyboardRemove()
        extra_info = ""
        if field_name == 'month_year':
             extra_info = " (у форматі 'Місяць Рік', наприклад, 'Січень 2024')"
        elif field_name == 'level':
             level_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
             for level_opt in EMPLOYEE_LEVELS:
                  level_keyboard.add(types.KeyboardButton(level_opt))
             reply_markup = level_keyboard
             extra_info = f" (Допустимі: {', '.join(EMPLOYEE_LEVELS)})"
        elif field_name in ['actual_hours', 'tasks_completed_value', 'usd_rate', 'eur_rate']:
             extra_info = " (число)"

        bot.send_message(chat_id, f"Введіть нове значення для поля '{field_name}' (поточне: '{current_value}'){extra_info}:\nНатисніть /skip або Enter, щоб залишити без змін.", reply_markup=reply_markup)
        bot.register_next_step_handler(message, edit_value_step)


    def edit_value_step(message):
        """Крок 3 редагування: Введення нового значення та завершення."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        # Дозволяємо порожнє повідомлення або /skip
        if get_user_state(chat_id) != STATE_EDIT_VALUE: return

        field_to_edit = user_data[chat_id].get('field_to_edit')
        record_id = user_data[chat_id].get('record_id_to_edit')

        if not field_to_edit or record_id is None:
             logger.error(f"Внутрішня помилка редагування: Відсутнє поле або ID в чаті {chat_id}. Дані: {user_data.get(chat_id)}")
             bot.send_message(chat_id, "❌ Внутрішня помилка редагування. Спробуйте почати з /edit ще раз.", reply_markup=get_main_menu_markup())
             reset_user_state(chat_id)
             return

        new_value_input = message.text.strip()

        if new_value_input.lower() == '/skip' or not new_value_input:
            # Користувач пропустив або залишив поле порожнім - не редагуємо це поле
            updates = {} # Порожній словник змін для менеджера
        else:
            # Готуємо словник з оновленням для менеджера
            updates = {field_to_edit: new_value_input}

        # Викликаємо метод редагування менеджера
        result = manager.edit_salary_record(record_id, updates)

        if isinstance(result, manager.MonthlySalaryRecord):
            bot.send_message(chat_id,
                f"✅ Запис #{result.id} успішно оновлено!\n"
                f"Нова розрахована зарплата: {format_salary(result.calculated_salary_uah, result.usd_rate, result.eur_rate)}",
                reply_markup=get_main_menu_markup()
            )
        elif isinstance(result, str) and result == "Змін не внесено.":
             bot.send_message(chat_id, "Змін не внесено.", reply_markup=get_main_menu_markup())
        else:
            bot.send_message(chat_id, f"❌ Помилка при редагуванні запису: {result}", reply_markup=get_main_menu_markup())

        reset_user_state(chat_id)


    # --- Функції кроків для видалення запису (/delete) ---
    # delete_start оголошена вище (може приймати record_id як аргумент)
    def delete_start(message, record_id=None):
        """Починає процес видалення запису."""
        chat_id = message.chat.id
        reset_user_state(chat_id)
        set_user_state(chat_id, STATE_DELETE_ID_CONFIRM)

        if record_id is not None:
             # Якщо ID передано (наприклад, з Inline кнопки), одразу переходимо
             message.text = str(record_id) # Імітуємо повідомлення з текстом ID
             bot.send_message(chat_id, f"Видалення запису #{record_id}. Перевіряю ID...", reply_markup=types.ReplyKeyboardRemove())
             delete_id_step(message)
        else:
            # Якщо ID не передано, запитуємо його
            bot.send_message(chat_id, "Видалення запису. Введіть ID запису, який потрібно видалити (натисніть /cancel для скасування):", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, delete_id_step)

    def delete_id_step(message):
        """Крок 1 видалення: Введення ID та видалення."""
        chat_id = message.chat.id
        if message.text and message.text.strip() == '/cancel': cancel_action(message); return
        if not message.text:
             bot.send_message(chat_id, "Будь ласка, введіть ID запису числом:", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(message, delete_id_step); return
        if get_user_state(chat_id) != STATE_DELETE_ID_CONFIRM: return

        record_id_input = message.text.strip()

        # Викликаємо метод видалення менеджера
        result = manager.delete_salary_record(record_id_input)

        if isinstance(result, manager.MonthlySalaryRecord):
            bot.send_message(chat_id, f"✅ Запис #{result.id} за {result.month_year} для {result.employee_name} успішно видалено!", reply_markup=get_main_menu_markup())
        else:
            bot.send_message(chat_id, f"❌ Помилка при видаленні запису: {result}", reply_markup=get_main_menu_markup())

        reset_user_state(chat_id) # Завершуємо розмову

    # --- Запускаємо бота ---
    main() # Викликаємо основну функцію запуску