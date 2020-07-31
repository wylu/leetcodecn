#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   8.字符串转换整数-atoi.py
@Time    :   2020/07/30 10:03:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (20.72%)
# Likes:    773
# Dislikes: 0
# Total Accepted:    187.2K
# Total Submissions: 902K
# Testcase Example:  '"42"'
#
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
#
#
# 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
# 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
#
#
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
#
# 在任何情况下，若函数不能进行有效的转换时，请返回 0 。
#
# 提示：
#
#
# 本题中的空白字符只包括空格字符 ' ' 。
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX
# (2^31 − 1) 或 INT_MIN (−2^31) 。
#
#
#
#
# 示例 1:
#
# 输入: "42"
# 输出: 42
#
#
# 示例 2:
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
#
#
# 示例 3:
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
#
#
# 示例 4:
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
# ⁠    因此无法执行有效的转换。
#
# 示例 5:
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
# 因此返回 INT_MIN (−2^31) 。
#
#
#
"""
确定有限状态机（deterministic finite automaton, DFA）

思路:

字符串处理的题目往往涉及复杂的流程以及条件情况，如果直接上手写程序，一不
小心就会写出极其臃肿的代码。因此，为了有条理地分析每个输入字符的处理方法，
我们可以使用自动机这个概念：

我们的程序在每个时刻有一个状态 s，每次从序列中输入一个字符 c，并根据字符
c 转移到下一个状态 s'。这样，我们只需要建立一个覆盖所有情况的从 s 与 c
映射到 s' 的表格即可解决题目中的问题。

算法:

本题可以建立如下的自动机：

+--------------------------------------+
|      |  ' '     +/-     num    other |
|------+-------------------------------+
|start |  start   sign    num    end   |
|sign  |  end     end     num    end   |
|num   |  end     end     num    end   |
|end   |  end     end     end	 end   |
+--------------------------------------+
"""


# @lc code=start
class Automation(object):
    MAX_INT32 = (1 << 31) - 1
    MIN_INT32 = -(1 << 31)

    def __init__(self):
        # Intial State: 'start'
        self.state = 0

        self.ans = 0
        self.sign = 1
        self.MAX = (1 << 31) - 1
        self.overflow = False
        # 0: start, 1: sign, 2: num, 3: end
        self.table = (
            (0, 1, 2, 3),
            (3, 3, 2, 3),
            (3, 3, 2, 3),
            (3, 3, 3, 3),
        )

    def getCol(self, c: str):
        if c == ' ':
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def getState(self, c: str):
        self.state = self.table[self.state][self.getCol(c)]

        if self.state == 1:
            if c == '-':
                self.sign = -1
                self.MAX = 1 << 31

        elif self.state == 2:
            c = ord(c) - ord('0')

            if self.ans > self.MAX // 10 or (self.ans == self.MAX // 10
                                             and c > self.MAX % 10):
                self.overflow = True
                self.state = 3
                return self.state

            self.ans = self.ans * 10 + c

        return self.state


class Solution:
    def myAtoi(self, s: str) -> int:
        auto = Automation()
        for c in s:
            if auto.getState(c) != 3:
                continue

            if auto.overflow:
                return auto.MAX_INT32 if auto.sign == 1 else auto.MIN_INT32

        return auto.sign * auto.ans


# @lc code=end

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         if not s:
#             return 0

#         s = s.strip()
#         if not s or (s[0] != '-' and s[0] != '+' and not s[0].isdigit()):
#             return 0

#         sign = 1 if s[0] != '-' else -1
#         if s[0] == '-' or s[0] == '+':
#             s = s[1:]

#         MAX_INT32, MIN_INT32 = (1 << 31) - 1, -(1 << 31)
#         MAX = (1 << 31) - 1 if sign == 1 else (1 << 31)

#         ans = 0
#         for c in s:
#             if not c.isdigit():
#                 break

#             c = ord(c) - ord('0')
#             if ans > MAX // 10 or (ans == MAX // 10 and c > MAX % 10):
#                 return MAX_INT32 if sign == 1 else MIN_INT32

#             ans = ans * 10 + c

#         return sign * ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.myAtoi('42'))
