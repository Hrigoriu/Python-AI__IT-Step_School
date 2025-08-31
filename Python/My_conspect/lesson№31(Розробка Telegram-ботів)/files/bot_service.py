# bot_service.py
import random as rd
import string
import json
import os # Імпортуємо модуль os для роботи зі шляхами

class Service:
    def __init__(self):
        # {chat_id: {'topic': 'Назва вікторини', 'questions': [{}, ...], 'current': 0, 'score': 0}}
        self.user_quiz = {}

        # Виправляємо шлях до файлу, використовуючи os.path.join
        # Припускаємо, що quiz_data.json знаходиться в тій же папці, що й bot_service.py або головний скрипт
        base_dir = os.path.dirname(__file__) # Шлях до папки, де знаходиться bot_service.py
        quiz_file_path = os.path.join(base_dir, 'quiz_data.json') # Використовуємо коректний слеш

        try:
            with open(quiz_file_path, 'r', encoding='UTF-8') as json_file:
                self.quiz_data = json.load(json_file)
            print(f"Successfully loaded quiz data from {quiz_file_path}")
        except FileNotFoundError:
            print(f"Error: quiz_data.json not found at {quiz_file_path}")
            self.quiz_data = {} # Завантажуємо порожній словник, щоб бот міг запуститися
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {quiz_file_path}. Check file format.")
            self.quiz_data = {}

    def get_titles(self, chat_id: int) -> list[str] | None:
        """
        Повертає список назв вікторин, якщо користувач не проходить активну вікторину.
        """
        # Виправляємо логіку: повертаємо теми, якщо користувач НЕ в активній вікторині
        if chat_id in self.user_quiz:
            return None # Користувач вже проходить вікторину

        return list(self.quiz_data.keys())

    def start_quiz(self, chat_id: int, quiz_name: str) -> bool:
        """
        Починає нову вікторину для користувача.

        Returns:
            True, якщо вікторина розпочата успішно, False - якщо вже проходить або тема не знайдена.
        """
        if chat_id in self.user_quiz:
            return False # Користувач вже проходить вікторину

        if quiz_name not in self.quiz_data:
             return False # Тема вікторини не знайдена

        # Правильно зберігаємо список питань вікторини
        questions = self.quiz_data[quiz_name]
        if not questions: # Якщо вікторина порожня
             return False

        new_quiz_state = {
            'topic': quiz_name,
            'questions': questions, # Зберігаємо список питань
            'current': 0,
            'score': 0
        }
        self.user_quiz[chat_id] = new_quiz_state
        print(f"Quiz '{quiz_name}' started for user {chat_id}")
        return True

    def send_question(self, chat_id: int) -> dict | None:
        """
        Повертає дані поточного питання для користувача або None, якщо питання закінчились.
        """
        if chat_id not in self.user_quiz:
            return None # Користувач не проходить вікторину

        user_quiz_state = self.user_quiz[chat_id]
        current_index = user_quiz_state['current']
        questions_list = user_quiz_state['questions'] # Отримуємо список питань

        if current_index >= len(questions_list):
            # Питання закінчились
            return None

        # Правильно звертаємось до питання зі списку
        return questions_list[current_index]

    def check_answer(self, chat_id: int, user_answer_index: int) -> bool | None:
        """
        Перевіряє відповідь користувача.

        Args:
            chat_id: ID користувача.
            user_answer_index: Індекс відповіді, яку вибрав користувач (від 0).

        Returns:
            True, якщо відповідь правильна, False - якщо неправильна.
            None, якщо користувач не в вікторині або індекс відповіді невірний.
        """
        if chat_id not in self.user_quiz:
            return None # Користувач не проходить вікторину

        user_quiz_state = self.user_quiz[chat_id]
        current_index = user_quiz_state['current']
        questions_list = user_quiz_state['questions'] # Отримуємо список питань

        if current_index >= len(questions_list):
            return None # Питання вже закінчились

        current_question_data = questions_list[current_index]
        correct_answer_text = current_question_data['answer']
        options = current_question_data['options']

        # Перевіряємо, чи індекс відповіді коректний
        if not (0 <= user_answer_index < len(options)):
            print(f"User {chat_id}: Invalid answer index {user_answer_index}")
            # В цьому випадку просто переходимо до наступного питання, не додаючи бали
            user_quiz_state['current'] += 1
            return False # Вважаємо невірною відповіддю

        # Отримуємо текст відповіді, яку вибрав користувач
        user_answer_text = options[user_answer_index]

        # Правильно порівнюємо текст вибраної відповіді з текстом правильної відповіді
        is_correct = (user_answer_text == correct_answer_text)

        # Збільшуємо лічильник поточного питання
        user_quiz_state['current'] += 1

        if is_correct:
            user_quiz_state['score'] += 1
            print(f"User {chat_id}: Answer {user_answer_text} is CORRECT.")
            return True
        else:
            print(f"User {chat_id}: Answer {user_answer_text} is WRONG. Correct was {correct_answer_text}.")
            return False

    def end_quiz(self, chat_id: int) -> str | None:
        """
        Завершує вікторину для користувача та повертає результат у форматі 'score/total'.
        """
        if chat_id not in self.user_quiz:
            return None # Користувач не проходив вікторину

        user_quiz_state = self.user_quiz[chat_id]
        user_score = user_quiz_state['score']
        total_questions = len(user_quiz_state['questions']) # Правильно отримуємо загальну кількість питань

        # Правильно формуємо рядок результату
        result_string = f'{user_score}/{total_questions}'

        # Видаляємо стан вікторини для цього користувача
        del self.user_quiz[chat_id]
        print(f"Quiz ended for user {chat_id}. Result: {result_string}")

        # Повертаємо рядок результату
        return result_string

    @staticmethod
    def generate_password(message_len_str: str) -> str | None:
        """
        Генерує випадковий пароль заданої довжини.
        """
        message_len_str = message_len_str.strip()
        if not message_len_str.isdigit():
            return None # Повертаємо None, якщо не число

        message_len = int(message_len_str)
        if message_len not in range(8, 36): # Перевірка діапазону
            return None # Повертаємо None, якщо довжина поза діапазоном

        # Генеруємо пароль
        characters = string.ascii_letters + string.digits + string.punctuation # Додаємо пунктуацію для надійності
        return ''.join(rd.choice(characters) for _ in range(message_len))