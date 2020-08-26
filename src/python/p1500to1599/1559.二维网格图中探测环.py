#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1559.二维网格图中探测环.py
@Time    :   2020/08/26 23:35:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1559 lang=python3
#
# [1559] 二维网格图中探测环
#
# https://leetcode-cn.com/problems/detect-cycles-in-2d-grid/description/
#
# algorithms
# Hard (32.37%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 5.6K
# Testcase Example:
# '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
#
# 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。
#
# 一个环是一条开始和结束于同一个格子的长度 大于等于 4
# 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。
#
# 同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到
# (1, 1) 回到了上一次移动时的格子。
#
# 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# 输出：true
# 解释：如下图所示，有 2 个用不同颜色标出来的环：
#
#
#
# 示例 2：
#
#
#
# 输入：grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# 输出：true
# 解释：如下图所示，只有高亮所示的一个合法环：
#
#
#
# 示例 3：
#
#
#
# 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# 输出：false
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid 只包含小写英文字母。
#
#
#
import sys
from typing import List
"""
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


# @lc code=start
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


# @lc code=end
