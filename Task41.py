import random


class Node:
    def __init__(self, value):
        self.value = value
        self.priority = random.random()
        self.size = 1
        self.left = None
        self.right = None


class ImplicitTreap:
    def __init__(self):
        self.root = None

    def build(self, array):
        for i in range(len(array)):
            self.insert(i, array[i])

    def sum(self, _from, _to):
        left, mid = self._split_by_size(self.root, _from - 1)
        mid, right = self._split_by_size(mid, _to - _from)
        total_sum = self._get_sum(mid)
        self.root = self._merge(left, self._merge(mid, right))
        return total_sum

    def insert(self, pos, value):
        left, right = self._split_by_size(self.root, pos - 1)
        new_node = Node(value)
        self.root = self._merge(self._merge(left, new_node), right)

    def erase(self, pos):
        left, right = self._split_by_size(self.root, pos)
        e, r = self._split_by_size(right, 1)
        self._merge(left, r)

    def erase_region(self, pos, count):
        left, right = self._split_by_size(self.root, pos - 1)
        e, r = self._split_by_size(right, count)
        self._merge(left, r)

    def _merge(self, left, right):
        if not left or not right:
            return left if not right else right

        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            _update_size(left)
            return left
        else:
            right.left = self._merge(left, right.left)
            _update_size(right)
            return right

    def _split_by_size(self, node, index):
        if not node:
            return None, None

        if index <= _size(node.left):
            left, right = self._split_by_size(node.left, index)
            node.left = right
            _update_size(node)
            return left, node
        else:
            left, right = self._split_by_size(node.right, index - _size(node.left) - 1)
            node.right = left
            _update_size(node)
            return node, right

    def _get_sum(self, node):
        return node.value + self._get_sum(node.left) + self._get_sum(node.right) if node else 0


def _size(node):
    return node.size if node else 0


def _update_size(node):
    if node:
        node.size = _size(node.left) + _size(node.right) + 1


# tests

treap = ImplicitTreap()

initial_array = [1, 2, 3, 4, 5]
treap.build(initial_array)
print(initial_array)

from_idx, to_idx = 2, 4
sum_result = treap.sum(from_idx, to_idx)
print(sum_result)

new_value = 6
insert_index = 1
treap.insert(insert_index, new_value)
print(treap.sum(1, len(initial_array) - 1))

treap.erase(insert_index)
print(treap.sum(1, len(initial_array) - 1))

treap.erase_region(1, 2)
print(treap.sum(1, len(initial_array) - 1))
