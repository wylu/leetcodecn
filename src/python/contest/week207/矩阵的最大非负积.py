#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   矩阵的最大非负积.py
@Time    :   2020/09/20 10:55:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        f = [[[0, 0] for _ in range(m)] for _ in range(n)]
        f[0][0] = [grid[0][0], grid[0][0]]
        for i in range(1, m):
            f[0][i][0] = f[0][i - 1][0] * grid[0][i]
            f[0][i][1] = f[0][i][0]

        for i in range(1, n):
            f[i][0][0] = f[i - 1][0][0] * grid[i][0]
            f[i][0][1] = f[i][0][0]
            for j in range(1, m):
                f[i][j][0] = min(f[i][j - 1][0] * grid[i][j],
                                 f[i][j - 1][1] * grid[i][j],
                                 f[i - 1][j][0] * grid[i][j],
                                 f[i - 1][j][1] * grid[i][j])
                f[i][j][1] = max(f[i][j - 1][0] * grid[i][j],
                                 f[i][j - 1][1] * grid[i][j],
                                 f[i - 1][j][0] * grid[i][j],
                                 f[i - 1][j][1] * grid[i][j])

        ans = f[n - 1][m - 1][1]
        return -1 if ans < 0 else ans % (10**9 + 7)


if __name__ == '__main__':
    solu = Solution()
    # print(solu.maxProductPath([[-1, -4], [-2, -3]]))
    # print(solu.maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
    print(solu.maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))
    print(
        solu.maxProductPath([[-1, -4, 2], [4, 3, -1], [2, -4, 4], [1, -1,
                                                                   -4]]))
