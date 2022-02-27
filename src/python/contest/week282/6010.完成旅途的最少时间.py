#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6010.完成旅途的最少时间.py
@Time    :   2022/02/27 10:34:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def check(mid: int) -> bool:
            return sum(mid // t for t in time) >= totalTrips

        left, right = 0, (1 << 63) - 1
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumTime(time=[1, 2, 3], totalTrips=5))
    print(solu.minimumTime(time=[2], totalTrips=1))
    print(solu.minimumTime(time=[10000], totalTrips=10000000))
