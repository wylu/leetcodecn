#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5830.三除数.py
@Time    :   2021/08/01 12:04:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isThree(self, n: int) -> bool:
        if n == 4:
            return True

        if n <= 2 or n % 2 == 0:
            return False

        for i in range(3, n // 2 + 1, 2):
            d, r = divmod(n, i)
            if r == 0:
                return d == i

        return False
