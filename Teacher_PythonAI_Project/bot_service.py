import random as rd
import string
import json


class Service:
    def __init__(self):
        self.user_quiz = {}  # {id: {'topic', 'current', 'score', 'start_time'}}

        with open('files\\quiz.json', 'r', encoding='UTF-8') as json_file:
            self.quiz_data = json.load(json_file)

    def get_titles(self, chat_id):
        if chat_id in self.user_quiz:
            return

        return self.quiz_data.keys()

    def start_quiz(self, chat_id, quiz_name):
        if chat_id in self.user_quiz:  # якщо користувач вже ПРОХОДИТЬ вікторину
            return

        quiz = self.quiz_data[quiz_name]

        new_dict = {'quiz': quiz, 'current': 0, 'score': 0}
        self.user_quiz[chat_id] = new_dict

    def send_question(self, chat_id):
        if chat_id not in self.user_quiz:
            return

        user_quiz_dict = self.user_quiz[chat_id]
        current_index = user_quiz_dict['current']

        if current_index >= len(user_quiz_dict['quiz']):
            return

        return user_quiz_dict['quiz'][current_index]

    def check_answer(self, chat_id, answer_index: int):
        if chat_id not in self.user_quiz:
            return

        user_quiz_dict = self.user_quiz[chat_id]
        current_index = user_quiz_dict['current']

        answer = user_quiz_dict['quiz'][current_index]['options'][answer_index]
        current_answer = user_quiz_dict['quiz'][current_index]['answer']

        user_quiz_dict['current'] += 1

        if answer == current_answer:
            user_quiz_dict['score'] += 1
            return True
        else:
            return False

    def end_quiz(self, chat_id):
        if chat_id not in self.user_quiz:
            return

        user_quiz_dict = self.user_quiz[chat_id]
        user_score = user_quiz_dict['score']

        result = f'{user_score}/{len(user_quiz_dict['quiz'])}'
        del self.user_quiz[chat_id]

        return result

    @staticmethod
    def generate_password(message_len: str):
        message_len = message_len.strip()
        if not message_len.isdigit():
            return

        message_len = int(message_len)
        if message_len not in range(8, 36):
            return

        return ''.join(rd.choice(string.ascii_letters + string.digits) for _ in range(message_len))
