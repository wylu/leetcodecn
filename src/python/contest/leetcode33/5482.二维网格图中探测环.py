#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5482.二维网格图中探测环.py
@Time    :   2020/08/23 08:41:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
思路：用dfs检测环。
环的判断条件：
dfs搜索过程会形成一棵树T（隐式的有向图）。
当搜索过程中，访问到非父节点的祖先节点时，认为有环。

(x,y): 本次要访问的节点
(px,py): (x,y)的父节点
grid: 网格图
visit[i][j]: 顶点去重

dfs(x, y, px, py){
    visit[x][y] = 1;
    for((nx, ny) in (x, y)的有效相邻顶点){
        if((nx, ny) == (px, py))  // 父节点，跳过；
        if(grid(nx, ny) == grid(x, y)){  // 相同字符
            if(visit(nx, ny)){  //访问到祖先节点，有环
                返回true;
            }
            rt = dfs(nx, ny, x, y);
            if(rt) 有环，返回true;
        }
    }
    无环，返回false;
}
"""
import sys
from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x: int, y: int, px: int, py: int) -> bool:
            visit[x][y] = True
            for i in range(4):
                nx, ny = x + d[i], y + d[i + 1]
                if nx == px and ny == py:
                    continue

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[x][y]:
                    if visit[nx][ny]:
                        return True

                    if dfs(nx, ny, x, y):
                        return True
            return False

        sys.setrecursionlimit(999999999)
        d = (0, 1, 0, -1, 0)
        n, m = len(grid), len(grid[0])
        visit = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if not visit[i][j] and dfs(i, j, -1, -1):
                    return True

        return False
