#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   695.岛屿的最大面积.py
@Time    :   2020/08/19 21:09:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (63.87%)
# Likes:    337
# Dislikes: 0
# Total Accepted:    57.9K
# Total Submissions: 90.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
#
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
#
#
#
# 示例 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
#
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
#
# 示例 2:
#
# [[0,0,0,0,0,0,0,0]]
#
# 对于上面这个给定的矩阵, 返回 0。
#
#
#
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
#
#
from typing import List


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                return 0
            area = 1
            grid[x][y] = 0
            for i in range(4):
                area += dfs(x + d[i], y + d[i + 1])
            return area

        n, m = len(grid), len(grid[0])
        d = (0, 1, 0, -1, 0)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))

        return ans


# @lc code=end
