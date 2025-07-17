from sqlalchemy import create_engine, Column, Integer, String, text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column

import datetime


engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/alchemy')

Base = declarative_base()  # базовий клас для ОРМ моделей
Session = sessionmaker(engine)


class Worker(Base):
    __tablename__ = 'workers'

    # id = Column(Integer, primary_key=True, autoincrement=True)  # застарілий перший спосіб

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # другий спосіб
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

    def info(self) -> str:
        pass


Base.metadata.create_all(engine)  # створення таблиць на основі моделей


# with Session() as session:
#     # session.add(Worker(name='Petro', salary=10_000))
#     # session.add(Worker(name='Olga', salary=15_000))
#     # session.add(Worker(name='Anton', salary=5_000))
#     # session.add(Worker(name='Sergiy', salary=3_000))
#     # session.add(Worker(name='Oleh', salary=0))
#     #
#     # session.commit()
#
#     all_workers = session.query(Worker).all()  # SELECT * FROM workers
#
#     for worker in all_workers:
#         print(worker.say_hello())
#         print(worker.is_rich())


with Session() as session:
    # session.add(WorkerResume(title='Моє друге резюме', worker_id=2))
    # session.commit()

    all_resume = session.query(WorkerResume).all()

    for res in all_resume:
        print(res.title)
        print(res.create_date)
