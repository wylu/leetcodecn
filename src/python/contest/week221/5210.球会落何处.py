#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5210.球会落何处.py
@Time    :   2020/12/27 11:03:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n

        def check(ci: int, cj: int) -> int:
            if ((cj == 0 and grid[ci][cj] == -1)
                    or (cj == n - 1 and grid[ci][cj] == 1)):
                return -1
            if ((grid[ci][cj] == -1 and grid[ci][cj - 1] == 1)
                    or (grid[ci][cj] == 1 and grid[ci][cj + 1] == -1)):
                return -1
            return cj - 1 if grid[ci][cj] == -1 else cj + 1

        def run(ci: int, cj: int) -> int:
            if ci == m - 1:
                return check(ci, cj)

            if grid[ci][cj] == 1 and cj + 1 < n and grid[ci][cj + 1] == 1:
                return run(ci + 1, cj + 1)

            if grid[ci][cj] == -1 and cj - 1 >= 0 and grid[ci][cj - 1] == -1:
                return run(ci + 1, cj - 1)

            return -1

        for i in range(n):
            ans[i] = run(0, i)

        return ans


if __name__ == "__main__":
    solu = Solution()
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    print(solu.findBall(grid))

    grid = [[-1]]
    print(solu.findBall(grid))
