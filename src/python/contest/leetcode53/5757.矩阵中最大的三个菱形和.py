#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5757.矩阵中最大的三个菱形和.py
@Time    :   2021/05/29 22:43:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        hill = [[0] * (n + 1) for _ in range(m + 1)]
        dale = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(n - 1, -1, -1):
                hill[i][j] = grid[i - 1][j] + hill[i - 1][j + 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dale[i][j] = grid[i - 1][j - 1] + dale[i - 1][j - 1]

        pq = []
        for i in range(m):
            for j in range(n):
                sz = 0
                while (i - sz >= 0 and i + sz < m and j - sz >= 0
                       and j + sz < n):
                    if sz == 0:
                        tot = grid[i][j]
                    else:
                        tot = hill[i + 1][j - sz] - hill[i - sz][j + 1]
                        tot += hill[i + sz + 1][j] - hill[i][j + sz + 1]
                        tot += dale[i + 1][j + sz + 1] - dale[i - sz][j]
                        tot += dale[i + sz + 1][j + 1] - dale[i][j - sz]
                        tot -= (grid[i - sz][j] + grid[i + sz][j] +
                                grid[i][j - sz] + grid[i][j + sz])
                    heapq.heappush(pq, (tot, sz))
                    sz += 1

        ans = [tot for tot, _ in set(pq)]
        ans.sort(reverse=True)
        return ans[:3]


if __name__ == '__main__':
    solu = Solution()
    grid = [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10],
            [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]
    print(solu.getBiggestThree(grid))

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solu.getBiggestThree(grid))

    grid = [[7, 7, 7]]
    print(solu.getBiggestThree(grid))
