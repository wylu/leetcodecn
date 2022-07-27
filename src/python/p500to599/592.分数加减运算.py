#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   592.分数加减运算.py
@Time    :   2022/07/27 15:50:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#
# https://leetcode.cn/problems/fraction-addition-and-subtraction/description/
#
# algorithms
# Medium (58.77%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 26.3K
# Testcase Example:  '"-1/2+1/2"'
#
# 给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。
#
# 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为
# 2/1。
#
#
#
# 示例 1:
#
#
# 输入: expression = "-1/2+1/2"
# 输出: "0/1"
#
#
# 示例 2:
#
#
# 输入: expression = "-1/2+1/2+1/3"
# 输出: "1/3"
#
#
# 示例 3:
#
#
# 输入: expression = "1/3-1/2"
# 输出: "-1/6"
#
#
#
#
# 提示:
#
#
# 输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。
# 输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
# 输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
# 输入的分数个数范围是 [1,10]。
# 最终结果的分子与分母保证是 32 位整数范围内的有效整数。
#
#
#

# @lc code=start
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        i, n = 0, len(expression)

        def read_number() -> int:
            nonlocal i
            sign = -1 if expression[i] == '-' else 1
            if not expression[i].isdigit():
                i += 1
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            return sign * num

        a, b = 0, 1
        while i < n:
            c = read_number()
            i += 1  # skip /
            d = read_number()

            # a/b + c/d -> a*d/b*d + c*b/b*d
            a, b = a * d + c * b, b * d

        g = gcd(a, b)
        a //= g
        b //= g

        return f'{a}/{b}'


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.fractionAddition("-1/2+1/2"))
    print(solu.fractionAddition("-1/2+1/2+1/3"))
    print(solu.fractionAddition("1/3-1/2"))
