#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   204.计数质数.py
@Time    :   2020/08/02 23:00:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (34.37%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    68.6K
# Total Submissions: 198.5K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#
"""
方法一：欧拉线性筛法

基本思路:
任意一个合数（2 不是合数），都可以表示成素数的乘积。
每个合数必有一个最小素因子，如果每个合数都用最小素因子筛去，那个这个合数就不会
被重复标记筛去，所以算法为线性时间复杂度。

例如合数 30 = 2 * 3 * 5 ，这个合数一定是被最小素因子 2 筛去的。

方法二：埃拉托斯特尼筛法

当一个数是素数的时候，它的倍数肯定不是素数，对于这些数可以直接标记筛除。
"""


# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        ans, marks = 0, [True] * n
        for i in range(2, n):
            if marks[i]:
                ans += 1
                for j in range(i + i, n, i):
                    marks[j] = False
        return ans


# @lc code=end

# 欧拉线性筛法
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 2:
#             return 0

#         # 元素值为 True 表示该元素下标值为素数
#         mark = [True for _ in range(n)]
#         primes = []
#         for i in range(2, n):
#             if mark[i]:
#                 primes.append(i)

#             j, lp = 0, len(primes)
#             while j < lp and i * primes[j] < n:
#                 mark[i * primes[j]] = False

#                 if i % primes[j] == 0:
#                     break

#                 j += 1

#         ans = 0
#         for i in range(2, n):
#             if mark[i]:
#                 ans += 1
#         return ans
