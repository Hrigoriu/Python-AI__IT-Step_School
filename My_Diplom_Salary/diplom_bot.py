import os
import logging
import telebot as tb
from telebot import types

# Імпорти класів та функцій з наших файлів
from constants import (
    DATABASE_FILE, EMPLOYEE_LEVELS, MONTHS,
    STATE_IDLE, STATE_ADD_SURNAME, STATE_ADD_FIRST_NAME,
    STATE_ADD_PATRONYMIC, STATE_ADD_MONTH, STATE_ADD_LEVEL,
    STATE_ADD_HOURS, STATE_ADD_TASKS, STATE_ADD_USD, STATE_ADD_EUR,
    STATE_EDIT_ID, STATE_EDIT_FIELD, STATE_EDIT_VALUE,
    STATE_DELETE_ID_CONFIRM, STATE_REPORT_MONTH_INPUT, STATE_REPORT_YEAR_INPUT
) # Імпортуємо всі потрібні константи станів та інші з constants.py
from salary_manager import SalaryManager # Імпортуємо менеджер логіки зарплат (з salary_manager.py)
from utils import format_salary, validate_month_format, LOCALE_SETUP_MESSAGE # Імпортуємо утиліти (з utils.py)
# Прибрано імпортів random та string, оскільки вони не використовуються

# --- Налаштування бота та менеджера даних ---

TOKEN = '7917068514:AAF7-QdQQNg55_raHMDZN0_yI8ZNxkEfd-M'
# ADMIN_ID = 523793990 # ID адміністратора, якщо потрібно для інших цілей. Не використовується в поточному коді Salary.
#name: Salary
#name_bot: Salary_AI_bot


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

bot = tb.TeleBot(TOKEN)

manager = SalaryManager(DATABASE_FILE)
logger.info(f"Статус завантаження даних: {manager._load_data()}")
logger.info(LOCALE_SETUP_MESSAGE)


# --- Управління станами розмови ---
user_states = {}
user_data = {}

def get_user_state(chat_id):
    """Повертає поточний стан діалогу для заданого чату."""
    return user_states.get(chat_id, STATE_IDLE)

def set_user_state(chat_id, state):
    """Встановлює поточний стан діалогу для заданого чату."""
    user_states[chat_id] = state

def reset_user_state(chat_id):
    """Скидає стан діалогу та очищає тимчасові дані користувача."""
    user_states.pop(chat_id, None)
    user_data.pop(chat_id, None)
    try:
        bot.clear_step_handler(chat_id)
    except Exception:
        pass


# --- Головне меню ReplyKeyboardMarkup ---
def get_main_menu_markup():
    """Створює ReplyKeyboardMarkup для головного меню (тільки функціонал Salary)."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_add = types.KeyboardButton('➕ Додати запис')
    btn_list = types.KeyboardButton('📋 Список записів')
    btn_reports = types.KeyboardButton('📊 Звіти')
    btn_settings = types.KeyboardButton('⚙️ Налаштування')

    markup.add(btn_add, btn_list)
    markup.add(btn_reports, btn_settings)

    return markup


# --- Обробники команд ---

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Обробляє команди /start та /help. Показує головне меню."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    user_name = message.from_user.first_name if message.from_user else 'Користувач'

    welcome_text = (
        f"Привіт, {user_name}! Я бот для обліку зарплат.\n"
        "Використовуйте кнопки меню нижче або надсилайте команди:\n"
        "/list, /month, /year_total, /year_avg, /settings, /settings_edit, /details, /add, /edit, /delete\n"
        "Натисніть /cancel, щоб скасувати поточну дію в будь-який момент."
    )
    bot.send_message(chat_id, welcome_text, reply_markup=get_main_menu_markup())

@bot.message_handler(commands=['cancel'])
def cancel_action(message):
    """Обробляє команду /cancel."""
    chat_id = message.chat.id
    current_state = get_user_state(chat_id)
    reset_user_state(chat_id)
    if current_state != STATE_IDLE:
        bot.send_message(chat_id, "Дію скасовано.", reply_markup=get_main_menu_markup())
    else:
        bot.send_message(chat_id, "Немає активної дії для скасування.", reply_markup=get_main_menu_markup())


# --- Обробники команд Salary Bot ---

@bot.message_handler(commands=['list'])
def list_records_command(message):
    """Показує всі записи про зарплату (сортовані за місяцем)."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    records = manager.get_all_salary_records(sort_by='month')

    if not records:
        bot.send_message(chat_id, "Дані відсутні.")
        return

    report_parts = ["--- Усі записи про зарплату (за місяцем) ---"]
    for record in records:
        report_parts.append(manager.get_record_details_string(record))
    report_parts.append("--- Кінець списку ---")

    full_report = "\n".join(report_parts)
    for i in range(0, len(full_report), 4000):
         bot.send_message(chat_id, full_report[i:i+4000])


