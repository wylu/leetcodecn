#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   201.数字范围按位与.py
@Time    :   2020/08/23 09:54:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#
# https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (47.14%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 40.8K
# Testcase Example:  '5\n7'
#
# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
#
# 示例 1:
#
# 输入: [5,7]
# 输出: 4
#
# 示例 2:
#
# 输入: [0,1]
# 输出: 0
#
#


# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0 or m == n:
            return m

        def left1idx(x: int) -> int:
            i = 0
            while x:
                x >>= 1
                i += 1
            return i - 1

        ln, lm = left1idx(n), left1idx(m)
        if ln != lm:
            return 0

        ans, c = 0, ln
        while c >= 0 and n & (1 << c) == m & (1 << c):
            ans ^= n & (1 << c)
            c -= 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.rangeBitwiseAnd(5, 7))
    print(solu.rangeBitwiseAnd(0, 1))
    print(solu.rangeBitwiseAnd(6, 7))
    print(solu.rangeBitwiseAnd(10, 11))
