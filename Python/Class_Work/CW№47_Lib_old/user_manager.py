from db import DB

class UserManager:
    def __init__(self, db: DB):
        self.db = db

    def add_user(self, name, email):
        query = 'INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;'
        return self.db.execute(query, (name, email), fetchone=True)[0]

    def get_user(self, user_id):
        query = 'SELECT * FROM users WHERE id = %s;'
        return self.db.execute(query, (user_id,), fetchone=True)