@bot.message_handler(commands=['month'])
def report_by_month_command(message):
    """Обробляє команду /month <Місяць Рік>."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    args = message.text.split()[1:]
    if not args:
        set_user_state(chat_id, STATE_REPORT_MONTH_INPUT)
        bot.send_message(chat_id, "Будь ласка, вкажіть місяць після команди (наприклад, '/month Січень 2024') або введіть його окремо:", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, process_report_month_input)
        return

    month_year_input = " ".join(args)
    result = manager.get_salary_report_by_month(month_year_input)

    if isinstance(result, str):
        bot.send_message(chat_id, result)
    else:
        report_parts = [f"--- Записи за {result[0].month_year} ---"] if result else [f"Дані за {month_year_input} не знайдено."]
        for record in result:
             report_parts.append(manager.get_record_details_string(record))
        if result:
            report_parts.append("--- Кінець списку за місяць ---")
        full_report = "\n".join(report_parts)
        for i in range(0, len(full_report), 4000):
            bot.send_message(chat_id, full_report[i:i+4000])


@bot.message_handler(commands=['year_total'])
def report_year_total_command(message):
    """Обробляє команду /year_total <Рік>."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    args = message.text.split()[1:]
    if not args:
        set_user_state(chat_id, STATE_REPORT_YEAR_INPUT)
        user_data[chat_id] = {'report_type': 'year_total'}
        bot.send_message(chat_id, "Будь ласка, вкажіть рік після команди (наприклад, '/year_total 2024') або введіть його окремо:", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, process_report_year_input)
        return

    year_input = args[0]
    result = manager.get_total_salary_report_by_year(year_input)

    if isinstance(result, str):
         bot.send_message(chat_id, result)
    else:
         report_text = (
             f"--- Загальна зарплата за {result['year']} рік ---\n"
             f"Всього записів за рік: {result['record_count']}\n"
             f"Загальна сума: {result['formatted_total']}\n"
             "------------------------------"
         )
         bot.send_message(chat_id, report_text)


@bot.message_handler(commands=['year_avg'])
def report_year_avg_command(message):
    """Обробляє команду /year_avg <Рік>."""
    chat_id = message.chat.id
    reset_user_state(chat_id)

    args = message.text.split()[1:]
    if not args:
        set_user_state(chat_id, STATE_REPORT_YEAR_INPUT)
        user_data[chat_id] = {'report_type': 'year_avg'}
        bot.send_message(chat_id, "Будь ласка, вкажіть рік після команди (наприклад, '/year_avg 2024') або введіть його окремо:", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, process_report_year_input)
        return

    year_input = args[0]
    result = manager.get_average_salary_report_by_year(year_input)

    if isinstance(result, str):
         bot.send_message(chat_id, result)
    else:
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
    reset_user_state(chat_id)

    args = message.text.split()[1:]
    if not args:
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
        formatted_help_text = "<b>Як редагувати налаштування:</b>\n" + help_text.replace('`', '<code>').replace('\n', '<br>')
        bot.send_message(chat_id, formatted_help_text, parse_mode="HTML")
        return

    setting_type = args[0].lower()
    result = "Невірний формат команди або недостатньо параметрів. Використовуйте `/settings_edit` для довідки."

    if setting_type == 'base_amount' and len(args) == 3:
        level = args[1]
        value = args[2]
        result = manager.edit_base_amount_setting(level, value)
    elif setting_type == 'coefficient' and len(args) == 3:
        level = args[1]
        value = args[2]
        result = manager.edit_coefficient_setting(level, value)
    elif setting_type == 'task_cost' and len(args) >= 3:
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

    details_text = manager.get_record_details_string(record)

    action_markup = types.InlineKeyboardMarkup(row_width=2)
    btn_edit = types.InlineKeyboardButton('✍️ Редагувати', callback_data=f'edit_rec_{record.id}')
    btn_delete = types.InlineKeyboardButton('🗑️ Видалити', callback_data=f'delete_rec_{record.id}')
    action_markup.add(btn_edit, btn_delete)

    bot.send_message(chat_id, details_text, reply_markup=action_markup)


