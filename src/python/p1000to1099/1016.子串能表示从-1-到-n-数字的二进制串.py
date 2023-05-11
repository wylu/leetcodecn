#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1016.子串能表示从-1-到-n-数字的二进制串.py
@Time    :   2023/05/11 12:41:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2023, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#
# https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (58.32%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    15.6K
# Total Submissions: 25K
# Testcase Example:  '"0110"\n3'
#
# 给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回
# false 。
#
# 子字符串 是字符串中连续的字符序列。
#
#
#
# 示例 1：
#
#
# 输入：s = "0110", n = 3
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "0110", n = 4
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s[i] 不是 '0' 就是 '1'
# 1 <= n <= 10^9
#
#
#


# @lc code=start
class Solution:

    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            if bin(i)[2:] not in s:
                return False
        return True


# @lc code=end
