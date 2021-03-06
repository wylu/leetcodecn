#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   367.有效的完全平方数.py
@Time    :   2020/10/05 00:14:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.52%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    45K
# Total Submissions: 103.3K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
#
# 输入：16
# 输出：True
#
# 示例 2：
#
# 输入：14
# 输出：False
#
#
#


# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left < right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            else:
                right = mid
        return left * left == num


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.isPerfectSquare(16))
    print(solu.isPerfectSquare(14))
    print(solu.isPerfectSquare(1))
    print(solu.isPerfectSquare(2))
