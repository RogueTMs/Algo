class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        dist = [[int(1e9)] * n for i in range(n)]

        for i, j, d in edges:
            dist[i][j] = dist[j][i] = d

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        city_res = [[] for i in range(n)]
        city_min_cnt = int(1e9)

        for i in range(n):
            for j in range(n):
                if dist[i][j] <= dt:
                    city_res[i].append(j)

            if len(city_res[i]):
                city_min_cnt = min(len(city_res[i]), city_min_cnt)

        res = []
        for i in range(n):
            if len(city_res[i]) == city_min_cnt:
                res.append(i)

        return max(res)