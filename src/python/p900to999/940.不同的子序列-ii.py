#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   940.不同的子序列-ii.py
@Time    :   2022/10/14 10:41:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=940 lang=python3
#
# [940] 不同的子序列 II
#
# https://leetcode.cn/problems/distinct-subsequences-ii/description/
#
# algorithms
# Hard (43.48%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 25.4K
# Testcase Example:  '"abc"'
#
# 给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
#
# 字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
#
#
# 例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "abc"
# 输出：7
# 解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
#
#
# 示例 2：
#
#
# 输入：s = "aba"
# 输出：6
# 解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
#
#
# 示例 3：
#
#
# 输入：s = "aaa"
# 输出：3
# 解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 2000
# s 仅由小写英文字母组成
#
#
#
#
#


# @lc code=start
class Solution:

    def distinctSubseqII(self, s: str) -> int:
        last = [-1] * 26
        f = [1] * len(s)

        for i, ch in enumerate(s):
            for j in range(26):
                if last[j] != -1:
                    f[i] += f[last[j]]
            last[ord(ch) - ord('a')] = i

        ans = 0
        for i in range(26):
            if last[i] != -1:
                ans += f[last[i]]

        return ans % (10**9 + 7)


# @lc code=end
