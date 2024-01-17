"""
LeetCode: https://leetcode.com/problems/range-sum-query-mutable/
Task: Найти город с наименьшим числом достижимых из него
городов, которые расположены ближе, чем заданное
расстояние

Input: There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [from(i), to(i), weight(i)]
represents a bidirectional and weighted edge between cities from(i) and to(i), and given the integer distanceThreshold.

Output: boolean

"""
from typing import List


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * 4 * self.n
        self.buildTree(nums, 0, self.n - 1, 1)

    def buildTree(self, nums, left, right, index):
        if left == right:
            self.tree[index] = nums[left]
            return

        mid = (left + right) >> 1


        self.buildTree(nums, left, mid, 2 * index)
        self.buildTree(nums, mid + 1, right, 2 * index + 1)
        self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def getSum(self, v, tl, tr, l, r: int) -> int:
        if l == tl and r == tr:
            return self.tree[v]

        tm = (tl + tr) >> 1
        res = 0
        if l <= tm:
            res += self.getSum(v * 2, tl, tm, l, min(r, tm))
        if r >= tm + 1:
            res += self.getSum(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        return res

    def update(self, left, right, index, pos, val):
        if left == right:
            self.tree[index] = val
            return

        mid = (left + right) >> 1
        if pos <= mid:
            self.update(left, mid, 2 * index, pos, val)
        else:
            self.update(mid + 1, right, 2 * index + 1, pos, val)

        self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]


class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segTree.update(0, self.segTree.n - 1, 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.getSum(1, 0, self.segTree.n - 1, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
