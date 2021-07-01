#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   07.传递信息.py
@Time    :   2021/07/01 16:46:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from functools import lru_cache
from collections import defaultdict
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        graph = defaultdict(set)
        for u, v in relation:
            graph[u].add(v)

        @lru_cache(None)
        def dfs(u, c):
            if c == k:
                return bool(u == n - 1)

            if u not in graph:
                return 0

            return sum(dfs(v, c + 1) for v in graph[u])

        return dfs(0, 0)


if __name__ == '__main__':
    solu = Solution()
    n = 5
    relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    k = 3
    print(solu.numWays(n, relation, k))

    n = 3
    relation = [[0, 2], [2, 1]]
    k = 2
    print(solu.numWays(n, relation, k))
