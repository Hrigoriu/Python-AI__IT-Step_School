import locale
import re
from constants import MONTHS

# --- Утиліти ---

def setup_locale():
    """Налаштовує локалізацію для коректного форматування чисел та валют."""
    try:
        # Спробуємо різні варіанти локалі для сумісності
        locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
        return "Локалізацію встановлено: uk_UA.UTF-8"
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'uk_UA')
            return "Локалізацію встановлено: uk_UA"
        except locale.Error:
             # Fallback до системної локалі, якщо українську не знайдено
             try:
                 locale.setlocale(locale.LC_ALL, '')
                 return "Не вдалося встановити локалізацію 'uk_UA.UTF-8' або 'uk_UA'. Використовується системна локалізація."
             except locale.Error:
                 return "Не вдалося встановити жодну локалізацію. Форматування може бути некоректним."


def validate_month_format(month_str):
    """Перевіряє, чи відповідає введений місяць формату 'Місяць Рік'."""
    if not isinstance(month_str, str):
         return False, "Введене значення не є текстом."

    month_str = month_str.strip()
    pattern = rf"^([А-Яа-яІіЄєЇї\w]+)\s+(\d{{4}})$"
    match = re.match(pattern, month_str, re.IGNORECASE)

    if not match:
        return False, "Місяць має бути у форматі 'Місяць Рік' (наприклад, 'Січень 2024')!"

    month_name, year_str = match.groups()

    month_name_capitalized = month_name.capitalize()
    if month_name_capitalized not in MONTHS:
        return False, f"Місяць має бути одним із: {', '.join(MONTHS)}!"

    try:
        year = int(year_str)
        if year < 2022 or year > 2100:
            return False, "Рік має бути між 2022 і 2100!"
    except ValueError:
        return False, "Рік має бути числом (наприклад, 2024)!"

    return True, f"{month_name_capitalized} {year_str}"

def month_to_tuple(month_year_str):
    """Перетворює місяць у формат (рік, номер місяця) для хронологічного сортування."""
    if not isinstance(month_year_str, str):
        return 0, 0

    parts = month_year_str.split()
    if len(parts) != 2:
        return 0, 0

    month_name, year_str = parts
    try:
        year = int(year_str)
        month_num = MONTHS.index(month_name) + 1
        return year, month_num
    except (ValueError, IndexError):
        try:
            year = int(year_str)
            return year, 0
        except ValueError:
            return 0, 0


def format_salary(amount, usd_rate, eur_rate):
    """Форматує зарплату у гривнях, доларах і євро."""
    usd = amount / usd_rate if usd_rate and usd_rate > 0 else 0
    eur = amount / eur_rate if eur_rate and eur_rate > 0 else 0

    try:
         formatted_uah = locale.format_string("%.2f", float(amount), grouping=True).replace(',', ' ')
         formatted_usd = locale.format_string("%.2f", float(usd), grouping=True).replace(',', ' ')
         formatted_eur = locale.format_string("%.2f", float(eur), grouping=True).replace(',', ' ')

         return f"{formatted_uah} грн ({formatted_usd} USD / {formatted_eur} EUR)"
    except Exception as e:
         print(f"Помилка форматування локалі: {e}. Використання резервного формату.")
         return f"{amount:.2f} грн ({usd:.2f} USD / {eur:.2f} EUR)"

LOCALE_SETUP_MESSAGE = setup_locale()
