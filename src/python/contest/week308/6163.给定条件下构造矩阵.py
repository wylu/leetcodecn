#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6163.给定条件下构造矩阵.py
@Time    :   2022/08/28 10:53:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from collections import deque
from typing import List


class Solution:

    def buildMatrix(self, k: int, rowConditions: List[List[int]],
                    colConditions: List[List[int]]) -> List[List[int]]:

        def topo_sort(conditions):
            graph = defaultdict(list)
            indegrees = [0] * (k + 1)
            for u, v in conditions:
                graph[u].append(v)
                indegrees[v] += 1

            res = []
            que = deque(i for i, v in enumerate(indegrees) if i and v == 0)
            while que:
                u = que.popleft()
                res.append(u)
                for v in graph[u]:
                    indegrees[v] -= 1
                    if indegrees[v] == 0:
                        que.append(v)

            return [] if len(res) != k else res

        row = topo_sort(rowConditions)
        if not row:
            return []

        col = topo_sort(colConditions)
        if not col:
            return []

        x2j = {x: i for i, x in enumerate(col)}
        ans = [[0] * k for _ in range(k)]
        for i, x in enumerate(row):
            j = x2j[x]
            ans[i][j] = x

        return ans


if __name__ == '__main__':
    solu = Solution()
    k = 3
    rowConditions = [[1, 2], [3, 2]]
    colConditions = [[2, 1], [3, 2]]
    print(solu.buildMatrix(k, rowConditions, colConditions))

    k = 3
    rowConditions = [[1, 2], [2, 3], [3, 1], [2, 3]]
    colConditions = [[2, 1]]
    print(solu.buildMatrix(k, rowConditions, colConditions))

    k = 8
    rowConditions = [[1, 2], [7, 3], [4, 3], [5, 8], [7, 8], [8, 2], [5, 8],
                     [3, 2], [1, 3], [7, 6], [4, 3], [7, 4], [4, 8], [7, 3],
                     [7, 5]]
    colConditions = [[5, 7], [2, 7], [4, 3], [6, 7], [4, 3], [2, 3], [6, 2]]
    print(solu.buildMatrix(k, rowConditions, colConditions))
