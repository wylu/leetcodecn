#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   01矩阵.py
@Time    :   2020/09/22 23:26:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


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
                    ans[i][j] = bfs(i, j)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
