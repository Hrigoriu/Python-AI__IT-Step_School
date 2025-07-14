import sqlite3

class WorkerManager:
    def __init__(self, db_name='company.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def add_worker(self, name, age, salary, position):
        self.cursor.execute(
            'INSERT INTO workers (name, age, salary, position) VALUES (?, ?, ?, ?)',
            (name, age, salary, position)
        )
        self.connection.commit()

    def delete_worker(self, worker_id):
        self.cursor.execute('DELETE FROM workers WHERE id=?', (worker_id,))
        self.connection.commit()

    def get_all_workers(self):
        self.cursor.execute('SELECT * FROM workers')
        return self.cursor.fetchall()

    def find_worker_by_name(self, name):
        self.cursor.execute('SELECT * FROM workers WHERE name LIKE ?', ('%' + name + '%',))
        return self.cursor.fetchall()

    def get_workers_sorted_by_salary(self, descending=True):
        order = 'DESC' if descending else 'ASC'
        self.cursor.execute(f'SELECT * FROM workers ORDER BY salary {order}')
        return self.cursor.fetchall()

    def update_worker_position(self, worker_id, new_position):
        self.cursor.execute(
            'UPDATE workers SET position=? WHERE id=?',
            (new_position, worker_id)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()
