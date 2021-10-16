#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   282.给表达式添加运算符.py
@Time    :   2021/10/16 19:03:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] 给表达式添加运算符
#
# https://leetcode-cn.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (45.86%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    14.2K
# Total Submissions: 30.9K
# Testcase Example:  '"123"\n6'
#
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 *
# ，返回所有能够得到目标值的表达式。
#
#
#
# 示例 1:
#
#
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]
#
#
# 示例 2:
#
#
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
#
# 示例 3:
#
#
# 输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"]
#
# 示例 4:
#
#
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
#
#
# 示例 5:
#
#
# 输入: num = "3456237490", target = 9191
# 输出: []
#
#
#
# 提示：
#
#
# 1 <= num.length <= 10
# num 仅含数字
# -2^31 <= target <= 2^31 - 1
#
#
#
from typing import List
"""
方法一：回溯
设字符串 num 的长度为 n，为构建表达式，我们可以往 num 中间的 n-1 个空隙添加
+ 号、- 号或 * 号，或者不添加符号。

我们可以用「回溯法」来模拟这个过程。从左向右构建表达式，并实时计算表达式的结果。
由于乘法运算优先级高于加法和减法运算，我们还需要保存最后一个连乘串（如 2*3*4）
的运算结果。

定义递归函数 backtrack(expr, i, res, mul)，其中：

- expr 为当前构建出的表达式；
- i 表示当前的枚举到了 num 的第 i 个数字；
- res 为当前表达式的计算结果；
- mul 为表达式最后一个连乘串的计算结果。

该递归函数分为两种情况：

如果 i=n，说明表达式已经构造完成，若此时有 res=target，则找到了一个可行解，
我们将 expr 放入答案数组中，递归结束；

如果 i<n，需要枚举当前表达式末尾要添加的符号（+ 号、- 号或 * 号），以及该
符号之后需要截取多少位数字。设该符号之后的数字为 val，按符号分类讨论：

- 若添加 + 号，则 res 增加 val，且 val 单独组成表达式最后一个连乘串；
- 若添加 - 号，则 res 减少 val，且 -val 单独组成表达式最后一个连乘串；
- 若添加 * 号，由于乘法运算优先级高于加法和减法运算，我们需要对 res
  撤销之前 mul 的计算结果，并添加新的连乘结果 mul*val，也就是将 res
  减少 mul 并增加 mul*val。

代码实现时，为避免字符串拼接所带来的额外时间开销，我们采用字符数组的形式来
构建表达式。此外，运算过程中可能会产生超过 32 位整数的结果，我们要用 64
位整数存储中间运算结果。
"""


# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def dfs(expr: List[str], i: int, res: int, mul: int) -> None:
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return

            signIndex = len(expr)
            if i > 0:
                expr.append('')  # 占位，下面填充符号

            val = 0
            for j in range(i, n):  # 枚举截取的数字长度（取多少位）
                if j > i and num[i] == '0':  # 数字可以是单个 0 但不能有前导零
                    break

                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:
                    # 表达式开头不能添加符号
                    dfs(expr, j + 1, val, val)
                else:
                    # 枚举符号
                    expr[signIndex] = '+'
                    dfs(expr, j + 1, res + val, val)
                    expr[signIndex] = '-'
                    dfs(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*'
                    dfs(expr, j + 1, res - mul + mul * val, mul * val)

            del expr[signIndex:]

        dfs([], 0, 0, 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.addOperators(num="123", target=6))
    print(solu.addOperators(num="232", target=8))
    print(solu.addOperators(num="105", target=5))
    print(solu.addOperators(num="00", target=0))
    print(solu.addOperators(num="3456237490", target=9191))