# --- Обробник головного меню ReplyKeyboardMarkup та інших текстових повідомлень ---
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    """Обробляє текстові повідомлення, які не є командами."""
    chat_id = message.chat.id
    message_text = message.text.strip()
    current_state = get_user_state(chat_id)

    if current_state != STATE_IDLE:
         bot.send_message(chat_id, "❌ Поточну операцію перервано або виникла помилка. Спробуйте ще раз або натисніть /cancel.", reply_markup=get_main_menu_markup())
         reset_user_state(chat_id)
         return

    match message_text:
        case '➕ Додати запис':
            add_start(message)
        case '📋 Список записів':
            list_records_command(message)
        case '📊 Звіти':
            report_markup = types.InlineKeyboardMarkup()
            btn_month_report = types.InlineKeyboardButton('Звіт за місяць', callback_data='report_type_month')
            btn_year_total = types.InlineKeyboardButton('Загальний за рік', callback_data='report_type_year_total')
            btn_year_avg = types.InlineKeyboardButton('Середній за рік', callback_data='report_type_year_avg')
            report_markup.add(btn_month_report, btn_year_total, btn_year_avg, row_width=1)
            bot.send_message(chat_id, "Оберіть тип звіту:", reply_markup=report_markup)
        case '⚙️ Налаштування':
            settings_markup = types.InlineKeyboardMarkup()
            btn_show_settings = types.InlineKeyboardButton('Показати поточні', callback_data='settings_show')
            btn_edit_settings_help = types.InlineKeyboardButton('Як редагувати', callback_data='settings_edit_help')
            settings_markup.add(btn_show_settings, btn_edit_settings_help, row_width=1)
            bot.send_message(chat_id, "Оберіть дію з налаштуваннями:", reply_markup=settings_markup)

        case _:
            bot.send_message(chat_id, "Невідома команда або текст. Використовуйте кнопки меню або команди.", reply_markup=get_main_menu_markup())


