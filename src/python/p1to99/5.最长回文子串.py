#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5.最长回文子串.py
@Time    :   2020/10/02 15:00:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.98%)
# Likes:    2748
# Dislikes: 0
# Total Accepted:    389.7K
# Total Submissions: 1.2M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        n = len(s)
        start, end = 0, 0

        def expandAroundCenter(left: int, right: int) -> tuple:
            while 0 <= left and right < n and s[left] == s[right]:
                left, right = left - 1, right + 1
            return left + 1, right - 1

        for i in range(n):
            l1, r1 = expandAroundCenter(i, i)
            l2, r2 = expandAroundCenter(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.longestPalindrome("babad"))
    print(solu.longestPalindrome("cbbd"))
