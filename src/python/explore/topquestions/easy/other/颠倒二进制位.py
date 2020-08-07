#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   颠倒二进制位.py
@Time    :   2020/08/07 21:57:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        ans, power = 0, 31
        while n:
            ans += (n & 1) << power
            n >>= 1
            power -= 1
        return ans
