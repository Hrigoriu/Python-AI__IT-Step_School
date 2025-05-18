import os
from typing import Any

# --- Конфігурація та константи ---

# Ім'я файлу для зберігання даних
# Створюємо папку 'files', якщо не має
DATA_DIR = 'files'
DATABASE_FILE = os.path.join(DATA_DIR, 'salary_data.json')

# Список допустимих місяців українською
MONTHS: list[str | Any] = [
    "Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
    "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"
]

# Допустимі рівні працівників
EMPLOYEE_LEVELS = ["Junior", "Middle", "Senior", "Team Lead"]
