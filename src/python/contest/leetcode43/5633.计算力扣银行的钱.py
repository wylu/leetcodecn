#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5633.计算力扣银行的钱.py
@Time    :   2021/01/09 22:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        ans, base = 0, 0
        while n:
            day = min(n, 7)
            a1, a2 = base + 1, base + day
            ans += (a1 + a2) * day // 2
            n -= day
            base += 1
        return ans
