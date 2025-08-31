import telebot  # Імпортуємо pyTelegramBotAPI
from telebot import types
from tictactoe_game_01 import TicTacToeGame  # Імпортуємо наш клас гри

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

def create_board_markup(game_id: int, board: list[list[str]]) -> types.InlineKeyboardMarkup:    #Метод для створення Inline клавіатуру, що представляє дошку.
    markup = types.InlineKeyboardMarkup()
    for r_idx, row in enumerate(board):
        buttons = []
        for c_idx, cell in enumerate(row):
            # Використовуємо вміст клітинки або пробіл, якщо порожньо
            button_text = cell if cell != ' ' else '⋅'      # Використовуємо '⋅' для візуалізації порожніх клітинок
            callback_data = f"{game_id}:{r_idx}:{c_idx}"    # callback_data включає game_id, рядок та стовпець
            buttons.append(types.InlineKeyboardButton(text=button_text, callback_data=callback_data))
        markup.add(*buttons)  # Додаємо кнопки рядком
    return markup


def send_or_update_board(chat_id: int, game_id: int):   #Метод, який надсилає або оновлює повідомлення з дошки до гравця.
    game_state = active_games[game_id]
    game_instance = game_state['instance']
    board = game_instance.get_board()
    message_id = game_state['message_ids'].get(chat_id)
    current_turn_id = game_state['current_turn_id']
    player_x_id = list(game_state['players'].keys())[0]  # Отримуємо id гравця X
    player_o_id = list(game_state['players'].keys())[1]  # Отримуємо id гравця O

    # Визначаємо нікнейми гравців (або просто X/O)
    player_x_name = bot.get_chat(player_x_id).first_name if player_x_id else 'Гравець X'
    player_o_name = bot.get_chat(player_o_id).first_name if player_o_id else 'Гравець O'

    text = f'Гра #{game_id}\n'
    text += f' "{game_state["players"][player_x_id]}": {player_x_name}\n'
    text += f' "{game_state["players"][player_o_id]}": {player_o_name}\n\n'

    if game_instance.is_game_over():
        winner_mark = None
        for mark in ['X', 'O']:
            if game_instance.check_win(mark):
                winner_mark = mark
                break

        if winner_mark:
            winner_name = player_x_name if game_state['players'][player_x_id] == winner_mark else player_o_name
            text += f'✨ Гра закінчена! Переміг гравець "{winner_mark}" ({winner_name})! ✨'
        elif game_instance.check_draw():
            text += '🤝 Гра закінчена! Нічия! 🤝'
        else:
            text += '❗ Гра закінчена. Невідомий результат.'

        # Після завершення гри кнопки робимо неактивними
        markup = create_board_markup(game_id, board)
        for row_buttons in markup.keyboard:
            for button in row_buttons:
                button.callback_data = 'game_over'

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
                reply_markup=markup
            )
        else:
            msg = bot.send_message(
                chat_id=chat_id,
                text=text,
                reply_markup=markup
            )
            game_state['message_ids'][chat_id] = msg.message_id
    except telebot.apihelper.ApiTelegramException as e:
        print(f'Помилка при надсиланні/редагуванні дошки для {chat_id}: {e}')


# --- Обробники команд ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):  # Метод, який відправляє команди /start та /help
    chat_id = message.chat.id
    user_name = message.from_user.first_name if message.from_user else 'Користувач'

    welcome_message = f"""
Привіт, {user_name}! Я бот "Хрестики-Нулики".
Ти можеш зіграти зі своїм другом прямо тут!

Використовуй команду /play, щоб знайти суперника і розпочати нову гру.
"""
    bot.send_message(chat_id, welcome_message)


