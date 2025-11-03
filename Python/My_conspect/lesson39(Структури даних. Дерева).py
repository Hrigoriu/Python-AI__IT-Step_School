# Дерева

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # ліва частина (всі елементи, що менші)
        self.right = None  # права частина (всі елементи, що більші)


class BinaryTree:
    def __init__(self):
        self.root = None  # початок дерева

    def insert(self, value):
        if not self.root:  # якщо дерево порожнє
            self.root = TreeNode(value)  # робимо його початок
        else:
            self.__insert(self.root, value)

    def __insert(self, node: TreeNode, value):  # node - поточна гілка, value - нове значення
        if value > node.value:  # якщо наше нове значення більше за значення в поточній гілці
            if node.right:  # якщо правий елемент є - рухаємось далі вправо
                self.__insert(node.right, value)
            else:  # якщо правого елементу немає
                node.right = TreeNode(value)    #рухаємося вліво
        else:  # якщо значення менше
            if node.left:
                self.__insert(node.left, value)
            else:
                node.left = TreeNode(value)

    def inorder_traversal(self):  # друк всього дерева
        return self.__inorder_traversal(self.root)

    def __inorder_traversal(self, node: TreeNode):
        result = []
        if node:
            result = self.__inorder_traversal(node.left)
            result.append(node.value)
            result.extend(self.__inorder_traversal(node.right))
        return result

    def search(self, value):  # Реалізуйте метод, який шукає value у дереві
        return self.__search(self.root, value)

    def __search(self, node: TreeNode, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value > node.value:
            return self.__search(node.right, value)
        else:
            return self.__search(node.left, value)

tree = BinaryTree()

tree.insert(10)
tree.insert(15)
tree.insert(9)
tree.insert(-1)
tree.insert(3)
tree.insert(21)
tree.insert(30)
tree.insert(17)
tree.insert(12)
tree.insert(5)

print(tree.inorder_traversal())

print(tree.search(12))
print(tree.search(35))
print(tree.search(-1))
print(tree.search(2))

"""
[-1, 3, 5, 9, 10, 12, 15, 17, 21, 30]
True
False
True
False
"""
#=========================================================================
"""
stack = [1, 2, 3]
stack.append(4)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
"""
import queue

# Stack: Останній зайшов - перший вийшов (LIFO) Last in-First out
# Queue: Перший зайшов - перший вийшов (FIFO)   First in-First out

def recursive_counter(n: int):
    if n <= 0:
        return
    print(n)
    return recursive_counter(n - 1)
recursive_counter(10)
print('END')
#--------------------------------------

q = queue.Queue()  # створюємо чергу
q.put(10)  # перший зайшов
q.put(20)  # другий зайшов
q.put(30)  # третій зайшов
print(q.get())#10

stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.get())#30
#-------------------------------

pr_q = queue.PriorityQueue()
pr_q.put(10)
pr_q.put(20)
pr_q.put(30)

#-------------------------------------------
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
"""
Елемент СУПЕР ВАЖЛИВЕ. Важливість: 1
Елемент Середня важливість 1. Важливість: 2
Елемент Середня важливість 2. Важливість: 2
Елемент Не важливе. Важливість: 3
"""