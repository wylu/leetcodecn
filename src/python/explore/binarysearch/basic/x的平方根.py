#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   x的平方根.py
@Time    :   2020/10/02 23:21:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) // 2
            val = mid * mid
            if val == x:
                return mid
            elif val < x:
                left = mid
            else:
                right = mid - 1
        return left
