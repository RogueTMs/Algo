"""
LeetCode: https://leetcode.com/problems/unique-binary-search-trees
Task: Найти количество уникальных (по форме) BST
Input: int n - num of nodes
Output: number of structurally unique BST's
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]  # j-1: left, i-j: right
        return dp[n]