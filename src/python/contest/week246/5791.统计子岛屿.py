#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5791.统计子岛屿.py
@Time    :   2021/06/20 10:59:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]],
                        grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        d = (0, 1, 0, -1, 0)
        seen = [[False] * n for _ in range(m)]

        def dfs(x, y):
            seen[x][y] = True
            res = grid1[x][y] == 1
            for i in range(4):
                nx, ny = x + d[i], y + d[i + 1]
                if (nx < 0 or nx >= m or ny < 0 or ny >= n or seen[nx][ny]
                        or grid2[nx][ny] == 0):
                    continue
                if not dfs(nx, ny):
                    res = False
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if (not seen[i][j] and grid1[i][j] == 1 and grid2[i][j] == 1
                        and dfs(i, j)):
                    ans += 1

        return ans


# class Solution:
#     def countSubIslands(self, grid1: List[List[int]],
#                         grid2: List[List[int]]) -> int:
#         m, n = len(grid1), len(grid1[0])
#         d = (0, 1, 0, -1, 0)
#         seen1 = [[False] * n for _ in range(m)]
#         seen2 = [[False] * n for _ in range(m)]

#         def dfs(grid, x, y, cur, seen):
#             seen[x][y] = True
#             cur.add((x, y))
#             for i in range(4):
#                 nx, ny = x + d[i], y + d[i + 1]
#                 if (nx < 0 or nx >= m or ny < 0 or ny >= n or seen[nx][ny]
#                         or grid[nx][ny] == 0):
#                     continue
#                 dfs(grid, nx, ny, cur, seen)

#         ans = 0
#         island1 = {}
#         for i in range(m):
#             for j in range(n):
#                 s1, s2 = set(), set()
#                 if not seen1[i][j] and grid1[i][j] == 1:
#                     dfs(grid1, i, j, s1, seen1)
#                 for pos in s1:
#                     island1[pos] = s1

#                 if not seen2[i][j] and grid2[i][j] == 1:
#                     dfs(grid2, i, j, s2, seen2)

#                 s1 = island1.get((i, j))
#                 if s1 and 0 < len(s2) <= len(s1) and s2.issubset(s1):
#                     ans += 1

#         return ans

if __name__ == '__main__':
    solu = Solution()
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0],
             [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    print(solu.countSubIslands(grid1, grid2))

    grid1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
    grid2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    print(solu.countSubIslands(grid1, grid2))

    grid1 = [[1, 1, 1, 1, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1],
             [1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0],
             [0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 0],
             [1, 1, 1, 1, 1, 0]]
    grid2 = [[1, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1],
             [0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1],
             [1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1],
             [1, 0, 0, 1, 0, 0]]
    print(solu.countSubIslands(grid1, grid2))  # 0

    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0],
             [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    print(solu.countSubIslands(grid1, grid2))  # 3
