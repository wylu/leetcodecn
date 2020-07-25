#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5457.和为奇数的子数组数目.py
@Time    :   2020/07/25 22:36:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even = 0, 1
        total, ans = 0, 0

        for num in arr:
            total += num
            if total % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1

        return ans % 1000000007


# class Solution:
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         if arr[0] % 2 == 1:
#             even, odd = 0, 1
#         else:
#             even, odd = 1, 0

#         ans = odd
#         for i in range(1, len(arr)):
#             if arr[i] % 2 == 1:
#                 even, odd = odd, even + 1
#             else:
#                 even, odd = even + 1, odd
#             ans += odd

#         return ans % 1000000007

# class Solution:
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         MOD = int(pow(10, 9)) + 7
#         n = len(arr)

#         dp = [[0, 0] for _ in range(n)]
#         if arr[0] % 2 == 1:
#             dp[0][0], dp[0][1] = 0, 1
#         else:
#             dp[0][0], dp[0][1] = 1, 0

#         ans = dp[0][1]
#         for i in range(1, n):
#             if arr[i] % 2 == 1:
#                 dp[i][0], dp[i][1] = dp[i - 1][1], dp[i - 1][0] + 1
#             else:
#                 dp[i][0], dp[i][1] = dp[i - 1][0] + 1, dp[i - 1][1]

#             ans = (ans + dp[i][1]) % MOD

#         return ans
