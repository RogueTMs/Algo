class Solution:
    def canJump(self, nums):
        return self.solve(nums, 0)

    def solve(self, nums, pos):
        ret = 0
        save_pos = 0
        cur_jump = nums[pos]
        if cur_jump + pos >= len(nums) - 1:
            return True
        for i in range(pos + 1, pos + cur_jump + 1):
            if nums[i] + i >= ret:
                ret = nums[i] + i
                save_pos = i
        print(save_pos, ret)
        if ret == 0:
            return False

        return self.solve(nums, save_pos)


# nums = [1, 1, 2, 2, 0, 1, 1]
sol = Solution()
nums = [4,2,5,0,1,0,4,4,4,0,4,0]
print(sol.canJump(nums))