# --- Обробник Inline клавіатур ---
@bot.callback_query_handler(func=lambda call: call.data.startswith(('report_type_', 'settings_', 'edit_rec_', 'delete_rec_')))
def handle_inline_buttons(call):
    """Обробляє натискання Inline кнопок."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    callback_data = call.data

    bot.answer_callback_query(call.id, text='ОК')

    if callback_data.startswith('report_type_'):
        report_type = callback_data.split('_')[2]

        try:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Оберіть тип звіту:', reply_markup=None)
        except Exception as e:
             logger.error(f"Помилка при редагуванні повідомлення {message_id} в чаті {chat_id}: {e}")
             pass

        if report_type == 'month':
            set_user_state(chat_id, STATE_REPORT_MONTH_INPUT)
            bot.send_message(chat_id, "Введіть місяць для звіту (наприклад, 'Січень 2024'):", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(call.message, process_report_month_input)
        elif report_type in ['year_total', 'year_avg']:
             user_data[chat_id] = {'report_type': report_type}
             set_user_state(chat_id, STATE_REPORT_YEAR_INPUT)
             bot.send_message(chat_id, "Введіть рік для звіту (наприклад, '2024'):", reply_markup=types.ReplyKeyboardRemove())
             bot.register_next_step_handler(call.message, process_report_year_input)

    elif callback_data.startswith('settings_'):
        action = callback_data.split('_')[1]
        try:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Оберіть дію з налаштуваннями:', reply_markup=None)
        except Exception as e:
             logger.error(f"Помилка при редагуванні повідомлення {message_id} в чаті {chat_id}: {e}")
             pass

        if action == 'show':
            bot.send_message(chat_id, manager.get_settings_string(), reply_markup=get_main_menu_markup())
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
             formatted_help_text = "<b>Як редагувати налаштування:</b>\n" + help_text.replace('`', '<code>').replace('\n', '<br>')
             bot.send_message(chat_id, formatted_help_text, parse_mode="HTML", reply_markup=get_main_menu_markup())


    elif callback_data.startswith(('edit_rec_', 'delete_rec_')):
         parts = callback_data.split('_')
         action = parts[0]
         try:
             record_id = int(parts[2])

             try:
                  original_text = call.message.text
                  action_text = "➡️ Редагування запису..." if action == 'edit' else "➡️ Видалення запису..."
                  bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=original_text + f"\n\n{action_text}", reply_markup=None)
             except Exception as e:
                  logger.error(f"Помилка при редагуванні повідомлення деталей {message_id} в чаті {chat_id}: {e}")
                  pass

             if action == 'delete' :
                  result = manager.delete_salary_record(record_id)
                  if isinstance(result, manager.MonthlySalaryRecord):
                       bot.send_message(chat_id, f"✅ Запис #{record_id} успішно видалено!", reply_markup=get_main_menu_markup())
                  else:
                       bot.send_message(chat_id, f"❌ Помилка видалення запису #{record_id}: {result}", reply_markup=get_main_menu_markup())
             elif action == 'edit':
                  bot.send_message(chat_id, f"ОК. Починаю редагування запису #{record_id}.", reply_markup=types.ReplyKeyboardRemove())
                  edit_start(call.message, record_id=record_id)

         except (ValueError, IndexError) as e:
             logger.error(f"Помилка парсингу callback_data '{callback_data}': {e}")
             bot.send_message(chat_id, "Помилка: Невірний формат даних для редагування/видалення.", reply_markup=get_main_menu_markup())


# --- Обробка введених даних для звітів (кроки після вибору типу звіту) ---
def process_report_month_input(message):
    """Крок 1 звіту за місяць: введення Місяць Рік."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_REPORT_MONTH_INPUT:
         bot.send_message(chat_id, "Неочікуване повідомлення. Операцію скасовано.", reply_markup=get_main_menu_markup())
         reset_user_state(chat_id)
         return

    month_year_input = message.text.strip()

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть місяць текстом (наприклад, 'Січень 2024') або /cancel:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, process_report_month_input)
         return


    result = manager.get_salary_report_by_month(month_year_input)

    if isinstance(result, str):
        bot.send_message(chat_id, f"❌ Помилка або дані не знайдено: {result}\nСпробуйте ще раз або /cancel.")
        bot.register_next_step_handler(message, process_report_month_input)
        return
    else:
        report_parts = [f"--- Записи за {result[0].month_year} ---"] if result else [f"Дані за {month_year_input} не знайдено."]
        for record in result:
             report_parts.append(manager.get_record_details_string(record))
        if result:
            report_parts.append("--- Кінець списку за місяць ---")
        full_report = "\n".join(report_parts)
        for i in range(0, len(full_report), 4000):
            bot.send_message(chat_id, full_report[i:i+4000])

        reset_user_state(chat_id)
        bot.send_message(chat_id, "Виберіть наступну дію:", reply_markup=get_main_menu_markup())


