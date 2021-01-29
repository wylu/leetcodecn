#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1631.最小体力消耗路径.py
@Time    :   2021/01/29 23:28:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#
# https://leetcode-cn.com/problems/path-with-minimum-effort/description/
#
# algorithms
# Medium (48.57%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 33.9K
# Testcase Example:  '[[1,2,2],[3,8,2],[5,3,5]]'
#
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子
# (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0
# 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
#
# 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
#
# 请你返回从左上角走到右下角的最小 体力消耗值 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
# 输出：2
# 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
# 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
#
#
# 示例 2：
#
#
#
#
# 输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
# 输出：1
# 解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
#
#
# 示例 3：
#
#
# 输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# 输出：0
# 解释：上图所示路径不需要消耗任何体力。
#
#
#
#
# 提示：
#
#
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6
#
#
#
from typing import List
"""
本题实际上即为：

1.将每个格子抽象成图中的一个点；
2.将每两个相邻的格子之间连接一条边，长度为这两个格子本身权值的差的绝对值；
3.需要找到一条从左上角到右下角的「最短路径」，其中路径的长度定义为路径上
  所有边的权值的最大值。

这也是一道比较经典的题目了，常用的方法有如下几种：

「二分答案」：我们可以对最短路径的长度进行二分。当我们二分枚举到的长度为
x 时，我们只保留所有长度 <= x 的边。随后从左上角开始进行搜索（深度优先
搜索、广度优先搜索）均可，只需要判断是否能够到达右下角即可。如果能够到达
右下角，我们就可以减小 x 的值，反之增大 x 的值。

「并查集」：我们可以将所有边按照长度进行排序并依次添加进并查集，直到左上
角和右下角连通为止。

「最短路」：我们可以使用任一单源最短路径的算法（例如 Dijkstra 算法），
只需要在维护当前路径长度时，将其修改为题目中的定义即可。
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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        edges = []
        m, n = len(heights), len(heights[0])

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if i > 0:
                    edges.append(
                        (idx - n, idx, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append(
                        (idx - 1, idx, abs(heights[i][j] - heights[i][j - 1])))

        edges.sort(key=lambda x: x[2])

        uf = UnionFind(m * n)
        for x, y, v in edges:
            uf.union(x, y)
            if uf.connected(0, m * n - 1):
                return v

        return 0


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(solu.minimumEffortPath(heights))

    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(solu.minimumEffortPath(heights))

    heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1],
               [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print(solu.minimumEffortPath(heights))
