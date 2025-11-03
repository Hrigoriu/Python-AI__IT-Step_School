import json
import os
from datetime import datetime
from constants import DATABASE_FILE, EMPLOYEE_LEVELS
from models import SalarySettings, MonthlySalaryRecord
from utils import validate_month_format, month_to_tuple, format_salary

# --- Клас управління даними ---

class SalaryManager:
    """Клас для управління всіма даними про зарплату."""
    def __init__(self, database_file):
        self.database_file = database_file
        self.settings = SalarySettings()
        self.monthly_records = []
        self._load_data()

    def _load_data(self):
        """Завантажує дані з JSON-файлу."""
        data_dir = os.path.dirname(self.database_file)
        if data_dir and not os.path.exists(data_dir):
            try:
                os.makedirs(data_dir)
            except OSError as e:
                return f"Помилка при створенні папки {data_dir}: {e}"

        if not os.path.exists(self.database_file):
             self.settings = SalarySettings()
             self.monthly_records = []
             self._save_data()
             return f"Файл даних не знайдено. Створено нову база даних у {self.database_file}."

        try:
            with open(self.database_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                settings_data = data.get("settings", {})
                self.settings = SalarySettings.from_dict(settings_data)

                records_data = data.get("monthly_records", [])
                loaded_records = []
                errors = []
                for record_data in records_data:
                    try:
                        record = MonthlySalaryRecord.from_dict(record_data)
                        loaded_records.append(record)
                    except (ValueError, TypeError, KeyError) as e:
                         errors.append(f"Помилка завантаження запису з ID {record_data.get('id', 'N/A')}: {e}")

                self.monthly_records = loaded_records

                if errors:
                    return f"Дані завантажено з {self.database_file}, але виникли помилки при обробці {len(errors)} записів:\n" + "\n".join(errors)
                else:
                     recalculated_count = 0
                     for record in self.monthly_records:
                          old_salary = record.calculated_salary_uah
                          new_salary = self.calculate_salary_value(record.level, record.actual_hours, record.tasks_completed_value)
                          if old_salary is None or abs(old_salary - new_salary) > 0.01:
                               record.calculated_salary_uah = new_salary
                               recalculated_count += 1

                     if recalculated_count > 0:
                          self._save_data()
                          return f"Дані успішно завантажено з {self.database_file}. Перераховано зарплату для {recalculated_count} записів."
                     else:
                          return f"Дані успішно завантажено з {self.database_file}."


        except json.JSONDecodeError:
            self.settings = SalarySettings()
            self.monthly_records = []
            self._save_data()
            return f"Файл даних пошкоджений або порожній. Створено нову база даних у {self.database_file}."

        except Exception as e:
            self.settings = SalarySettings()
            self.monthly_records = []
            return f"Невідома помилка при завантаженні даних: {e}. Створено нову база даних."


    def _save_data(self):
        """Зберігає поточні дані у JSON-файл."""
        data_to_save = {
            "settings": self.settings.to_dict(),
            "monthly_records": [record.to_dict() for record in self.monthly_records]
        }
        try:
            with open(self.database_file, 'w', encoding='utf-8') as file:
                json.dump(data_to_save, file, indent=4, ensure_ascii=False)
            return f"Дані успішно збережено."
        except Exception as e:
            return f"Помилка при збереженні даних: {e}"

    def get_next_record_id(self):
        """Генерує унікальний ID для нового запису."""
        return max([r.id for r in self.monthly_records], default=0) + 1

    def calculate_salary_value(self, level, actual_hours, tasks_completed_value):
        """Розраховує зарплату за формулою."""
        base_amount = self.settings.base_amounts.get(level, 0.0)
        coefficient = self.settings.coefficients.get(level, 1.0)
        standard_hours = self.settings.standard_monthly_hours

        if standard_hours <= 0:
            print("Попередження: Стандартна кількість годин не встановлена або дорівнює нулю. Базова частина зарплати буде нульовою.")
            hourly_base_rate = 0.0
        else:
            hourly_base_rate = base_amount / standard_hours

        base_salary_part = hourly_base_rate * actual_hours
        additional_salary_part = tasks_completed_value

        total_uah_before_coeff = base_salary_part + additional_salary_part
        final_salary_uah = total_uah_before_coeff * coefficient

        return final_salary_uah

    # --- Методи для управління записами ---

    def add_salary_record(self, employee_name, month_year, level, actual_hours, tasks_completed_value, usd_rate=None, eur_rate=None):
        """Додає новий запис про зарплату за місяць."""
        # ПОКРАЩЕННЯ: Застосовуємо strip() до вхідних рядків на рівні менеджера для чистоти
        employee_name = str(employee_name).strip()
        month_year = str(month_year).strip()
        level = str(level).strip()
        actual_hours_str = str(actual_hours).strip()
        tasks_completed_value_str = str(tasks_completed_value).strip()
        usd_rate_str = str(usd_rate).strip() if usd_rate is not None else ''
        eur_rate_str = str(eur_rate).strip() if eur_rate is not None else ''


        if not employee_name:
            return "Помилка: Ім'я працівника не може бути порожнім!"

        is_valid_month, month_year_formatted = validate_month_format(month_year) # validate_month_format робить strip/capitalize
        if not is_valid_month:
            return f"Помилка: {month_year_formatted}"

        # Регістр рівня буде скориговано в конструкторі MonthlySalaryRecord, але перевірка тут
        if level.capitalize() not in EMPLOYEE_LEVELS:
             return f"Помилка: Невірний рівень '{level}'. Допустимі: {', '.join(EMPLOYEE_LEVELS)}"


        try:
            actual_hours = float(actual_hours_str)
            if actual_hours < 0:
                return "Помилка: Відпрацьовані години не можуть бути від'ємними!"
        except (ValueError, TypeError):
            return "Помилка: Відпрацьовані години мають бути числом!"

        try:
            tasks_completed_value = float(tasks_completed_value_str)
            if tasks_completed_value < 0:
                return "Помилка: Вартість виконаних завдань не може бути від'ємною!"
        except (ValueError, TypeError):
            return "Помилка: Вартість виконаних завдань має бути числом!"

        last_record = next(iter(reversed(self.monthly_records)), None)
        default_usd = last_record.usd_rate if last_record else self.settings.default_rates.get("USD", 40.0)
        default_eur = last_record.eur_rate if last_record else self.settings.default_rates.get("EUR", 43.0)

        try:
            usd_rate = float(usd_rate_str) if usd_rate_str != '' else default_usd
            if usd_rate <= 0:
                return "Помилка: Курс долара не може бути від'ємним або нульовим!"
        except (ValueError, TypeError):
            return "Помилка: Курс долара має бути числом!"

        try:
            eur_rate = float(eur_rate_str) if eur_rate_str != '' else default_eur
            if eur_rate <= 0:
                return "Помилка: Курс євро не може бути від'ємним або нульовим!"
        except (ValueError, TypeError):
             return "Помилка: Курс євро має бути числом!"

        # Перевірка унікальності за іменем та місяцем (регістронезалежна)
        if any(r.employee_name.lower() == employee_name.lower() and r.month_year.lower() == month_year_formatted.lower() for r in self.monthly_records):
            return f"Помилка: Дані за {month_year_formatted} для працівника {employee_name} уже існують! Використовуйте редагування для зміни."


        calculated_salary = self.calculate_salary_value(level, actual_hours, tasks_completed_value)

        new_record_id = self.get_next_record_id()
        try:
             # Конструктор MonthlySalaryRecord виконає фінальну чистку і валідацію регістру
             new_record = MonthlySalaryRecord(
                 record_id=new_record_id,
                 employee_name=employee_name,
                 month_year=month_year_formatted,
                 level=level,
                 actual_hours=actual_hours,
                 tasks_completed_value=tasks_completed_value,
                 usd_rate=usd_rate,
                 eur_rate=eur_rate,
                 calculated_salary_uah=calculated_salary
             )
             self.monthly_records.append(new_record)
             self._save_data()
             return new_record
        except ValueError as e:
             return f"Помилка при створенні запису: {e}"


    def find_record_by_id(self, record_id):
        """Знаходить запис за його ID."""
        try:
            record_id = int(record_id)
            for record in self.monthly_records:
                if record.id == record_id:
                    return record
            return None
        except ValueError:
            return None

    def delete_salary_record(self, record_id):
        """Видаляє запис про зарплату за номером."""
        if not self.monthly_records:
            return "Помилка: Дані відсутні."

        record_to_delete = self.find_record_by_id(record_id)

        if record_to_delete:
            self.monthly_records.remove(record_to_delete)
            for index, record in enumerate(self.monthly_records, start=1):
                 record.id = index
            self._save_data()
            return record_to_delete
        else:
            return f"Помилка: Запис із номером {record_id} не знайдено!"

    def edit_salary_record(self, record_id, updates):
        """Редагує дані для конкретного запису про зарплату."""
        record_to_edit = self.find_record_by_id(record_id)

        if not record_to_edit:
            return f"Помилка: Запис із номером {record_id} не знайдено!"

        changes = {}

        if 'employee_name' in updates and updates['employee_name'] is not None:
             new_name = str(updates['employee_name']).strip().title() # ПОКРАЩЕННЯ: Strip та Title Case
             if not new_name:
                  return "Помилка редагування: Ім'я працівника не може бути порожнім!"

             if new_name.lower() != record_to_edit.employee_name.lower():
                  if any(r.employee_name.lower() == new_name.lower() and r.month_year.lower() == record_to_edit.month_year.lower() and r.id != record_to_edit.id for r in self.monthly_records):
                      return f"Помилка редагування: Дані за {record_to_edit.month_year} для працівника {new_name} уже існують!"
                  changes['employee_name'] = {'old': record_to_edit.employee_name, 'new': new_name}
                  record_to_edit.employee_name = new_name


        if 'month_year' in updates and updates['month_year'] is not None:
             new_month_year_input = str(updates['month_year']).strip() # ПОКРАЩЕННЯ: Strip
             is_valid_month, month_year_formatted = validate_month_format(new_month_year_input) # validate_month_format робить strip/capitalize
             if not is_valid_month:
                  return f"Помилка редагування: {month_year_formatted}"
             if month_year_formatted.lower() != record_to_edit.month_year.lower():
                 if any(r.employee_name.lower() == record_to_edit.employee_name.lower() and r.month_year.lower() == month_year_formatted.lower() and r.id != record_to_edit.id for r in self.monthly_records):
                      return f"Помилка редагування: Дані за {month_year_formatted} для працівника {record_to_edit.employee_name} уже існують!"
                 changes['month_year'] = {'old': record_to_edit.month_year, 'new': month_year_formatted}
                 record_to_edit.month_year = month_year_formatted


        if 'level' in updates and updates['level'] is not None:
             new_level = str(updates['level']).strip().capitalize() # ПОКРАЩЕННЯ: Strip та Capitalize
             if new_level not in EMPLOYEE_LEVELS:
                  return f"Помилка редагування: Невірний рівень '{new_level}'. Допустимі: {', '.join(EMPLOYEE_LEVELS)}"
             if new_level != record_to_edit.level:
                  changes['level'] = {'old': record_to_edit.level, 'new': new_level}
                  record_to_edit.level = new_level


        if 'actual_hours' in updates and updates['actual_hours'] is not None:
             try:
                 new_hours = float(str(updates['actual_hours']).strip()) # ПОКРАЩЕННЯ: Strip
                 if new_hours < 0:
                     return "Помилка редагування: Відпрацьовані години не можуть бути від'ємними!"
                 if new_hours != record_to_edit.actual_hours:
                     changes['actual_hours'] = {'old': record_to_edit.actual_hours, 'new': new_hours}
                     record_to_edit.actual_hours = new_hours
             except (ValueError, TypeError):
                 return "Помилка редагування: Відпрацьовані години мають бути числом!"

        if 'tasks_completed_value' in updates and updates['tasks_completed_value'] is not None:
             try:
                 new_tasks_value = float(str(updates['tasks_completed_value']).strip()) # ПОКРАЩЕННЯ: Strip
                 if new_tasks_value < 0:
                     return "Помилка редагування: Вартість виконаних завдань не може бути від'ємною!"
                 if new_tasks_value != record_to_edit.tasks_completed_value:
                     changes['tasks_completed_value'] = {'old': record_to_edit.tasks_completed_value, 'new': new_tasks_value}
                     record_to_edit.tasks_completed_value = new_tasks_value
             except (ValueError, TypeError):
                 return "Помилка редагування: Вартість виконаних завдань має бути числом!"

        if 'usd_rate' in updates and updates['usd_rate'] is not None:
             try:
                 new_usd_rate = float(str(updates['usd_rate']).strip()) # ПОКРАЩЕННЯ: Strip
                 if new_usd_rate <= 0:
                     return "Помилка редагування: Курс долара не може бути від'ємним або нульовим!"
                 if new_usd_rate != record_to_edit.usd_rate:
                     changes['usd_rate'] = {'old': record_to_edit.usd_rate, 'new': new_usd_rate}
                     record_to_edit.usd_rate = new_usd_rate
             except (ValueError, TypeError):
                 return "Помилка редагування: Курс долара має бути числом!"

        if 'eur_rate' in updates and updates['eur_rate'] is not None:
             try:
                 new_eur_rate = float(str(updates['eur_rate']).strip()) # ПОКРАЩЕННЯ: Strip
                 if new_eur_rate <= 0:
                     return "Помилка редагування: Курс євро не може бути від'ємним або нульовим!"
                 if new_eur_rate != record_to_edit.eur_rate:
                     changes['eur_rate'] = {'old': record_to_edit.eur_rate, 'new': new_eur_rate}
                     record_to_edit.eur_rate = new_eur_rate
             except (ValueError, TypeError):
                 return "Помилка редагування: Курс євро має бути числом!"

        if changes:
            old_salary = record_to_edit.calculated_salary_uah
            record_to_edit.calculated_salary_uah = self.calculate_salary_value(
                 record_to_edit.level,
                 record_to_edit.actual_hours,
                 record_to_edit.tasks_completed_value
            )
            if old_salary is None or abs(old_salary - record_to_edit.calculated_salary_uah) > 0.01:
                 changes['calculated_salary_uah'] = {'old': old_salary, 'new': record_to_edit.calculated_salary_uah}

            record_to_edit.add_history_entry(changes)
            self._save_data()
            return record_to_edit
        else:
            return "Змін не внесено."

    def get_record_details_string(self, record):
         """Форматує деталі одного запису про зарплату у рядок."""
         if not isinstance(record, MonthlySalaryRecord):
              return "Помилка: Передано некоректний об'єкт запису."

         details = [
             f"--- Запис #{record.id} ---",
             f"  Працівник: {record.employee_name}",
             f"  Місяць: {record.month_year}",
             f"  Рівень: {record.level}",
             f"  Відпрацьовані години: {record.actual_hours:.2f}",
             f"  Вартість виконаних завдань: {record.tasks_completed_value:.2f} грн",
             f"  Курс долара: {record.usd_rate:.2f} грн",
             f"  Курс євро: {record.eur_rate:.2f} грн",
             f"  Зарплата: {format_salary(record.calculated_salary_uah, record.usd_rate, record.eur_rate) if record.calculated_salary_uah is not None else 'Не розраховано'}",
             f"  Дата додавання: {record.date_added}",
         ]

         if record.history:
              details.append("  Історія змін:")
              for entry in record.history:
                   timestamp = entry.get('timestamp', 'Невідома дата')
                   changes_list = [f"{key}: '{val.get('old', 'N/A')}' -> '{val.get('new', 'N/A')}'" for key, val in entry.get('changes', {}).items()]
                   details.append(f"    - {timestamp}: {', '.join(changes_list)}")
         details.append("-" * 30)
         return "\n".join(details)


    def get_all_salary_records(self, sort_by='month', year_filter=None):
        """Повертає список записів, відфільтрованих та відсортованих."""
        if not self.monthly_records:
            return []

        filtered_records = self.monthly_records
        if year_filter:
            try:
                year_str = str(int(year_filter))
                filtered_records = [r for r in self.monthly_records if r.month_year.split()[-1] == year_str]
            except ValueError:
                 return []


        if not filtered_records:
             return []

        if sort_by == 'month':
            sorted_records = sorted(filtered_records, key=lambda r: month_to_tuple(r.month_year))
        elif sort_by == 'salary':
            sorted_records = sorted(filtered_records, key=lambda r: r.calculated_salary_uah if r.calculated_salary_uah is not None else -1, reverse=True)
        elif sort_by == 'employee':
             sorted_records = sorted(filtered_records, key=lambda r: (r.employee_name.lower(), month_to_tuple(r.month_year)))
        else:
            sorted_records = filtered_records

        return sorted_records

    def get_salary_report_by_month(self, month_year):
        """Повертає список записів за конкретний місяць."""
        if not self.monthly_records:
            return "Дані відсутні."

        is_valid, month_year_formatted = validate_month_format(month_year)
        if not is_valid:
            return month_year_formatted

        found_records = [r for r in self.monthly_records if r.month_year.lower() == month_year_formatted.lower()]

        if not found_records:
            return f"Дані за {month_year_formatted} не знайдено!"

        sorted_records = sorted(found_records, key=lambda r: r.employee_name.lower())

        return sorted_records


    def get_total_salary_report_by_year(self, year):
        """Обчислює загальну зарплату за рік."""
        if not self.monthly_records:
            return "Дані відсутні."

        try:
             year_str = str(int(year))
        except (ValueError, TypeError):
             return "Помилка: Будь ласка, введіть коректний рік (число)."

        year_records = [r for r in self.monthly_records if r.month_year.split()[-1] == year_str and r.calculated_salary_uah is not None]

        if not year_records:
            return f"Дані за {year_str} рік не знайдено!"

        total_salary = sum(r.calculated_salary_uah for r in year_records)

        avg_usd_rate = sum(r.usd_rate for r in year_records) / len(year_records) if year_records else self.settings.default_rates.get("USD", 1.0)
        avg_eur_rate = sum(r.eur_rate for r in year_records) / len(year_records) if year_records else self.settings.default_rates.get("EUR", 1.0)

        return {
            'year': year_str,
            'record_count': len(year_records),
            'total_salary_uah': total_salary,
            'average_usd_rate': avg_usd_rate,
            'average_eur_rate': avg_eur_rate,
            'formatted_total': format_salary(total_salary, avg_usd_rate, avg_eur_rate)
        }

    def get_average_salary_report_by_year(self, year):
        """Обчислює середню зарплату за місяць за рік."""
        if not self.monthly_records:
            return "Дані відсутні."

        try:
             year_str = str(int(year))
        except (ValueError, TypeError):
             return "Помилка: Будь ласка, введіть коректний рік (число)."


        year_records = [r for r in self.monthly_records if r.month_year.split()[-1] == year_str and r.calculated_salary_uah is not None]

        if not year_records:
            return f"Дані за {year_str} рік не знайдено!"

        total_salary = sum(r.calculated_salary_uah for r in year_records)
        average_salary = total_salary / len(year_records) if len(year_records) > 0 else 0

        avg_usd_rate = sum(r.usd_rate for r in year_records) / len(year_records) if len(year_records) > 0 else self.settings.default_rates.get("USD", 1.0)
        avg_eur_rate = sum(r.eur_rate for r in year_records) / len(year_records) if len(year_records) > 0 else self.settings.default_rates.get("EUR", 1.0)


        return {
            'year': year_str,
            'record_count': len(year_records),
            'average_salary_uah': average_salary,
            'average_usd_rate': avg_usd_rate,
            'average_eur_rate': avg_eur_rate,
            'formatted_average': format_salary(average_salary, avg_usd_rate, avg_eur_rate)
        }

    # --- Методи для управління налаштуваннями ---

    def get_settings_string(self):
         """Повертає поточні налаштування у форматованому рядку."""
         settings_str = "--- Поточні налаштування ---\n"
         settings_str += "\nБазові ставки за рівнями (грн):"
         for level, amount in self.settings.base_amounts.items():
              settings_str += f"\n  {level}: {amount:.2f} грн"

         settings_str += "\n\nКоефіцієнти за рівнями:"
         for level, coeff in self.settings.coefficients.items():
              settings_str += f"\n  {level}: {coeff:.2f}"

         settings_str += "\n\nВартість типів завдань (грн):"
         if self.settings.task_costs:
            for task_type, cost in self.settings.task_costs.items():
                 settings_str += f"\n  '{task_type}': {cost:.2f} грн"
         else:
            settings_str += "\n  (Немає визначених типів завдань)"

         settings_str += f"\n\nСтандартна кількість робочих годин на місяць: {self.settings.standard_monthly_hours:.2f}"

         settings_str += "\n\nКурси валют за замовчуванням:"
         settings_str += f"\n  1 USD = {self.settings.default_rates.get('USD', 0):.2f} грн"
         settings_str += f"\n  1 EUR = {self.settings.default_rates.get('EUR', 0):.2f} грн"
         settings_str += "\n" + "-" * 30
         return settings_str

    def edit_base_amount_setting(self, level, amount):
         result = self.settings.update_base_amount(level, amount)
         if result.startswith("Базова ставка"):
             self._save_data()
         return result

    def edit_coefficient_setting(self, level, coefficient):
         result = self.settings.update_coefficient(level, coefficient)
         if result.startswith("Коефіцієнт"):
             self._save_data()
         return result

    def edit_task_cost_setting(self, task_type, cost):
         result = self.settings.update_task_cost(task_type, cost)
         if result.startswith("Вартість завдання") and not result.startswith("Помилка"):
             self._save_data()
         return result

    def delete_task_cost_setting(self, task_type):
         result = self.settings.delete_task_cost(task_type)
         if result.startswith("Вартість завдання") and not result.startswith("Помилка"):
             self._save_data()
         return result

    def edit_standard_hours_setting(self, hours):
         result = self.settings.update_standard_hours(hours)
         if result.startswith("Стандартна кількість"):
             self._save_data()
         return result

    def edit_default_rates_setting(self, usd_rate, eur_rate):
         result = self.settings.update_default_rates(usd_rate, eur_rate)
         if result.startswith("Курси валют"):
             self._save_data()
         return result
