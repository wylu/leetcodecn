#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   326.3-的幂.py
@Time    :   2020/08/02 23:30:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (46.93%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    52.7K
# Total Submissions: 112.3K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1:
#
# 输入: 27
# 输出: true
#
#
# 示例 2:
#
# 输入: 0
# 输出: false
#
# 示例 3:
#
# 输入: 9
# 输出: true
#
# 示例 4:
#
# 输入: 45
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#


# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1


# @lc code=end

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         # 3^19 = 1162261467 < (2^31 - 1)
#         return n > 0 and 1162261467 % n == 0
