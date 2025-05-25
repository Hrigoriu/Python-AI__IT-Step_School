import telebot  # Імпортуємо pyTelegramBotAPI
from telebot import types
from tictactoe_game import TicTacToeGame  # Імпортуємо наш клас гри
import random # Потрібен для випадкового вибору першого гравця

TOKEN ='7052289932:AAFGphvPUSHdSMjZfqHTy3iE6ODWSzTjC8A' # мій токен :)
#name: «Хрестики-Нулики»
#bot: @tictactoe_HW_bot

if not TOKEN:
    print('Помилка: Не знайдено "@tictactoe_HW_bot"!')
    print('Будь ласка, встановіть її перед запуском.')
    exit(1)

bot = telebot.TeleBot(TOKEN)

# --- Стан бота для керування іграми та гравцями ---

# Гравець, який очікує на пару. Зберігає chat_id.
waiting_player: int | None = None

"""
# Активні ігри.
Ключ: chat_id гравця X (це унікальний ідентифікатор гри),
Значення: словник зі станом гри:
 {'instance': TicTacToeGame object,
  'players': {chat_id_X: 'X', chat_id_O: 'O'},
  'current_turn_id': chat_id гравця, чий хід,
  'message_ids': {chat_id_X: board_message_id_for_X, chat_id_O: board_message_id_for_O}
 }
"""
active_games: dict[int, dict] = {}

# Зворотне відображення: chat_id гравця -> chat_id гравця X (тобто game_id)
player_to_game: dict[int, int] = {}

# --- Функції для створення клавіатур ---

def create_main_reply_keyboard():
    """Створює головну Reply клавіатуру з кнопкою 'Знайти суперника'."""
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    find_button = types.KeyboardButton('Знайти суперника')
    markup.add(find_button)
    return markup

def create_board_markup(game_id: int, board: list[list[str]]) -> types.InlineKeyboardMarkup:
    """Метод для створення Inline клавіатуру, що представляє дошку."""
    markup = types.InlineKeyboardMarkup()
    for r_idx, row in enumerate(board):
        buttons = []
        for c_idx, cell in enumerate(row):
            button_text = cell if cell != ' ' else '⋅'      # Використовуємо '⋅' для візуалізації порожніх клітинок
            callback_data = f"{game_id}:{r_idx}:{c_idx}"
            buttons.append(types.InlineKeyboardButton(text=button_text, callback_data=callback_data))
        markup.add(*buttons)
    return markup


def send_or_update_board(chat_id: int, game_id: int):
    """Метод, який надсилає або оновлює повідомлення з дошки до гравця."""
    game_state = active_games.get(game_id)
    if not game_state:
        return

    game_instance = game_state['instance']
    board = game_instance.get_board()
    message_id = game_state['message_ids'].get(chat_id)
    current_turn_id = game_state['current_turn_id']

    # Отримуємо id гравців X та O. Використовуємо sorted, щоб завжди мати однаковий порядок,
    player_ids = list(game_state['players'].keys())
    player_x_id = player_ids[0] if game_state['players'][player_ids[0]] == 'X' else player_ids[1]
    player_o_id = player_ids[0] if game_state['players'][player_ids[0]] == 'O' else player_ids[1]


    # Обробляємо можливі помилки, якщо chat_id вже не дійсний
    try:
        player_x_name = bot.get_chat(player_x_id).first_name if player_x_id else 'Гравець X'
    except Exception:
        player_x_name = 'Гравець X (недоступно)'
    try:
         player_o_name = bot.get_chat(player_o_id).first_name if player_o_id else 'Гравець O'
    except Exception:
         player_o_name = 'Гравець O (недоступно)'


    text = f'Гра #{game_id}\n'
    text += f'"{game_state["players"][player_x_id]}": {player_x_name}\n'
    text += f'"{game_state["players"][player_o_id]}": {player_o_name}\n\n'

    if game_instance.is_game_over():
        winner_mark = None
        for player_id, mark in game_state['players'].items():
             if game_instance.check_win(mark):
                 winner_mark = mark
                 break

        if winner_mark:
            winner_name = player_x_name if game_state['players'][player_x_id] == winner_mark else player_o_name
            text += f'✨ Гра закінчена! Переміг гравець "{winner_mark}" ({winner_name})! ✨'
        elif game_instance.check_draw(): # check_draw сам встановлює _is_game_over
            text += '🤝 Гра закінчена! Нічия! 🤝'
        else:
             text += '❗ Гра завершена, результат невизначений.'

        # Після завершення гри кнопки робимо неактивними або прибираємо
        markup = create_board_markup(game_id, board)
        for row_buttons in markup.keyboard:
            for button in row_buttons:
                button.callback_data = 'game_over' # Встановлюємо спеціальний callback
        markup = None


    else:
        current_player_name = player_x_name if current_turn_id == player_x_id else player_o_name
        current_player_mark = game_state['players'][current_turn_id]
        text += f'⏳ Хід гравця "{current_player_mark}" ({current_player_name}).'
        markup = create_board_markup(game_id, board)

    try:
        if message_id:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=text,
                reply_markup=markup # Це inline клавіатура дошки
            )
        else:
            msg = bot.send_message(
                chat_id=chat_id,
                text=text,
                reply_markup=markup, # Це inline клавіатура дошки
                parse_mode='Markdown'
            )
            game_state['message_ids'][chat_id] = msg.message_id
    except telebot.apihelper.ApiTelegramException as e:
        print(f'Помилка при надсиланні/редагуванні дошки для {chat_id}: {e}')
        if message_id:
             try:
                  bot.delete_message(chat_id, message_id)
             except Exception:
                  pass

             try:
                  msg = bot.send_message(
                      chat_id=chat_id,
                      text=text,
                      reply_markup=markup,
                      parse_mode='Markdown'
                  )
                  game_state['message_ids'][chat_id] = msg.message_id
             except Exception as e2:
                  print(f'Помилка при надсиланні нового повідомлення для {chat_id}: {e2}')


