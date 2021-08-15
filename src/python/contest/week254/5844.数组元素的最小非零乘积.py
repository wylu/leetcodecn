#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5844.数组元素的最小非零乘积.py
@Time    :   2021/08/15 11:33:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        max_num = 2**p - 1
        x = max_num - 1
        y = 2**(p - 1) - 1

        def power(x: int, y: int) -> int:
            if y == 0:
                return 1
            res = power(x, y // 2)
            res = (res * res) % MOD
            extra = x if y % 2 else 1
            return res * extra % MOD

        return power(x, y) * max_num % MOD


if __name__ == '__main__':
    solu = Solution()
    print(solu.minNonZeroProduct(p=1))
    print(solu.minNonZeroProduct(p=2))
    print(solu.minNonZeroProduct(p=3))
    print(solu.minNonZeroProduct(p=4))  # 581202553
    print(solu.minNonZeroProduct(p=5))
    print(solu.minNonZeroProduct(p=6))
    print(solu.minNonZeroProduct(p=7))
    print(solu.minNonZeroProduct(p=8))
    print(solu.minNonZeroProduct(p=60))
