from typing import List


class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.counter = 0


class Solution:
    def _build(self, left, right):
        root = SegmentTreeNode(self.nums[left], self.nums[right])
        if left == right:
            return root

        mid = (left + right) // 2
        root.left = self._build(left, mid)
        root.right = self._build(mid + 1, right)
        return root

    def _update(self, root, val):
        if not root:
            return
        if root.low <= val <= root.high:
            root.counter += 1
            self._update(root.left, val)
            self._update(root.right, val)

    def _query(self, root, lower, upper):
        if lower <= root.low and root.high <= upper:
            return root.counter
        if upper < root.low or root.high < lower:
            return 0
        return self._query(root.left, lower, upper) + self._query(
            root.right, lower, upper
        )

    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        self.nums = sorted(list(set(nums)))
        root = self._build(0, len(self.nums) - 1) if nums else None

        res = []
        for n in nums:
            res.append(self._query(root, float("-inf"), n - 1))
            self._update(root, n)
        return res[::-1]
