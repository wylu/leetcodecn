#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   709.转换成小写字母.py
@Time    :   2021/12/12 10:15:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#
# https://leetcode-cn.com/problems/to-lower-case/description/
#
# algorithms
# Easy (76.33%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    78.6K
# Total Submissions: 103.1K
# Testcase Example:  '"Hello"'
#
# 给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "Hello"
# 输出："hello"
#
#
# 示例 2：
#
#
# 输入：s = "here"
# 输出："here"
#
#
# 示例 3：
#
#
# 输入：s = "LOVELY"
# 输出："lovely"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 100
# s 由 ASCII 字符集中的可打印字符组成
#
#
#


# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


# @lc code=end
