#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5792.统计平方和三元组的数目.py
@Time    :   2021/07/10 22:30:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for c in range(1, n + 1):
            sc = c * c
            for a in range(1, n + 1):
                sa = a * a
                for b in range(1, n + 1):
                    sb = b * b
                    if sa + sb > sc:
                        break
                    if sa + sb == sc:
                        ans += 1
        return ans
