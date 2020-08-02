#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   爬楼梯.py
@Time    :   2020/08/02 16:09:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0

        f = [1, 2]
        if n <= 2:
            return f[n - 1]

        for _ in range(3, n + 1):
            f[0], f[1] = f[1], f[0] + f[1]

        return f[1]
