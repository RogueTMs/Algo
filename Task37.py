"""
LeetCode: https://leetcode.com/problems/dungeon-game
Task: Помогите рыцарю выйти из подземелья!
Input: 2d int array
Output: the knight's minimum initial health so that he can rescue the princess
"""

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, columns = len(dungeon) - 1, len(dungeon[0]) - 1

        # hp needed at finish
        dungeon[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # set last column
        for r in range(rows - 1, -1, -1):
            dungeon[r][-1] = max(1, dungeon[r + 1][-1] - dungeon[r][-1])

        # set last row
        for c in range(columns - 1, -1, -1):
            dungeon[-1][c] = max(1, dungeon[-1][c + 1] - dungeon[-1][c])

        # calculate inside cells
        for r in range(rows - 1, -1, -1):
            for c in range(columns - 1, -1, -1):
                dungeon[r][c] = max(1, min(dungeon[r + 1][c], dungeon[r][c + 1]) - dungeon[r][c])

        return dungeon[0][0]
