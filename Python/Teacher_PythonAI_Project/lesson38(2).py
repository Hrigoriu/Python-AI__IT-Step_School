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
