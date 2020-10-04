#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   pow-x-n.py
@Time    :   2020/10/04 23:26:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int) -> float:
            if n == 0:
                return 1
            res = pow(x, n // 2)
            res *= res
            return res * x if n % 2 == 1 else res

        if n < 0:
            x = 1 / x
            n = -n

        return pow(x, n)


if __name__ == "__main__":
    solu = Solution()
    print(solu.myPow(2.00000, 10))
    print(solu.myPow(2.10000, 3))
    print(solu.myPow(2.00000, -2))
