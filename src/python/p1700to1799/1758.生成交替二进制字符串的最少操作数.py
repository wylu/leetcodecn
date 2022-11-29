#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1758.生成交替二进制字符串的最少操作数.py
@Time    :   2022/11/29 12:33:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#
# https://leetcode.cn/problems/minimum-changes-to-make-alternating-binary-string/description/
#
# algorithms
# Easy (63.20%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    22.2K
# Total Submissions: 32K
# Testcase Example:  '"0100"'
#
# 给你一个仅由字符 '0' 和 '1' 组成的字符串 s 。一步操作中，你可以将任一 '0' 变成 '1' ，或者将 '1' 变成 '0' 。
#
# 交替字符串 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 "010" 是交替字符串，而字符串 "0100"
# 不是。
#
# 返回使 s 变成 交替字符串 所需的 最少 操作数。
#
#
#
# 示例 1：
#
# 输入：s = "0100"
# 输出：1
# 解释：如果将最后一个字符变为 '1' ，s 就变成 "0101" ，即符合交替字符串定义。
#
#
# 示例 2：
#
# 输入：s = "10"
# 输出：0
# 解释：s 已经是交替字符串。
#
#
# 示例 3：
#
# 输入：s = "1111"
# 输出：2
# 解释：需要 2 步操作得到 "0101" 或 "1010" 。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s[i] 是 '0' 或 '1'
#
#
#


# @lc code=start
class Solution:

    def minOperations(self, s: str) -> int:

        def count(c: int) -> int:
            cnt = 0
            for ch in s:
                cnt += int(c != int(ch))
                c ^= 1
            return cnt

        return min(count(0), count(1))


# @lc code=end
