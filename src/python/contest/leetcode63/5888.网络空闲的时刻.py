#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5888.网络空闲的时刻.py
@Time    :   2021/10/16 22:45:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]],
                           patience: List[int]) -> int:
        n = len(patience)
        dist = [0x7FFFFFFF] * n
        seen = {0}

        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def bfs(u: int):
            que = deque([u])
            depth = 0
            while que:
                depth += 1
                for _ in range(len(que)):
                    u = que.popleft()
                    for v in graph[u]:
                        if v in seen:
                            continue
                        dist[v] = depth
                        que.append(v)
                        seen.add(v)

        bfs(0)
        # print(dist)
        # print(patience)

        ans = 0
        for i in range(1, n):
            d, p = dist[i], patience[i]
            tot = d * 2
            if p < tot:
                r = p if tot % p == 0 else tot % p
                tot += (tot - r)
            ans = max(ans, tot)

        return ans + 1


if __name__ == '__main__':
    solu = Solution()
    edges = [[0, 1], [1, 2]]
    patience = [0, 2, 1]
    print(solu.networkBecomesIdle(edges, patience))

    edges = [[0, 1], [0, 2], [1, 2]]
    patience = [0, 10, 10]
    print(solu.networkBecomesIdle(edges, patience))

    edges = [[3, 8], [4, 13], [0, 7], [0, 4], [1, 8], [14, 1], [7, 2],
             [13, 10], [9, 11], [12, 14], [0, 6], [2, 12], [11, 5], [6, 9],
             [10, 3]]
    patience = [0, 3, 2, 1, 5, 1, 5, 5, 3, 1, 2, 2, 2, 2, 1]
    print(solu.networkBecomesIdle(edges, patience))
