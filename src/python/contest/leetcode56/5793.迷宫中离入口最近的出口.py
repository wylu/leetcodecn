#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5793.迷宫中离入口最近的出口.py
@Time    :   2021/07/10 22:35:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        seen = set()
        seen.add((entrance[0], entrance[1]))
        m, n = len(maze), len(maze[0])
        que = deque([(entrance[0], entrance[1])])
        d = (0, 1, 0, -1, 0)

        def check(x: int, y: int) -> bool:
            return ((((x == 0 or x == m - 1) and 0 <= y < n) or
                     ((y == 0 or y == n - 1) and 0 <= x < m))
                    and maze[x][y] != '+')

        ans = 0

        while que:
            ans += 1
            for _ in range(len(que)):
                x, y = que.popleft()
                for i in range(4):
                    nx = x + d[i]
                    ny = y + d[i + 1]
                    next = (nx, ny)
                    if (0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.'
                            and next not in seen):
                        if check(nx, ny):
                            return ans
                        que.append(next)
                        seen.add(next)

        return -1
