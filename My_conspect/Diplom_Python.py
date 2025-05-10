import json
from datetime import datetime
import locale
import os # Імпортуємо модуль os для роботи зі шляхами до файлів

# --- Конфігурація та утиліти ---

# Налаштування локалізації для коректного форматування чисел та валют
try:
    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
except locale.Error:
    print("Не вдалося встановити локалізацію 'uk_UA.UTF-8'. Використовується стандартна локалізація.")

# Ім'я файлу для зберігання даних
# Створюємо папку 'files', якщо вона не існує
DATA_DIR = 'files'
DATABASE_FILE = os.path.join(DATA_DIR, 'files\\salary_data.json') # Об'єднуємо шлях до папки та ім'я файлу

# Список допустимих місяців українською
MONTHS = [
    "Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
    "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"
]

# Допустимі рівні працівників
EMPLOYEE_LEVELS = ["Junior", "Middle", "Senior", "Team Lead"]

def validate_month_format(month_str):
    """Перевіряє, чи відповідає введений місяць формату 'Місяць Рік'."""
    parts = month_str.strip().split()
    if len(parts) != 2:
        return False, "Місяць має бути у форматі 'Місяць Рік' (наприклад, 'Січень 2024')!"

    month_name, year_str = parts
    # Перетворюємо введений місяць у правильний регістр
    month_name = month_name.capitalize()
    if month_name not in MONTHS:
        return False, f"Місяць має бути одним із: {', '.join(MONTHS)}!"

    try:
        year = int(year_str)
        if year < 2022 or year > 2100: # Обмежуємо діапазон років
            return False, "Рік має бути між 2022 і 2100!"
    except ValueError:
        return False, "Рік має бути числом (наприклад, 2024)!"

    return True, month_name + " " + str(year)

def month_to_tuple(month_year_str):
    """Перетворює місяць у формат (рік, номер місяця) для хронологічного сортування."""
    try:
        month_name, year_str = month_year_str.split()
        month_num = MONTHS.index(month_name) + 1
        return (int(year_str), month_num)
    except (ValueError, IndexError):
        # Обробка помилки, якщо формат місяця невірний (хоча validate_month_format має запобігти цьому)
        print(f"Помилка форматування місяця: {month_year_str}. Сортування може бути невірним.")
        return (0, 0) # Повертаємо значення, яке буде внизу списку при сортуванні


# --- Класи даних та управління ---

class SalarySettings:
    """
    Клас для зберігання глобальних налаштувань розрахунку зарплати.
    """
    def __init__(self, base_amounts=None, coefficients=None, task_costs=None, standard_monthly_hours=164, default_rates=None):
        # Базові ставки зарплати (фіксована частина) для кожного рівня
        # Якщо не передано, встановлюємо значення за замовчуванням
        self.base_amounts = base_amounts if base_amounts is not None else {
            "Junior": 10000,
            "Middle": 20000,
            "Senior": 35000,
            "Team Lead": 50000
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
            "Simple": 100,
            "Medium": 250,
            "Complex": 500
        }
        # Стандартна кількість робочих годин на місяць (для розрахунку вартості години з базової ставки)
        self.standard_monthly_hours = standard_monthly_hours if standard_monthly_hours > 0 else 164
        # Курси валют за замовчуванням (на випадок, якщо немає жодного запису)
        self.default_rates = default_rates if default_rates is not None else {
            "USD": 41.84,
            "EUR": 47.17
        }

        # Перевірка, що для всіх допустимих рівнів є ставки та коефіцієнти
        for level in EMPLOYEE_LEVELS:
            if level not in self.base_amounts:
                 print(f"Попередження: Для рівня '{level}' не встановлено базову ставку. Використовується 0.")
                 self.base_amounts[level] = 0
            if level not in self.coefficients:
                 print(f"Попередження: Для рівня '{level}' не встановлено коефіцієнт. Використовується 1.0.")
                 self.coefficients[level] = 1.0

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
        """Створює об'єкт із словника, завантаженого з JSON."""
        return cls(
            base_amounts=data.get("base_amounts"),
            coefficients=data.get("coefficients"),
            task_costs=data.get("task_costs"),
            standard_monthly_hours=data.get("standard_monthly_hours", 164), # Враховуємо старі файли без цього поля
            default_rates=data.get("default_rates")
        )

    def update_base_amount(self, level, amount):
        """Оновлює базову ставку для певного рівня."""
        if level in EMPLOYEE_LEVELS:
            self.base_amounts[level] = amount
            print(f"Базова ставка для рівня '{level}' оновлена до {amount} UAH.")
        else:
            print(f"Невідомий рівень працівника: '{level}'.")

    def update_coefficient(self, level, coefficient):
        """Оновлює коефіцієнт для певного рівня."""
        if level in EMPLOYEE_LEVELS:
            self.coefficients[level] = coefficient
            print(f"Коефіцієнт для рівня '{level}' оновлено до {coefficient}.")
        else:
            print(f"Невідомий рівень працівника: '{level}'.")

    def update_task_cost(self, task_type, cost):
        """Оновлює або додає вартість типу завдання."""
        self.task_costs[task_type] = cost
        print(f"Вартість завдання '{task_type}' оновлена/додана: {cost} UAH.")

    def delete_task_cost(self, task_type):
        """Видаляє вартість типу завдання."""
        if task_type in self.task_costs:
            del self.task_costs[task_type]
            print(f"Вартість завдання '{task_type}' видалено.")
        else:
            print(f"Тип завдання '{task_type}' не знайдено.")

    def update_standard_hours(self, hours):
        """Оновлює стандартну кількість робочих годин на місяць."""
        if hours > 0:
            self.standard_monthly_hours = hours
            print(f"Стандартна кількість робочих годин на місяць оновлена до {hours}.")
        else:
            print("Стандартна кількість годин має бути більше нуля.")

    def update_default_rates(self, usd_rate, eur_rate):
        """Оновлює курси валют за замовчуванням."""
        if usd_rate > 0 and eur_rate > 0:
            self.default_rates["USD"] = usd_rate
            self.default_rates["EUR"] = eur_rate
            print(f"Курси валют за замовчуванням оновлено: 1 USD = {usd_rate} UAH, 1 EUR = {eur_rate} UAH.")
        else:
            print("Курси валют мають бути більше нуля.")


