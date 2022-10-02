#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   777.在lr字符串中交换相邻字符.py
@Time    :   2022/10/02 21:10:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
#
# https://leetcode.cn/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (33.02%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 53.3K
# Testcase Example:  '"RXXLRXRXL"\n"XRLXXRRLX"'
#
# 在一个由 'L' , 'R' 和 'X'
# 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时，
# 返回True。
#
#
#
# 示例 :
#
# 输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#
#
#
#
# 提示：
#
#
# 1 <= len(start) = len(end) <= 10000。
# start和end中的字符串仅限于'L', 'R'和'X'。
#
#
#


# @lc code=start
class Solution:

    def canTransform(self, start: str, end: str) -> bool:
        n, i, j = len(start), 0, 0

        while i < n or j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1

            if i == n or j == n:
                return i == j

            if start[i] != end[j]:
                return False

            if start[i] == 'L' and i < j:
                return False

            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return i == j


# @lc code=end
