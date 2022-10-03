#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1784.检查二进制字符串字段.py
@Time    :   2022/10/03 11:33:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1784 lang=python3
#
# [1784] 检查二进制字符串字段
#
# https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/
#
# algorithms
# Easy (42.78%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    21.8K
# Total Submissions: 41.1K
# Testcase Example:  '"1001"'
#
# 给你一个二进制字符串 s ，该字符串 不含前导零 。
#
# 如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。
#
# 如果 s 中 由连续若干个 '1' 组成的字段 数量不超过 1，返回 true​​​ 。否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：s = "1001"
# 输出：false
# 解释：由连续若干个 '1' 组成的字段数量为 2，返回 false
#
#
# 示例 2：
#
#
# 输入：s = "110"
# 输出：true
#
#
#
# 提示：
#
#
# 1 <= s.length <= 100
# s[i]​​​​ 为 '0' 或 '1'
# s[0] 为 '1'
#
#
#


# @lc code=start
class Solution:

    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s


# @lc code=end
