#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   696.计数二进制子串.py
@Time    :   2020/08/10 12:36:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#
# https://leetcode-cn.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (53.64%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 38.3K
# Testcase Example:  '"00110"'
#
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
#
# 重复出现的子串要计算它们出现的次数。
#
# 示例 1 :
#
#
# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
#
# 请注意，一些重复出现的子串要计算它们出现的次数。
#
# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
#
#
# 示例 2 :
#
#
# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
#
#
# 注意：
#
#
# s.length 在1到50,000之间。
# s 只包含“0”或“1”字符。
#
#
#


# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def count(i: int, j: int) -> int:
            cnt = 1
            while i > 0 and j < n - 1:
                i -= 1
                j += 1
                if s[i] == s[i + 1] and s[j - 1] == s[j]:
                    cnt += 1
                else:
                    break
            return cnt

        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans += count(i - 1, i)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.countBinarySubstrings('000111000'))
