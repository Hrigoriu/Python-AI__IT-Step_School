import queue


# Stack: Останній зайшов - перший вийшов (LIFO)
# Queue: Перший зайшов - перший вийшов (FIFO)

def recursive_counter(n: int):
    if n <= 0:
        return

    print(n)

    return recursive_counter(n - 1)


recursive_counter(10)
print('END')


q = queue.Queue()  # створюємо чергу

q.put(10)  # перший зайшов
q.put(20)  # другий зайшов
q.put(30)  # третій зайшов

print(q.get())

stack = queue.LifoQueue()

stack.put(10)
stack.put(20)
stack.put(30)

print(stack.get())

pr_q = queue.PriorityQueue()

pr_q.put(10)
pr_q.put(20)
pr_q.put(30)


class Queue:  # власна кастомна черга
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)


class PriorityQueueItem:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __str__(self):
        return f'Елемент {self.value}. Важливість: {self.priority}'


class PriorityQueue:
    def __init__(self):
        self.items: list[PriorityQueueItem] = []

    def is_empty(self):
        return len(self.items) == 0

    def put(self, value, priority):
        new_item = PriorityQueueItem(value, priority)

        self.items.append(new_item)
        self.items.sort(key=lambda el: el.priority)

    def get(self):
        return self.items.pop(0)


pr_q = PriorityQueue()

pr_q.put('Середня важливість 1', 2)
pr_q.put('Середня важливість 2', 2)

pr_q.put('СУПЕР ВАЖЛИВЕ', 1)

pr_q.put('Не важливе', 3)

for _ in range(4):
    print(pr_q.get())