class MonthlySalaryRecord:
    """
    Клас для зберігання даних про зарплату конкретного працівника за конкретний місяць.
    """
    def __init__(self, record_id, employee_name, month_year, level, actual_hours, tasks_completed_value, usd_rate, eur_rate, calculated_salary_uah=None, date_added=None, history=None):
        self.id = record_id
        self.employee_name = employee_name
        # Перевіряємо формат місяця при створенні
        is_valid, result = validate_month_format(month_year)
        if not is_valid:
             # Це має бути перехоплено до створення об'єкта, але на всякий випадок
             raise ValueError(f"Невірний формат місяця: {month_year}. {result}")
        self.month_year = result
        self.level = level
        self.actual_hours = actual_hours
        self.tasks_completed_value = tasks_completed_value
        self.usd_rate = usd_rate
        self.eur_rate = eur_rate
        # Якщо зарплата не передана при створенні (наприклад, при завантаженні зі старого файлу),
        # вона буде розрахована менеджером.
        self.calculated_salary_uah = calculated_salary_uah
        # Дата додавання запису (автоматично встановлюється при створенні)
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
        """Створює об'єкт із словника, завантаженого з JSON."""
        # Додаємо перевірку наявності всіх ключів, використовуючи .get()
        return cls(
            record_id=data.get("id"),
            employee_name=data.get("employee_name", "Невідомий працівник"), # Забезпечуємо дефолтне значення
            month_year=data.get("month_year"),
            level=data.get("level", "Junior"), # Дефолтний рівень, якщо відсутній
            actual_hours=data.get("actual_hours", 0), # Дефолтне значення, якщо відсутнє
            tasks_completed_value=data.get("tasks_completed_value", 0), # Дефолтне значення, якщо відсутнє
            usd_rate=data.get("usd_rate"),
            eur_rate=data.get("eur_rate"),
            calculated_salary_uah=data.get("calculated_salary_uah"),
            date_added=data.get("date_added"),
            history=data.get("history")
        )

    def add_history_entry(self, changes):
        """Додає запис про зміни до історії."""
        self.history.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'changes': changes
        })


