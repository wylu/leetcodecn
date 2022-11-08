#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1684.统计一致字符串的数目.py
@Time    :   2022/11/08 21:31:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#
# https://leetcode.cn/problems/count-the-number-of-consistent-strings/description/
#
# algorithms
# Easy (82.12%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    51.5K
# Total Submissions: 60.1K
# Testcase Example:  '"ab"\n["ad","bd","aaab","baa","badab"]'
#
# 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是
# 一致字符串 。
#
# 请你返回 words 数组中 一致字符串 的数目。
#
#
#
# 示例 1：
#
#
# 输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# 输出：2
# 解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。
#
#
# 示例 2：
#
#
# 输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# 输出：7
# 解释：所有字符串都是一致的。
#
#
# 示例 3：
#
#
# 输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# 输出：4
# 解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。
#
#
#
#
# 提示：
#
#
# 1 <= words.length <= 10^4
# 1 <= allowed.length <= 26
# 1 <= words[i].length <= 10
# allowed 中的字符 互不相同 。
# words[i] 和 allowed 只包含小写英文字母。
#
#
#
from typing import List


# @lc code=start
class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        allowed = set(allowed)
        for word in words:
            for ch in word:
                if ch not in allowed:
                    cnt += 1
                    break
        return len(words) - cnt


# @lc code=end
