import random

class GuessGame:
    def __init__(self, min_number: int = 1, max_number: int = 100):
        if min_number >= max_number:
            raise ValueError('Мінімальне число має бути меншим за максимальне')

        self.min_number: int = min_number
        self.max_number: int = max_number
        self.secret_number: int = random.randint(min_number, max_number)
        self.attempts: int = 0

    def make_guess(self, guess: int) -> str:    # Метод для вгадування числа.
        self.attempts += 1

        if guess == self.secret_number:
            return 'correct'
        elif guess < self.secret_number:
            return 'low'
        else:
            return 'high'

    def get_attempts(self) -> int:  # Метод підрахунку кількості спроб.
        return self.attempts

    def get_range(self) -> tuple[int, int]: #   Метод для формування чисел для гри.
        return self.min_number, self.max_number