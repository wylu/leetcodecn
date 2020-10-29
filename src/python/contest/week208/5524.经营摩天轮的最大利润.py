#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5524.经营摩天轮的最大利润.py
@Time    :   2020/09/27 10:35:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int,
                               runningCost: int) -> int:
        ans, cnt = 0, -1
        i, cur, take, n = 0, 0, 0, len(customers)

        while i < n or cur != 0:
            if i < n:
                cur += customers[i]
            i += 1

            if cur <= 4:
                take += cur
                cur = 0
            else:
                take += 4
                cur -= 4

            benefit = take * boardingCost - i * runningCost
            if benefit > ans:
                ans, cnt = benefit, i

        return -1 if ans == 0 else cnt


if __name__ == "__main__":
    solu = Solution()
    print(solu.minOperationsMaxProfit([8, 3], 5, 6))
    print(solu.minOperationsMaxProfit([10, 9, 6], 6, 4))
    print(solu.minOperationsMaxProfit([8, 3], 5, 6))
    print(solu.minOperationsMaxProfit([2], 2, 4))
