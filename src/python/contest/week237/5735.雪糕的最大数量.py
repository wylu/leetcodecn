#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5735.雪糕的最大数量.py
@Time    :   2021/04/18 10:32:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for cost in costs:
            if coins < cost:
                break
            ans += 1
            coins -= cost
        return ans
