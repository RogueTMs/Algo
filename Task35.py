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

        if self.rank[a] < self.rank[b]:
            a, b = b, a

        self.nodes[b] = a

        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1


class Solution:
    def __init__(self, data):  # id, deadline, fine
        self.size = len(data)
        self.res = [-1] * self.size
        self.data = sorted(data, key=lambda x: x[2], reverse=True)

    def naive(self):
        total_fine = 0
        res = [-1] * len(self.data)
        for day in range(len(self.data)):
            res[day] = self.data[day][0]
            if day > self.data[day][1]:
                total_fine += self.data[day][2]

        return res, total_fine

    def optim(self):
        # ans = [-1] * len(self.data)
        # uf = UnionFind(self.data)
        # for id, deadline, fine in uf.data:

        total_fine = 0
        for id, deadline, fine in self.data:
            if self.res[deadline] == -1:
                self.res[deadline] = id
            else:
                deadline -= 1
                while deadline != -1:
                    if self.res[deadline] == -1:
                        self.res[deadline] = id
                        break
                    deadline -= 1
                if deadline == -1:
                    total_fine += fine
                    deadline = self.size - 1
                    while deadline:
                        if self.res[deadline] == -1:
                            self.res[deadline] = id
                            break
                        deadline -= 1

        return self.res, total_fine


test = [[0, 2, 25], [1, 3, 10], [2, 0, 30], [3, 2, 50], [4, 2, 20]]

sol = Solution(test)

print(sol.naive(), sol.optim())
