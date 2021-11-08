#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5921.最大化一张图中的路径价值.py
@Time    :   2021/11/08 19:16:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]],
                           maxTime: int) -> int:
        n = len(values)
        graph = defaultdict(set)
        cost = [[maxTime] * n for _ in range(n)]

        for u, v, t in edges:
            graph[u].add(v)
            graph[v].add(u)
            cost[u][v] = cost[v][u] = t

        ans = values[0]
        seen = set()

        def dfs(u: int, cur_time: int, cur_value: int) -> None:
            nonlocal ans
            if u == 0:
                ans = max(ans, cur_value)

            for v in graph[u]:
                if cur_time + cost[u][v] > maxTime:
                    continue

                flag = v in seen
                if not flag:
                    seen.add(v)
                    cur_value += values[v]

                dfs(v, cur_time + cost[u][v], cur_value)

                if not flag:
                    seen.discard(v)
                    cur_value -= values[v]

        dfs(0, 0, 0)
        return ans


if __name__ == '__main__':
    solu = Solution()
    values = [0, 32, 10, 43]
    edges = [[0, 1, 10], [1, 2, 15], [0, 3, 10]]
    maxTime = 49
    print(solu.maximalPathQuality(values, edges, maxTime))

    values = [5, 10, 15, 20]
    edges = [[0, 1, 10], [1, 2, 10], [0, 3, 10]]
    maxTime = 30
    print(solu.maximalPathQuality(values, edges, maxTime))

    values = [1, 2, 3, 4]
    edges = [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]]
    maxTime = 50
    print(solu.maximalPathQuality(values, edges, maxTime))

    values = [0, 1, 2]
    edges = [[1, 2, 10]]
    maxTime = 10
    print(solu.maximalPathQuality(values, edges, maxTime))

    values = [95]
    edges = []
    maxTime = 83
    print(solu.maximalPathQuality(values, edges, maxTime))
