from datetime import datetime
from constants import EMPLOYEE_LEVELS # Імпортуємо константи
from utils import validate_month_format # Імпортуємо утиліту

# --- Класи даних ---

class SalarySettings:
    """
    Клас для зберігання глобальних налаштувань розрахунку зарплати.
    """
    def __init__(self, base_amounts=None, coefficients=None, task_costs=None, standard_monthly_hours=164.0, default_rates=None):
        # Базові ставки зарплати (фіксована частина) для кожного рівня
        # Якщо не передано, встановлюємо значення за замовчуванням
        self.base_amounts = base_amounts if base_amounts is not None else {
            "Junior": 10000.0,
            "Middle": 20000.0,
            "Senior": 35000.0,
            "Team Lead": 50000.0
        }
        # Коефіцієнти для кожного рівня (впливають як на базову, так і на додаткову частину)
        self.coefficients = coefficients if coefficients is not None else {
            "Junior": 1.0,
            "Middle": 1.5,
            "Senior": 2.0,
            "Team Lead": 2.5
        }
        # Вартість різних типів завдань (приклад)
        self.task_costs = task_costs if task_costs is not None else {
            "Simple": 1000.0,
            "Medium": 2000.0,
            "Complex": 3000.0
        }
        # Стандартна кількість робочих годин на місяць (для розрахунку вартості години з базової ставки)
        self.standard_monthly_hours = standard_monthly_hours if standard_monthly_hours > 0 else 164.0 # Забезпечуємо float і > 0
        # Курси валют за замовчуванням (на випадок, якщо немає жодного запису)
        self.default_rates = default_rates if default_rates is not None else {
            "USD": 40.00,
            "EUR": 43.00
        }

        # Перевірка, що для всіх допустимих рівнів є ставки та коефіцієнти
        # Якщо відсутні, додаємо з дефолтними нульовими значеннями, але краще попередити
        for level in EMPLOYEE_LEVELS:
            if level not in self.base_amounts:
                 #print(f"Попередження: Для рівня '{level}' не встановлено базову ставку. Використовується 0.")
                 self.base_amounts[level] = 0.0
            if level not in self.coefficients:
                 #print(f"Попередження: Для рівня '{level}' не встановлено коефіцієнт. Використовується 1.0.")
                 self.coefficients[level] = 1.0

        # Переконуємося, що стандартні години є float
        self.standard_monthly_hours = float(self.standard_monthly_hours)

        # Переконуємося, що ставки та вартість завдань є float
        for level in self.base_amounts:
             self.base_amounts[level] = float(self.base_amounts[level])
        for level in self.coefficients:
             self.coefficients[level] = float(self.coefficients[level])
        for task in self.task_costs:
             self.task_costs[task] = float(self.task_costs[task])
        for currency in self.default_rates:
            self.default_rates[currency] = float(self.default_rates[currency])


    def to_dict(self):
        """Перетворює об'єкт на словник для збереження у JSON."""
        return {
            "base_amounts": self.base_amounts,
            "coefficients": self.coefficients,
            "task_costs": self.task_costs,
            "standard_monthly_hours": self.standard_monthly_hours,
            "default_rates": self.default_rates
        }

    @classmethod
    def from_dict(cls, data):
        """Створює об'єкт зі словника, завантаженого з JSON."""
        # Використовуємо .get() з дефолтними значеннями для сумісності зі старими форматами файлів
        # Переконуємося, що числові значення конвертуються у float
        base_amounts = {k: float(v) for k, v in data.get("base_amounts", {}).items()}
        coefficients = {k: float(v) for k, v in data.get("coefficients", {}).items()}
        task_costs = {k: float(v) for k, v in data.get("task_costs", {}).items()}
        standard_monthly_hours = float(data.get("standard_monthly_hours", 164.0))
        default_rates = {k: float(v) for k, v in data.get("default_rates", {"USD": 40.0, "EUR": 43.0}).items()}

        return cls(
            base_amounts=base_amounts,
            coefficients=coefficients,
            task_costs=task_costs,
            standard_monthly_hours=standard_monthly_hours,
            default_rates=default_rates
        )

    # Методи оновлення тепер можуть повертати повідомлення про статус
    def update_base_amount(self, level, amount):
        """Оновлює базову ставку для певного рівня."""
        if level in EMPLOYEE_LEVELS:
            try:
                amount = float(amount)
                if amount < 0:
                     return f"Помилка: Базова ставка не може бути від'ємною ({amount})."
                self.base_amounts[level] = amount
                return f"Базова ставка для рівня '{level}' оновлена до {amount:.2f} грн."
            except ValueError:
                 return "Помилка: Введіть коректне числове значення для базової ставки."
        else:
            return f"Помилка: Невідомий рівень працівника: '{level}'. Допустимі: {', '.join(EMPLOYEE_LEVELS)}."

    def update_coefficient(self, level, coefficient):
        """Оновлює коефіцієнт для певного рівня."""
        if level in EMPLOYEE_LEVELS:
            try:
                coefficient = float(coefficient)
                if coefficient < 0:
                    return f"Помилка: Коефіцієнт не може бути від'ємним ({coefficient})."
                self.coefficients[level] = coefficient
                return f"Коефіцієнт для рівня '{level}' оновлено до {coefficient:.2f}."
            except ValueError:
                 return "Помилка: Введіть коректне числове значення для коефіцієнта."
        else:
            return f"Помилка: Невідомий рівень працівника: '{level}'. Допустимі: {', '.join(EMPLOYEE_LEVELS)}."

    def update_task_cost(self, task_type, cost):
        """Оновлює або додає вартість типу завдання."""
        if not task_type:
             return "Помилка: Назва типу завдання не може бути порожньою."
        try:
            cost = float(cost)
            if cost < 0:
                 return f"Помилка: Вартість завдання не може бути від'ємною ({cost})."
            self.task_costs[task_type.strip()] = cost # Прибираємо пробіли на кінцях
            return f"Вартість завдання '{task_type.strip()}' оновлена/додана: {cost:.2f} грн."
        except ValueError:
            return "Помилка: Введіть коректне числове значення для вартості завдання."


    def delete_task_cost(self, task_type):
        """Видаляє вартість типу завдання."""
        task_type_stripped = task_type.strip()
        if task_type_stripped in self.task_costs:
            del self.task_costs[task_type_stripped]
            return f"Вартість завдання '{task_type_stripped}' видалено."
        else:
            return f"Помилка: Тип завдання '{task_type_stripped}' не знайдено."

    def update_standard_hours(self, hours):
        """Оновлює стандартну кількість робочих годин на місяць."""
        try:
            hours = float(hours)
            if hours <= 0:
                return "Помилка: Стандартна кількість годин має бути більше нуля."
            self.standard_monthly_hours = hours
            return f"Стандартна кількість робочих годин на місяць оновлена до {hours:.2f}."
        except ValueError:
            return "Помилка: Введіть коректне числове значення для годин."


    def update_default_rates(self, usd_rate, eur_rate):
        """Оновлює курси валют за замовчуванням."""
        try:
            usd = float(usd_rate)
            eur = float(eur_rate)
            if usd <= 0 or eur <= 0:
                return "Помилка: Курси валют мають бути більше нуля."
            self.default_rates["USD"] = usd
            self.default_rates["EUR"] = eur
            return f"Курси валют за замовчуванням оновлено: 1 USD = {usd:.2f} грн, 1 EUR = {eur:.2f} грн."
        except ValueError:
             return "Помилка: Введіть коректні числові значення для курсів валют."


