#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   65.有效数字.py
@Time    :   2021/05/23 19:30:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
# https://leetcode-cn.com/problems/valid-number/description/
#
# algorithms
# Hard (22.48%)
# Likes:    185
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 115.5K
# Testcase Example:  '"0"'
#
# 有效数字（按顺序）可以分成以下几个部分：
#
#
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
#
#
# 小数（按顺序）可以分成以下几个部分：
#
#
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
#
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
#
#
#
#
# 整数（按顺序）可以分成以下几个部分：
#
#
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
#
#
# 部分有效数字列举如下：
#
#
# ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
# "53.5e93", "-123.456e789"]
#
#
# 部分无效数字列举如下：
#
#
# ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
#
#
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
#
#
#
# 示例 1：
#
#
# 输入：s = "0"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "e"
# 输出：false
#
#
# 示例 3：
#
#
# 输入：s = "."
# 输出：false
#
#
# 示例 4：
#
#
# 输入：s = ".1"
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
#
#
#
from typing import Tuple
"""
思路：

表示数值的字符串遵循模式 A[.[B]][e|EC] 或者 .B[e|EC]，其中：

A 为数值的整数部分（可能以 '+' 或 '-' 开头的 0-9 的数位串）
B 紧跟着小数点为数值的小数部分（0-9 的数位串）
C 紧跟 'e' 或 'E' 为数值的指数部分（可能以 '+' 或 '-' 开头的 0-9 的数位串）

在小数里可能没有整数部分，如小数 .123 等于 0.123，因此 A 部分不是必需的。
如果一个数没有整数部分，那么它的小数部分不能为空。
"""


# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)

        def scanUnsignedInteger(s: str, idx: int) -> Tuple[bool, int]:
            cur = idx
            while cur < n and '0' <= s[cur] <= '9':
                cur += 1
            return cur > idx, cur

        def scanInteger(s: str, idx: int) -> Tuple[bool, int]:
            if idx < n and (s[idx] == '+' or s[idx] == '-'):
                idx += 1
            return scanUnsignedInteger(s, idx)

        if not s:
            return False

        A, idx = scanInteger(s, 0)
        if idx != n and s[idx] == '.':
            B, idx = scanUnsignedInteger(s, idx + 1)
            A = B or A

        if idx != n and (s[idx] == 'e' or s[idx] == 'E'):
            C, idx = scanInteger(s, idx + 1)
            A = A and C

        return A and idx == n


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.isNumber("2"))
    print(solu.isNumber("0089"))
    print(solu.isNumber("-0.1"))
    print(solu.isNumber("+3.14"))
    print(solu.isNumber("4."))
    print(solu.isNumber("-.9"))
    print(solu.isNumber("2e10"))
    print(solu.isNumber("-90E3"))
    print(solu.isNumber("3e+7"))
    print(solu.isNumber("+6e-1"))
    print(solu.isNumber("53.5e93"))
    print(solu.isNumber("-123.456e789"))

    print(solu.isNumber("abc"))
    print(solu.isNumber("1a"))
    print(solu.isNumber("1e"))
    print(solu.isNumber("e3"))
    print(solu.isNumber("99e2.5"))
    print(solu.isNumber("--6"))
    print(solu.isNumber("-+3"))
    print(solu.isNumber("95a54e53"))
