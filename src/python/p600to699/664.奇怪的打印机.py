#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   664.奇怪的打印机.py
@Time    :   2021/05/24 22:18:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#
# https://leetcode-cn.com/problems/strange-printer/description/
#
# algorithms
# Hard (63.89%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 26.7K
# Testcase Example:  '"aaabbb"'
#
# 有台奇怪的打印机有以下两个特殊要求：
#
#
# 打印机每次只能打印由 同一个字符 组成的序列。
# 每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
#
#
# 给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。
#
#
# 示例 1：
#
#
# 输入：s = "aaabbb"
# 输出：2
# 解释：首先打印 "aaa" 然后打印 "bbb"。
#
#
# 示例 2：
#
#
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 100
# s 由小写英文字母组成
#
#
#
"""
方法一：动态规划
思路及算法

我们可以使用动态规划解决本题，令 f[i][j] 表示打印完成区间 [i,j] 的最少操作数。

当我们尝试计算出 f[i][j] 时，需要考虑两种情况：

1. s[i] = s[j]，即区间两端的字符相同，那么当我们打印左侧字符 s[i] 时，可以
顺便打印右侧字符 s[j]，这样我们即可忽略右侧字符对该区间的影响，只需要考虑如何
尽快打印完区间 [i,j-1] 即可，即此时有 f[i][j] = f[i][j-1]。我们无需关心区间
[i,j-1] 的具体打印方案，因为我们总可以第一步完成 s[i] 的打印，此时可以顺便
完成s[j] 的打印，不会影响打印完成区间 [i,j-1] 的最少操作数。
2. s[i] != s[j]，即区间两端的字符不同，那么我们需要分别完成该区间的左右两部分
的打印。我们记两部分分别为区间 [i,k] 和区间 [k+1,j]（其中 i <= k < j），此时
f[i][j] = min{f[i][k] + f[k+1][j]},  k = [i,j)。

总结状态转移方程为：

    f[i][j] = f[i][j-1],  s[i] = s[j]
    f[i][j] = min{f[i][k] + f[k+1][j]},  k = [i,j)

边界条件为 f[i][i] = 1，对于长度为 1 的区间，需要打印 1 次。最后的答案为
f[0][n-1]。

注意到 f[i][j] 的计算需要用到 f[i][k] 和 f[k+1][j]（其中 i <= k < j）。
为了保证动态规划的计算过程满足无后效性，在实际代码中，我们需要改变动态规划的
计算顺序，从大到小地枚举 i，并从小到大地枚举 j，这样可以保证当计算 f[i][j]时，
f[i][k] 和 f[k+1][j] 都已经被计算过。
"""


# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        f = [[0x7FFFFFFF] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i][j - 1]
                    continue

                for k in range(i, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j])

        return f[0][n - 1]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.strangePrinter(s="aaabbb"))
    print(solu.strangePrinter(s="aba"))
