#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   22.括号生成.py
@Time    :   2020/08/28 23:07:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.10%)
# Likes:    1269
# Dislikes: 0
# Total Accepted:    170.3K
# Total Submissions: 223.7K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例：
#
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
#
#
#
from typing import List


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(cur: int, lc: int) -> None:
            if cur == 2 * n:
                ans.append(''.join(stack))
                return

            if lc < n:
                stack.append('(')
                dfs(cur + 1, lc + 1)
                stack.pop()

            if lc > cur - lc:
                stack.append(')')
                dfs(cur + 1, lc)
                stack.pop()

        if n <= 0:
            return ''

        ans, stack = [], []
        dfs(0, 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.generateParenthesis(3))
