#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   224.基本计算器.py
@Time    :   2021/03/10 22:43:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (41.29%)
# Likes:    474
# Dislikes: 0
# Total Accepted:    47K
# Total Submissions: 113.7K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
#
#
#
# 示例 1：
#
#
# 输入：s = "1 + 1"
# 输出：2
#
#
# 示例 2：
#
#
# 输入：s = " 2-1 + 2 "
# 输出：3
#
#
# 示例 3：
#
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 3 * 105
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
#
#
#
"""
方法一：括号展开 + 栈

由于字符串除了数字与括号外，只有加号和减号两种运算符。因此，如果展开
表达式中所有的括号，则得到的新表达式中，数字本身不会发生变化，只是
每个数字前面的符号会发生变化。

因此，我们考虑使用一个取值为 {−1,+1} 的整数 sign 代表「当前」的符号。
根据括号表达式的性质，它的取值：

  - 与字符串中当前位置的运算符有关；
  - 如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关：
    每当遇到一个以 - 号开头的括号，则意味着此后的符号都要被「翻转」。

考虑到第二点，我们需要维护一个栈 ops，其中栈顶元素记录了当前位置所处
的每个括号所「共同形成」的符号。例如，对于字符串 1+2+(3-(4+5))：

  - 扫描到 1+2 时，由于当前位置没有被任何括号所包含，则栈顶元素为
    初始值 +1；
  - 扫描到 1+2+(3 时，当前位置被一个括号所包含，该括号前面的符号为
    + 号，因此栈顶元素依然 +1；
  - 扫描到 1+2+(3-(4 时，当前位置被两个括号所包含，分别对应着 + 号
    和 - 号，由于 + 号和 - 号合并的结果为 - 号，因此栈顶元素变为 -1。

在得到栈 ops 之后，sign 的取值就能够确定了：如果当前遇到了 + 号，
则更新 sign <- ops.top()；如果遇到了遇到了 - 号，则更新
sign <- −ops.top()。

然后，每当遇到 ( 时，都要将当前的 sign 取值压入栈中；每当遇到 ) 时，
都从栈中弹出一个元素。这样，我们能够在扫描字符串的时候，即时地更新
ops 中的元素。
"""


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1

        ans = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and '0' <= s[i] <= '9':
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ans += sign * num

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.calculate("1 + 1"))
    print(solu.calculate(" 2-1 + 2 "))
    print(solu.calculate("(1+(4+5+2)-3)+(6+8)"))
