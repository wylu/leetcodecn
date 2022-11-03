#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1668.最大重复子字符串.py
@Time    :   2022/11/03 12:40:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#
# https://leetcode.cn/problems/maximum-repeating-substring/description/
#
# algorithms
# Easy (44.39%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    23.7K
# Total Submissions: 50.3K
# Testcase Example:  '"ababc"\n"ab"'
#
# 给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的
# 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence
# 的子串，那么重复值 k 为 0 。
#
# 给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。
#
#
#
# 示例 1：
#
#
# 输入：sequence = "ababc", word = "ab"
# 输出：2
# 解释："abab" 是 "ababc" 的子字符串。
#
#
# 示例 2：
#
#
# 输入：sequence = "ababc", word = "ba"
# 输出：1
# 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
#
#
# 示例 3：
#
#
# 输入：sequence = "ababc", word = "ac"
# 输出：0
# 解释："ac" 不是 "ababc" 的子字符串。
#
#
#
#
# 提示：
#
#
# 1 <= sequence.length <= 100
# 1 <= word.length <= 100
# sequence 和 word 都只包含小写英文字母。
#
#
#


# @lc code=start
class Solution:

    def maxRepeating(self, sequence: str, word: str) -> int:
        ans, i, m, n = 0, 0, len(sequence), len(word)

        while i <= m - n:
            cur, j = 0, i
            while j + n <= m and sequence[j:j + n] == word:
                cur += 1
                j += n
            ans = max(ans, cur)
            i = i + 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    print(solu.maxRepeating(sequence, word))
