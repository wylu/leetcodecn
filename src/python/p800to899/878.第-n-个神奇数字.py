#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   878.第-n-个神奇数字.py
@Time    :   2022/11/22 19:11:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#
# https://leetcode.cn/problems/nth-magical-number/description/
#
# algorithms
# Hard (30.35%)
# Likes:    179
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 45.5K
# Testcase Example:  '1\n2\n3'
#
# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
#
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 10^9 + 7 取模 后的值。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：n = 1, a = 2, b = 3
# 输出：2
#
#
# 示例 2：
#
#
# 输入：n = 4, a = 2, b = 3
# 输出：6
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^9
# 2 <= a, b <= 4 * 10^4
#
#
#
#
#
import math


# @lc code=start
class Solution:

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        left, right = min(a, b), min(a, b) * n
        c = a * b // math.gcd(a, b)

        while left < right:
            mid = (left + right) // 2
            cnt = mid // a + mid // b - mid // c
            if cnt < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD


# @lc code=end
