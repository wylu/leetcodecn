#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   有效的完全平方数.py
@Time    :   2020/10/04 23:59:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left < right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            else:
                right = mid
        return left * left == num


if __name__ == "__main__":
    solu = Solution()
    print(solu.isPerfectSquare(16))
    print(solu.isPerfectSquare(14))
    print(solu.isPerfectSquare(1))
    print(solu.isPerfectSquare(2))
