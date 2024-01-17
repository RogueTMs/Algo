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

        # self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
        self.merge(nums, 2 * index, 2 * index + 1)

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

    def merge(self, nums, left, right):
        mid = (left + right) >> 1
        l = left
        r = mid + 1
        temp = []
        while l <= mid and r <= right:
            if nums[l][0] > nums[r][0]:
                temp.append(nums[l])
                self.tree[nums[l][1]] += (right - r + 1)
                l += 1
            else:

                temp.append(nums[r])
                r += 1

        while l <= mid:
            temp.append(nums[l])
            l += 1

        while r <= right:
            temp.append(nums[r])
            r += 1

        for i in range(left, right + 1):
            nums[i] = temp[i - left]



class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

