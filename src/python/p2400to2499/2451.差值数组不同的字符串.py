#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2451.差值数组不同的字符串.py
@Time    :   2023/05/25 23:48:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2023, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=2451 lang=python3
#
# [2451] 差值数组不同的字符串
#
# https://leetcode.cn/problems/odd-string-difference/description/
#
# algorithms
# Easy (60.21%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    19.1K
# Total Submissions: 28.8K
# Testcase Example:  '["adc","wzy","abc"]'
#
# 给你一个字符串数组 words ，每一个字符串长度都相同，令所有字符串的长度都为 n 。
#
# 每个字符串 words[i] 可以被转化为一个长度为 n - 1 的 差值整数数组 difference[i] ，其中对于 0 <= j <= n - 2
# 有 difference[i][j] = words[i][j+1] - words[i][j] 。注意两个字母的差值定义为它们在字母表中 位置
# 之差，也就是说 'a' 的位置是 0 ，'b' 的位置是 1 ，'z' 的位置是 25 。
#
#
# 比方说，字符串 "acb" 的差值整数数组是 [2 - 0, 1 - 2] = [2, -1] 。
#
#
# words 中所有字符串 除了一个字符串以外 ，其他字符串的差值整数数组都相同。你需要找到那个不同的字符串。
#
# 请你返回 words中 差值整数数组 不同的字符串。
#
#
#
# 示例 1：
#
#
# 输入：words = ["adc","wzy","abc"]
# 输出："abc"
# 解释：
# - "adc" 的差值整数数组是 [3 - 0, 2 - 3] = [3, -1] 。
# - "wzy" 的差值整数数组是 [25 - 22, 24 - 25]= [3, -1] 。
# - "abc" 的差值整数数组是 [1 - 0, 2 - 1] = [1, 1] 。
# 不同的数组是 [1, 1]，所以返回对应的字符串，"abc"。
#
#
# 示例 2：
#
#
# 输入：words = ["aaa","bob","ccc","ddd"]
# 输出："bob"
# 解释：除了 "bob" 的差值整数数组是 [13, -13] 以外，其他字符串的差值整数数组都是 [0, 0] 。
#
#
#
#
# 提示：
#
#
# 3 <= words.length <= 100
# n == words[i].length
# 2 <= n <= 20
# words[i] 只含有小写英文字母。
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:

    def oddString(self, words: List[str]) -> str:
        cnt = defaultdict(list)
        for word in words:
            key = tuple(
                ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1))
            cnt[key].append(word)

        for value in cnt.values():
            if len(value) == 1:
                return value[0]

        return ''


# @lc code=end
