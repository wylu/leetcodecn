#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   67.二进制求和.py
@Time    :   2020/08/05 23:08:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (54.35%)
# Likes:    445
# Dislikes: 0
# Total Accepted:    117.7K
# Total Submissions: 216.6K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。
#
#
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
#
# 提示：
#
#
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
#
#
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a

        ans = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            ans.append(str(carry % 2))
            carry //= 2

        if carry > 0:
            ans.append(str(carry))

        ans.reverse()
        return ''.join(ans)


# @lc code=end
