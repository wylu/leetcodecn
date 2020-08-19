#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   647.回文子串.py
@Time    :   2020/08/19 16:44:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (63.11%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 79.5K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
#
#
#
# 示例 1：
#
# 输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#
#
# 示例 2：
#
# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#
#
#
# 提示：
#
#
# 输入的字符串长度不会超过 1000 。
#
#
#
"""
Dynamic Programming

State:
  dp[i][j]: 表示以s[i]为开头和s[j]为结尾的子串是否为回文串

Initial State:
  dp[i][j] = True,  i == j, 0 <= i,j < len(s)
  dp[i][j] = False, i != j, 0 <= i,j < len(s)

State Transition:
  i < j
  if (s[i] == s[j]) dp[i][j] = (i + 1 == j) or dp[i + 1][j - 1];
  else dp[i][j] = False;
"""


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        def expand(i: int, j: int) -> int:
            cnt = 0
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                cnt += 1
                i -= 1
                j += 1
            return cnt

        ans, n = 0, len(s)
        for i in range(n):
            ans += expand(i, i)
            ans += expand(i, i + 1)
        return ans


# @lc code=end

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         if not s:
#             return 0

#         n = len(s)
#         ans = 0
#         dp = [[False] * n for _ in range(n)]

#         for j in range(n):
#             for i in range(j, -1, -1):
#                 if i == j:
#                     dp[i][j] = True
#                 if not dp[i][j] and s[i] == s[j]:
#                     dp[i][j] = (i + 1 == j) or dp[i + 1][j - 1]
#                 if dp[i][j]:
#                     ans += 1

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.countSubstrings('abc'))
    print(solu.countSubstrings('aaa'))
