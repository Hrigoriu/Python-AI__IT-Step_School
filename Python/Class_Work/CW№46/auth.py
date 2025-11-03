import sqlite3

class AuthManager:
    def __init__(self, db_name='company.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def register_user(self, login, password, recovery_code):
        try:
            self.cursor.execute(
                'INSERT INTO users (login, password, recovery_code) VALUES (?, ?, ?)',
                (login, password, recovery_code)
            )
            self.connection.commit()
        except sqlite3.IntegrityError:
            print('Користувач із таким логіном вже існує.')

    def login_user(self, login, password):
        self.cursor.execute(
            'SELECT * FROM users WHERE login=? AND password=?',
            (login, password)
        )
        return self.cursor.fetchone() is not None

    def reset_password(self, login, recovery_code, new_password):
        self.cursor.execute(
            'SELECT * FROM users WHERE login=? AND recovery_code=?',
            (login, recovery_code)
        )
        if self.cursor.fetchone():
            self.cursor.execute(
                'UPDATE users SET password=? WHERE login=?',
                (new_password, login)
            )
            self.connection.commit()
            print('Пароль змінено.')
        else:
            print('Невірний код відновлення.')

    def close(self):
        self.connection.close()
