from salary_manager import SalaryManager
from constants import DATABASE_FILE, EMPLOYEE_LEVELS
from utils import format_salary, LOCALE_SETUP_MESSAGE
from models import MonthlySalaryRecord # ВИПРАВЛЕННЯ: Імпортуємо MonthlySalaryRecord напряму

# --- Головна частина програми (CLI) ---

def main():
    """Головна функція програми, що управляє меню та взаємодією через консоль."""
    manager = SalaryManager(DATABASE_FILE) # Створюємо менеджер даних
    print(LOCALE_SETUP_MESSAGE) # Виводимо статус локалі
    # Рядок 14: Лінтер може показувати попередження тут через код всередині _load_data,
    # але саме створення словників там є коректним.
    print(f"Статус завантаження даних: {manager._load_data()}") # Виводимо статус завантаження

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
        print('13. Управління налаштуваннями')
        print('14. Вийти')
        print('\n' + '=' * 30)
        choice = input('Виберіть опцію: ').strip()
        print('*!' * 15)

        if choice == '1':
            # --- Додати запис ---
            print("\n--- Додати запис про зарплату ---")
            employee_name = input("Введіть ім'я працівника: ").strip()
            month_year = input("Введіть місяць (наприклад, 'Січень 2024'): ").strip()
            print(f"Допустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
            level = input("Введіть рівень працівника: ").strip()
            actual_hours = input("Введіть фактично відпрацьовані години: ").strip()
            tasks_completed_value = input("Введіть загальну вартість виконаних завдань: ").strip()
            # Курси валют можна ввести або залишити порожнім для дефолту
            last_record = next(iter(reversed(manager.monthly_records)), None) # Останній запис для підказки
            default_usd = last_record.usd_rate if last_record else manager.settings.default_rates.get("USD", 40.0)
            default_eur = last_record.eur_rate if last_record else manager.settings.default_rates.get("EUR", 43.0)

            usd_rate = input(f"Введіть курс долара (гривень за 1 USD, за замовчуванням {default_usd:.2f}, або Enter): ").strip()
            eur_rate = input(f"Введіть курс євро (гривень за 1 EUR, за замовчуванням {default_eur:.2f}, або Enter): ").strip()

            # Викликаємо метод менеджера і обробляємо його результат
            result = manager.add_salary_record(
                employee_name,
                month_year,
                level,
                actual_hours, # Передаємо як рядок, менеджер сконвертує і провалідує
                tasks_completed_value, # Передаємо як рядок
                usd_rate if usd_rate else None, # Передаємо None, якщо порожньо
                eur_rate if eur_rate else None  # Передаємо None, якщо порожньо
            )

            # ВИПРАВЛЕННЯ: Використовуємо імпортований MonthlySalaryRecord
            if isinstance(result, MonthlySalaryRecord):
                 print(f'\nЗапис #{result.id} за {result.month_year} для {result.employee_name} успішно додано!')
                 print(f"Розрахована зарплата: {format_salary(result.calculated_salary_uah, result.usd_rate, result.eur_rate)}")
            else:
                 print(f"\nПомилка додавання: {result}")

        elif choice == '2':
            # --- Видалити запис ---
            record_id_input = input("Введіть номер запису для видалення: ").strip()
            result = manager.delete_salary_record(record_id_input)

            # ВИПРАВЛЕННЯ: Використовуємо імпортований MonthlySalaryRecord
            if isinstance(result, MonthlySalaryRecord):
                 print(f'Запис #{result.id} за {result.month_year} для {result.employee_name} видалено!')
            else:
                 print(result) # Це повідомлення про помилку

        elif choice == '3':
             # --- Редагувати запис ---
            record_id_input = input("Введіть номер запису для редагування: ").strip()
            record_to_edit = manager.find_record_by_id(record_id_input)

            if not record_to_edit:
                 print(f"Запис із номером {record_id_input} не знайдено!")
                 continue # Повертаємось до головного меню

            print(manager.get_record_details_string(record_to_edit)) # Показуємо поточні дані

            print("\n--- Редагування запису (залиште порожнім, щоб не змінювати) ---")

            # Рядок 96: Лінтер може показувати попередження, але {} - це правильний спосіб
            updates = {}
            updates['employee_name'] = input(f"Введіть нове ім'я працівника (поточне: '{record_to_edit.employee_name}'): ").strip() or None
            updates['month_year'] = input(f"Введіть новий місяць (поточний: '{record_to_edit.month_year}'): ").strip() or None
            print(f"Допустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
            updates['level'] = input(f"Введіть новий рівень (поточний: '{record_to_edit.level}'): ").strip() or None
            updates['actual_hours'] = input(f"Введіть нові відпрацьовані години (поточне: '{record_to_edit.actual_hours:.2f}'): ").strip() or None
            updates['tasks_completed_value'] = input(f"Введіть нову загальну вартість завдань (поточне: '{record_to_edit.tasks_completed_value:.2f}'): ").strip() or None
            updates['usd_rate'] = input(f"Введіть новий курс долара (поточний: '{record_to_edit.usd_rate:.2f}'): ").strip() or None
            updates['eur_rate'] = input(f"Введіть новий курс євро (поточний: '{record_to_edit.eur_rate:.2f}'): ").strip() or None

            # Видаляємо None значення, щоб не намагатись оновити їх
            updates = {k: v for k, v in updates.items() if v is not None}

            if not updates:
                 print("Змін не внесено.")
                 continue # Повертаємось до головного меню

            result = manager.edit_salary_record(record_to_edit.id, updates)

            # ВИПРАВЛЕННЯ: Використовуємо імпортований MonthlySalaryRecord
            if isinstance(result, MonthlySalaryRecord):
                 print(f"\nДані для запису #{result.id} оновлено!")
                 print(f"Нова розрахована зарплата: {format_salary(result.calculated_salary_uah, result.usd_rate, result.eur_rate)}")
            else:
                 print(f"\nПомилка редагування: {result}")


        elif choice in ['4', '5', '6', '10', '11', '12']:
             # --- Показати/Фільтрувати записи ---
             sort_by = 'month' # Дефолтне сортування
             year_filter = None # Дефолтний фільтр відсутній

             if choice == '5': sort_by = 'salary'
             elif choice == '6': sort_by = 'employee'
             elif choice in ['10', '11', '12']:
                  year_filter = input("Введіть рік для фільтрації: ").strip()
                  if choice == '11': sort_by = 'salary'
                  elif choice == '12': sort_by = 'employee'

             records = manager.get_all_salary_records(sort_by=sort_by, year_filter=year_filter)

             if isinstance(records, str): # Якщо менеджер повернув повідомлення про помилку фільтрації (хоча get_all не повертає)
                  print(records)
             elif not records:
                 if year_filter:
                    print(f"Дані за {year_filter} рік не знайдено!")
                 else:
                    print("Дані відсутні.")
             else:
                  print("\n--- Усі записи про зарплату ---")
                  for record in records:
                      print(manager.get_record_details_string(record))
                  print("--- Кінець списку ---")

        elif choice == '7':
            # --- Показати зарплату за місяцем ---
            month_year_input = input("Введіть місяць для пошуку (наприклад, 'Січень 2024'): ").strip()
            result = manager.get_salary_report_by_month(month_year_input)

            if isinstance(result, str): # Повідомлення про помилку або відсутність даних
                 print(result)
            else: # Список об'єктів MonthlySalaryRecord
                 print(f"\n--- Записи за {result[0].month_year} ---") # result[0] безпечно, бо список не порожній
                 for record in result:
                      print(manager.get_record_details_string(record))
                 print("--- Кінець списку за місяць ---")

        elif choice == '8':
            # --- Показати загальну зарплату за рік ---
            year_input = input("Введіть рік для пошуку загальної зарплати: ").strip()
            result = manager.get_total_salary_report_by_year(year_input)

            if isinstance(result, str): # Повідомлення про помилку або відсутність даних
                 print(result)
            else: # Словник з результатом
                 print(f"\n--- Загальна зарплата за {result['year']} рік ---")
                 print(f"Всього записів за рік: {result['record_count']}")
                 print(f"Загальна сума: {result['formatted_total']}")
                 print("-" * 30)

        elif choice == '9':
            # --- Показати середню зарплату за рік ---
            year_input = input("Введіть рік для пошуку середньої зарплати: ").strip()
            result = manager.get_average_salary_report_by_year(year_input)

            if isinstance(result, str): # Повідомлення про помилку або відсутність даних
                 print(result)
            else: # Словник з результатом
                 print(f"\n--- Середня зарплата за місяць у {result['year']} році ---")
                 print(f"Розраховано на основі {result['record_count']} записів.")
                 print(f"Середня сума: {result['formatted_average']}")
                 print("-" * 30)

        elif choice == '13':
             # --- Управління налаштуваннями ---
             manage_settings_cli(manager) # Перехід у підменю налаштувань

        elif choice == '14':
            print('Дякую за використання програми! До побачення!')
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')

def manage_settings_cli(manager):
    """CLI підменю для управління налаштуваннями."""
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
             print(manager.get_settings_string())

        elif choice == '2':
             print("\n--- Редагування базових ставок ---")
             print("Поточні ставки:")
             for level, amount in manager.settings.base_amounts.items():
                  print(f"  {level}: {amount:.2f} грн")
             print(f"\nДопустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
             level_to_edit = input("Введіть рівень для редагування (або Enter для скасування): ").strip()
             if level_to_edit and level_to_edit in EMPLOYEE_LEVELS:
                  new_amount_input = input(f"Введіть нову базову ставку для '{level_to_edit}' (поточна: {manager.settings.base_amounts.get(level_to_edit, 0):.2f}, або Enter): ").strip()
                  if new_amount_input:
                       result = manager.edit_base_amount_setting(level_to_edit, new_amount_input)
                       print(result)
                  else:
                       print("Залишено без змін.")
             elif level_to_edit:
                  print(f"Невірний рівень '{level_to_edit}'.")
             else:
                  print("Редагування скасовано.")

        elif choice == '3':
             print("\n--- Редагування коефіцієнтів ---")
             print("Поточні коефіцієнти:")
             for level, coeff in manager.settings.coefficients.items():
                  print(f"  {level}: {coeff:.2f}")
             print(f"\nДопустимі рівні: {', '.join(EMPLOYEE_LEVELS)}")
             level_to_edit = input("Введіть рівень для редагування (або Enter для скасування): ").strip()
             if level_to_edit and level_to_edit in EMPLOYEE_LEVELS:
                  new_coeff_input = input(f"Введіть новий коефіцієнт для '{level_to_edit}' (поточний: {manager.settings.coefficients.get(level_to_edit, 1.0):.2f}, або Enter): ").strip()
                  if new_coeff_input:
                       result = manager.edit_coefficient_setting(level_to_edit, new_coeff_input)
                       print(result)
                  else:
                       print("Залишено без змін.")
             elif level_to_edit:
                  print(f"Невірний рівень '{level_to_edit}'.")
             else:
                  print("Редагування скасовано.")

        elif choice == '4':
             print("\n--- Редагування вартості типів завдань ---")
             print("Поточні типи завдань та їх вартість:")
             if manager.settings.task_costs:
                 for task_type, cost in manager.settings.task_costs.items():
                     print(f"  '{task_type}': {cost:.2f} грн")
             else:
                 print("  (Немає визначених типів завдань)")

             print("\nОпції: додати/редагувати тип (введіть назву), видалити тип (введіть 'видалити'), або Enter для скасування.")
             task_action = input("Введіть назву типу завдання або 'видалити': ").strip()

             if not task_action:
                  print("Редагування скасовано.")
             elif task_action.lower() == 'видалити':
                  task_to_delete = input("Введіть назву типу завдання для видалення: ").strip()
                  if task_to_delete:
                       result = manager.delete_task_cost_setting(task_to_delete)
                       print(result)
                  else:
                       print("Видалення скасовано.")
             else: # Додавання/редагування
                 task_type = task_action
                 current_cost = manager.settings.task_costs.get(task_type, 0)
                 new_cost_input = input(f"Введіть нову вартість для завдання '{task_type}' (поточна: {current_cost:.2f}, або Enter): ").strip()
                 if new_cost_input:
                      result = manager.edit_task_cost_setting(task_type, new_cost_input)
                      print(result)
                 else:
                      print("Залишено без змін.")


        elif choice == '5':
             print("\n--- Редагування стандартних годин ---")
             print(f"Поточна стандартна кількість годин: {manager.settings.standard_monthly_hours:.2f}")
             new_hours_input = input("Введіть нову стандартну кількість робочих годин на місяць (або Enter для скасування): ").strip()
             if new_hours_input:
                  result = manager.edit_standard_hours_setting(new_hours_input)
                  print(result)
             else:
                  print("Залишено без змін.")

        elif choice == '6':
             print("\n--- Редагування курсів валют за замовчуванням ---")
             print(f"Поточні курси: 1 USD = {manager.settings.default_rates.get('USD', 0):.2f} грн, 1 EUR = {manager.settings.default_rates.get('EUR', 0):.2f} грн")
             new_usd_input = input(f"Введіть новий курс долара (або Enter '{manager.settings.default_rates.get('USD', 0):.2f}'): ").strip()
             new_eur_input = input(f"Введіть новий курс євро (або Enter '{manager.settings.default_rates.get('EUR', 0):.2f}'): ").strip()

             # Передаємо порожній рядок або введене значення
             usd_rate = new_usd_input if new_usd_input else manager.settings.default_rates.get('USD', '0') # Передаємо поточне значення як рядок, якщо Enter
             eur_rate = new_eur_input if new_eur_input else manager.settings.default_rates.get('EUR', '0')

             result = manager.edit_default_rates_setting(usd_rate, eur_rate)
             print(result)


        elif choice == '7':
             print("Вихід з меню налаштувань.")
             break
        else:
             print('Невірний вибір. Спробуйте ще раз.')


# Точка входу для CLI
if __name__ == "__main__":
    main()
