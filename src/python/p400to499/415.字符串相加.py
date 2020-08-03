#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   415.字符串相加.py
@Time    :   2020/08/03 12:56:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (50.11%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    55.6K
# Total Submissions: 108.1K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
#
#


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return -1

        ans = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1

            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1

            ans.append(str(carry % 10))
            carry //= 10

        if carry > 0:
            ans.append(str(carry))

        ans.reverse()
        return ''.join(ans)


# @lc code=end
