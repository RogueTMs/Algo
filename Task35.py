"""
LeetCode: None
Task: построить максимальное (и самое дорогое) выполнимое множество задач
Input: [[id, deadline, fine], ...]
Output: Tasks sequence, total fine
"""


class UnionFind:
    def __init__(self, data):
        size = len(data)
        self.nodes = [x for x in range(size)]  # 0, ... , size-1
        self.rank = [0] * size

    def find(self, x):  # -> класс эквивалентности
        if self.nodes[x] != x:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]
        else:
            return x

    def union(self, x, y):  # объединяет два класса эквивалентности
        a = self.find(x)
        b = self.find(y)
        if self.rank[a] < self.rank[b]:
            a, b = b, a

        self.nodes[a] = b
        if self.rank[b] == self.rank[a]:
            self.rank[b] += 1


class Solution:
    def __init__(self, data):  # id, deadline, fine
        self.size = len(data)
        self.data = sorted(data, key=lambda x: x[2], reverse=True)  # sorted by fine

    def naive(self):
        total_fine = 0
        res = [-1] * self.size
        for i in range(self.size):
            task = self.data[i]
            res[i] = task[0]
            if i < task[1]:
                total_fine += task[2]
        return res, total_fine

    def optim(self):
        union_find = UnionFind(self.data)
        res = [-1] * self.size
        total_fine = 0

        for task in self.data:
            equivalence_class = union_find.find(task[1])
            union_find.union(equivalence_class, equivalence_class - 1)
            res[equivalence_class] = task[0]
            if equivalence_class > task[1]:
                total_fine += task[2]

        return res, total_fine


# id, deadline, fine
test1 = [['A', 2, 25], ['B', 3, 10], ['C', 0, 30], ['D', 2, 50], ['E', 2, 20]]
test2 = [[0, 3, 80], [1, 3, 100], [2, 1, 90], [3, 0, 95], [4, 2, 40]]
test3 = [[0, 1, 40], [1, 1, 70], [2, 1, 60], [3, 0, 30], [4, 3, 55]]

tests = [test1, test2, test3]
for test in tests:
    sol = Solution(test)
    print(sol.naive(), sol.optim())
