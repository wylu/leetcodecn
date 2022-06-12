#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5259.计算应缴税款总额.py
@Time    :   2022/06/12 10:30:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = i = 0
        while income:
            cur = brackets[i][0]
            if i > 0:
                cur -= brackets[i - 1][0]

            cur = min(income, cur)
            ans += cur * brackets[i][1] / 100
            i += 1
            income -= cur

        return ans
