#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   47.礼物的最大价值.py
@Time    :   2020/12/04 22:06:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = max(dp[j - 1], dp[j]) + grid[i][j]
        return dp[n - 1]


if __name__ == "__main__":
    solu = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(solu.maxValue(grid))
