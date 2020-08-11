#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   130.被围绕的区域.py
@Time    :   2020/08/11 21:55:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (40.55%)
# Likes:    330
# Dislikes: 0
# Total Accepted:    61.8K
# Total Submissions: 147.8K
# Testcase Example:
# '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
# 任何不在边界上，或不与边界上的 'O' 相连的 'O'，
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#
from typing import List
"""
给定的矩阵中有三种元素：
  - 字母 X；
  - 被字母 X 包围的字母 O；
  - 没有被字母 X 包围的字母 O。
本题要求将所有被字母 X 包围的字母 O都变为字母 X ，但很难判断哪些 O 是被包围的，
哪些 O 不是被包围的。

注意到题目解释中提到：任何边界上的 O 都不会被填充为 X。 我们可以想到，所有的
不被包围的 O 都直接或间接与边界上的 O 相连。我们可以利用这个性质判断 O 是否
在边界上，具体地说：

对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；
最后我们遍历这个矩阵，对于每一个字母：
如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X。
"""


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return

        n, m = len(board), len(board[0])
        d = (0, 1, 0, -1, 0)

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != 'O':
                return
            board[x][y] = '#'
            for i in range(4):
                dfs(x + d[i], y + d[i + 1])

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(1, m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


# @lc code=end
