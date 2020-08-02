#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   买卖股票的最佳时机.py
@Time    :   2020/08/02 16:14:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        ans, minVal = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] - minVal > ans:
                ans = prices[i] - minVal
            if prices[i] < minVal:
                minVal = prices[i]

        return ans