class SalaryManager:
    """
    Клас для управління всіма даними про зарплату, включаючи налаштування та записи за місяцями.
    """
    def __init__(self, database_file):
        self.database_file = database_file
        self.settings = SalarySettings() # Ініціалізуємо налаштування за замовчуванням
        self.monthly_records = [] # Список для зберігання об'єктів MonthlySalaryRecord
        self._load_data() # Автоматично завантажуємо дані при створенні менеджера

    def _load_data(self):
        """
        Завантажує дані з JSON-файлу.
        Якщо файл не існує або порожній/пошкоджений, ініціалізує порожні дані
        з налаштуваннями за замовчуванням.
        """
        # Перевіряємо, чи існує папка, і створюємо її, якщо ні
        data_dir = os.path.dirname(self.database_file)
        if data_dir and not os.path.exists(data_dir):
            try:
                os.makedirs(data_dir)
                print(f"Створено папку для даних: {data_dir}")
            except OSError as e:
                print(f"Помилка при створенні папки {data_dir}: {e}")
                # Продовжуємо роботу, можливо, з помилками збереження пізніше

        try:
            with open(self.database_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Завантажуємо налаштування
                settings_data = data.get("settings", {})
                self.settings = SalarySettings.from_dict(settings_data)

                # Завантажуємо записи про зарплату
                records_data = data.get("monthly_records", [])
                self.monthly_records = [MonthlySalaryRecord.from_dict(record) for record in records_data]

            print(f"Дані успішно завантажено з {self.database_file}.")

        except FileNotFoundError:
            print(f"Файл {self.database_file} не знайдено. Створюється нова база даних.")
            self.settings = SalarySettings() # Ініціалізуємо налаштування за замовчуванням
            self.monthly_records = []
            self._save_data() # Зберігаємо початкову структуру файлу

        except json.JSONDecodeError:
            print(f"Помилка: Файл {self.database_file} пошкоджений або порожній. Створюється нова база даних.")
            self.settings = SalarySettings() # Ініціалізуємо налаштування за замовчуванням
            self.monthly_records = []
            self._save_data() # Зберігаємо початкову структуру файлу

        except Exception as e:
            print(f"Невідома помилка при завантаженні даних: {e}")
            self.settings = SalarySettings() # Ініціалізуємо налаштування за замовчуванням
            self.monthly_records = []


    def _save_data(self):
        """Зберігає поточні дані (налаштування та записи) у JSON-файл."""
        data_to_save = {
            "settings": self.settings.to_dict(),
            "monthly_records": [record.to_dict() for record in self.monthly_records]
        }
        try:
            with open(self.database_file, 'w', encoding='utf-8') as file:
                json.dump(data_to_save, file, indent=4, ensure_ascii=False) # ensure_ascii=False для збереження кирилиці
            # print(f"Дані успішно збережено у {self.database_file}.") # Можна вимкнути для менш "багатослівного" виводу
        except Exception as e:
            print(f"Помилка при збереженні даних у {self.database_file}: {e}")

    def get_next_record_id(self):
        """Генерує унікальний ID для нового запису (простий інкремент)."""
        return max([r.id for r in self.monthly_records], default=0) + 1

    def calculate_salary(self, level, actual_hours, tasks_completed_value):
        """
        Розраховує зарплату за формулою:
        Зарплата = ((Базова_ставка_за_рівнем / Стандартні_години) * Фактичні_години + Вартість_завдань) * Коефіцієнт_за_рівнем
        """
        base_amount = self.settings.base_amounts.get(level, 0)
        coefficient = self.settings.coefficients.get(level, 1.0)
        standard_hours = self.settings.standard_monthly_hours

        if standard_hours <= 0:
            print("Попередження: Стандартна кількість годин не встановлена або дорівнює нулю. Базова частина зарплати буде нульовою.")
            hourly_base_rate = 0
        else:
            hourly_base_rate = base_amount / standard_hours

        base_salary_part = hourly_base_rate * actual_hours
        additional_salary_part = tasks_completed_value # Вартість завдань вже розрахована

        total_uah_before_coeff = base_salary_part + additional_salary_part
        final_salary_uah = total_uah_before_coeff * coefficient

        return final_salary_uah

    def convert_currency(self, amount, usd_rate, eur_rate):
        """Переводить суму з гривень у долари та євро."""
        usd = amount / usd_rate if usd_rate > 0 else 0
        eur = amount / eur_rate if eur_rate > 0 else 0
        return usd, eur

    def format_salary(self, amount, usd_rate, eur_rate):
        """Форматує зарплату у гривнях, доларах і євро."""
        usd, eur = self.convert_currency(amount, usd_rate, eur_rate)
        # locale.format_string може мати проблеми з float, використовуємо f-string для контролю форматування
        # Або використовуємо locale.currency, якщо потрібно форматування валюти
        try:
             # Спробуємо формат з урахуванням локалі, але простіший
             formatted_uah = locale.format_string("%.2f", amount, grouping=True).replace(',', ' ') # Заміна коми на пробіл для тисяч
             formatted_usd = locale.format_string("%.2f", usd, grouping=True).replace(',', ' ')
             formatted_eur = locale.format_string("%.2f", eur, grouping=True).replace(',', ' ')
             return f"{formatted_uah} гривень ({formatted_usd} долар / {formatted_eur} євро)"
        except Exception:
             # Резервний варіант без локалі
             return f"{amount:.2f} гривень ({usd:.2f} долар / {eur:.2f} євро)"


    def add_salary_record(self):
        """Додає новий запис про зарплату за місяць для працівника."""
        print("\n--- Додати запис про зарплату ---")
        employee_name = input("Введіть ім'я працівника: ").strip()
        if not employee_name:
            print("Ім'я працівника не може бути порожнім!")
            return

        month_year = input("Введіть місяць (наприклад, 'Січень 2024'): ").strip()
        is_valid, result = validate_month_format(month_year)
        if not is_valid:
            print(result)
            return
        month_year = result

        # Перевірка унікальності запису для цього працівника за цей місяць
        if any(r.employee_name.lower() == employee_name.lower() and r.month_year.lower() == month_year.lower() for r in self.monthly_records):
            print(f"Дані за {month_year} для працівника {employee_name} уже існують! Використовуйте редагування для зміни.")
            return

        print(f"Допустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
        level = input("Введіть рівень працівника (Junior, Middle, Senior, Team Lead): ").strip()
        if level not in EMPLOYEE_LEVELS:
            print(f"Невірний рівень. Виберіть зі списку: {', '.join(EMPLOYEE_LEVELS)}")
            return

        try:
            actual_hours = float(input("Введіть фактично відпрацьовані години в місяць: "))
            if actual_hours < 0:
                print("Відпрацьовані години не можуть бути від'ємними!")
                return

            # Вартість завдань можна ввести напряму або розрахувати на основі типів завдань
            # Для спрощення, вводимо загальну вартість виконаних завдань за місяць
            print(f"Доступні типи завдань та їх вартість: {self.settings.task_costs}")
            tasks_completed_value = float(input("Введіть загальну вартість виконаних завдань за місяць: "))
            if tasks_completed_value < 0:
                print("Вартість виконаних завдань не може бути від'ємною!")
                return

            # Використовуємо курси з останнього запису або дефолтні
            last_record = next(iter(reversed(self.monthly_records)), None) # Останній запис
            default_usd = last_record.usd_rate if last_record else self.settings.default_rates["USD"]
            default_eur = last_record.eur_rate if last_record else self.settings.default_rates["EUR"]

            usd_rate_input = input(f"Введіть курс долара (гривень за 1 USD, за замовчуванням {default_usd}): ").strip()
            usd_rate = float(usd_rate_input) if usd_rate_input else default_usd
            if usd_rate <= 0:
                print("Курс долара не може бути від'ємним або нульовим!")
                return
            if usd_rate < 10 or usd_rate > 200: # Розширимо діапазон на всякий випадок
                print("Курс долара має бути в межах 10–200 гривень!")
                # Можна запитати підтвердження, якщо курс виходить за межі нормального діапазону

            eur_rate_input = input(f"Введіть курс євро (гривень за 1 EUR, за замовчуванням {default_eur}): ").strip()
            eur_rate = float(eur_rate_input) if eur_rate_input else default_eur
            if eur_rate <= 0:
                print("Курс євро не може бути від'ємним або нульовим!")
                return
            if eur_rate < 10 or eur_rate > 200:
                print("Курс євро має бути в межах 10–200 гривень!")
                # Можна запитати підтвердження

        except ValueError:
            print("Будь ласка, введіть коректні числові значення!")
            return

        # Розраховуємо зарплату
        calculated_salary = self.calculate_salary(level, actual_hours, tasks_completed_value)

        # Створюємо новий об'єкт запису
        new_record_id = self.get_next_record_id()
        new_record = MonthlySalaryRecord(
            record_id=new_record_id,
            employee_name=employee_name,
            month_year=month_year,
            level=level,
            actual_hours=actual_hours,
            tasks_completed_value=tasks_completed_value,
            usd_rate=usd_rate,
            eur_rate=eur_rate,
            calculated_salary_uah=calculated_salary # Зберігаємо розраховану зарплату
        )

        self.monthly_records.append(new_record)
        self._save_data()
        print(f'\nЗапис #{new_record.id} за {new_record.month_year} для {new_record.employee_name} успішно додано!')
        print(f"Розрахована зарплата: {self.format_salary(new_record.calculated_salary_uah, new_record.usd_rate, new_record.eur_rate)}")

    def find_record_by_id(self, record_id):
        """Знаходить запис за його ID."""
        try:
            record_id = int(record_id)
            for record in self.monthly_records:
                if record.id == record_id:
                    return record
            return None
        except ValueError:
            return None # Якщо введено не число

    def delete_salary_record(self):
        """Видаляє запис про зарплату за номером."""
        if not self.monthly_records:
            print("Дані відсутні.")
            return

        record_id_input = input("Введіть номер запису для видалення: ").strip()
        record_to_delete = self.find_record_by_id(record_id_input)

        if record_to_delete:
            self.monthly_records.remove(record_to_delete)
            # Оновлюємо ID інших записів, щоб вони йшли по порядку (опціонально, але робить список охайнішим)
            for index, record in enumerate(self.monthly_records, start=1):
                 record.id = index
            self._save_data()
            print(f'Запис #{record_to_delete.id} за {record_to_delete.month_year} для {record_to_delete.employee_name} видалено!')
        else:
            print("Запис із таким номером не знайдено!")

    def edit_salary_record(self):
        """Редагує дані для конкретного запису про зарплату."""
        if not self.monthly_records:
            print("Дані відсутні.")
            return

        record_id_input = input("Введіть номер запису для редагування: ").strip()
        record_to_edit = self.find_record_by_id(record_id_input)

        if not record_to_edit:
            print("Запис із таким номером не знайдено!")
            return

        print(f"\n--- Редагування запису #{record_to_edit.id} за {record_to_edit.month_year} для {record_to_edit.employee_name} ---")
        print(f"Поточні дані:")
        print(f"  Ім'я працівника: {record_to_edit.employee_name}")
        print(f"  Місяць: {record_to_edit.month_year}")
        print(f"  Рівень: {record_to_edit.level}")
        print(f"  Відпрацьовані години: {record_to_edit.actual_hours}")
        print(f"  Вартість завдань: {record_to_edit.tasks_completed_value}")
        print(f"  Курс долара: {record_to_edit.usd_rate} UAH")
        print(f"  Курс євро: {record_to_edit.eur_rate} UAH")
        print(f"  Розрахована зарплата: {self.format_salary(record_to_edit.calculated_salary_uah, record_to_edit.usd_rate, record_to_edit.eur_rate)}")

        changes = {} # Словник для відстеження змін

        # Редагування полів з можливістю залишити без змін (Enter)
        new_employee_name = input(f"Введіть нове ім'я працівника (або Enter '{record_to_edit.employee_name}'): ").strip()
        if new_employee_name and new_employee_name.lower() != record_to_edit.employee_name.lower():
             changes['employee_name'] = {'old': record_to_edit.employee_name, 'new': new_employee_name}
             record_to_edit.employee_name = new_employee_name

        new_month_year = input(f"Введіть новий місяць (або Enter '{record_to_edit.month_year}'): ").strip()
        if new_month_year and new_month_year.lower() != record_to_edit.month_year.lower():
            is_valid, result = validate_month_format(new_month_year)
            if not is_valid:
                print(f"Помилка формату місяця: {result}. Редагування скасовано.")
                return
            new_month_year_formatted = result
            # Перевірка унікальності нового місяця для цього працівника
            if any(r.employee_name.lower() == record_to_edit.employee_name.lower() and r.month_year.lower() == new_month_year_formatted.lower() and r.id != record_to_edit.id for r in self.monthly_records):
                 print(f"Дані за {new_month_year_formatted} для працівника {record_to_edit.employee_name} уже існують! Редагування скасовано.")
                 return

            changes['month_year'] = {'old': record_to_edit.month_year, 'new': new_month_year_formatted}
            record_to_edit.month_year = new_month_year_formatted


        print(f"Допустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
        new_level = input(f"Введіть новий рівень ({', '.join(EMPLOYEE_LEVELS)}, або Enter '{record_to_edit.level}'): ").strip()
        if new_level: # Якщо щось ввели
             if new_level not in EMPLOYEE_LEVELS:
                  print(f"Невірний рівень. Виберіть зі списку: {', '.join(EMPLOYEE_LEVELS)}. Редагування скасовано.")
                  return
             if new_level != record_to_edit.level:
                  changes['level'] = {'old': record_to_edit.level, 'new': new_level}
                  record_to_edit.level = new_level


        try:
            hours_input = input(f"Введіть нові відпрацьовані години (або Enter '{record_to_edit.actual_hours}'): ").strip()
            if hours_input: # Якщо щось ввели
                new_hours = float(hours_input)
                if new_hours < 0:
                    print("Відпрацьовані години не можуть бути від'ємними! Редагування скасовано.")
                    return
                if new_hours != record_to_edit.actual_hours:
                    changes['actual_hours'] = {'old': record_to_edit.actual_hours, 'new': new_hours}
                    record_to_edit.actual_hours = new_hours

            tasks_input = input(f"Введіть нову загальну вартість завдань (або Enter '{record_to_edit.tasks_completed_value}'): ").strip()
            if tasks_input: # Якщо щось ввели
                new_tasks_value = float(tasks_input)
                if new_tasks_value < 0:
                    print("Вартість виконаних завдань не може бути від'ємною! Редагування скасовано.")
                    return
                if new_tasks_value != record_to_edit.tasks_completed_value:
                    changes['tasks_completed_value'] = {'old': record_to_edit.tasks_completed_value, 'new': new_tasks_value}
                    record_to_edit.tasks_completed_value = new_tasks_value

            usd_rate_input = input(f"Введіть новий курс долара (або Enter '{record_to_edit.usd_rate}'): ").strip()
            if usd_rate_input: # Якщо щось ввели
                new_usd_rate = float(usd_rate_input)
                if new_usd_rate <= 0:
                    print("Курс долара не може бути від'ємним або нульовим! Редагування скасовано.")
                    return
                if new_usd_rate != record_to_edit.usd_rate:
                    changes['usd_rate'] = {'old': record_to_edit.usd_rate, 'new': new_usd_rate}
                    record_to_edit.usd_rate = new_usd_rate

            eur_rate_input = input(f"Введіть новий курс євро (або Enter '{record_to_edit.eur_rate}'): ").strip()
            if eur_rate_input: # Якщо щось ввели
                new_eur_rate = float(eur_rate_input)
                if new_eur_rate <= 0:
                    print("Курс євро не може бути від'ємним або нульовим! Редагування скасовано.")
                    return
                if new_eur_rate != record_to_edit.eur_rate:
                    changes['eur_rate'] = {'old': record_to_edit.eur_rate, 'new': new_eur_rate}
                    record_to_edit.eur_rate = new_eur_rate

        except ValueError:
            print("Будь ласка, введіть коректні числові значення! Редагування скасовано.")
            return

        # Якщо були зміни, перераховуємо зарплату, додаємо в історію та зберігаємо
        if changes:
            old_salary = record_to_edit.calculated_salary_uah # Запам'ятовуємо стару зарплату
            record_to_edit.calculated_salary_uah = self.calculate_salary(
                 record_to_edit.level,
                 record_to_edit.actual_hours,
                 record_to_edit.tasks_completed_value
            )
            # Додаємо зміну зарплати до логу
            if old_salary != record_to_edit.calculated_salary_uah:
                 changes['calculated_salary_uah'] = {'old': old_salary, 'new': record_to_edit.calculated_salary_uah}

            record_to_edit.add_history_entry(changes) # Логуємо всі зміни
            self._save_data()
            print(f"Дані для запису #{record_to_edit.id} оновлено!")
            print(f"Нова розрахована зарплата: {self.format_salary(record_to_edit.calculated_salary_uah, record_to_edit.usd_rate, record_to_edit.eur_rate)}")
        else:
            print("Змін не внесено.")

    def display_record_details(self, record):
         """Виводить деталі одного запису про зарплату."""
         print(f"\n--- Запис #{record.id} ---")
         print(f"  Працівник: {record.employee_name}")
         print(f"  Місяць: {record.month_year}")
         print(f"  Рівень: {record.level}")
         print(f"  Відпрацьовані години: {record.actual_hours}")
         print(f"  Вартість виконаних завдань: {record.tasks_completed_value:.2f} UAH")
         print(f"  Курс долара: {record.usd_rate:.2f} UAH")
         print(f"  Курс євро: {record.eur_rate:.2f} UAH")
         print(f"  Зарплата: {self.format_salary(record.calculated_salary_uah, record.usd_rate, record.eur_rate)}")
         print(f"  Дата додавання: {record.date_added}")
         if record.history:
              print("  Історія змін:")
              for entry in record.history:
                   timestamp = entry.get('timestamp', 'Невідома дата')
                   changes_list = [f"{key}: '{val.get('old', 'N/A')}' -> '{val.get('new', 'N/A')}'" for key, val in entry.get('changes', {}).items()]
                   print(f"    - {timestamp}: {', '.join(changes_list)}")
         print("-" * 30)


    def print_all_salary_data(self, sort_by='month', year_filter=None):
        """Виводить усі записи про зарплату з можливістю сортування та фільтрації за роком."""
        if not self.monthly_records:
            print("Дані відсутні.")
            return

        filtered_records = self.monthly_records
        if year_filter:
            filtered_records = [r for r in self.monthly_records if r.month_year.split()[-1] == year_filter]
            if not filtered_records:
                print(f"Дані за {year_filter} рік не знайдено!")
                return

        if sort_by == 'month':
            # Сортування за роком, потім за місяцем
            sorted_records = sorted(filtered_records, key=lambda r: month_to_tuple(r.month_year))
        elif sort_by == 'salary':
            # Сортування за зарплатою (від більшої до меншої)
            sorted_records = sorted(filtered_records, key=lambda r: r.calculated_salary_uah, reverse=True)
        elif sort_by == 'employee':
             # Сортування за іменем працівника, потім за місяцем
             sorted_records = sorted(filtered_records, key=lambda r: (r.employee_name.lower(), month_to_tuple(r.month_year)))
        else:
            sorted_records = filtered_records # Без сортування

        print("\n--- Усі записи про зарплату ---")
        for record in sorted_records:
            self.display_record_details(record)
        print("--- Кінець списку ---")


    def print_salary_by_month(self):
        """Виводить зарплату за конкретний місяць для всіх працівників."""
        if not self.monthly_records:
            print("Дані відсутні.")
            return

        month_year = input("Введіть місяць для пошуку (наприклад, 'Січень 2024'): ").strip()
        is_valid, result = validate_month_format(month_year)
        if not is_valid:
            print(result)
            return
        month_year = result

        found_records = [r for r in self.monthly_records if r.month_year.lower() == month_year.lower()]

        if not found_records:
            print(f"Дані за {month_year} не знайдено!")
            return

        print(f"\n--- Записи за {month_year} ---")
        # Сортуємо записи за іменем працівника для зручності
        sorted_records = sorted(found_records, key=lambda r: r.employee_name.lower())
        for record in sorted_records:
             self.display_record_details(record)
        print("--- Кінець списку за місяць ---")


    def calculate_total_salary_by_year(self, year):
        """Обчислює загальну зарплату за рік для всіх працівників."""
        year_str = str(year)
        year_records = [r for r in self.monthly_records if r.month_year.split()[-1] == year_str]

        if not year_records:
            return 0, []

        total_salary = sum(r.calculated_salary_uah for r in year_records)

        # Для переведення в іноземні валюти використовуємо середній курс за рік
        avg_usd_rate = sum(r.usd_rate for r in year_records) / len(year_records) if year_records else self.settings.default_rates["USD"]
        avg_eur_rate = sum(r.eur_rate for r in year_records) / len(year_records) if year_records else self.settings.default_rates["EUR"]

        return total_salary, year_records, avg_usd_rate, avg_eur_rate


    def print_salary_by_year(self):
        """Виводить загальну зарплату за рік."""
        if not self.monthly_records:
            print("Дані відсутні.")
            return

        year_input = input("Введіть рік для пошуку загальної зарплати (наприклад, '2024'): ").strip()
        try:
             year = int(year_input)
        except ValueError:
             print("Будь ласка, введіть коректний рік (число).")
             return

        total_salary, year_records, avg_usd_rate, avg_eur_rate = self.calculate_total_salary_by_year(year)

        if not year_records:
            print(f"Дані за {year} рік не знайдено!")
            return

        print(f"\n--- Загальна зарплата за {year} рік ---")
        print(f"Всього записів за рік: {len(year_records)}")
        print(f"Загальна сума: {self.format_salary(total_salary, avg_usd_rate, avg_eur_rate)}")
        print("-" * 30)


    def print_average_salary_by_year(self):
        """Виводить середню зарплату за місяць за рік."""
        if not self.monthly_records:
            print("Дані відсутні.")
            return

        year_input = input("Введіть рік для пошуку середньої зарплати (наприклад, '2024'): ").strip()
        try:
             year = int(year_input)
        except ValueError:
             print("Будь ласка, введіть коректний рік (число).")
             return

        total_salary, year_records, avg_usd_rate, avg_eur_rate = self.calculate_total_salary_by_year(year)

        if not year_records:
            print(f"Дані за {year} рік не знайдено!")
            return

        average_salary = total_salary / len(year_records)
        print(f"\n--- Середня зарплата за місяць у {year} році ---")
        print(f"Розраховано на основі {len(year_records)} записів.")
        print(f"Середня сума: {self.format_salary(average_salary, avg_usd_rate, avg_eur_rate)}")
        print("-" * 30)

    def manage_settings(self):
         """Меню управління налаштуваннями."""
         while True:
             print('\n' + '=' * 30)
             print(' Меню налаштувань:')
             print(' 1. Показати поточні налаштування')
             print(' 2. Редагувати базові ставки за рівнями')
             print(' 3. Редагувати коефіцієнти за рівнями')
             print(' 4. Редагувати вартість типів завдань')
             print(' 5. Редагувати стандартну кількість робочих годин')
             print(' 6. Редагувати курси валют за замовчуванням')
             print(' 7. Вийти з меню налаштувань')
             print('=' * 30)

             choice = input('Виберіть опцію налаштувань: ').strip()
             print('*!' * 15)

             if choice == '1':
                  self.print_settings()
             elif choice == '2':
                  self.edit_base_amounts()
             elif choice == '3':
                  self.edit_coefficients()
             elif choice == '4':
                  self.edit_task_costs()
             elif choice == '5':
                  self.edit_standard_hours()
             elif choice == '6':
                  self.edit_default_rates()
             elif choice == '7':
                  print("Вихід з меню налаштувань.")
                  break
             else:
                  print('Невірний вибір. Спробуйте ще раз.')


    def print_settings(self):
         """Виводить поточні налаштування розрахунку зарплати."""
         print("\n--- Поточні налаштування ---")
         print("Базові ставки за рівнями (UAH):")
         for level, amount in self.settings.base_amounts.items():
              print(f"  {level}: {amount:.2f} UAH")

         print("\nКоефіцієнти за рівнями:")
         for level, coeff in self.settings.coefficients.items():
              print(f"  {level}: {coeff:.2f}")

         print("\nВартість типів завдань (UAH):")
         if self.settings.task_costs:
            for task_type, cost in self.settings.task_costs.items():
                 print(f"  '{task_type}': {cost:.2f} UAH")
         else:
            print("  (Немає визначених типів завдань)")


         print(f"\nСтандартна кількість робочих годин на місяць: {self.settings.standard_monthly_hours}")

         print("\nКурси валют за замовчуванням:")
         print(f"  1 USD = {self.settings.default_rates.get('USD', 0):.2f} UAH")
         print(f"  1 EUR = {self.settings.default_rates.get('EUR', 0):.2f} UAH")
         print("-" * 30)


    def edit_base_amounts(self):
        """Редагує базові ставки за рівнями."""
        print("\n--- Редагування базових ставок ---")
        print("Поточні ставки:")
        for level, amount in self.settings.base_amounts.items():
            print(f"  {level}: {amount:.2f} UAH")

        print(f"\nДопустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
        level_to_edit = input("Введіть рівень для редагування (або Enter для скасування): ").strip()

        if not level_to_edit:
             print("Редагування скасовано.")
             return

        if level_to_edit not in EMPLOYEE_LEVELS:
             print(f"Невірний рівень. Виберіть зі списку: {', '.join(EMPLOYEE_LEVELS)}.")
             return

        try:
             current_amount = self.settings.base_amounts.get(level_to_edit, 0)
             new_amount_input = input(f"Введіть нову базову ставку для '{level_to_edit}' (поточна: {current_amount:.2f}, або Enter): ").strip()
             if new_amount_input:
                  new_amount = float(new_amount_input)
                  if new_amount < 0:
                       print("Ставка не може бути від'ємною!")
                       return
                  self.settings.update_base_amount(level_to_edit, new_amount)
                  self._save_data()
             else:
                  print("Залишено без змін.")
        except ValueError:
             print("Будь ласка, введіть коректне числове значення.")


    def edit_coefficients(self):
        """Редагує коефіцієнти за рівнями."""
        print("\n--- Редагування коефіцієнтів ---")
        print("Поточні коефіцієнти:")
        for level, coeff in self.settings.coefficients.items():
            print(f"  {level}: {coeff:.2f}")

        print(f"\nДопустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
        level_to_edit = input("Введіть рівень для редагування (або Enter для скасування): ").strip()

        if not level_to_edit:
             print("Редагування скасовано.")
             return

        if level_to_edit not in EMPLOYEE_LEVELS:
             print(f"Невірний рівень. Виберіть зі списку: {', '.join(EMPLOYEE_LEVELS)}.")
             return

        try:
             current_coeff = self.settings.coefficients.get(level_to_edit, 1.0)
             new_coeff_input = input(f"Введіть новий коефіцієнт для '{level_to_edit}' (поточний: {current_coeff:.2f}, або Enter): ").strip()
             if new_coeff_input:
                  new_coeff = float(new_coeff_input)
                  if new_coeff < 0:
                       print("Коефіцієнт не може бути від'ємним!")
                       return
                  self.settings.update_coefficient(level_to_edit, new_coeff)
                  self._save_data()
             else:
                  print("Залишено без змін.")
        except ValueError:
             print("Будь ласка, введіть коректне числове значення.")


    def edit_task_costs(self):
        """Редагує вартість типів завдань."""
        print("\n--- Редагування вартості типів завдань ---")
        print("Поточні типи завдань та їх вартість:")
        if self.settings.task_costs:
            for task_type, cost in self.settings.task_costs.items():
                print(f"  '{task_type}': {cost:.2f} UAH")
        else:
            print("  (Немає визначених типів завдань)")

        print("\nОпції: додати/редагувати тип (введіть назву), видалити тип (введіть 'видалити'), або Enter для скасування.")
        task_action = input("Введіть назву типу завдання або 'видалити': ").strip()

        if not task_action:
             print("Редагування скасовано.")
             return

        if task_action.lower() == 'видалити':
             task_to_delete = input("Введіть назву типу завдання для видалення: ").strip()
             if task_to_delete:
                  self.settings.delete_task_cost(task_to_delete)
                  self._save_data()
             else:
                  print("Видалення скасовано.")
             return

        # Якщо введено назву типу завдання (для додавання/редагування)
        task_type = task_action
        try:
            current_cost = self.settings.task_costs.get(task_type, 0) # 0, якщо тип новий
            new_cost_input = input(f"Введіть нову вартість для завдання '{task_type}' (поточна: {current_cost:.2f}, або Enter): ").strip()

            if new_cost_input:
                new_cost = float(new_cost_input)
                if new_cost < 0:
                    print("Вартість завдання не може бути від'ємною!")
                    return
                self.settings.update_task_cost(task_type, new_cost)
                self._save_data()
            else:
                print("Залишено без змін.")

        except ValueError:
             print("Будь ласка, введіть коректне числове значення для вартості.")


    def edit_standard_hours(self):
        """Редагує стандартну кількість робочих годин на місяць."""
        print("\n--- Редагування стандартних годин ---")
        print(f"Поточна стандартна кількість годин: {self.settings.standard_monthly_hours}")

        try:
            new_hours_input = input("Введіть нову стандартну кількість робочих годин на місяць (або Enter для скасування): ").strip()
            if new_hours_input:
                new_hours = float(new_hours_input)
                self.settings.update_standard_hours(new_hours)
                self._save_data()
            else:
                print("Залишено без змін.")
        except ValueError:
            print("Будь ласка, введіть коректне числове значення.")

    def edit_default_rates(self):
        """Редагує курси валют за замовчуванням."""
        print("\n--- Редагування курсів валют за замовчуванням ---")
        print(f"Поточні курси: 1 USD = {self.settings.default_rates.get('USD', 0):.2f} UAH, 1 EUR = {self.settings.default_rates.get('EUR', 0):.2f} UAH")

        try:
            new_usd_input = input(f"Введіть новий курс долара (або Enter '{self.settings.default_rates.get('USD', 0):.2f}'): ").strip()
            new_eur_input = input(f"Введіть новий курс євро (або Enter '{self.settings.default_rates.get('EUR', 0):.2f}'): ").strip()

            new_usd = float(new_usd_input) if new_usd_input else self.settings.default_rates.get('USD', 0)
            new_eur = float(new_eur_input) if new_eur_input else self.settings.default_rates.get('EUR', 0)

            self.settings.update_default_rates(new_usd, new_eur)
            self._save_data()

        except ValueError:
            print("Будь ласка, введіть коректні числові значення.")


# --- Головна частина програми ---

def main():
    """Головна функція програми, що управляє меню та взаємодією."""
    manager = SalaryManager(DATABASE_FILE) # Створюємо менеджер даних

    while True:
        print('\n' + '=' * 30)
        print('\nМеню:')
        print('1. Додати дані про зарплату за місяць')
        print('2. Видалити запис про зарплату за ID')
        print('3. Редагувати запис про зарплату за ID')
        print('4. Показати всі записи (сортувати за місяцем)')
        print('5. Показати всі записи (сортувати за зарплатою)')
        print('6. Показати всі записи (сортувати за працівником)')
        print('7. Показати зарплату за конкретним місяцем')
        print('8. Показати загальну зарплату за рік')
        print('9. Показати середню зарплату за місяць за рік')
        print('10. Фільтрувати записи за роком (сортувати за місяцем)')
        print('11. Фільтрувати записи за роком (сортувати за зарплатою)')
        print('12. Фільтрувати записи за роком (сортувати за працівником)')
        print('13. Управління налаштуваннями (базові ставки, коефіцієнти, завдання, години, курси)')
        print('14. Вийти')
        print('\n' + '=' * 30)
        choice = input('Виберіть опцію: ').strip()
        print('*!' * 15)

        if choice == '1':
            manager.add_salary_record()
        elif choice == '2':
            manager.delete_salary_record()
        elif choice == '3':
            manager.edit_salary_record()
        elif choice == '4':
            manager.print_all_salary_data(sort_by='month')
        elif choice == '5':
            manager.print_all_salary_data(sort_by='salary')
        elif choice == '6':
             manager.print_all_salary_data(sort_by='employee')
        elif choice == '7':
            manager.print_salary_by_month()
        elif choice == '8':
            manager.print_salary_by_year()
        elif choice == '9':
            manager.print_average_salary_by_year()
        elif choice == '10':
            year = input("Введіть рік для фільтрації (наприклад, '2024'): ").strip()
            manager.print_all_salary_data(sort_by='month', year_filter=year)
        elif choice == '11':
            year = input("Введіть рік для фільтрації (наприклад, '2024'): ").strip()
            manager.print_all_salary_data(sort_by='salary', year_filter=year)
        elif choice == '12':
            year = input("Введіть рік для фільтрації (наприклад, '2024'): ").strip()
            manager.print_all_salary_data(sort_by='employee', year_filter=year)
        elif choice == '13':
            manager.manage_settings() # Перехід у підменю налаштувань
        elif choice == '14':
            print('Дякую за використання програми! До побачення!')
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')


# Точка входу в програму
if __name__ == "__main__":
    main()