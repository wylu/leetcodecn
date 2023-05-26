#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1091.二进制矩阵中的最短路径.py
@Time    :   2023/05/26 22:54:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2023, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
# https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (38.73%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    74K
# Total Submissions: 184.4K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
#
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n -
# 1)）的路径，该路径同时满足下述要求：
#
#
# 路径途经的所有单元格的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
#
#
# 畅通路径的长度 是该路径途经的单元格总数。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,1],[1,0]]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
# 输出：4
#
#
# 示例 3：
#
#
# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
#
#
#
#
# 提示：
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] 为 0 或 1
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ans, n = 0, len(grid)
        queue, seen = deque([(0, 0)]), set()
        while queue:
            ans += 1

            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == y == n - 1:
                    return ans

                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        flag = nx * n + ny
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue

                        if not grid[nx][ny] and flag not in seen:
                            queue.append((nx, ny))
                            seen.add(flag)

        return -1


# @lc code=end
