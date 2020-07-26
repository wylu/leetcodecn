#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   63.股票的最大利润.py
@Time    :   2020/07/26 23:24:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        ans, curMin = 0, prices[0]
        for price in prices:
            ans = max(ans, price - curMin)
            curMin = min(curMin, price)
        return ans
