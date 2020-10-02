#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   14.最长公共前缀.py
@Time    :   2020/07/31 23:40:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (38.46%)
# Likes:    1191
# Dislikes: 0
# Total Accepted:    323.8K
# Total Submissions: 840.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
from typing import List
"""
用 LCP(S[1],...,S[n]) 表示字符串 S[1],...,S[n] 的最长公共前缀。

可以得到以下结论：

LCP(S[1],...,S[n]) = LCP(LCP(LCP(S[1],S[2]),S[3]),...S[n])

基于该结论，可以得到一种查找字符串数组中的最长公共前缀的简单方法。依次遍历字符串数组
中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，
即可得到字符串数组中的最长公共前缀。

如果在尚未遍历完所有的字符串时，最长公共前缀已经是空串，则最长公共前缀一定是空串，
因此不需要继续遍历剩下的字符串，直接返回空串即可。
"""


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans = strs[0]
        for i in range(1, len(strs)):
            cur = strs[i]
            j, n = 0, min(len(ans), len(cur))
            while j < n and ans[j] == cur[j]:
                j += 1

            ans = ans[:j]
            if not ans:
                break

        return ans


# @lc code=end

# class Solution:
#     def longestCommonPrefix(self, words: List[str]) -> str:
#         if not words:
#             return ''

#         prefix = words[0]
#         for i in range(1, len(words)):
#             prefix = self.getPrefix(prefix, words[i])
#             if not prefix:
#                 break

#         return prefix

#     def getPrefix(self, prefix: str, word: str) -> str:
#         ml = min(len(prefix), len(word))
#         for i in range(ml):
#             if prefix[i] != word[i]:
#                 return prefix[:i]
#         return prefix[:ml]
