#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   784.字母大小写全排列.py
@Time    :   2022/10/30 20:54:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode.cn/problems/letter-case-permutation/description/
#
# algorithms
# Medium (70.33%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    90.7K
# Total Submissions: 125.9K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
#
# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
#
#
#
# 示例 1：
#
#
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#
#
# 示例 2:
#
#
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]
#
#
#
#
# 提示:
#
#
# 1 <= s.length <= 12
# s 由小写英文字母、大写英文字母和数字组成
#
#
#
from typing import List


# @lc code=start
class Solution:

    def letterCasePermutation(self, s: str) -> List[str]:
        ans, stk, n = [], [], len(s)

        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(stk))
                return

            stk.append(s[i])
            dfs(i + 1)
            stk.pop()

            if 'a' <= s[i] <= 'z':
                stk.append(s[i].upper())
                dfs(i + 1)
                stk.pop()

            if 'A' <= s[i] <= 'Z':
                stk.append(s[i].lower())
                dfs(i + 1)
                stk.pop()

        dfs(0)
        return ans


# @lc code=end
