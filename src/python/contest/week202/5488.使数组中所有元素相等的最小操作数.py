#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5488.使数组中所有元素相等的最小操作数.py
@Time    :   2020/08/16 10:38:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1:
            avg = 2 * (n // 2) + 1
        else:
            a, b = n // 2, n // 2 - 1
            avg = ((2 * a + 1) + (2 * b + 1)) // 2

        ans = 0
        for i in range(0, n // 2):
            ans += avg - (2 * i + 1)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minOperations(3))
    print(solu.minOperations(6))
    print(solu.minOperations(1))
