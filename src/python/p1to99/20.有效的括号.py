#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   20.有效的括号.py
@Time    :   2020/08/07 22:58:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (42.07%)
# Likes:    1746
# Dislikes: 0
# Total Accepted:    349.1K
# Total Submissions: 829.2K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif not stack or stack.pop() != brackets[c]:
                return False

        return not stack


# @lc code=end
