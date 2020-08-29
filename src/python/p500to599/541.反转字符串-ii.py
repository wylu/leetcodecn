#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   541.反转字符串-ii.py
@Time    :   2020/08/30 00:06:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
# https://leetcode-cn.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (54.96%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 36.5K
# Testcase Example:  '"abcdefg"\n2'
#
# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
#
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#
#
#
#
# 示例:
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#
#
#
#
# 提示：
#
#
# 该字符串只包含小写英文字母。
# 给定字符串的长度和 k 在 [1, 10000] 范围内。
#
#
#


# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)


# @lc code=end

# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         def reverse(i: int, j: int) -> None:
#             while i < j:
#                 s[i], s[j] = s[j], s[i]
#                 i += 1
#                 j -= 1

#         s = list(s)
#         n, i = len(s), 0
#         while i < n:
#             j = min(n - 1, i + k - 1)
#             reverse(i, j)
#             i += 2 * k

#         return ''.join(s)

if __name__ == '__main__':
    solu = Solution()
    print(solu.reverseStr('abcdefg', 2))
    print(solu.reverseStr('abcdef', 2))
    print(solu.reverseStr('abcdeghi', 3))
