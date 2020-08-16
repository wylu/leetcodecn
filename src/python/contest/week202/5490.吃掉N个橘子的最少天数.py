#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5490.吃掉N个橘子的最少天数.py
@Time    :   2020/08/16 11:21:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def minDays(self, n: int) -> int:
        cache = {0: 0, 1: 1}

        def dfs(n: int) -> int:
            if n in cache:
                return cache[n]

            # 吃二分之一的代价
            a = n % 2 + 1 + dfs(n // 2)
            # 吃三分之二的代价
            b = n % 3 + 1 + dfs(n // 3)
            cache[n] = min(a, b)

            return cache[n]

        return dfs(n)


if __name__ == '__main__':
    solu = Solution()
    print(solu.minDays(10))
    print(solu.minDays(6))
    print(solu.minDays(1))
    print(solu.minDays(56))
    print(solu.minDays(10**4))
    print(solu.minDays(2 * (10**9)))
