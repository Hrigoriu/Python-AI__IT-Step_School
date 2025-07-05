    # Структури даних
from numpy.ma.core import append


# 1. ОДНОЗВ'ЯЗНИЙ СПИСОК
class SingleElement:  # клас елемента списку (композиція)
    def __init__(self, data):
        self.data = data  # значення елементу (value)
        self.next = None  # посилання на правий елемент (наступний)

    def __str__(self):
        return str(self.data)


class SingleLinkedList:  # клас однозв'язного списку
    def __init__(self):
        self.head = None

    def __len__(self):  # Завдання: повернути довжину списку
        counter = 0
        last_el = self.head
        while last_el:
            counter += 1
            last_el = last_el.next
        return counter

    def append(self, data):  # додавання нового елементу в кінець списку
        new_el = SingleElement(data)  # створюємо об'єкт SingleElement (композиція)
        if not self.head:  # якщо голова порожня
            self.head = new_el
            return  # ранній вихід
        last_el = self.head  # починаємо з голови
        while last_el.next:  # поки у елемента є наступний
            last_el = last_el.next  # знаходимо останній елемент
        last_el.next = new_el  # записуємо останньому елементу новий елемент у next

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        current_el = self.head  # зберігаємо поточний елемент (починаємо з HEAD)
        prev_el = None  # зберігаємо попередній елемент (у HEAD нема попереднього, тому None)
        while current_el and current_el.data != data:
            prev_el = current_el  # запам'ятовуємо попередній елемент як поточний
            current_el = current_el.next  # робимо поточний елемент наступним
        if not current_el:
            raise ValueError('Елемент не існує у списку!')
        prev_el.next = current_el.next
        del current_el

    def print_all(self):
        current_el = self.head
        print('HEAD ->', end=' ')
        while current_el:
            print(f'{current_el} ->', end=' ')
            current_el = current_el.next
        print('END')

l = SingleLinkedList()
print(len(l))

l.append(20)
l.append(30)
print(len(l))

l.append(40)
print(len(l))

l.print_all()
l.append(50)
l.print_all()

l.remove(40)
l.print_all()

"""
0
2
3
HEAD -> 20 -> 30 -> 40 -> END
HEAD -> 20 -> 30 -> 40 -> 50 -> END
HEAD -> 20 -> 30 -> 50 -> END
"""

#=====================================================================

# Структури даних

# 2. ДВОЗВ'ЯЗНИЙ СПИСОК
class DoubleElement:
    def __init__(self, data):
        self.data = data  # значення
        self.prev = None  # попередній елемент
        self.next = None  # наступний елемент

    def __str__(self):
        return str(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_el = DoubleElement(data)
        if not self.head:
            self.head = new_el
            return
        last_el = self.head
        while last_el.next:
            last_el = last_el.next
        last_el.next = new_el  # в НАСТУПНИЙ елемент останнього записуємо новий
        new_el.prev = last_el  # в ПОПЕРЕДНІЙ елемент нового записуємо останній

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        current_el = self.head  # зберігаємо поточний елемент (починаємо з HEAD)
        while current_el and current_el.data != data:
            current_el = current_el.next  # робимо поточний елемент наступним
        if not current_el:
            raise ValueError('Елемент не існує у списку!')
        prev_el = current_el.prev
        next_el = current_el.next
        prev_el.next = next_el
        if next_el:
            next_el.prev = prev_el
        del current_el

    def print_all(self):
        current = self.head
        print('HEAD')
        print('-------')
        while current:
            prev = current.prev
            next = current.next
            print(f'{prev} <- {current} -> {next}')
            print('-------')
            current = current.next
        print('END')


l = DoubleLinkedList()

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)

l.print_all()
l.remove(40)
l.print_all()
