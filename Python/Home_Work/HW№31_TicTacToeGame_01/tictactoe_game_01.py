class TicTacToeGame:
    def __init__(self):         #Ініціалізація нової гри: порожня дошка.
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self._is_game_over = False

    def make_move(self, row: int, col: int, player_mark: str) -> bool:  #Метод, який робить хід на дошці.
        """
        Args:
            row: Рядок (0, 1, 2).
            col: Стовпець (0, 1, 2).
            player_mark: Маркер гравця ('X' або 'O').

        Returns:
            True, якщо хід зроблено успішно, False, якщо поле зайняте або координати невірні.
        """
        if not (0 <= row < 3 and 0 <= col < 3):
            return False # Невірні координати

        if self.board[row][col] == ' ':
            self.board[row][col] = player_mark
            return True # Хід успішний
        else:
            return False # Поле зайняте

    def check_win(self, player_mark: str) -> bool:  # Метод, який перевіряє, чи виграв гравець

        # Перевірка рядків
        for row in self.board:
            if all(cell == player_mark for cell in row):
                self._is_game_over = True
                return True

        # Перевірка стовпців
        for col in range(3):
            if all(self.board[row][col] == player_mark for row in range(3)):
                self._is_game_over = True
                return True

        # Перевірка діагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player_mark:
            self._is_game_over = True
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player_mark:
            self._is_game_over = True
            return True

        return False # Немає перемоги для цього гравця

    def check_draw(self) -> bool:   #Метод, який перевіряє, чи є нічия.

        if not self._is_game_over and all(cell != ' ' for row in self.board for cell in row):
            self._is_game_over = True
            return True
        return False

    def is_game_over(self) -> bool: #Метод, якщо гра закінчена (перемога або нічия).
        return self._is_game_over

    def get_board(self) -> list[list[str]]: #Метод, який вертає стан дошки.
        return self.board