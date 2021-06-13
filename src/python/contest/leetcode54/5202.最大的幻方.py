#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5202.最大的幻方.py
@Time    :   2021/06/12 22:45:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rps = [[0] * (n + 1) for _ in range(m)]
        cps = [[0] * (n) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                rps[i][j + 1] = rps[i][j] + grid[i][j]
                cps[i + 1][j] = cps[i][j] + grid[i][j]

        def check_dale_hill(rs, re, cs, ce):
            dale = hill = 0
            for i in range(re - rs + 1):
                dale += grid[rs + i][cs + i]
                hill += grid[rs + i][ce - i]
            return dale == hill, dale

        def check(size):
            res, tot = True, 0
            for i in range(m - size + 1):
                rs, re = i, i + size - 1
                for j in range(n - size + 1):
                    cs, ce = j, j + size - 1
                    res, tot = check_dale_hill(rs, re, cs, ce)
                    if not res:
                        continue

                    for k in range(size):
                        if rps[rs + k][ce + 1] - rps[rs + k][cs] != tot:
                            res = False
                            break
                        if cps[re + 1][cs + k] - cps[rs][cs + k] != tot:
                            res = False
                            break

                    if res:
                        return True

            return res

        for size in range(min(m, n), 0, -1):
            if check(size):
                return size

        return 1


if __name__ == '__main__':
    solu = Solution()
    grid = [[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]
    print(solu.largestMagicSquare(grid))

    grid = [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
    print(solu.largestMagicSquare(grid))
