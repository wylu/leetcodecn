#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   329.矩阵中的最长递增路径.py
@Time    :   2020/07/26 19:43:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (41.30%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 56.4K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
#
# 示例 1:
#
# 输入: nums =
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
# 输出: 4
# 解释: 最长递增路径为 [1, 2, 6, 9]。
#
# 示例 2:
#
# 输入: nums =
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
# 输出: 4
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#
#
#

from typing import List
"""
记忆化深度优先搜索

将矩阵看成一个有向图，每个单元格对应图中的一个节点，如果相邻的两个单元格的值
不相等，则在相邻的两个单元格之间存在一条从较小值指向较大值的有向边。问题转化
成在有向图中寻找最长路径。

深度优先搜索是非常直观的方法。从一个单元格开始进行深度优先搜索，即可找到从该
单元格开始的最长递增路径。对每个单元格分别进行深度优先搜索之后，即可得到矩阵
中的最长递增路径的长度。

但是如果使用朴素深度优先搜索，时间复杂度是指数级，会超出时间限制，因此必须加
以优化。

朴素深度优先搜索的时间复杂度过高的原因是进行了大量的重复计算，同一个单元格会
被访问多次，每次访问都要重新计算。由于同一个单元格对应的最长递增路径的长度是
固定不变的，因此可以使用记忆化的方法进行优化。用矩阵 memo 作为缓存矩阵，已经
计算过的单元格的结果存储到缓存矩阵中。

使用记忆化深度优先搜索，当访问到一个单元格 (i,j) 时，如果 memo[i][j] != 0，
说明该单元格的结果已经计算过，则直接从缓存中读取结果，如果 memo[i][j] = 0，
说明该单元格的结果尚未被计算过，则进行搜索，并将计算得到的结果存入缓存中。

遍历完矩阵中的所有单元格之后，即可得到矩阵中的最长递增路径的长度。
"""


# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(matrix, i, j, memo))

        return ans

    def dfs(self, matrix: List[List[int]], x: int, y: int,
            memo: List[List[int]]) -> int:
        if memo[x][y] != 0:
            return memo[x][y]

        memo[x][y] = 1

        d = (0, 1, 0, -1, 0)
        for i in range(4):
            nx, ny = x + d[i], y + d[i + 1]
            if (nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0])
                    or matrix[nx][ny] <= matrix[x][y]):
                continue

            memo[x][y] = max(memo[x][y], 1 + self.dfs(matrix, nx, ny, memo))

        return memo[x][y]


# @lc code=end