def process_report_year_input(message):
    """Крок 1 звіту за рік: введення Рік."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_REPORT_YEAR_INPUT:
         bot.send_message(chat_id, "Неочікуване повідомлення. Операцію скасовано.", reply_markup=get_main_menu_markup())
         reset_user_state(chat_id)
         return

    year_input = message.text.strip()

    try:
        int(year_input)
    except ValueError:
        bot.send_message(chat_id, "❌ Будь ласка, введіть рік числом (наприклад, '2024') або /cancel:", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, process_report_year_input)
        return


    report_type = user_data[chat_id].get('report_type')

    if report_type == 'year_total':
        result = manager.get_total_salary_report_by_year(year_input)
    elif report_type == 'year_avg':
        result = manager.get_average_salary_report_by_year(year_input)
    else:
        result = "Внутрішня помилка: Невідомий тип звіту."

    if isinstance(result, str):
         bot.send_message(chat_id, f"❌ Помилка або дані не знайдено: {result}\nСпробуйте ще раз або /cancel.")
         bot.register_next_step_handler(message, process_report_year_input)
    else:
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
              report_text = result
         bot.send_message(chat_id, report_text)

         reset_user_state(chat_id)
         bot.send_message(chat_id, "Виберіть наступну дію:", reply_markup=get_main_menu_markup())


# --- Реалізація багатоетапних діалогів Salary Bot (/add, /edit, /delete) ---

def add_start(message):
    """Починає процес додавання запису, запитуючи прізвище працівника."""
    chat_id = message.chat.id
    reset_user_state(chat_id)
    set_user_state(chat_id, STATE_ADD_SURNAME)
    user_data[chat_id] = {}
    bot.send_message(chat_id, "Додавання нового запису про зарплату.\nВведіть прізвище працівника:", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, add_surname_step)

# --- Функції кроків для додавання запису (/add) ---
def add_surname_step(message):
    """Крок 1 додавання: Прізвище працівника."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_SURNAME: return

    if not message.text:
         bot.send_message(chat_id, "Прізвище не може бути порожнім. Введіть прізвище працівника:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, add_surname_step); return

    surname = message.text.strip().title()
    user_data[chat_id]['surname'] = surname
    set_user_state(chat_id, STATE_ADD_FIRST_NAME)
    bot.send_message(chat_id, "Введіть ім'я працівника:")
    bot.register_next_step_handler(message, add_first_name_step)

def add_first_name_step(message):
    """Крок 2 додавання: Ім'я працівника."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_FIRST_NAME: return

    if not message.text:
         bot.send_message(chat_id, "Ім'я не може бути порожнім. Введіть ім'я працівника:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, add_first_name_step); return

    first_name = message.text.strip().title()
    user_data[chat_id]['first_name'] = first_name
    set_user_state(chat_id, STATE_ADD_PATRONYMIC)
    bot.send_message(chat_id, "Введіть по-батькові працівника (або Enter, якщо немає):")
    bot.register_next_step_handler(message, add_patronymic_step)

def add_patronymic_step(message):
    """Крок 3 додавання: По-батькові працівника."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_PATRONYMIC: return

    patronymic = message.text.strip().title() if message.text else ""
    user_data[chat_id]['patronymic'] = patronymic

    surname = user_data[chat_id].get('surname', '')
    first_name = user_data[chat_id].get('first_name', '')
    full_name_parts = [part for part in [surname, first_name, patronymic] if part]
    full_employee_name = " ".join(full_name_parts)

    if not full_employee_name:
         bot.send_message(chat_id, "Ім'я працівника не може бути повністю порожнім. Спробуйте ввести прізвище або ім'я.", reply_markup=types.ReplyKeyboardRemove())
         add_start(message)
         return


    user_data[chat_id]['employee_name'] = full_employee_name

    set_user_state(chat_id, STATE_ADD_MONTH)
    bot.send_message(chat_id, f"OK, працівник: {full_employee_name}\nВведіть місяць (наприклад, 'Січень 2024'):")
    bot.register_next_step_handler(message, add_month_step)

def add_month_step(message):
    """Крок додавання: Місяць."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_MONTH: return

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть місяць текстом (наприклад, 'Січень 2024'):")
         bot.register_next_step_handler(message, add_month_step); return

    month_year = message.text.strip()
    is_valid, result = validate_month_format(month_year)
    if not is_valid:
        bot.send_message(chat_id, f"❌ Помилка: {result}\nВведіть місяць ще раз (наприклад, 'Січень 2024'):")
        bot.register_next_step_handler(message, add_month_step)
        return

    user_data[chat_id]['month_year'] = result

    employee_name = user_data[chat_id].get('employee_name')
    if employee_name is None:
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
    """Крок додавання: Рівень."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_LEVEL: return

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть рівень текстом або виберіть кнопку:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, add_level_step); return

    level = message.text.strip().capitalize()
    if level not in EMPLOYEE_LEVELS:
        level_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for level_opt in EMPLOYEE_LEVELS:
             level_keyboard.add(types.KeyboardButton(level_opt))
        bot.send_message(chat_id, f"❌ Невірний рівень '{message.text}'. Виберіть зі списку: {', '.join(EMPLOYEE_LEVELS)}:", reply_markup=level_keyboard)
        bot.register_next_step_handler(message, add_level_step)
        return

    user_data[chat_id]['level'] = level
    set_user_state(chat_id, STATE_ADD_HOURS)
    bot.send_message(chat_id, "Введіть фактично відпрацьовані години (число):", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, add_hours_step)

