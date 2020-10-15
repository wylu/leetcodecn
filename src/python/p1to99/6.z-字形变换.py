#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6.z-字形变换.py
@Time    :   2020/10/15 11:53:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (48.91%)
# Likes:    869
# Dislikes: 0
# Total Accepted:    180.3K
# Total Submissions: 368.5K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
#
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#
#
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
#
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or not s:
            return s

        rows = [[] for _ in range(min(len(s), numRows))]
        cur, sign = 0, -1

        for ch in s:
            rows[cur].append(ch)
            if cur == 0 or cur == numRows - 1:
                sign = -sign
            cur += sign

        ans = []
        for row in rows:
            ans += row

        return ''.join(ans)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.convert("LEETCODEISHIRING", 3))
    print(solu.convert("LEETCODEISHIRING", 4))
    print(solu.convert("LEETCODEISHIRING", 1))
