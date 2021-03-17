#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   115.不同的子序列.py
@Time    :   2021/03/17 21:06:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#
# https://leetcode-cn.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (53.35%)
# Likes:    447
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 75.6K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
#
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE"
# 的一个子序列，而 "AEC" 不是）
#
# 题目数据保证答案符合 32 位带符号整数范围。
#
#
#
# 示例 1：
#
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# 示例 2：
#
#
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
#
#
#
# 提示：
#
#
# 0 <= s.length, t.length <= 1000
# s 和 t 由英文字母组成
#
#
#
"""
动态规划

dp[i][j] 代表 T 前 i 个字符可以由 S 前 j 个字符组成的最多个数.

所以动态方程:

    当 S[j] == T[i] , dp[i][j] = dp[i-1][j-1] + dp[i][j-1];
    当 S[j] != T[i] , dp[i][j] = dp[i][j-1]

举个例子,如示例的

    +-------+-------+-------+-------+-------+-------+-------+-------+-------+
    | T \ S |  ""   |   b   |   a   |   b   |   g   |   b   |   a   |   g   |  # noqa W605
    +-------+-------+-------+-------+-------+-------+-------+-------+-------+
    |  ""   |   1   |   1   |   1   |   1   |   1   |   1   |   1   |   1   |
    +-------+-------+-------+-------+-------+-------+-------+-------+-------+
    |   b   |   0   |   1   |   1   |   2   |   2   |   3   |   3   |   3   |
    +-------+-------+-------+-------+-------+-------+-------+-------+-------+
    |   a   |   0   |   0   |   1   |   1   |   1   |   1   |   2   |   2   |
    +-------+-------+-------+-------+-------+-------+-------+-------+-------+
    |   g   |   0   |   0   |   0   |   0   |   1   |   1   |   1   |   2   |
    +-------+-------+-------+-------+-------+-------+-------+-------+-------+

对于第一行, T 为空,因为空集是所有字符串子集, 所以我们第一行都是 1；
对于第一列, S 为空,这样组成 T 个数当然为 0 了。
"""


# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t) + 1, len(s) + 1
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[m - 1][n - 1]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.numDistinct(s="rabbbit", t="rabbit"))
    print(solu.numDistinct(s="babgbag", t="bag"))
