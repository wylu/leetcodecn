#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   389.找不同.py
@Time    :   2020/12/18 17:35:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (68.72%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    67.5K
# Total Submissions: 98.2K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。
#
#
#
# 示例 1：
#
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
#
#
# 示例 2：
#
# 输入：s = "", t = "y"
# 输出："y"
#
#
# 示例 3：
#
# 输入：s = "a", t = "aa"
# 输出："a"
#
#
# 示例 4：
#
# 输入：s = "ae", t = "aea"
# 输出："a"
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s 和 t 只包含小写字母
#
#
#


# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for ch in s:
            ans ^= ord(ch)
        for ch in t:
            ans ^= ord(ch)
        return chr(ans)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findTheDifference("abcd", "abcde"))
    print(solu.findTheDifference("", "y"))
    print(solu.findTheDifference("a", "aa"))
    print(solu.findTheDifference("ae", "aea"))
