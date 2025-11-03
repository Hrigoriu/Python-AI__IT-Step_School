"""
Завдання 1
Реалізуйте базу даних зі штрафами податкової інспекції.
Ідентифікувати кожну конкретну людину буде
персональний ідентифікаційний код.
В однієї людини може бути багато штрафів.
Реалізуйте:
1. Повний друк бази даних;
2. Друк даних за конкретним кодом;
3. Друк даних за конкретним типом штрафу;
4. Друк даних за конкретним містом;
5. Додавання нової людини з інформацією про неї;
6. Додавання нових штрафів для вже існуючого запису;
7. Видалення штрафу;
8. Заміна інформації про людину та її штрафи.
Використайте дерево для реалізації цього завдання.
"""
import uuid  # Будемо використовувати для унікальних ID штрафів

class Fine: #Клас, що представляє штраф
    def __init__(self, fine_type: str, amount: float):
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного штрафу
        self.type = fine_type
        self.amount = amount

    def __str__(self):
        return f'  - Тип: {self.type}, Сума: {self.amount} грн (ID: {self.id})'


class Person:   #Клас, що представляє людину з її штрафами
    def __init__(self, pic: int, name: str, city: str):
        if not isinstance(pic, int):
            raise TypeError('Персональний ідентифікаційний код має бути числом.')
        self.pic = pic  # Персональний ідентифікаційний код (ПІК)
        self.name = name
        self.city = city
        self.fines: list[Fine] = []

    def add_fine(self, fine_type: str, amount: float):  #Метод, який додає новий штраф
        self.fines.append(Fine(fine_type, amount))
        print(f'Додано новий штраф для {self.name} (ПІК: {self.pic}).')

    def __str__(self):
        fines_str = '\n'.join(map(str, self.fines)) if self.fines else ' - Штрафів немає'
        return (f'ПІК: {self.pic}, Ім\'я: {self.name}, Місто: {self.city}\n'
                f' Штрафи:\n{fines_str}')


class TaxNode:  #Дерево податкової бази даних
    def __init__(self, person: Person):
        self.person = person
        self.left = None
        self.right = None


class TaxDatabase:  #Клас бази даних податкової інспекції
    def __init__(self):
        self.root = None

#5. Додавання нової людини
    def add_person(self, pic: int, name: str, city: str):   #Метод, який створює новий запис про людину в базі даних.
        person = Person(pic, name, city)
        if not self.root:
            self.root = TaxNode(person)
            print(f'Створено запис для {name} (ПІК: {pic}). База даних була порожньою.')
        else:
            self._insert_node(self.root, person)

    def _insert_node(self, current_node: TaxNode, person: Person):
        if person.pic < current_node.person.pic:
            if current_node.left:
                self._insert_node(current_node.left, person)
            else:
                current_node.left = TaxNode(person)
                print(f'Створено запис для {person.name} (ПІК: {person.pic}).')
        elif person.pic > current_node.person.pic:
            if current_node.right:
                self._insert_node(current_node.right, person)
            else:
                current_node.right = TaxNode(person)
                print(f'Створено запис для {person.name} (ПІК: {person.pic}).')
        else:
            print(f'Помилка: Людина з ПІК {person.pic} вже існує в базі даних.')

    def _find_node(self, pic: int) -> TaxNode | None:   #Приватний метод для пошуку за ПІК
        current_node = self.root
        while current_node:
            if pic == current_node.person.pic:
                return current_node
            elif pic < current_node.person.pic:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

#6. Додавання нових штрафів для вже існуючого запису
    def add_fine_to_person(self, pic: int, fine_type: str, amount: float):  #Метод, який додає штраф для людини за її ПІК
        node_to_update = self._find_node(pic)
        if node_to_update:
            node_to_update.person.add_fine(fine_type, amount)
        else:
            print(f'Помилка: Людину з ПІК {pic} не знайдено.')

#7. Видалення штрафу
    def delete_fine(self, pic: int, fine_id: str):  #Метод, який видаляє конкретний штраф у людини за ПІК та ID штрафу
        person_node = self._find_node(pic)
        if not person_node:
            print(f'Помилка: Людину з ПІК {pic} не знайдено.')
            return

        fine_to_delete = None
        for fine in person_node.person.fines:
            if fine.id == fine_id:
                fine_to_delete = fine
                break

        if fine_to_delete:
            person_node.person.fines.remove(fine_to_delete)
            print(f'Штраф з ID {fine_id} видалено для людини з ПІК {pic}.')
        else:
            print(f'Помилка: Штраф з ID {fine_id} не знайдено для людини з ПІК {pic}.')

