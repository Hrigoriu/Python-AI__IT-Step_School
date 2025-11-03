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
                node.right = TreeNode(value)
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
