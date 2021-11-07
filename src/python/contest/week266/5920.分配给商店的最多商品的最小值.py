#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5920.分配给商店的最多商品的最小值.py
@Time    :   2021/11/07 10:52:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)

        def check(limit: int) -> bool:
            i, k = 0, n
            while k > 0 and i < m:
                d, r = divmod(quantities[i], limit)
                k -= d
                if r:
                    k -= 1
                i += 1
            return i == m and k >= 0

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimizedMaximum(n=6, quantities=[11, 6]))
    print(solu.minimizedMaximum(n=7, quantities=[15, 10, 10]))
    print(solu.minimizedMaximum(n=1, quantities=[100000]))
