"""
LeetCode: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
Task: Найти город с наименьшим числом достижимых из него
городов, которые расположены ближе, чем заданное
расстояние

Input: There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [from(i), to(i), weight(i)]
represents a bidirectional and weighted edge between cities from(i) and to(i), and given the integer distanceThreshold.

Output: boolean

"""
import math
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        dist = [[math.inf] * n for i in range(n)]

        for _from, to, weight in edges:
            dist[_from][to] = dist[to][_from] = weight

        for i in range(n):
            dist[i][i] = 0

        # Floyd–Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        res = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] <= dt:
                    res[j] += 1

        ans = n - 1
        for i in range(n):
            if res[i] <= res[ans]:
                ans = i

        return ans