def end_game_for_players(game_id: int):
    """Видаляє гру зі стану та повідомляє гравців, повертаючи головну клавіатуру."""
    game_state = active_games.get(game_id)
    if not game_state:
        return

    players_to_notify = list(game_state['players'].keys())

    del active_games[game_id]
    for player_id in players_to_notify:
        if player_id in player_to_game:
             del player_to_game[player_id]

    print(f'Гра {game_id} видалена зі стану.')

    # Надсилаємо гравцям повідомлення про завершення та головну клавіатуру
    finish_message = 'Гра завершена.'

    # Надсилаємо нове повідомлення з пропозицією зіграти ще раз
    prompt_new_game_text = 'Щоб знайти нового суперника, натисніть кнопку нижче 👇'
    main_keyboard = create_main_reply_keyboard()

    for player_id in players_to_notify:
         try:
              bot.send_message(player_id, prompt_new_game_text, reply_markup=main_keyboard)
         except Exception as e:
              print(f'Помилка надсилання повідомлення гравцю {player_id} після завершення гри: {e}')


# --- Функція для обробки пошуку гравця (спільна логіка для команди і кнопки) ---

def _handle_find_player_action(chat_id: int):
    """Обробляє логіку пошуку або черги гравця."""
    global waiting_player

    if chat_id in player_to_game:
        bot.send_message(chat_id, 'Ти вже береш участь у грі! 😉')
        return

    if waiting_player is None:
        waiting_player = chat_id
        bot.send_message(chat_id, 'Шукаємо суперника... Зачекай іншого гравця або попроси друга написати play або натиснути "Знайти суперника".')
        print(f'Гравець {chat_id} став у чергу.')
    else:
        player1_id = waiting_player
        player2_id = chat_id

        if player1_id == player2_id:
            bot.send_message(chat_id, 'Ти вже в черзі на пошук суперника.')
            return

        waiting_player = None # Прибираємо першого гравця з черги

        game_id = player1_id    # Використовуємо chat_id гравця X як ID гри

        new_game = TicTacToeGame()

        players = {}
        if random.choice([True, False]):
            players[player1_id] = 'X'
            players[player2_id] = 'O'
            first_turn_id = player1_id
        else:
            players[player1_id] = 'O'
            players[player2_id] = 'X'
            first_turn_id = player2_id

        active_games[game_id] = {
            'instance': new_game,
            'players': players,
            'current_turn_id': first_turn_id,
            'message_ids': {}  # Будуть заповнені після першого надсилання дошки
        }
        player_to_game[player1_id] = game_id
        player_to_game[player2_id] = game_id

        print(f'Розпочато гру {game_id} між {player1_id} та {player2_id}. X={player1_id if players[player1_id]=="X" else player2_id}, O={player1_id if players[player1_id]=="O" else player2_id}. Перший хід: {first_turn_id}.')

        # Надсилаємо дошки обом гравцям, прибираючи Reply клавіатуру
        send_or_update_board(player1_id, game_id)
        send_or_update_board(player2_id, game_id)


# --- Обробники команд ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'

    welcome_message = f"""
Привіт, {user_name}! Я бот "Хрестики-Нулики".
Ти можеш зіграти зі своїм другом прямо тут!

Щоб почати, натисни кнопку "Знайти суперника" нижче або напиши /play.
"""
    bot.send_message(chat_id, welcome_message, reply_markup=create_main_reply_keyboard())


# Обробник команди /play
@bot.message_handler(commands=['play'])
def handle_play_command(message):
    _handle_find_player_action(message.chat.id)

# Обробник натискання кнопки "Знайти суперника"
@bot.message_handler(func=lambda message: message.text == 'Знайти суперника' and message.content_type == 'text')
def handle_find_button(message):
    _handle_find_player_action(message.chat.id)

