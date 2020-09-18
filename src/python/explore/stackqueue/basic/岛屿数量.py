#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   岛屿数量.py
@Time    :   2020/09/18 13:19:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        d = (0, 1, 0, -1, 0)
        ans, n, m = 0, len(grid), len(grid[0])

        def ok(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'

        def bfs(x: int, y: int) -> None:
            q = deque()
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + d[i], y + d[i + 1]
                    if ok(nx, ny):
                        grid[nx][ny] = '0'
                        q.append((nx, ny))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    bfs(i, j)
                    ans += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
    print(solu.numIslands(grid))
