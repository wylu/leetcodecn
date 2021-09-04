#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   10.斐波那契数列I.py
@Time    :   2021/09/04 09:56:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def fib(self, n: int) -> int:
        MOD = 10**9 + 7
        f = [0, 1]
        for _ in range(n):
            f[0], f[1] = f[1], (f[0] + f[1]) % MOD
        return f[0]
