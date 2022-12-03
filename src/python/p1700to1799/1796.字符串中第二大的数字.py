#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1796.字符串中第二大的数字.py
@Time    :   2022/12/03 10:03:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#
# https://leetcode.cn/problems/second-largest-digit-in-a-string/description/
#
# algorithms
# Easy (48.79%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    16.7K
# Total Submissions: 32.2K
# Testcase Example:  '"dfa12321afd"'
#
# 给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
#
# 混合字符串 由小写英文字母和数字组成。
#
#
#
# 示例 1：
#
#
# 输入：s = "dfa12321afd"
# 输出：2
# 解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
#
#
# 示例 2：
#
#
# 输入：s = "abc1111"
# 输出：-1
# 解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
#
#
#
#
# 提示：
#
#
# 1
# s 只包含小写英文字母和（或）数字。
#
#
#


# @lc code=start
class Solution:

    def secondHighest(self, s: str) -> int:
        digits = sorted(set(int(ch) for ch in s if ch.isdigit()))
        return -1 if len(digits) < 2 else digits[-2]


# @lc code=end
