#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   30.串联所有单词的子串.py
@Time    :   2020/11/13 10:02:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (32.56%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    48.8K
# Total Submissions: 149.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
#
#
# 示例 1：
#
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#
#
# 示例 2：
#
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
#
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.
#
from collections import defaultdict
from typing import List
"""
We use an unordered_map<string, int> counts to record the expected
times of each word and another unordered_map<string, int> seen to
record the times we have seen. Then we check for every possible
position of i. Once we meet an unexpected word or the times of
some word is larger than its expected times, we stop the check.
If we finish the check successfully, push i to the result indexes.
"""


# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        cnts = defaultdict(int)
        for word in words:
            cnts[word] += 1

        def check(ss: str) -> bool:
            seen = defaultdict(int)
            for i in range(0, len(ss), wl):
                seen[ss[i:i + wl]] += 1
            return cnts == seen

        ans = []
        m, n, wl = len(s), len(words), len(words[0])
        for i in range(m - n * wl + 1):
            if check(s[i:i + n * wl]):
                ans.append(i)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(
        solu.findSubstring("wordgoodgoodgoodbestword",
                           ["word", "good", "best", "word"]))
