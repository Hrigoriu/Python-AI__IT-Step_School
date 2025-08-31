from typing import Dict, Optional

class ChatManager:  #Клас, що керує станом анонімних чатів між користувачами.
    def __init__(self):
        self.waiting_user: Optional[int] = None
        self.active_chats: Dict[int, int] = {}  # Словник активних чатів. Key: chat_id одного гравця, Item: chat_id його партнера.

    def find_partner(self, user_chat_id: int) -> str:   # Метод, який шукає партнера для користувача або ставить його в чергу.
        if user_chat_id in self.active_chats:   # Перевіряємо, чи користувач вже в активному чаті
            return 'В активному чаті:'
        if self.waiting_user == user_chat_id:   # Перевіряємо, чи користувач вже очікує
            return 'уже очікує'
        if self.waiting_user is None:   # Перевіряємо, чи є хтось в черзі
            self.waiting_user = user_chat_id
            print(f'Користувач {user_chat_id} зараз очікує.')
            return 'Очікує'
        else:
            partner_chat_id = self.waiting_user # Знайшли партнера!
            self.waiting_user = None # Прибираємо з черги
            self.active_chats[user_chat_id] = partner_chat_id
            self.active_chats[partner_chat_id] = user_chat_id
            print(f'Користувачі {user_chat_id} та {partner_chat_id} утворили пару.')
            return 'в парі!'

    def get_partner(self, user_chat_id: int) -> Optional[int]:  # Метод, який повертає chat_id партнера користувача в активному чаті.
        return self.active_chats.get(user_chat_id)

    def end_chat(self, user_chat_id: int) -> Optional[int]: # Метод, який завершує активний чат користувача або прибирає його з черги.
        if user_chat_id in self.active_chats:   # Перевіряємо, чи користувач в активному чаті
            partner_chat_id = self.active_chats.pop(user_chat_id)
            self.active_chats.pop(partner_chat_id, None)
            print(f'Чат між {user_chat_id} та {partner_chat_id} закінчено.')
            return partner_chat_id

        if self.waiting_user == user_chat_id:   # Перевіряємо, чи користувач очікує
            self.waiting_user = None
            print(f'Користувач {user_chat_id} залишив чергу.')
            return None

        return None