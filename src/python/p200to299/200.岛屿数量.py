#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   200.岛屿数量.py
@Time    :   2020/08/19 21:18:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.07%)
# Likes:    717
# Dislikes: 0
# Total Accepted:    144.5K
# Total Submissions: 288.5K
# Testcase Example:
# '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1:
#
# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != '1':
                return
            grid[x][y] = '0'
            for i in range(4):
                dfs(x + d[i], y + d[i + 1])

        n, m = len(grid), len(grid[0])
        d = (0, 1, 0, -1, 0)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1

        return ans


# @lc code=end
