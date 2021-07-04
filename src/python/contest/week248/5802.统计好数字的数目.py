#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5802.统计好数字的数目.py
@Time    :   2021/07/04 10:53:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        odd = n // 2
        even = n - odd

        def cal_odd(m: int):
            if m == 0:
                return 1
            if m == 1:
                return 4
            extra = 4 if m % 2 else 1
            res = cal_odd(m // 2)
            return extra * res * res % MOD

        def cal_even(m: int):
            if m == 0:
                return 1
            if m == 1:
                return 5
            extra = 5 if m % 2 else 1
            res = cal_even(m // 2)
            return extra * res * res % MOD

        # print(odd, even)

        return cal_odd(odd) * cal_even(even) % MOD


if __name__ == '__main__':
    solu = Solution()
    print(solu.countGoodNumbers(n=1))
    print(solu.countGoodNumbers(n=4))
    print(solu.countGoodNumbers(n=50))
    print(solu.countGoodNumbers(n=806166225460393))
