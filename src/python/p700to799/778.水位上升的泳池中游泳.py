#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   778.水位上升的泳池中游泳.py
@Time    :   2021/01/30 21:32:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#
# https://leetcode-cn.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (58.89%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 26.8K
# Testcase Example:  '[[0,2],[1,3]]'
#
# 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
#
# 现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t
# 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
#
# 你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？
#
#
#
# 示例 1:
#
#
# 输入: [[0,2],[1,3]]
# 输出: 3
# 解释:
# 时间为0时，你位于坐标方格的位置为 (0, 0)。
# 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
#
# 等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
#
#
# 示例2:
#
#
# 输入:
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# 输出: 16
# 解释:
# ⁠0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
#
# 最终的路线用加粗进行了标记。
# 我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
#
#
#
#
# 提示:
#
#
# 2 <= N <= 50.
# grid[i][j] 是 [0, ..., N*N - 1] 的排列。
#
#
#
from typing import List
"""
参考 1631. 最小体力消耗路径
"""


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        self.par[self.find(x)] = self.find(y)

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = {grid[i][j]: (i, j) for i in range(n) for j in range(n)}

        d = (0, 1, 0, -1, 0)
        uf = UnionFind(n * n)
        for t in range(n * n):
            x, y = pos[t]

            for i in range(4):
                u, v = x + d[i], y + d[i + 1]
                if u < 0 or u >= n or v < 0 or v >= n or grid[u][v] > t:
                    continue

                uf.union(x * n + y, u * n + v)
                if uf.connected(0, n * n - 1):
                    return t

        return -1


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    grid = [[0, 2], [1, 3]]
    print(solu.swimInWater(grid))

    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(solu.swimInWater(grid))