def add_hours_step(message):
    """Крок додавання: Години."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_HOURS: return

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть відпрацьовані години числом:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, add_hours_step); return

    try:
        hours = float(message.text.strip())
        if hours < 0:
            bot.send_message(chat_id, "❌ Відпрацьовані години не можуть бути від'ємними. Введіть число годин:")
            bot.register_next_step_handler(message, add_hours_step)
            return
        user_data[chat_id]['actual_hours'] = hours
        set_user_state(chat_id, STATE_ADD_TASKS)
        bot.send_message(chat_id, f"Введіть загальну вартість виконаних завдань за місяць (число). Наприклад, {manager.settings.task_costs.get('Simple', 1000.0):.2f} за Simple задачу:")
        bot.register_next_step_handler(message, add_tasks_step)
    except (ValueError, TypeError):
        bot.send_message(chat_id, "❌ Будь ласка, введіть коректне числове значення для годин:")
        bot.register_next_step_handler(message, add_hours_step)

def add_tasks_step(message):
    """Крок додавання: Вартість завдань."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_TASKS: return

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть вартість завдань числом:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, add_tasks_step); return

    try:
        tasks_value = float(message.text.strip())
        if tasks_value < 0:
            bot.send_message(chat_id, "❌ Вартість завдань не може бути від'ємною. Введіть число:")
            bot.register_next_step_handler(message, add_tasks_step)
            return
        user_data[chat_id]['tasks_completed_value'] = tasks_value
        set_user_state(chat_id, STATE_ADD_USD)

        last_record = next(iter(reversed(manager.monthly_records)), None)
        default_usd = last_record.usd_rate if last_record else manager.settings.default_rates.get("USD", 40.0)

        bot.send_message(chat_id, f"Введіть курс долара (USD) за місяць (наприклад, {default_usd:.2f}). Надішліть Enter, щоб використати це значення:")
        bot.register_next_step_handler(message, add_usd_rate_step)

    except (ValueError, TypeError):
        bot.send_message(chat_id, "❌ Будь ласка, введіть коректне числове значення для вартості завдань:")
        bot.register_next_step_handler(message, add_tasks_step)

