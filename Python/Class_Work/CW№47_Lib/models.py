from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class Book:
    id: int
    title: str
    author: str
    available: bool

@dataclass
class Rental:
    id: int
    user_id: int
    book_id: int
    rental_date: datetime
    return_date: datetime | None