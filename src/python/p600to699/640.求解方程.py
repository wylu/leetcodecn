#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   640.求解方程.py
@Time    :   2022/08/10 12:41:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#
# https://leetcode.cn/problems/solve-the-equation/description/
#
# algorithms
# Medium (44.44%)
# Likes:    139
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 48.7K
# Testcase Example:  '"x+5-3+x=6+x-2"'
#
# 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。
#
# 如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。
#
# 题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。
#
#
#
# 示例 1：
#
#
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"
#
#
# 示例 2:
#
#
# 输入: equation = "x=x"
# 输出: "Infinite solutions"
#
#
# 示例 3:
#
#
# 输入: equation = "2x=x"
# 输出: "x=0"
#
#
#
#
# 提示:
#
#
# 3 <= equation.length <= 1000
# equation 只有一个 '='.
# equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。 ​​​
#
#
#


# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')

        def count(s: str):
            cx = cs = 0
            i, n = 0, len(s)
            while i < n:
                sign = -1 if s[i] == '-' else 1
                if s[i] == '-' or s[i] == '+':
                    i += 1

                # read the number
                num = 1 if s[i] == 'x' else 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                if i < n and s[i] == 'x':
                    cx += sign * num
                    i += 1
                else:
                    cs += sign * num

            return cx, cs

        lx, ls = count(left)
        rx, rs = count(right)
        x, s = lx - rx, rs - ls
        if x == 0 and s == 0:
            return 'Infinite solutions'
        if x == 0 and s != 0:
            return 'No solution'
        return f'x={s//x}'


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.solveEquation(equation="x+5-3+x=6+x-2"))
    print(solu.solveEquation(equation="x=x"))
    print(solu.solveEquation(equation="x=x+1"))
    print(solu.solveEquation(equation="2x+3x-6x=x+2"))
    print(solu.solveEquation(equation="0x=0"))
