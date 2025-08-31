import sqlite3

class HumanManager:  # клас для роботи з БД
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def _create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS humans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER)    
        ''')

    def add_human(self, name: str, age: int):
        self.cursor.execute('INSERT INTO humans (name, age) VALUES (?, ?)', (name, age))
        self.connection.commit()

    def get_all_humans(self):
        self.cursor.execute('SELECT * FROM humans')
        return self.cursor.fetchall()

    def find_human_by_name(self, name: str):
        #pass    # задача: знайти та повернути всіх людей з бази, у яких співпадає ім'я з name
        self.cursor.execute('''
            SELECT * FROM humans 
            WHERE name = ?''', (name,))
        return self.cursor.fetchall()
manager = HumanManager('files\\db.sl3')

# manager.add_human('Sergiu', 10)
# manager.add_human('Petro', 20)
# manager.add_human('Roman', 40)


print(manager.get_all_humans())
print(manager.find_human_by_name('Roman'))