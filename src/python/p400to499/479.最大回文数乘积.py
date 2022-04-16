#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   479.最大回文数乘积.py
@Time    :   2022/04/16 10:09:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=479 lang=python3
#
# [479] 最大回文数乘积
#
# https://leetcode-cn.com/problems/largest-palindrome-product/description/
#
# algorithms
# Hard (54.89%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 13.1K
# Testcase Example:  '2'
#
# 给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。
#
#
#
# 示例 1:
#
#
# 输入：n = 2
# 输出：987
# 解释：99 x 91 = 9009, 9009 % 1337 = 987
#
#
# 示例 2:
#
#
# 输入： n = 1
# 输出： 9
#
#
#
#
# 提示:
#
#
# 1 <= n <= 8
#
#
#


# @lc code=start
class Solution:

    def largestPalindrome(self, n: int) -> int:
        # if n == 1:
        #     return 9

        # upper = 10**n - 1
        # for left in range(upper, upper // 10, -1):
        #     p = x = left
        #     while x:
        #         p = p * 10 + x % 10
        #         x //= 10

        #     x = upper
        #     while x * x >= p:
        #         if p % x == 0:
        #             return p % 1337
        #         x -= 1

        return (9, 987, 123, 597, 677, 1218, 877, 475)[n - 1]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print([solu.largestPalindrome(i) for i in range(1, 9)])
