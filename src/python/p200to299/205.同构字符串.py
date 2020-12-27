#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   205.同构字符串.py
@Time    :   2020/12/27 12:15:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (48.41%)
# Likes:    293
# Dislikes: 0
# Total Accepted:    68.9K
# Total Submissions: 141.6K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
#
# 输入: s = "egg", t = "add"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "foo", t = "bar"
# 输出: false
#
# 示例 3:
#
# 输入: s = "paper", t = "title"
# 输出: true
#
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
#
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for i in range(len(s)):
            if ((s[i] in s2t and s2t[s[i]] != t[i])
                    or (t[i] in t2s and t2s[t[i]] != s[i])):
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]

        return True


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.isIsomorphic("egg", "add"))
    print(solu.isIsomorphic("foo", "bar"))
    print(solu.isIsomorphic("paper", "title"))
    print(solu.isIsomorphic("ab", "aa"))
