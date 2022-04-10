#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6037.按奇偶性交换后的最大数字.py
@Time    :   2022/04/10 10:30:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def largestInteger(self, num: int) -> int:
        odd, even = [], []
        cur = num
        while cur:
            cur, digit = divmod(cur, 10)
            if digit % 2:
                odd.append(digit)
            else:
                even.append(digit)

        odd.sort()
        even.sort()

        ans = 0
        for digit in str(num):
            digit = int(digit)
            if digit % 2:
                ans = ans * 10 + odd.pop()
            else:
                ans = ans * 10 + even.pop()

        return ans
