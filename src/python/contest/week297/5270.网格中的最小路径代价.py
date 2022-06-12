#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5270.网格中的最小路径代价.py
@Time    :   2022/06/12 10:37:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minPathCost(self, grid: List[List[int]],
                    moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = grid[0][:]

        for i in range(m - 1):
            t = [0x7FFFFFFF] * n
            for j in range(n):
                v = grid[i][j]
                for k in range(n):
                    cost = moveCost[v][k]
                    t[k] = min(t[k], f[j] + grid[i + 1][k] + cost)
            f = t

        return min(f)


if __name__ == '__main__':
    solu = Solution()
    grid = [[5, 3], [4, 0], [2, 1]]
    moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
    print(solu.minPathCost(grid, moveCost))
