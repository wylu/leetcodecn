#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   537.复数乘法.py
@Time    :   2022/02/25 20:14:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#
# https://leetcode-cn.com/problems/complex-number-multiplication/description/
#
# algorithms
# Medium (74.60%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 44.3K
# Testcase Example:  '"1+1i"\n"1+1i"'
#
# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
#
#
# 实部 是一个整数，取值范围是 [-100, 100]
# 虚部 也是一个整数，取值范围是 [-100, 100]
# i^2 == -1
#
#
# 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。
#
#
#
# 示例 1：
#
#
# 输入：num1 = "1+1i", num2 = "1+1i"
# 输出："0+2i"
# 解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
#
#
# 示例 2：
#
#
# 输入：num1 = "1+-1i", num2 = "1+-1i"
# 输出："0+-2i"
# 解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。
#
#
#
#
# 提示：
#
#
# num1 和 num2 都是有效的复数表示。
#
#
#


# @lc code=start
class Solution:

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = map(int, num1[:-1].split('+'))
        a2, b2 = map(int, num2[:-1].split('+'))
        return f'{a1 * a2 - b1 * b2}+{a1 * b2 + b1 * a2}i'


# @lc code=end

# class Solution:

#     def complexNumberMultiply(self, num1: str, num2: str) -> str:
#         i = num1.index('+')
#         a1, b1 = int(num1[:i]), int(num1[i + 1:-1])

#         i = num2.index('+')
#         a2, b2 = int(num2[:i]), int(num2[i + 1:-1])

#         return f'{(a1 * a2) - (b1 * b2)}+{(b1 * a2) + (a1 * b2)}i'

if __name__ == '__main__':
    solu = Solution()
    print(solu.complexNumberMultiply(num1="1+1i", num2="1+1i"))
    print(solu.complexNumberMultiply(num1="1+-1i", num2="1+-1i"))
