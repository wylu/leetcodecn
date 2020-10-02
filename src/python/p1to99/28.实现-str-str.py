#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   28.实现-str-str.py
@Time    :   2020/10/02 16:07:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.69%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    239.6K
# Total Submissions: 603.8K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
#
#
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
#
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
#


# @lc code=start
class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p:
            return 0

        n = len(p)
        fail = [-1] * n
        k, j = -1, 0
        while j < n - 1:
            if k == -1 or p[k] == p[j]:
                k += 1
                j += 1
                fail[j] = k
            else:
                k = fail[k]

        m = len(s)
        i, j = 0, 0
        while i < m and j < n:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = fail[j]

        return i - j if j == n else -1


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.strStr("hello", "ll"))
    print(solu.strStr("aaaaa", "bba"))
    print(solu.strStr("", "a"))
