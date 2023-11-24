class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = [0] * (self.n + 1)
        self.consturctTree(nums)

    def consturctTree(self, nums):
        for i in range(len(nums)):
            self.updateBit(i, nums[i])

    def updateBit(self, index, value):
        index += 1
        while index <= self.n:
            self.bit[index] += value
            index += (index & -index)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateBit(index, diff)

    def getSum(self, index):
        index += 1
        result = 0
        while index > 0:
            result += self.bit[index]
            index -= (index & -index)
        return result

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right) - self.getSum(left - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)