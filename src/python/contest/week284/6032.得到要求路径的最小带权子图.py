#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6032.得到要求路径的最小带权子图.py
@Time    :   2022/03/13 18:26:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List
from typing import Tuple


class Solution:

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int,
                      src2: int, dest: int) -> int:

        INF = 10**12

        def dijkstra(graph: List[List[Tuple[int, int]]],
                     src: int) -> List[int]:
            dist = [INF] * n
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                d, u = heapq.heappop(pq)
                if dist[u] < d:
                    continue

                for v, w in graph[u]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))

            return dist

        adj = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]
        for u, v, c in edges:
            adj[u].append((v, c))
            rev[v].append((u, c))

        dist1 = dijkstra(adj, src1)
        dist2 = dijkstra(adj, src2)
        dist3 = dijkstra(rev, dest)

        ans = INF
        for i in range(n):
            ans = min(ans, dist1[i] + dist2[i] + dist3[i])

        return -1 if ans == INF else ans


if __name__ == '__main__':
    solu = Solution()
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3],
             [2, 3, 4], [3, 4, 2], [4, 5, 1]]
    src1 = 0
    src2 = 1
    dest = 5
    print(solu.minimumWeight(n, edges, src1, src2, dest))

    n = 5
    edges = [[4, 2, 20], [4, 3, 46], [0, 1, 15], [0, 1, 43], [0, 1, 32],
             [3, 1, 13]]

    src1 = 0
    src2 = 4
    dest = 1
    print(solu.minimumWeight(n, edges, src1, src2, dest))