class MonthlySalaryRecord:
    """
    Клас для зберігання даних про зарплату конкретного працівника за конкретний місяць.
    """
    def __init__(self, record_id, employee_name, month_year, level, actual_hours, tasks_completed_value, usd_rate, eur_rate, calculated_salary_uah=None, date_added=None, history=None):
        if not isinstance(record_id, int) or record_id <= 0:
             raise ValueError("ID запису має бути додатнім цілим числом.")
        if not employee_name or not isinstance(employee_name, str):
             raise ValueError("Ім'я працівника не може бути порожнім.")

        # Перевіряємо формат місяця при створенні
        is_valid, result = validate_month_format(month_year)
        if not is_valid:
             raise ValueError(f"Невірний формат місяця: {month_year}. {result}")

        if level not in EMPLOYEE_LEVELS:
             raise ValueError(f"Невірний рівень працівника: '{level}'. Допустимі: {', '.join(EMPLOYEE_LEVELS)}.")

        try:
            actual_hours = float(actual_hours)
            if actual_hours < 0:
                 raise ValueError("Відпрацьовані години не можуть бути від'ємними.")
        except (ValueError, TypeError):
            raise ValueError("Відпрацьовані години мають бути числом.")

        try:
            tasks_completed_value = float(tasks_completed_value)
            if tasks_completed_value < 0:
                 raise ValueError("Вартість виконаних завдань не може бути від'ємною.")
        except (ValueError, TypeError):
            raise ValueError("Вартість виконаних завдань має бути числом.")

        try:
            usd_rate = float(usd_rate)
            if usd_rate <= 0:
                 raise ValueError("Курс долара має бути додатнім числом.")
        except (ValueError, TypeError):
             raise ValueError("Курс долара має бути числом.")

        try:
            eur_rate = float(eur_rate)
            if eur_rate <= 0:
                 raise ValueError("Курс євро має бути додатнім числом.")
        except (ValueError, TypeError):
             raise ValueError("Курс євро має бути числом.")


        self.id = record_id
        self.employee_name = employee_name.strip() # Прибираємо пробіли на кінцях
        self.month_year = result # Зберігаємо валідований та відформатований рядок місяця
        self.level = level
        self.actual_hours = actual_hours
        self.tasks_completed_value = tasks_completed_value
        self.usd_rate = usd_rate
        self.eur_rate = eur_rate
        # calculated_salary_uah може бути None, якщо розрахунок буде пізніше
        self.calculated_salary_uah = float(calculated_salary_uah) if calculated_salary_uah is not None else None
        # Дата додавання запису
        self.date_added = date_added if date_added is not None else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Історія змін запису
        self.history = history if history is not None else []

    def to_dict(self):
        """Перетворює об'єкт на словник для збереження у JSON."""
        return {
            "id": self.id,
            "employee_name": self.employee_name,
            "month_year": self.month_year,
            "level": self.level,
            "actual_hours": self.actual_hours,
            "tasks_completed_value": self.tasks_completed_value,
            "usd_rate": self.usd_rate,
            "eur_rate": self.eur_rate,
            "calculated_salary_uah": self.calculated_salary_uah,
            "date_added": self.date_added,
            "history": self.history
        }

    @classmethod
    def from_dict(cls, data):
        """Створює об'єкт зі словника, завантаженого з JSON."""
        # Використовуємо .get() для безпечного доступу та конвертуємо числа у float
        record_id = data.get("id")
        employee_name = data.get("employee_name", "Невідомий працівник")
        month_year = data.get("month_year")
        level = data.get("level", "Junior")
        actual_hours = float(data.get("actual_hours", 0.0))
        tasks_completed_value = float(data.get("tasks_completed_value", 0.0))
        usd_rate = float(data.get("usd_rate", 1.0)) # Дефолтний курс 1.0, якщо відсутній (краще б дефолт з settings)
        eur_rate = float(data.get("eur_rate", 1.0)) # TODO: Можливо, брати дефолт з settings, якщо тут None?

        # calculated_salary_uah може бути None у старих записах
        calculated_salary_uah_raw = data.get("calculated_salary_uah")
        calculated_salary_uah = float(calculated_salary_uah_raw) if calculated_salary_uah_raw is not None else None

        date_added = data.get("date_added")
        history = data.get("history", []) # Забезпечуємо, що історія є списком

        # Повертаємо екземпляр, конструктор MonthlySalaryRecord виконає валідацію
        try:
             return cls(
                 record_id=record_id,
                 employee_name=employee_name,
                 month_year=month_year,
                 level=level,
                 actual_hours=actual_hours,
                 tasks_completed_value=tasks_completed_value,
                 usd_rate=usd_rate,
                 eur_rate=eur_rate,
                 calculated_salary_uah=calculated_salary_uah,
                 date_added=date_added,
                 history=history
             )
        except ValueError as e:
             # Якщо дані в JSON невалідна, це може статися.
             # Логуємо або обробляємо як помилку завантаження.
             print(f"Помилка при завантаженні запису з ID : {e}. Запис буде пропущено або матиме дефолтні значення.")
             # Можна повернути None або створити "зіпсований" об'єкт з повідомленням про помилку
             # Для простоти, повертаємо об'єкт з тими даними, що є, але логуємо помилку.
             # Або краще - нехай менеджер обробляє помилки від from_dict і фільтрує недійсні записи.
             raise e # Перекидаємо помилку, щоб менеджер міг її обробити під час завантаження

    def add_history_entry(self, changes):
        """Додає запис про зміни до історії."""
        self.history.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'changes': changes
        })