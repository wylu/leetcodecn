#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5219.每个小孩最多能分到多少糖果.py
@Time    :   2022/04/03 10:46:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maximumCandies(self, candies: List[int], k: int) -> int:

        def check(mid: int) -> bool:
            cur = 0
            for candy in candies:
                cur += candy // mid
                if cur >= k:
                    return True
            return False

        candies.sort()
        left, right = 0, candies[-1] + 1
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumCandies(candies=[5, 8, 6], k=3))
    print(solu.maximumCandies(candies=[2, 5], k=11))
    print(solu.maximumCandies(candies=[4, 7, 5], k=4))
