"""
LeetCode: https://leetcode.com/problems/regular-expression-matching/description/
Task: Решить задачу распознавания строки по регулярному
выражению через динамическое программирование

Input: Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

Output: boolean

example of dp(s = "aab", p = "c*a*b"):

          c  *  a  *  b
       0  1  2  3  4  5
   0  [T, F, T, F, T, F]
a  1  [F, F, F, T, T, F]
a  2  [F, F, F, F, T, F]
b  3  [F, F, F, F, F, T]
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == '*':
                dp[0][i + 1] = dp[0][i - 1]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]

                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':  # in this case, _* only counts as empty
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]

        return dp[len(s)][len(p)]
