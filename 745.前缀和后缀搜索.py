#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   745.前缀和后缀搜索.py
@Time    :   2022/07/14 20:24:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#
# https://leetcode.cn/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (42.80%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 39.8K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]],["a","e"]]'
#
# 设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。
#
# 实现 WordFilter 类：
#
#
# WordFilter(string[] words) 使用词典中的单词 words 初始化对象。
# f(string pref, string suff) 返回词典中具有前缀 prefix 和后缀 suff
# 的单词的下标。如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。
#
#
#
#
# 示例：
#
#
# 输入
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# 输出
# [null, 0]
# 解释
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e"
# 。
#
#
#
# 提示：
#
#
# 1 <= words.length <= 10^4
# 1 <= words[i].length <= 7
# 1 <= pref.length, suff.length <= 7
# words[i]、pref 和 suff 仅由小写英文字母组成
# 最多对函数 f 执行 10^4 次调用
#
#
#
from typing import List


# @lc code=start
class WordFilter:
    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefix_size in range(1, m + 1):
                for suffix_size in range(1, m + 1):
                    key = word[:prefix_size] + '#' + word[-suffix_size:]
                    self.d[key] = i

    def f(self, pref: str, suff: str) -> int:
        return self.d.get(pref + '#' + suff, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end
