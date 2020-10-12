#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   242.有效的字母异位词.py
@Time    :   2020/10/12 14:14:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (61.66%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    144.5K
# Total Submissions: 234.3K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnts = [0] * 26
        for ch in s:
            cnts[ord(ch) - ord('a')] += 1
        for ch in t:
            cnts[ord(ch) - ord('a')] -= 1
        for c in cnts:
            if c != 0:
                return False
        return True


# @lc code=end
