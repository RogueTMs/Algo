from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        rows, columns = len(dungeon) - 1, len(dungeon[0]) - 1

        dungeon[columns][rows] = max(1, 1 - dungeon[columns][rows])
        for r in range(rows - 1, -1, -1):
            dungeon[r][columns] = max(1, dungeon[r + 1][columns] - dungeon[r][columns])

        for c in range(columns - 1, -1, -1):
            dungeon[-1][c] = max(1, dungeon[columns][c + 1] - dungeon[columns][c])

        for r in range(rows - 1, -1, -1):
            for c in range(columns - 1, -1, -1):
                dungeon[r][c] = max(1, min(dungeon[r + 1][c], dungeon[r][c + 1]) - dungeon[r][c])

        return dungeon[0][0]