def add_usd_rate_step(message):
    """Крок додавання: Курс USD."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_USD: return

    usd_input = message.text.strip()
    last_record = next(iter(reversed(manager.monthly_records)), None)
    default_usd = last_record.usd_rate if last_record else manager.settings.default_rates.get("USD", 40.0)
    usd_rate = default_usd

    if usd_input:
        try:
            usd_rate = float(usd_input)
            if usd_rate <= 0:
                bot.send_message(chat_id, "❌ Курс долара має бути більше нуля. Введіть число або залиште поле порожнім:")
                bot.register_next_step_handler(message, add_usd_rate_step)
                return
            if usd_rate < 10 or usd_rate > 200:
                 bot.send_message(chat_id, f"⚠️ Увага: Введений курс долара ({usd_rate:.2f}) виглядає незвично.")
        except (ValueError, TypeError):
            bot.send_message(chat_id, "❌ Будь ласка, введіть коректне числове значення для курсу долара або залиште поле порожнім:")
            bot.register_next_step_handler(message, add_usd_rate_step)
            return

    user_data[chat_id]['usd_rate'] = usd_rate
    set_user_state(chat_id, STATE_ADD_EUR)
    default_eur = last_record.eur_rate if last_record else manager.settings.default_rates.get("EUR", 43.0)

    bot.send_message(chat_id, f"Введіть курс євро (EUR) за місяць (наприклад, {default_eur:.2f}). Надішліть Enter, щоб використати це значення:")
    bot.register_next_step_handler(message, add_eur_rate_step)


def add_eur_rate_step(message):
    """Крок додавання: Курс EUR та завершення."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_ADD_EUR: return

    eur_input = message.text.strip()
    last_record = next(iter(reversed(manager.monthly_records)), None)
    default_eur = last_record.eur_rate if last_record else manager.settings.default_rates.get("EUR", 43.0)
    eur_rate = default_eur

    if eur_input:
        try:
            eur_rate = float(eur_input)
            if eur_rate <= 0:
                bot.send_message(chat_id, "❌ Курс євро має бути більше нуля. Введіть число або залиште поле порожнім:")
                bot.register_next_step_handler(message, add_eur_rate_step)
                return
            if eur_rate < 10 or eur_rate > 200:
                bot.send_message(chat_id, f"⚠️ Увага: Введений курс євро ({eur_rate:.2f}) виглядає незвично.")
        except (ValueError, TypeError):
            bot.send_message(chat_id, "❌ Будь ласка, введіть коректне числове значення для курсу євро або залиште поле порожнім:")
            bot.register_next_step_handler(message, add_eur_rate_step)
            return

    user_data[chat_id]['eur_rate'] = eur_rate

    name = user_data[chat_id].get('employee_name')
    month = user_data[chat_id].get('month_year')
    level = user_data[chat_id].get('level')
    hours = user_data[chat_id].get('actual_hours')
    tasks = user_data[chat_id].get('tasks_completed_value')
    usd = user_data[chat_id].get('usd_rate')
    eur = user_data[chat_id].get('eur_rate')

    if None in [name, month, level, hours, tasks, usd, eur]:
         logger.error(f"Внутрішня помилка: Неповні дані для додавання запису в чаті {chat_id}. Дані: {user_data.get(chat_id)}")
         bot.send_message(chat_id, "❌ Внутрішня помилка: Не всі дані були зібрані. Спробуйте ще раз /add.", reply_markup=get_main_menu_markup())
    else:
        result = manager.add_salary_record(name, month, level, hours, tasks, usd, eur)

        if isinstance(result, manager.MonthlySalaryRecord):
            bot.send_message(chat_id,
                f"✅ Запис #{result.id} за {result.month_year} для {result.employee_name} успішно додано!\n"
                f"Розрахована зарплата: {format_salary(result.calculated_salary_uah, result.usd_rate, result.eur_rate)}",
                reply_markup=get_main_menu_markup()
            )
        else:
            bot.send_message(chat_id, f"❌ Помилка при додаванні запису: {result}", reply_markup=get_main_menu_markup())

    reset_user_state(chat_id)


# --- Функції кроків для редагування запису (/edit) ---
@bot.message_handler(commands=['edit'])
def edit_start(message, record_id=None):
    """Починає процес редагування запису."""
    chat_id = message.chat.id
    reset_user_state(chat_id)
    set_user_state(chat_id, STATE_EDIT_ID)
    user_data[chat_id] = {}

    if record_id is not None:
         message.text = str(record_id)
         edit_id_step(message)
    else:
        bot.send_message(chat_id, "Редагування запису. Введіть ID запису, який потрібно редагувати (натисніть /cancel для скасування):", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, edit_id_step)

