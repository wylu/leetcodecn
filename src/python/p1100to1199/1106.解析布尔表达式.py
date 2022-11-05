#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1106.解析布尔表达式.py
@Time    :   2022/11/05 15:57:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#
# https://leetcode.cn/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (58.84%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 22.7K
# Testcase Example:  '"&(|(f))"'
#
# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
#
# 有效的表达式需遵循以下约定：
#
#
# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
# "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
# "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
#
#
#
#
# 示例 1：
#
# 输入：expression = "!(f)"
# 输出：true
#
#
# 示例 2：
#
# 输入：expression = "|(f,t)"
# 输出：true
#
#
# 示例 3：
#
# 输入：expression = "&(t,f)"
# 输出：false
#
#
# 示例 4：
#
# 输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= expression.length <= 20000
# expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
# expression 是以上述形式给出的有效表达式，表示一个布尔值。
#
#
#


# @lc code=start
class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        stk = []

        for c in expression:
            if c == ',':
                continue
            if c != ')':
                stk.append(c)
                continue

            t = f = 0
            while stk[-1] != '(':
                if stk.pop() == 't':
                    t += 1
                else:
                    f += 1

            stk.pop()
            op = stk.pop()
            if op == '!':
                stk.append('t' if f == 1 else 'f')
            elif op == '&':
                stk.append('t' if f == 0 else 'f')
            elif op == '|':
                stk.append('t' if t else 'f')

        return stk[-1] == 't'


# @lc code=end

# class Solution:

#     def parseBoolExpr(self, expression: str) -> bool:

#         def execute(i: int, j: int) -> bool:
#             if i == j:
#                 return expression[i] == 't'

#             if expression[i] == '!':
#                 return not execute(i + 2, j - 1)

#             s, e = i + 2, b2i[i + 1]
#             while s < e:
#                 if expression[s] in '!&|':
#                     result = execute(s, b2i[s + 1])
#                     if expression[i] == '&' and not result:
#                         return False
#                     if expression[i] == '|' and result:
#                         return True
#                     s = b2i[s + 1] + 2
#                 else:
#                     if expression[i] == '&' and expression[s] == 'f':
#                         return False
#                     if expression[i] == '|' and expression[s] == 't':
#                         return True
#                     s += 2

#             return expression[i] == '&'

#         b2i, stk = {}, []
#         for i, ch in enumerate(expression):
#             if ch == '(':
#                 stk.append(i)
#             elif ch == ')':
#                 b2i[stk.pop()] = i

#         return execute(0, len(expression) - 1)

# class Solution:

#     def parseBoolExpr(self, expression: str) -> bool:

#         def execute(i: int, j: int) -> bool:
#             if i == j:
#                 return expression[i] == 't'

#             if expression[i] == '!':
#                 return not execute(i + 2, j - 1)

#             elif expression[i] == '&':
#                 s, e = i + 2, b2i[i + 1]
#                 while s < e:
#                     if expression[s] in '!&|':
#                         if not execute(s, b2i[s + 1]):
#                             return False
#                         s = b2i[s + 1] + 2
#                     else:
#                         if expression[s] == 'f':
#                             return False
#                         s += 2
#                 return True

#             elif expression[i] == '|':
#                 s, e = i + 2, b2i[i + 1]
#                 while s < e:
#                     if expression[s] in '!&|':
#                         if execute(s, b2i[s + 1]):
#                             return True
#                         s = b2i[s + 1] + 2
#                     else:
#                         if expression[s] == 't':
#                             return True
#                         s += 2
#                 return False

#         b2i, stk = {}, []
#         for i, ch in enumerate(expression):
#             if ch == '(':
#                 stk.append(i)
#             elif ch == ')':
#                 b2i[stk.pop()] = i

#         return execute(0, len(expression) - 1)

if __name__ == '__main__':
    solu = Solution()
    print(solu.parseBoolExpr("!(f)"))
    print(solu.parseBoolExpr("|(f,t)"))
    print(solu.parseBoolExpr("&(t,f)"))
    print(solu.parseBoolExpr("|(&(t,f,t),!(t))"))
