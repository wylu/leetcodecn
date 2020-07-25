#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5456.在区间范围内统计奇数数目.py
@Time    :   2020/07/25 22:30:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return self.count(high) - self.count(low - 1)

    def count(self, x):
        return (x + 1) // 2


# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         cnt = (high - low) // 2
#         if low % 2 == 1 or high % 2 == 1:
#             return cnt + 1
#         return cnt
