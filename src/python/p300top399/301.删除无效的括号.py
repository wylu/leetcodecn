#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   301.删除无效的括号.py
@Time    :   2021/10/28 09:39:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (53.81%)
# Likes:    571
# Dislikes: 0
# Total Accepted:    40.9K
# Total Submissions: 76K
# Testcase Example:  '"()())()"'
#
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
#
# 返回所有可能的结果。答案可以按 任意顺序 返回。
#
#
#
# 示例 1：
#
#
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
#
#
# 示例 2：
#
#
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
#
#
# 示例 3：
#
#
# 输入：s = ")("
# 输出：[""]
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 25
# s 由小写英文字母以及括号 '(' 和 ')' 组成
# s 中至多含 20 个括号
#
#
#
from typing import List


# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s: str, start: int, lcnt: int, rcnt: int, lrem: int,
                   rrem: int) -> None:
            if lrem == 0 and rrem == 0:
                if isValid(s):
                    ans.append(s)
                return

            for i in range(start, len(s)):
                if i != start and s[i] == s[i - 1]:
                    if s[i] == '(':
                        lcnt += 1
                    elif s[i] == ')':
                        rcnt += 1
                    continue

                if lrem + rrem > len(s) - i:
                    return

                # 删除左括号
                if lrem and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lcnt, rcnt, lrem - 1, rrem)
                # 删除右括号
                if rrem and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lcnt, rcnt, lrem, rrem - 1)

                if s[i] == '(':
                    lcnt += 1
                elif s[i] == ')':
                    rcnt += 1
                if rcnt > lcnt:
                    return

        ans = []
        lrem = rrem = 0
        for ch in s:
            if ch == '(':
                lrem += 1
            elif ch == ')':
                if lrem == 0:
                    rrem += 1
                else:
                    lrem -= 1

        helper(s, 0, 0, 0, lrem, rrem)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.removeInvalidParentheses("()())()"))
    print(solu.removeInvalidParentheses("(a)())()"))
    print(solu.removeInvalidParentheses(")("))
