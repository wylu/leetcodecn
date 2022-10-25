#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   934.最短的桥.py
@Time    :   2022/10/25 19:43:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
# https://leetcode.cn/problems/shortest-bridge/description/
#
# algorithms
# Medium (48.04%)
# Likes:    363
# Dislikes: 0
# Total Accepted:    52.9K
# Total Submissions: 102.8K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。
#
# 岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。
#
#
#
# 你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。
#
# 返回必须翻转的 0 的最小数目。
#
#
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,1],[1,0]]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1
#
#
#
#
# 提示：
#
#
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] 为 0 或 1
# grid 中恰有两个岛
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = (0, 1, 0, -1, 0)
        seen = set()
        que = deque()

        def dfs(x: int, y: int) -> None:
            seen.add((x, y))
            for i in range(4):
                nx, ny = x + d[i], y + d[i + 1]
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                    if grid[nx][ny]:
                        dfs(nx, ny)
                    else:
                        seen.add((nx, ny))
                        que.append((nx, ny))

        for indice in range(n * n):
            i, j = divmod(indice, n)
            if grid[i][j] == 1:
                dfs(i, j)
                break

        ans = 0

        while que:
            ans += 1
            for _ in range(len(que)):
                x, y = que.popleft()
                for i in range(4):
                    nx, ny = x + d[i], y + d[i + 1]
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                        if grid[nx][ny]:
                            return ans
                        seen.add((nx, ny))
                        que.append((nx, ny))

        return ans


# @lc code=end
