from collections import namedtuple
from timeit import default_timer as timer
from datetime import timedelta


class UnionFind:
    def __init__(self, data):
        self.size = len(data)
        self.nodes = [x for x in range(self.size)]
        self.rank = [0] * self.size
        self.data = data

    def find(self, x):
        if self.nodes[x] != x:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]
        else:
            return x

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)

        if self.rank[a] > self.rank[b]:
            a, b = b, a

        self.nodes[a] = b

        self.rank[b] = self.rank[a]


class Solution:
    def __init__(self, data):  # id, deadline, fine
        self.size = len(data)
        self.data = sorted(data, key=lambda x: x[2], reverse=True)

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
            index = union_find.find(task[1] - 1)
            union_find.union(index, index - 1)
            res[index] = task[0]
            if index > task[1]:
                total_fine += task[2]

        return res, total_fine


# id, deadline, fine
test1 = [['A', 3, 25], ['B', 4, 10], ['C', 1, 30], ['D', 3, 50], ['E', 3, 20]]
test2 = [[0, 4, 80], [1, 4, 100], [2, 2, 90], [3, 1, 95], [4, 3, 40]]
test3 = [[0, 2, 40], [1, 2, 70], [2, 2, 60], [3, 1, 30], [4, 4, 55]]

tests = [test1, test2, test3]
for test in tests:
    sol = Solution(test)
    print(sol.naive(), sol.optim())
