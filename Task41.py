import random
from itertools import cycle

random_cycle = cycle([random.randint(1, 100) for _ in range(1000)])


class Treap:
    def __init__(T, key):
        T.key = key
        T.prior = next(random_cycle)
        T.size = 1
        T.sum = key
        T.l = None
        T.r = None


def size(T):
    return T.size if T else 0


def upd_size(T):
    if T:
        T.size = 1 + size(T.l) + size(T.r)
def upd_sum(T):
    if T:
        T.sum = T.key + (T.l.sum if T.l else 0) + (T.r.sum if T.r else 0)

def splitBySize(T, k):
    if not T:
        return None, None
    L, R = None, None
    if k <= T.l.size():
        LL, LR = splitBySize(T.l, k)
        T.l = LR
        L, R = LL, T
    else:
        RL, RR = splitBySize(T.r, k - T.l.size() - 1)
        T.right = RL
        L, R = T, RR
        return T, RR
    upd_size(L)
    upd_size(R)
    upd_sum(L)
    upd_sum(R)
    return L, R


def merge(T1, T2):
    if not T1: return T2
    if not T2: return T1
    T = None
    if T1.prior < T2.prior:
        T1.r = merge(T1.r, T2)
        T = T1
    else:
        T2.left = merge(T1, T2.left)
        T = T2
    upd_size(T)
    upd_sum(T)
    return T


def insert(T, key, pos):
    L, R = splitBySize(T, pos - 1)
    P = Treap(key)
    return merge(merge(L, P), R)


def erase(T, pos):
    L, R = splitBySize(T, pos - 1)
    E, RR = splitBySize(R, 1)
    upd_size(L)
    upd_size(RR)
    upd_sum(L)
    upd_sum(RR)
    return merge(L, RR)


def erase(T, pos, count):
    L, R = splitBySize(T, pos - 1)
    RL, RR = splitBySize(R, count)
    upd_size(L)
    upd_size(RR)
    upd_sum(L)
    upd_sum(RR)
    return merge(L, RR)


def sum(T, fr, to):
    L, R = splitBySize(T, fr - 1)
    RL, RR = splitBySize(R, to - fr + 1)
    ans = RL.sum if RL else 0
    T=merge(L, merge(RL, RR))
    return ans


def remove(T, key):
    L, R = splitBySize(T, key)
    R = R.r
    upd_size(L)
    upd_size(R)
    upd_sum(L)
    upd_sum(R)
    return merge(L, R)


def heapify(T):
    if not T:
        return
    min = T
    if T.l and T.l.prior < min.prior:
        min = T.l
    if T.r and T.r.prior < min.prior:
        min = T.r
    if min != T:
        T.prior, min.prior = min.prior, T.prior
        heapify(min)


def build(a: list, ind: int, n: int):
    if n == 0:
        return None
    mid = n / 2
    t = Treap(a[ind + mid])
    t.l = build(a, ind, mid)
    t.r = build(a, mid + 1, n - mid - 1)
    heapify(t)
    upd_size(t)
    upd_sum(t)
    return t
a=[0,1,2,3,4,5,6,7,8,9]
t=build(a,0,len(a))
t=insert(t,0,5)
t=erase(t,0)
t=erase(t,0,3)
all_sum=sum(t,0,6)
print(all_sum)