#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   整数反转.py
@Time    :   2020/07/29 10:54:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) if x < 0 else (1 << 31) - 1
        sign = 1 if x >= 0 else -1
        ans, x = 0, abs(x)

        while x != 0:
            pop = x % 10
            x //= 10

            if ans > MAX // 10 or (ans == MAX // 10 and pop > MAX % 10):
                return 0

            ans = ans * 10 + pop

        return sign * ans
