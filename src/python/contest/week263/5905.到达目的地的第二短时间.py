#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5905.到达目的地的第二短时间.py
@Time    :   2021/10/17 10:50:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int,
                      change: int) -> int:
        graph = [set() for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].add(v)
            graph[v].add(u)

        dist1, dist2 = [0x7FFFFFFF] * n, [0x7FFFFFFF] * n
        dist1[0] = 0
        q = [(0, 0)]

        while q:
            d1, u = heapq.heappop(q)
            if dist2[u] < d1:
                continue

            a, b = divmod(d1, change)
            cost = time
            if a % 2 == 1:
                cost += change - b

            for v in graph[u]:
                d2 = d1 + cost
                if dist1[v] > d2:
                    dist1[v], d2 = d2, dist1[v]
                    heapq.heappush(q, (dist1[v], v))

                if dist1[v] < d2 < dist2[v]:
                    dist2[v] = d2
                    heapq.heappush(q, (dist2[v], v))

        return dist2[n - 1]


if __name__ == '__main__':
    solu = Solution()
    # edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    # print(solu.secondMinimum(n=5, edges=edges, time=1, change=5))

    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    print(solu.secondMinimum(n=5, edges=edges, time=3, change=5))
