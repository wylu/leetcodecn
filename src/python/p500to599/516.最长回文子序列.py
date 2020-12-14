#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   516.最长回文子序列.py
@Time    :   2020/12/14 22:52:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (58.62%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    33.9K
# Total Submissions: 57.8K
# Testcase Example:  '"bbbab"'
#
# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
#
#
#
# 示例 1:
# 输入:
#
# "bbbab"
#
#
# 输出:
#
# 4
#
#
# 一个可能的最长回文子序列为 "bbbb"。
#
# 示例 2:
# 输入:
#
# "cbbd"
#
#
# 输出:
#
# 2
#
#
# 一个可能的最长回文子序列为 "bb"。
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 只包含小写英文字母
#
#
#
"""
Dynamic Programming

State:
  dp[i][j]: 表示 a[i], ..., a[j] 中的最长回文子序列的长度

Initial State:
  dp[i][i] = 1

State Transition:
  if (a[i] == a[j]) dp[i][j] = dp[i + 1][j - 1] + 2;
  else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
"""


# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.longestPalindromeSubseq("bbbab"))
    print(solu.longestPalindromeSubseq("cbbd"))
    print(solu.longestPalindromeSubseq("a"))
