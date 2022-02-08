#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1001.网格照明.py
@Time    :   2022/02/08 18:48:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1001 lang=python3
#
# [1001] 网格照明
#
# https://leetcode-cn.com/problems/grid-illumination/description/
#
# algorithms
# Hard (42.87%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    11.2K
# Total Submissions: 26.2K
# Testcase Example:  '5\n[[0,0],[4,4]]\n[[1,1],[1,0]]'
#
# 在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。
#
# 给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli]
# 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。
#
# 当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。
#
# 另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj]
# 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8
# 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。
#
# 返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。
#
#
#
# 示例 1：
#
#
# 输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
# 输出：[1,0]
# 解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1]
# 是否被照亮（蓝色方框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。
#
# 第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。
#
#
#
# 示例 2：
#
#
# 输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
# 输出：[1,1]
#
#
# 示例 3：
#
#
# 输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
# 输出：[1,1,0]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^9
# 0 <= lamps.length <= 20000
# 0 <= queries.length <= 20000
# lamps[i].length == 2
# 0 <= rowi, coli < n
# queries[j].length == 2
# 0 <= rowj, colj < n
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:

    def gridIllumination(self, n: int, lamps: List[List[int]],
                         queries: List[List[int]]) -> List[int]:
        lights = set()
        rows, cols = defaultdict(int), defaultdict(int)
        dales, hills = defaultdict(int), defaultdict(int)

        for x, y in lamps:
            if (x * n + y) not in lights:
                lights.add(x * n + y)
                rows[x] += 1
                cols[y] += 1
                dales[x - y] += 1
                hills[x + y] += 1

        ans = []
        for x, y in queries:
            lighten = bool(rows[x] or cols[y] or dales[x - y] or hills[x + y])
            ans.append(int(lighten))

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < n and 0 <= j < n and (i * n + j) in lights:
                        lights.discard(i * n + j)
                        rows[i] -= 1
                        cols[j] -= 1
                        dales[i - j] -= 1
                        hills[i + j] -= 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    n = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 1], [1, 0]]
    print(solu.gridIllumination(n, lamps, queries))

    n = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 1], [1, 1]]
    print(solu.gridIllumination(n, lamps, queries))

    n = 5
    lamps = [[0, 0], [0, 4]]
    queries = [[0, 4], [0, 1], [1, 4]]
    print(solu.gridIllumination(n, lamps, queries))

    n = 5
    lamps = [[0, 0], [4, 4]]
    queries = [[1, 1], [0, 0], [2, 2]]
    print(solu.gridIllumination(n, lamps, queries))

    n = 6
    lamps = [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]]
    queries = [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]
    print(solu.gridIllumination(n, lamps, queries))
