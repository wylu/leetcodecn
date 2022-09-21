#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   854.相似度为-k-的字符串.py
@Time    :   2022/09/21 23:07:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#
# https://leetcode.cn/problems/k-similar-strings/description/
#
# algorithms
# Hard (37.37%)
# Likes:    253
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 45K
# Testcase Example:  '"ab"\n"ba"'
#
# 对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。
#
# 给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。
#
#
#
# 示例 1：
#
#
# 输入：s1 = "ab", s2 = "ba"
# 输出：1
#
#
# 示例 2：
#
#
# 输入：s1 = "abc", s2 = "bca"
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 和 s2  只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母
# s2 是 s1 的一个字母异位词
#
#
#


# @lc code=start
class Solution:

    def kSimilarity(self, s1: str, s2: str) -> int:
        step, n = 0, len(s1)
        q, seen = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] and s2[i] != s2[j]:
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in seen:
                            seen.add(t)
                            q.append((t, i + 1))
            step += 1


# @lc code=end
