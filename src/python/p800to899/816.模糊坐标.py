#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   816.模糊坐标.py
@Time    :   2022/11/07 18:53:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#
# https://leetcode.cn/problems/ambiguous-coordinates/description/
#
# algorithms
# Medium (50.54%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 29.7K
# Testcase Example:  '"(123)"'
#
# 我们有一些二维坐标，如 "(1, 3)" 或 "(2,
# 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。
#
# 原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001",
# "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。
#
# 最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。
#
#
#
#
# 示例 1:
# 输入: "(123)"
# 输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
#
#
#
# 示例 2:
# 输入: "(00011)"
# 输出:  ["(0.001, 1)", "(0, 0.011)"]
# 解释:
# 0.0, 00, 0001 或 00.01 是不被允许的。
#
#
#
# 示例 3:
# 输入: "(0123)"
# 输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12,
# 3)"]
#
#
#
# 示例 4:
# 输入: "(100)"
# 输出: [(10, 0)]
# 解释:
# 1.0 是不被允许的。
#
#
#
#
# 提示:
#
#
# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。
#
#
#
#
#
from typing import List


# @lc code=start
class Solution:

    def ambiguousCoordinates(self, s: str) -> List[str]:

        def get_options(s: str) -> List[str]:
            options = []
            if s[0] != '0' or s == '0':
                options.append(s)
            for p in range(1, len(s)):
                if p != 1 and s[0] == '0' or s[-1] == '0':
                    continue
                options.append(s[:p] + '.' + s[p:])
            return options

        ans = []
        n = len(s) - 2
        s = s[1:-1]
        for k in range(1, n):
            lt = get_options(s[:k])
            if not lt:
                continue
            rt = get_options(s[k:])
            if not rt:
                continue
            for i in lt:
                for j in rt:
                    ans.append(f'({i}, {j})')

        return ans


# @lc code=end
