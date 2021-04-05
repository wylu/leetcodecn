#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   221.最大正方形.py
@Time    :   2021/04/05 11:07:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (45.03%)
# Likes:    729
# Dislikes: 0
# Total Accepted:    99.3K
# Total Submissions: 220.5K
# Testcase Example:
# '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
#
#
# 示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'
#
#
#
from typing import List
"""
方法一：动态规划
我们用 dp(i,j) 表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值。
如果我们能计算出所有 dp(i,j) 的值，那么其中的最大值即为矩阵中只包含 1
的正方形的边长最大值，其平方即为最大正方形的面积。

那么如何计算 dp 中的每个元素值呢？对于每个位置 (i,j)，检查在矩阵中该位置
的值：

如果该位置的值是 0，则 dp(i,j) = 0，因为当前位置不可能在由 1 组成的正方形中；
如果该位置的值是 1，则 dp(i,j) 的值由其上方、左方和左上方的三个相邻位置的
dp 值决定。具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 1，
状态转移方程如下：

    dp(i,j) = min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1)) + 1

如果读者对这个状态转移方程感到不解，可以参考 1277. 统计全为 1 的正方形子矩阵
的官方题解，其中给出了详细的证明。

此外，还需要考虑边界条件。如果 i 和 j 中至少有一个为 0，则以位置 (i,j)
为右下角的最大正方形的边长只能是 1，因此 dp(i,j) = 1。

以下用一个例子具体说明。原始矩阵如下

0 1 1 1 0
1 1 1 1 0
0 1 1 1 1
0 1 1 1 1
0 0 1 1 1

对应的 dp 值如下

0 1 1 1 0
1 1 2 2 0
0 1 2 3 1
0 1 2 3 2
0 0 1 2 3
"""


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])

        return ans * ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(solu.maximalSquare(matrix))

    matrix = [["0", "1"], ["1", "0"]]
    print(solu.maximalSquare(matrix))

    matrix = [["0"]]
    print(solu.maximalSquare(matrix))
