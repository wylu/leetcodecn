#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6148.矩阵中的局部最大值.py
@Time    :   2022/08/14 10:30:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                cur = 0
                for p in range(i, i + 3):
                    for q in range(j, j + 3):
                        cur = max(cur, grid[p][q])
                ans[i][j] = cur

        return ans


if __name__ == '__main__':
    solu = Solution()
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    print(solu.largestLocal(grid))

    grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]
    print(solu.largestLocal(grid))