# Обробник команди stopgame
@bot.message_handler(commands=['stopgame'])
def stop_game_command(message, waiting_player=None):
    chat_id = message.chat.id

    if chat_id in player_to_game:
        game_id = player_to_game[chat_id]
        game_state = active_games.get(game_id)
        if game_state:
             players_in_game = list(game_state['players'].keys())
             partner_id = players_in_game[0] if players_in_game[1] == chat_id else players_in_game[1]

             # Повідомляємо обох гравців
             bot.send_message(chat_id, 'Ви покинули гру.')
             try:
                  bot.send_message(partner_id, 'Ваш суперник покинув гру.')
             except Exception as e:
                  print(f'Помилка повідомлення партнера {partner_id} про вихід: {e}')

             # Завершуємо гру і повертаємо клавіатури
             end_game_for_players(game_id)

        elif chat_id in player_to_game:
            del player_to_game[chat_id]
            bot.send_message(chat_id, 'Гра була неактивна. Ви вийшли зі стану гри.', reply_markup=create_main_reply_keyboard())


    elif waiting_player == chat_id:
        waiting_player = None
        bot.send_message(chat_id, 'Ви покинули чергу пошуку суперника.', reply_markup=create_main_reply_keyboard())
        print(f'Гравець {chat_id} залишив чергу через stopgame.')

    else:
        bot.send_message(chat_id, 'Ви зараз не в грі і не очікуєте на суперника.', reply_markup=create_main_reply_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):    # Метод, який обробляє натискання Inline кнопок.
    chat_id = call.message.chat.id
    callback_data = call.data

    if callback_data == 'game_over':
        bot.answer_callback_query(call.id, 'Ця гра вже завершена!')
        return

    try:
        parts = callback_data.split(':')
        if len(parts) != 3:
            bot.answer_callback_query(call.id, 'Невідомий формат кнопки.')
            return

        game_id = int(parts[0])
        row = int(parts[1])
        col = int(parts[2])

    except (ValueError, IndexError):
        bot.answer_callback_query(call.id, 'Помилка при обробці даних ходу.')
        return

    if game_id not in active_games:
        bot.answer_callback_query(call.id, 'Ця гра вже неактивна або завершена.')
        return

    game_state = active_games[game_id]
    game_instance = game_state['instance']
    current_turn_id = game_state['current_turn_id']
    player_mark = game_state['players'].get(chat_id)  # Отримуємо маркер поточного гравця

    if game_instance.is_game_over(): # Додаткова перевірка, хоча кнопка має бути неактивна
         bot.answer_callback_query(call.id, 'Гра вже завершена!')
         send_or_update_board(chat_id, game_id) # Може, оновити на всяк випадок
         return

    if chat_id != current_turn_id:
        bot.answer_callback_query(call.id, 'Не твій хід!')
        return

    if game_instance.board[row][col] != ' ':
         bot.answer_callback_query(call.id, 'Це поле вже зайняте. Спробуй інше!')
         return

    if game_instance.make_move(row, col, player_mark):

        players_list = list(game_state['players'].keys())
        other_player_id = players_list[0] if players_list[1] == chat_id else players_list[1]

        if game_instance.check_win(player_mark):
            # Перемога!
            bot.answer_callback_query(call.id, 'Перемога!')
            send_or_update_board(chat_id, game_id)  # Оновлюємо дошку для обох
            send_or_update_board(other_player_id, game_id)
            end_game_for_players(game_id) # Завершуємо гру та повертаємо клавіатури

        elif game_instance.check_draw():
            bot.answer_callback_query(call.id, 'Нічия!')
            send_or_update_board(chat_id, game_id)
            send_or_update_board(other_player_id, game_id)
            end_game_for_players(game_id) # Завершуємо гру та повертаємо клавіатури
        else:
            game_state['current_turn_id'] = other_player_id
            send_or_update_board(chat_id, game_id)
            send_or_update_board(other_player_id, game_id)
            bot.answer_callback_query(call.id)
            print(f'Гра {game_id}. Хід {player_mark} на ({row},{col}). Наступний хід: {game_state["players"][other_player_id]} ({other_player_id}).')

    else:
        bot.answer_callback_query(call.id, 'Не вдалося зробити хід. Спробуйте ще раз.')


# --- Обробник інших текстових повідомлень ---
@bot.message_handler(func=lambda message: message.content_type == 'text' and message.text not in ['Знайти суперника', '/play', '/start', '/help', '/stopgame'])
def handle_other_messages(message):
    chat_id = message.chat.id
    if chat_id not in player_to_game and waiting_player != chat_id:
         bot.send_message(chat_id, 'Я бот для гри "Хрестики-Нулики". Натисни кнопку "Знайти суперника", щоб зіграти!', reply_markup=create_main_reply_keyboard())

# --- Запуск бота ---
print('Бот "Хрестики-Нулики" запущено...')
bot.polling(none_stop=True, interval=0, timeout=20)