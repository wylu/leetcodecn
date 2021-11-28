#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5925.统计农场中肥沃金字塔的数目.py
@Time    :   2021/11/28 12:10:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def count(grid: List[List[int]]) -> int:
            m, n = len(grid), len(grid[0])
            f = [0] * (n + 2)

            res = 0
            for i in range(m - 1, -1, -1):
                d = [0] * (n + 2)
                for j in range(n):
                    if grid[i][j] == 0:
                        continue
                    d[j + 1] = min(f[j], f[j + 1], f[j + 2]) + 1
                    res += d[j + 1] - 1
                f = d

            return res

        ans = count(grid)
        grid.reverse()
        ans += count(grid)
        return ans
