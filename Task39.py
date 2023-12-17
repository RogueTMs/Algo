"""
LeetCode: https://leetcode.com/problems/wildcard-matching/description/
Task: Решить задачу распознавания строки по wildcard через
динамическое программирование

Input: Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

Output: boolean

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == '*':
                dp[0][i + 1] = True
            else:
                break

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '?' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]

                if p[j] == '*':
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]

        return dp[len(s)][len(p)]
