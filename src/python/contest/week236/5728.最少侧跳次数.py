#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5728.最少侧跳次数.py
@Time    :   2021/04/11 11:11:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
Dynamic Programming

State:
  dp[i][j]: 表示青蛙当前处于点 i 的第 j 条跑道时的最少侧跳次数

Initial State:
  dp[0][1] = 0
  dp[i][j] = MAX_INT32  (0 <= i <= n && 1 <= j <= 3 && obstacles[i] != 0)

State Transition:
  if obstacles[i] == 0:
      dp[i][1] = dp[i-1][1]
      dp[i][2] = dp[i-1][2]
      dp[i][3] = dp[i-1][3]
      dp[i][1] = min(dp[i][1], dp[i][2] + 1, dp[i][3] + 1)
      dp[i][2] = min(dp[i][1] + 1, dp[i][2], dp[i][3] + 1)
      dp[i][3] = min(dp[i][1] + 1, dp[i][2] + 1, dp[i][3])
  else:
      dp[i][j] = dp[i-1][j]
      dp[i][j] = min(dp[i][j], dp[i][!j] + 1)
"""
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[0] * 3 for _ in range(n)]

        for i in range(1, n):
            if obstacles[i] == 0:
                for j in range(3):
                    dp[i][j] = dp[i - 1][j]
            else:
                for j in range(3):
                    if j + 1 != obstacles[i]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = 0x7FFFFFFF

            if obstacles[i] != 1:
                dp[i][0] = min(dp[i][0], dp[i][1] + 1, dp[i][2] + 1)
                if i == 1:
                    dp[i][0] += 1
            if obstacles[i] != 2:
                dp[i][1] = min(dp[i][0] + 1, dp[i][1], dp[i][2] + 1)
            if obstacles[i] != 3:
                dp[i][2] = min(dp[i][0] + 1, dp[i][1] + 1, dp[i][2])
                if i == 1:
                    dp[i][2] += 1

        return min(dp[n - 1])


if __name__ == '__main__':
    solu = Solution()
    print(solu.minSideJumps([0, 1, 2, 3, 0]))
    print(solu.minSideJumps([0, 1, 1, 3, 3, 0]))
    print(solu.minSideJumps([0, 2, 1, 0, 3, 0]))
