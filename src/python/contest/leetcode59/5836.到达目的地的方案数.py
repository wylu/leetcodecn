#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5836.到达目的地的方案数.py
@Time    :   2021/08/21 22:55:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        INF, MOD = float('inf'), 10**9 + 7
        cost = [[INF] * n for _ in range(n)]
        for u, v, t in roads:
            cost[u][v] = cost[v][u] = t

        dist = [INF] * n
        dist[0] = 0
        used = [False] * n
        nums = [0] * n
        nums[0] = 1

        for i in range(n):
            u = -1
            for v in range(n):
                if not used[v] and (u == -1 or dist[v] < dist[u]):
                    u = v

            used[u] = True
            for v in range(n):
                if not used[v] and cost[u][v] < INF:
                    if dist[u] + cost[u][v] < dist[v]:
                        dist[v] = dist[u] + cost[u][v]
                        nums[v] = nums[u]
                    elif dist[u] + cost[u][v] == dist[v]:
                        nums[v] += nums[u]

        return nums[n - 1] % MOD


if __name__ == '__main__':
    solu = Solution()
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1],
             [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    print(solu.countPaths(n, roads))

    n = 2
    roads = [[1, 0, 10]]
    print(solu.countPaths(n, roads))

    n = 1
    roads = []
    print(solu.countPaths(n, roads))
