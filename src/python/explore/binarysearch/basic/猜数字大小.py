#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   猜数字大小.py
@Time    :   2020/10/02 23:38:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher,
# otherwise return 0
# def guess(num: int) -> int:


def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1
