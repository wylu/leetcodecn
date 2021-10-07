#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   434.字符串中的单词数.py
@Time    :   2021/10/07 11:20:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (38.91%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    47.3K
# Total Submissions: 121.8K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:
#
# 输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
#
#
#


# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                ans += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.countSegments("Hello, my name is John"))
    print(solu.countSegments("  Hello  World "))

# class Solution:
#     def countSegments(self, s: str) -> int:
#         return len(s.split())
