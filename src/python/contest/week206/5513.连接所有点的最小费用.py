#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5513.连接所有点的最小费用.py
@Time    :   2020/09/13 11:18:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = (abs(points[i][0] - points[j][0]) +
                              abs(points[i][1] - points[j][1]))
                cost[j][i] = cost[i][j]

        ans = 0
        used = [False] * n
        mincost = [0x7FFFFFFF] * n
        mincost[0] = 0
        while True:
            v = -1
            for u in range(n):
                if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                    v = u

            if v == -1:
                break

            used[v] = True
            ans += mincost[v]
            for u in range(n):
                mincost[u] = min(mincost[u], cost[v][u])

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
    print(solu.minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]))
    print(solu.minCostConnectPoints([[-1000000, -1000000], [1000000,
                                                            1000000]]))
    print(solu.minCostConnectPoints([[0, 0]]))
