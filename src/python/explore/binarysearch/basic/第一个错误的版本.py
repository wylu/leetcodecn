#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   第一个错误的版本.py
@Time    :   2020/10/03 10:55:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left
