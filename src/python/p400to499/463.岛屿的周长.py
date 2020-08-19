#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   463.岛屿的周长.py
@Time    :   2020/08/19 19:44:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# https://leetcode-cn.com/problems/island-perimeter/description/
#
# algorithms
# Easy (67.84%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 32K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
#
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
#
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
#
#
#
# 示例 :
#
# 输入:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
#
# 输出: 16
#
# 解释: 它的周长是下面图片中的 16 个黄色的边：
#
#
#
#
#
from typing import List
"""
1.当前的点只与左边和上边的点有关系，在计算周长时，遇到一个陆地，周长为4；
2.如果该陆地左边也为陆地则 -2，同样地，如果上边也为陆地也 -2；
"""


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        ans -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        ans -= 2

        return ans


# @lc code=end

# class Solution:
#     """
#     当当前遍历的格子与边缘相连，出现一个周长的一边，+1
#     当当前遍历的格子与水相连，出现一个周长的一边，+1
#     当当前遍历的格子是1的时候，也就是陆地，此陆地会将当前遍历的陆地包围，不需要做什么
#     当当前遍历的格子是2的时候，也就是走过的陆地，也就是1，直接返回0，因为被计算过了
#     """
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         if not grid or not grid[0]:
#             return 0

#         def dfs(x: int, y: int) -> int:
#             if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
#                 return 1
#             if grid[x][y] == 2:
#                 return 0

#             grid[x][y] = 2
#             cnt = 0
#             for i in range(4):
#                 cnt += dfs(x + d[i], y + d[i + 1])

#             return cnt

#         d = (0, 1, 0, -1, 0)
#         n, m = len(grid), len(grid[0])
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     return dfs(i, j)

#         return 0
