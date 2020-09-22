#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   542.01-矩阵.py
@Time    :   2020/09/22 23:39:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (44.97%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    40.1K
# Total Submissions: 89.2K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
#
# 示例 1:
# 输入:
#
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
# 输出:
#
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
# 示例 2:
# 输入:
#
#
# 0 0 0
# 0 1 0
# 1 1 1
#
#
# 输出:
#
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
# 注意:
#
#
# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        d = (0, 1, 0, -1, 0)
        n, m = len(matrix), len(matrix[0])
        ans = [[0] * m for _ in range(n)]

        def bfs(x: int, y: int) -> int:
            dist = 0
            q = deque()
            q.append((x, y))
            while q:
                dist += 1
                size = len(q)
                for _ in range(size):
                    x, y = q.popleft()
                    for i in range(4):
                        nx, ny = x + d[i], y + d[i + 1]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if matrix[nx][ny] == 0:
                            return dist
                        q.append((nx, ny))
            return -1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    ans[i][j] += bfs(i, j)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