@bot.message_handler(commands=['play'])
def find_player(message):   # Метод, який шукає пару та ставить у чергу
    chat_id = message.chat.id

    if chat_id in player_to_game:
        bot.send_message(chat_id, 'Ти вже береш участь у грі! 😉')
        return

    global waiting_player
    if waiting_player is None:
        waiting_player = chat_id
        bot.send_message(chat_id, 'Шукаємо суперника... Зачекай іншого гравця або попроси друга написати /play.')
        print(f'Гравець {chat_id} став у чергу.')
    else:
        player1_id = waiting_player
        player2_id = chat_id

        if player1_id == player2_id:
            bot.send_message(chat_id, 'Ти вже в черзі.')
            return
        waiting_player = None

        new_game = TicTacToeGame()
        game_id = player1_id

        import random   # Випадково визначаємо, хто буде X, а хто O
        if random.choice([True, False]):
            players = {player1_id: 'X', player2_id: 'O'}
            first_turn_id = player1_id
        else:
            players = {player1_id: 'O', player2_id: 'X'}
            first_turn_id = player2_id

        active_games[game_id] = {
            'instance': new_game,
            'players': players,
            'current_turn_id': first_turn_id,
            'message_ids': {}  # Будуть заповнені після першого надсилання дошки
        }
        player_to_game[player1_id] = game_id
        player_to_game[player2_id] = game_id

        print(f'Розпочато гру {game_id} між {player1_id} та {player2_id}.')

        send_or_update_board(player1_id, game_id)
        send_or_update_board(player2_id, game_id)

        bot.send_message(player1_id, f'Знайдено суперника! Ти граєш "{players[player1_id]}".')
        bot.send_message(player2_id, f'Знайдено суперника! Ти граєш "{players[player2_id]}".')


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

    if game_id not in active_games:     # Перевіряємо, чи існує ця гра
        bot.answer_callback_query(call.id, 'Ця гра вже неактивна.')
        return

    game_state = active_games[game_id]
    game_instance = game_state['instance']
    current_turn_id = game_state['current_turn_id']
    player_mark = game_state['players'].get(chat_id)  # Отримуємо маркер поточного гравця


    if chat_id != current_turn_id:      # Перевіряємо, чи це хід гравця, який натиснув кнопку
        bot.answer_callback_query(call.id, 'Не твій хід!')
        return

    if game_instance.make_move(row, col, player_mark):

        players_list = list(game_state['players'].keys())
        other_player_id = players_list[0] if players_list[1] == chat_id else players_list[1]


        if game_instance.check_win(player_mark):    # Перевіряємо, чи гра закінчена
            send_or_update_board(chat_id, game_id)  # Оновлюємо дошку для переможця
            send_or_update_board(other_player_id, game_id)  # Оновлюємо дошку для програвшого
            bot.answer_callback_query(call.id, 'Перемога!')
            # Прибираємо гру зі стану
            del active_games[game_id]
            del player_to_game[chat_id]
            del player_to_game[other_player_id]
            print(f'Гра {game_id} завершена. Переміг {chat_id}.')

        elif game_instance.check_draw():
            # Нічия!
            send_or_update_board(chat_id, game_id)
            send_or_update_board(other_player_id, game_id)
            bot.answer_callback_query(call.id, 'Нічия!')
            # Прибираємо гру зі стану
            del active_games[game_id]
            del player_to_game[chat_id]
            del player_to_game[other_player_id]
            print(f'Гра {game_id} завершена. Нічия.')
        else:
            # Гра триває, передаємо хід іншому гравцю
            game_state['current_turn_id'] = other_player_id
            send_or_update_board(chat_id, game_id)  # Оновлюємо дошку для поточного гравця
            send_or_update_board(other_player_id, game_id)  # Оновлюємо дошку для іншого гравця
            bot.answer_callback_query(call.id)  # Підтверджуємо натискання (без повідомлення)
            print(
                f'Гра {game_id}. Хід {player_mark} на ({row},{col}). Наступний хід {game_state["players"][other_player_id]}.')

    else:   # Хід не успішний (поле зайняте)
        bot.answer_callback_query(call.id, 'Це поле вже зайняте. Спробуй інше!')


# --- Обробник інших текстових повідомлень (ігноруємо) ---
# Можна додати, якщо хочете ігнорувати будь-який текст, що не є командою
@bot.message_handler(func=lambda message: True)
def handle_other_messages(message): # Метод, щоб ігнорувати будь-який текст, що не є командою
    chat_id = message.chat.id
    if chat_id not in player_to_game and waiting_player != chat_id:
         bot.send_message(chat_id, 'Я бот для гри "Хрестики-Нулики". Напиши /play, щоб зіграти!')


# --- Запуск бота ---
print('Бот Хрестики-Нулики запущено...')
# Запускаємо цикл опитування Telegram API
bot.polling(none_stop=True)