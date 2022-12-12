#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1781.所有子字符串美丽值之和.py
@Time    :   2022/12/12 23:01:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1781 lang=python3
#
# [1781] 所有子字符串美丽值之和
#
# https://leetcode.cn/problems/sum-of-beauty-of-all-substrings/description/
#
# algorithms
# Medium (54.30%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    20.4K
# Total Submissions: 30.9K
# Testcase Example:  '"aabcb"'
#
# 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
#
#
# 比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
#
#
# 给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。
#
#
#
# 示例 1：
#
#
# 输入：s = "aabcb"
# 输出：5
# 解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。
#
# 示例 2：
#
#
# 输入：s = "aabcbaa"
# 输出：17
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 500
# s 只包含小写英文字母。
#
#
#
from collections import defaultdict


# @lc code=start
class Solution:

    def beautySum(self, s: str) -> int:
        ans, n = 0, len(s)
        for i in range(n):
            cnt = defaultdict(int)
            max_freq = -0x80000000
            for j in range(i, n):
                cnt[s[j]] += 1
                max_freq = max(max_freq, cnt[s[j]])
                ans += max_freq - min(cnt.values())
        return ans


# @lc code=end
