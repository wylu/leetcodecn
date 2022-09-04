#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6168.恰好移动k步到达某一位置的方法数目.py
@Time    :   2022/09/04 10:39:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

from math import comb


class Solution:

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        d = abs(startPos - endPos)
        if d > k or d % 2 != k % 2:
            return 0
        MOD = 10**9 + 7
        return comb(k, (d + k) // 2) % MOD


# class Solution:

#     def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
#         d = abs(startPos - endPos)
#         if d > k or d % 2 != k % 2:
#             return 0

#         MOD = 10**9 + 7

#         @cache
#         def f(x: int, r: int) -> int:
#             if abs(x - endPos) > r:
#                 return 0
#             if r == 0:
#                 return 1
#             return (f(x - 1, r - 1) + f(x + 1, r - 1)) % MOD

#         return f(startPos, k)

if __name__ == '__main__':
    solu = Solution()
    startPos = 1
    endPos = 2
    k = 3
    print(solu.numberOfWays(startPos, endPos, k))
