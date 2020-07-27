#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   792.匹配子序列的单词数.py
@Time    :   2020/07/27 21:33:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#
# https://leetcode-cn.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (41.97%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 11.3K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# 给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。
#
#
# 示例:
# 输入:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# 输出: 3
# 解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
#
#
# 注意:
#
#
# 所有在words和 S 里的单词都只由小写字母组成。
# S 的长度在 [1, 50000]。
# words 的长度在 [1, 5000]。
# words[i]的长度在[1, 50]。
#
#
#

from typing import List
"""
思路:

因为 S 很长，所以寻找一种只需遍历一次 S 的方法，避免暴力解法的多次遍历。

将所有单词根据首字母不同放入不同的桶中。例如当 words = ['dog', 'cat', 'cop']，
根据首字母不同可以分为 'c' : ('cat', 'cop'), 'd' : ('dog',)。换句话说，每个桶中
的单词就是该单词正在等待匹配的下一个字母。在遍历 S 的同时，将匹配到单词根据下一个
需要匹配的字母移动到不同的桶中。

例如，有字符串 S = 'dcaog'：

初始化 heads = 'c' : ('cat', 'cop'), 'd' : ('dog',)；
遍历 S[0] = 'd' 后，heads = 'c' : ('cat', 'cop'), 'o' : ('og',)；
遍历 S[1] = 'c' 后，heads = 'a' : ('at',), 'o' : ('og', 'op')；
遍历 S[2] = 'a' 后，heads = 'o' : ('og', 'op'), 't': ('t',) ;
遍历 S[3] = 'o' 后，heads = 'g' : ('g',), 'p': ('p',), 't': ('t',)；
遍历 S[0] = 'g' 后，heads = 'p': ('p',), 't': ('t',)。

算法:

使用长度为 26 的数组 heads 做桶，每个字母对应一个桶。访问 S 中的每个字母时，
将该字母对应桶中的所有单词，根据下一个等待匹配字母放入到不同的桶中。如果已经
匹配到单词的最后一个字母，那么子序列单词数加 1。
"""


# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        if not s or not words:
            return 0

        heads = [[] for _ in range(26)]
        for word in words:
            idx = ord(word[0]) - ord('a')
            heads[idx].append(word)

        ans = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            old_bucket = heads[idx]
            heads[idx] = []

            while old_bucket:
                wd = old_bucket.pop()
                if wd == ch:
                    ans += 1
                else:
                    heads[ord(wd[1]) - ord('a')].append(wd[1:])

        return ans


# @lc code=end
