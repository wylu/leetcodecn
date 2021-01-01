#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1704.判断字符串的两半是否相似.py
@Time    :   2021/01/01 22:04:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#
# https://leetcode-cn.com/problems/determine-if-string-halves-are-alike/description/
#
# algorithms
# Easy (81.05%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 5.4K
# Testcase Example:  '"book"'
#
# 给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。
#
# 两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s
# 可能同时含有大写和小写字母。
#
# 如果 a 和 b 相似，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：s = "book"
# 输出：true
# 解释：a = "bo" 且 b = "ok" 。a 中有 1 个元音，b 也有 1 个元音。所以，a 和 b 相似。
#
#
# 示例 2：
#
# 输入：s = "textbook"
# 输出：false
# 解释：a = "text" 且 b = "book" 。a 中有 1 个元音，b 中有 2 个元音。因此，a 和 b 不相似。
# 注意，元音 o 在 b 中出现两次，记为 2 个。
#
#
# 示例 3：
#
# 输入：s = "MerryChristmas"
# 输出：false
#
#
# 示例 4：
#
# 输入：s = "AbCdEfGh"
# 输出：true
#
#
#
#
# 提示：
#
#
# 2 <= s.length <= 1000
# s.length 是偶数
# s 由 大写和小写 字母组成
#
#
#


# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s) - 1
        left, right = 0, 0
        while i < j:
            if s[i] in vowel:
                left += 1
            if s[j] in vowel:
                right += 1
            i, j = i + 1, j - 1
        return left == right


# @lc code=end

# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         def count(s: str) -> int:
#             cnt = 0
#             for ch in s:
#                 if ch in vowel:
#                     cnt += 1
#             return cnt

#         vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
#         mid = len(s) // 2
#         return count(s[:mid]) == count(s[mid:])

if __name__ == "__main__":
    solu = Solution()
    print(solu.halvesAreAlike("book"))
    print(solu.halvesAreAlike("textbook"))
    print(solu.halvesAreAlike("MerryChristmas"))
    print(solu.halvesAreAlike("AbCdEfGh"))
