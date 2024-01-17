from typing import List


class BIT:

    def __init__(self, nums=None):
        if nums is None:
            self.nums = []
        else:
            self.nums = nums
        self.s = self.__buildS_i()

    @staticmethod
    def f(x):
        return x & (x + 1)

    @staticmethod
    def g(x):
        return x | (x + 1)

    def __buildPrefixes(self):
        prefixes = [0] * len(self.nums)

        currSum = 0
        for i in range(len(self.nums)):
            currSum += self.nums[i]
            prefixes[i] = currSum

        return prefixes

    @staticmethod
    def __sum(left: int, right: int, prefixes: List[int]) -> int:
        if left == 0:
            return prefixes[right]
        return prefixes[right] - prefixes[left - 1]

    def __buildS_i(self):
        prefixes = self.__buildPrefixes()
        s = []

        for i in range(len(self.nums)):
            s.append(self.__sum(self.f(i), i, prefixes))

        return s

    def getPrefixSum(self, pos: int) -> int:
        ans = 0
        current_pos = pos
        while current_pos >= 0:
            ans += self.s[current_pos]
            current_pos = self.f(current_pos) - 1
        return ans

    def sum(self, l, r: int) -> int:
        return self.getPrefixSum(r) - self.getPrefixSum(l - 1)

    def __increment(self, pos, val: int):
        i = pos

        while i < len(self.nums):
            self.s[i] += val
            i = self.g(i)

    def update(self, pos, val: int):
        self.__increment(pos, val - self.nums[pos])

