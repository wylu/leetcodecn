#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   921.使括号有效的最少添加.py
@Time    :   2022/10/04 19:23:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#
# https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (74.59%)
# Likes:    211
# Dislikes: 0
# Total Accepted:    53.1K
# Total Submissions: 72.6K
# Testcase Example:  '"())"'
#
# 只有满足下面几点之一，括号字符串才是有效的：
#
#
# 它是一个空字符串，或者
# 它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
# 它可以被写作 (A)，其中 A 是有效字符串。
#
#
# 给定一个括号字符串 s ，移动N次，你就可以在字符串的任何位置插入一个括号。
#
#
# 例如，如果 s = "()))" ，你可以插入一个开始括号为 "(()))" 或结束括号为 "())))" 。
#
#
# 返回 为使结果字符串 s 有效而必须添加的最少括号数。
#
#
#
# 示例 1：
#
#
# 输入：s = "())"
# 输出：1
#
#
# 示例 2：
#
#
# 输入：s = "((("
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 只包含 '(' 和 ')' 字符。
#
#
#


# @lc code=start
class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        ans, left = 0, 0
        for ch in s:
            if ch == '(':
                left += 1
            elif left > 0:
                left -= 1
            else:
                ans += 1
        return ans + left


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minAddToMakeValid("())"))
    print(solu.minAddToMakeValid("((("))
