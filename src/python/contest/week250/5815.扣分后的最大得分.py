#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5815.扣分后的最大得分.py
@Time    :   2021/07/18 10:41:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


# 超时
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        f = [[0] * n for _ in range(m)]

        for j in range(n):
            f[0][j] = points[0][j]

        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    f[i][j] = max(f[i][j],
                                  f[i - 1][k] + points[i][j] - abs(j - k))

        return max(f[m - 1])


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxPoints(points=[[1, 2, 3], [1, 5, 1], [3, 1, 1]]))
    print(solu.maxPoints(points=[[1, 5], [2, 3], [4, 2]]))
