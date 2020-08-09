#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5486.切棍子的最小成本.py
@Time    :   2020/08/09 19:57:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
Dynamic Programming

State:
  dp[i][j]: 表示完成 cuts[i],...,cuts[j] 之间的所有切割的最小总成本

Initia State:
  dp[i][j] = MAX
  dp[i][i+1] = 0

State Transition:
  i < k < j
  dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
"""
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        m = len(cuts)

        dp = [[0x7FFFFFFF] * m for _ in range(m)]
        for i in range(m - 1):
            dp[i][i + 1] = 0

        for size in range(2, m):
            i, j = 0, size

            while j < m:
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

                i += 1
                j = i + size

        return dp[0][m - 1]


if __name__ == '__main__':
    solu = Solution()
    print(solu.minCost(7, [1, 3, 4, 5]))