def edit_id_step(message):
    """Крок 1 редагування: Введення ID."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_EDIT_ID: return

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть ID запису числом:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, edit_id_step); return


    record_id_input = message.text.strip()
    record_to_edit = manager.find_record_by_id(record_id_input)

    if not record_to_edit:
        bot.send_message(chat_id, f"❌ Запис із ID '{record_id_input}' не знайдено. Будь ласка, введіть коректний ID або /cancel:")
        bot.register_next_step_handler(message, edit_id_step)
        return

    user_data[chat_id]['record_id_to_edit'] = record_to_edit.id
    user_data[chat_id]['record_data'] = record_to_edit.to_dict()

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
    if get_user_state(chat_id) != STATE_EDIT_FIELD: return

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть назву поля текстом:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, edit_field_step); return

    field_name = message.text.strip().lower()
    valid_fields = ['employee_name', 'month_year', 'level', 'actual_hours', 'tasks_completed_value', 'usd_rate', 'eur_rate']

    if field_name not in valid_fields:
        bot.send_message(chat_id, f"❌ Невідоме поле '{field_name}'. Будь ласка, введіть одне з наступних: {', '.join(valid_fields)}\n"
                                        "Натисніть /cancel для скасування.")
        bot.register_next_step_handler(message, edit_field_step)
        return

    user_data[chat_id]['field_to_edit'] = field_name
    current_value = user_data[chat_id]['record_data'].get(field_name, 'N/A')

    set_user_state(chat_id, STATE_EDIT_VALUE)
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
        updates = {}
        result = "Змін не внесено."
    else:
        updates = {field_to_edit: new_value_input}
        if field_to_edit in ['actual_hours', 'tasks_completed_value', 'usd_rate', 'eur_rate']:
            try:
                float(new_value_input)
            except ValueError:
                bot.send_message(chat_id, f"❌ Помилка: Значення для поля '{field_to_edit}' має бути числом. Спробуйте ввести значення ще раз або /cancel.", reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(message, edit_value_step)
                return
        if field_to_edit == 'month_year':
            is_valid, result_month_format = validate_month_format(new_value_input)
            if not is_valid:
                 bot.send_message(chat_id, f"❌ Помилка: {result_month_format}\nСпробуйте ввести місяць ще раз або /cancel.", reply_markup=types.ReplyKeyboardRemove())
                 bot.register_next_step_handler(message, edit_value_step)
                 return
            updates[field_to_edit] = result_month_format
        if field_to_edit == 'level':
             new_value_input_formatted = new_value_input.capitalize()
             if new_value_input_formatted not in EMPLOYEE_LEVELS:
                 level_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                 for level_opt in EMPLOYEE_LEVELS:
                      level_keyboard.add(types.KeyboardButton(level_opt))
                 bot.send_message(chat_id, f"❌ Помилка: Невірний рівень '{new_value_input}'. Допустимі: {', '.join(EMPLOYEE_LEVELS)}\nСпробуйте ввести рівень ще раз або /cancel.", reply_markup=level_keyboard)
                 bot.register_next_step_handler(message, edit_value_step)
                 return
             updates[field_to_edit] = new_value_input_formatted
        if field_to_edit == 'employee_name':
             updates[field_to_edit] = new_value_input.title()


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
@bot.message_handler(commands=['delete'])
def delete_start(message, record_id=None):
    """Починає процес видалення запису."""
    chat_id = message.chat.id
    reset_user_state(chat_id)
    set_user_state(chat_id, STATE_DELETE_ID_CONFIRM)

    if record_id is not None:
         message.text = str(record_id)
         delete_id_step(message)
    else:
        bot.send_message(chat_id, "Видалення запису. Введіть ID запису, який потрібно видалити (натисніть /cancel для скасування):", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, delete_id_step)

def delete_id_step(message):
    """Крок 1 видалення: Введення ID та видалення."""
    chat_id = message.chat.id
    if message.text and message.text.strip() == '/cancel': cancel_action(message); return
    if get_user_state(chat_id) != STATE_DELETE_ID_CONFIRM: return

    if not message.text:
         bot.send_message(chat_id, "Будь ласка, введіть ID запису числом:", reply_markup=types.ReplyKeyboardRemove())
         bot.register_next_step_handler(message, delete_id_step); return

    record_id_input = message.text.strip()

    try:
        int(record_id_input)
    except ValueError:
        bot.send_message(chat_id, f"❌ Помилка: ID запису має бути числом. Введіть коректний ID або /cancel:", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, delete_id_step); return

    result = manager.delete_salary_record(record_id_input)

    if isinstance(result, manager.MonthlySalaryRecord):
        bot.send_message(chat_id, f"✅ Запис #{result.id} за {result.month_year} для {result.employee_name} успішно видалено!", reply_markup=get_main_menu_markup())
    else:
        bot.send_message(chat_id, f"❌ Помилка при видаленні запису: {result}", reply_markup=get_main_menu_markup())

    reset_user_state(chat_id)


# --- Запускаємо бота ---
if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
