#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   买卖股票的最佳时机II.py
@Time    :   2020/07/26 09:26:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                ans += prices[i] - prices[i - 1]
        return ans
