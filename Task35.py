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
        res = [-1] * len(self.data)
        for day in range(len(self.data)):
            res[day] = self.data[day][0]
            if day > self.data[day][1]:
                total_fine += self.data[day][2]

        return res, total_fine

    def optim(self):
        ans = [-1] * self.size
        no_time = []
        total_fine = 0
        uf = UnionFind(self.data)
        for id, deadline, fine in uf.data:
            if ans[deadline] == -1:
                ans[deadline] = id
                uf.rank[deadline] = deadline
                if deadline - 1 != -1 and ans[deadline - 1] != -1:
                    uf.union(deadline, deadline - 1)
                if deadline + 1 != self.size and ans[deadline + 1] != -1:
                    uf.union(deadline, deadline + 1)
            else:
                if uf.rank[deadline] != 0:
                    ans[deadline - 1] = id
                    uf.rank[deadline - 1] = deadline - 1
                    uf.union(deadline - 1, deadline)
                    if deadline - 2 != -1 and ans[deadline - 2] != -1:
                        uf.union(deadline - 2, deadline - 1)
                else:
                    total_fine += fine
                    no_time.append(id)
            # print(id, deadline, fine, ans, total_fine)

        return ans[:self.size - len(no_time)] + no_time, total_fine

        # for id, deadline, fine in self.data:
        #     if self.res[deadline] == -1:
        #         self.res[deadline] = id
        #     else:
        #         deadline -= 1
        #         while deadline != -1:
        #             if self.res[deadline] == -1:
        #                 self.res[deadline] = id
        #                 break
        #             deadline -= 1
        #         if deadline == -1:
        #             total_fine += fine
        #             deadline = self.size - 1
        #             while deadline:
        #                 if self.res[deadline] == -1:
        #                     self.res[deadline] = id
        #                     break
        #                 deadline -= 1
        #
        # return self.res, total_fine


test1 = [[0, 2, 25], [1, 3, 10], [2, 0, 30], [3, 2, 50], [4, 2, 20]]
test2 = [[0, 3, 80], [1, 3, 100], [2, 1, 90], [3, 0, 95], [4, 2, 40]]
test3 = [[0, 1, 40], [1, 1, 70], [2, 1, 60], [3, 0, 30], [4, 3, 55]]


sol = Solution(test1)

print(sol.naive(), sol.optim())
