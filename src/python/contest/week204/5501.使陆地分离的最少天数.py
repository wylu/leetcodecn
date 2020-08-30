#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5501.使陆地分离的最少天数.py
@Time    :   2020/08/30 10:25:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
先计算岛屿个数吗，分三种情况：
  1.如果岛屿个数大于 1 或者等于 0，则返回 0；
  2.否则枚举每块地，看删除后，岛的数目是否大于 1，如果大于 1，则返回 1；
  3.如果枚举删除每块陆地都不能使岛数目大于 1，则返回 2；

对于第三种情况，为什么返回 2，可以考虑切角（最优的方案），如下所示：
  0 1 1 0      0 1 0 0
  0 1 1 0  ->  0 0 1 0
  0 0 0 0      0 0 0 0

  1 1 1 1      1 0 1 1
  1 1 1 1  ->  0 1 1 1
  1 1 1 1      1 1 1 1
"""
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, visit: List[List[bool]]) -> None:
            if (x < 0 or x >= n or y < 0 or y >= m or visit[x][y]
                    or grid[x][y] != 1):
                return
            visit[x][y] = True
            for i in range(4):
                dfs(x + d[i], y + d[i + 1], visit)

        def count() -> int:
            res = 0
            visit = [[False] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if not visit[i][j] and grid[i][j] == 1:
                        res += 1
                        dfs(i, j, visit)
            return res

        d = (0, 1, 0, -1, 0)
        n, m = len(grid), len(grid[0])

        ans = count()
        if ans == 0 or ans > 1:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = count()
                    if ans > 1:
                        return 1
                    grid[i][j] = 1

        return 2


if __name__ == '__main__':
    solu = Solution()
    print(solu.minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
    print(solu.minDays([[1, 1]]))
    print(solu.minDays([[1, 0, 1, 0]]))
    print(
        solu.minDays([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1],
                      [1, 1, 0, 1, 1]]))
    print(solu.minDays([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
