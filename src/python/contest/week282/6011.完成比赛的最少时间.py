#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6011.完成比赛的最少时间.py
@Time    :   2022/02/27 12:14:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minimumFinishTime(self, tires: List[List[int]], changeTime: int,
                          numLaps: int) -> int:
        INF, K = 0x7FFFFFFF, 20
        best = [INF] * (K + 1)
        for f, r in tires:
            lap, last, tot = 1, f, f
            while lap <= K and tot < INF:
                best[lap] = min(best[lap], tot)
                lap, last, tot = lap + 1, last * r, tot + last * r

        dp = [INF] * (numLaps + 1)
        dp[0] = 0
        for i in range(1, numLaps + 1):
            for j in range(max(0, i - K), i):
                dp[i] = min(dp[i], dp[j] + changeTime + best[i - j])

        return dp[numLaps] - changeTime
