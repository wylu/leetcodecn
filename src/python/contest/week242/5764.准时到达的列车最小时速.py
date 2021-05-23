#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5764.准时到达的列车最小时速.py
@Time    :   2021/05/23 10:37:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        def check(speed: int) -> bool:
            tot = 0
            for i in range(n - 1):
                tot += math.ceil(dist[i] / speed)
            tot += dist[n - 1] / speed
            return tot <= hour

        MAX_SPPED = (10**7) + 1
        left, right = 1, MAX_SPPED
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return -1 if left >= MAX_SPPED else left


if __name__ == '__main__':
    solu = Solution()
    print(solu.minSpeedOnTime(dist=[1, 3, 2], hour=6))
    print(solu.minSpeedOnTime(dist=[1, 3, 2], hour=2.7))
    print(solu.minSpeedOnTime(dist=[1, 3, 2], hour=1.9))
    print(solu.minSpeedOnTime(dist=[1, 1, 100000], hour=2.01))  # 100000
