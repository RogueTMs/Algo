from __future__ import annotations

import random
from itertools import cycle

random_cycle = cycle([random.randint(1, 100) for _ in range(1000)])


class Treap(object):
    def __init__(self, val):
        self.root = None
        self.priority = random.random()
        self.size = 1
        self.val = val
        self.sum = 0
        self.left = None
        self.right = None

    @staticmethod
    def _splitBySize(T: Treap, k) -> (Treap, Treap):
        if not T: return None, None

        if k <= T.root.left.size:
            LL, LR = Treap._splitBySize(T.left, k)
            T.left = LR
            T._update(T)
            return LL, T
        else:
            RL, RR = Treap._splitBySize(T.right, k - T.left.size - 1)
            T.right = RL
            T._update(T)
            return T, RR

    @staticmethod
    def _update(T: Treap):
        T.root.size = 1 + T.left.size + T.right.size

    @staticmethod
    def _merge(T1, T2: Treap) -> Treap:
        if not T1: return T2

        if not T2: return T1
        if T1.root.p < T2.root.p:
            T1.right = Treap._merge(T1.right, T2)
            return T1
        else:
            T2.left = Treap._merge(T1, T2.left)
            return T2

    def insert(self, val, pos):
        L, R = self._splitBySize(self, pos - 1)
        T = Treap(val)
        return Treap._merge(Treap._merge(L, T), R)

    def erase(self, pos):
        L, R = Treap._splitBySize(self, pos - 1)
        E, RR = Treap._splitBySize(R, 1)
        Treap._merge(L, RR)

    def sum(self, _from, to):
        L, R = self._splitBySize(self, _from - 1)
        RL, RR = self._splitBySize(R, to - _from + 1)
        return RL.sum


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t = build(a, 0, len(a))
t = insert(t, 0, 5)
t = erase(t, 0)
t = erase(t, 0, 3)
all_sum = sum(t, 0, 6)
print(all_sum)
