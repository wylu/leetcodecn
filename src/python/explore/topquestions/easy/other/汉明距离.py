#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   汉明距离.py
@Time    :   2020/08/07 21:48:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        z = x ^ y
        while z:
            z &= (z - 1)
            ans += 1

        return ans
