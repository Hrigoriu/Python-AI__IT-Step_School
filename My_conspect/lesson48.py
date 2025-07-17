
#query = 'SELECT * FROM students'

#
"""
workers:
is, name, salary
1   Bob   1000
2   Olga  2500
3   Anton 3500
"""
#=========================================================================================
'''
import sqlalchemy
from sqlalchemy import text

engine = sqlalchemy.create_engine('sqlite:///files/db.cl3')

with engine.connect() as connection:
    # створюємо таблицю humans, якщо вона не існує
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS humans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """))
    # створюємо таблицю dogs
    connection.execute(text('CREATE TABLE dogs (name, TEXT, age INT)'))
    connection.execute(text("INSERT INTO humans (name, age) VALUES (:name, :age);"),
                       {'name':'John', 'age': 41}
                       )
    #connection.execute(text("INSERT INTO humans VALUES ('Anna', 29);"))
    connection.commit()

    result = connection.execute(text('SELECT * FROM humans'))
    print(result.fetchall())
'''
#=========================================================================================
from sqlalchemy import create_engine, Column, Integer, String, text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column
import datetime


engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/alchemy')
                       #postgresql+psycopg2://логін:пароль@localhost/назва_БД

Base = declarative_base()   # базовий клас для ОРМ моделей
Session = sessionmaker(engine)

class Worker(Base):
    __tablename__ = 'workers'
    #id = Column(Integer, primary_key=True, autoincrement=True) # перший метод (Застарілий)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # другий спосіб
    name: Mapped[str] = mapped_column()
    salary: Mapped[int] = mapped_column()

    def __str__(self):
        return f'Worker {self.id}: {self.name}, {self.salary} $'

    def is_rich(self):
        return self.salary > 20_000

    def say_hello(self) -> str:
        return f'Hello, my name is {self.name}!'

class WorkerResume(Base):
    __tablename__ = 'resume'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime.date] = mapped_column(default=datetime.date.today)
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id'))

    def info(self) ->str:
        pass

Base.metadata.create_all(engine) #створення таблиць на основі моделей

# with Session() as session:
#     #session.add(Worker(name='Petro', salary=10_000))
#     #session.add(Worker(name='Olga', salary=15_000))
#     #session.add(Worker(name='Anton', salary=5_000))
#     #session.add(Worker(name='Sergiy', salary=3_000))
#     #session.add(Worker(name='Oleh', salary=0))
#     #session.commit()

#     result = session.query(Worker).all()    #SELECT * FROM workers
#     #for el in result:
#         #print(el)
#
#     for worker in all_workers:
#         print(worker.say_hello())
#         print(worker.is_rich())

with Session() as session:
    session.add(WorkerResume(title='Моє перше резюме', worker_id=2))
    session.commit()

    all_resume = session.query(WorkerResume).all()
    for res in all_resume:
        print(res.title)
        print(res.create_date)







