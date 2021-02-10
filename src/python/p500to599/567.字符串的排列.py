#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   567.字符串的排列.py
@Time    :   2021/02/10 18:19:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (40.64%)
# Likes:    281
# Dislikes: 0
# Total Accepted:    66.7K
# Total Submissions: 164.3K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#
#
# 示例2:
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
# 注意：
#
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
#
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        cnt, cur = [0] * 26, [0] * 26
        for i in range(m):
            cnt[ord(s1[i]) - ord('a')] += 1
            cur[ord(s2[i]) - ord('a')] += 1

        if cur == cnt:
            return True

        for i in range(m, n):
            cur[ord(s2[i]) - ord('a')] += 1
            cur[ord(s2[i - m]) - ord('a')] -= 1
            if cur == cnt:
                return True

        return False


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.checkInclusion(s1="ab", s2="eidbaooo"))
    print(solu.checkInclusion(s1="ab", s2="eidboaoo"))