#8. Заміна інформації про людину
    def update_person_info(self, pic: int, new_name: str = None, new_city: str = None):
        person_node = self._find_node(pic)
        if not person_node:
            print(f'Помилка: Людину з ПІК {pic} не знайдено.')
            return

        if new_name:
            person_node.person.name = new_name
        if new_city:
            person_node.person.city = new_city
        print(f'Інформацію для людини з ПІК {pic} оновлено.')


#1. Повний друк бази даних
    def print_all(self):    #Метод, який друкує всю базу даних
        print('\n--- Повний друк бази даних ---')
        if not self.root:
            print('База даних порожня.')
            return
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: TaxNode):
        if node:
            self._inorder_traversal(node.left)
            print('=' * 40)
            print(node.person)
            self._inorder_traversal(node.right)

#2. Друк даних за конкретним кодом
    def find_by_pic(self, pic: int):    #Метод, який шукає та друкує інформацію про людину за її ПІК
        print(f'\n--- Пошук за ПІК: {pic} ---')
        node = self._find_node(pic)
        if node:
            print(node.person)
        else:
            print('Людину з таким ПІК не знайдено.')

    def _collect_all_nodes(self, node, nodes_list):
        if node:
            nodes_list.append(node)
            self._collect_all_nodes(node.left, nodes_list)
            self._collect_all_nodes(node.right, nodes_list)

#3. Друк даних за конкретним типом штрафу
    def find_by_fine_type(self, fine_type: str):    #Метод, який шукає та друкує всіх людей, що мають штраф певного типу
        print(f'\n--- Пошук за типом штрафу: "{fine_type}" ---')
        all_nodes = []
        self._collect_all_nodes(self.root, all_nodes)

        found = False
        for node in all_nodes:
            if any(fine.type.lower() == fine_type.lower() for fine in node.person.fines):
                print('-' * 20)
                print(node.person)
                found = True
        if not found:
            print(f'Не знайдено людей зі штрафом типу "{fine_type}".')

#4. Друк даних за конкретним містом
    def find_by_city(self, city: str):  #Метод, який шукає та друкує всіх людей з певного міста
        print(f'\n--- Пошук за містом: "{city}" ---')
        all_nodes = []
        self._collect_all_nodes(self.root, all_nodes)

        found = False
        for node in all_nodes:
            if node.person.city.lower() == city.lower():
                print('-' * 20)
                print(node.person)
                found = True
        if not found:
            print(f'Не знайдено людей з міста "{city}".')


if __name__ == '__main__':
    db = TaxDatabase()

    print('=== Крок 1: Наповнення бази даних (Підпункт 5) ===')
    db.add_person(12345678, 'Іваненко Іван', 'Київ')
    db.add_person(87654321, 'Петренко Петро', 'Львів')
    db.add_person(55555555, 'Сидоренко Сидір', 'Одеса')
    db.add_person(11112222, 'Коваленко Марія', 'Львів')
    db.add_person(12345678, 'Дублікат Іван', 'Харків')  #дублікат (провірка, що буде)

    print('\n=== Крок 2: Додавання штрафів (Підпункт 6) ===')
    db.add_fine_to_person(12345678, 'Затримка подання декларації', 1700.0)
    db.add_fine_to_person(12345678, 'Несплата податку', 5500.50)
    db.add_fine_to_person(87654321, 'Затримка подання декларації', 1700.0)
    db.add_fine_to_person(99999999, 'Помилка', 100.0)  #неіснуюча людина (провірка, що буде)

    print('\n=== Крок 3: Повний друк бази (Підпункт 1) ===')
    db.print_all()

    print('\n=== Крок 4: Пошук за різними критеріями (Підпункти 2, 3, 4) ===')
    db.find_by_pic(87654321)
    db.find_by_pic(11111111)  # Неіснуючий (провірка, що буде)
    db.find_by_city('Львів')
    db.find_by_fine_type('Затримка подання декларації')
    db.find_by_fine_type('Перевищення швидкості')  # Неіснуючий тип (провірка, що буде)

    print('\n=== Крок 5: Видалення штрафу (Підпункти 7) ===')
    print('Штрафи Іваненка до видалення:')
    node_ivanenko = db._find_node(12345678)
    if node_ivanenko:
        print(node_ivanenko.person)
        if node_ivanenko.person.fines:
            fine_id_to_delete = node_ivanenko.person.fines[0].id
            db.delete_fine(12345678, fine_id_to_delete)
        else:
            print('У Іваненка немає штрафів для видалення.')

    print('\nШтрафи Іваненка після видалення:')
    db.find_by_pic(12345678)

    print('\n=== Крок 6: Оновлення інформації про людину (Підпункти 8) ===')
    db.update_person_info(87654321, new_city='Харків', new_name='Петренко Павло')
    print('\nДані про Петренка після оновлення:')
    db.find_by_pic(87654321)
