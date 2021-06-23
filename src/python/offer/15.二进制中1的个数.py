#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   15.二进制中1的个数.py
@Time    :   2021/06/23 09:23:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n - 1)
            ans += 1
        return ans


# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         ans = 0
#         for i in range(32):
#             if n & (1 << i) > 0:
#                 ans += 1
#         return ans

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count('1')
