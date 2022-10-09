#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   856.括号的分数.py
@Time    :   2022/10/09 20:02:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#
# https://leetcode.cn/problems/score-of-parentheses/description/
#
# algorithms
# Medium (63.35%)
# Likes:    416
# Dislikes: 0
# Total Accepted:    41.6K
# Total Submissions: 61.6K
# Testcase Example:  '"()"'
#
# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
#
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。
#
#
#
#
# 示例 1：
#
# 输入： "()"
# 输出： 1
#
#
# 示例 2：
#
# 输入： "(())"
# 输出： 2
#
#
# 示例 3：
#
# 输入： "()()"
# 输出： 2
#
#
# 示例 4：
#
# 输入： "(()(()))"
# 输出： 6
#
#
#
#
# 提示：
#
#
# S 是平衡括号字符串，且只含有 ( 和 ) 。
# 2 <= S.length <= 50
#
#
#


# @lc code=start
class Solution:

    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        for ch in s:
            if ch == '(':
                stk.append(0)
            else:
                num = stk.pop()
                stk[-1] += max(1, num * 2)
        return stk[-1]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.scoreOfParentheses("()"))
    print(solu.scoreOfParentheses("(())"))
    print(solu.scoreOfParentheses("()()"))
    print(solu.scoreOfParentheses("(()(()))"))
