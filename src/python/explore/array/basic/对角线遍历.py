#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   对角线遍历.py
@Time    :   2020/10/02 11:39:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        ans = []
        r, c = -1, 1
        i, j = 0, 0

        while i != m - 1 or j != n - 1:
            if 0 <= i < m and 0 <= j < n:
                ans.append(matrix[i][j])
                i, j = i + r, j + c
            else:
                r, c = c, r
                if j >= n:  # 超出右边界
                    i, j = i + 2, n - 1
                elif i < 0:  # 超出上边界
                    i = 0
                elif i >= m:  # 超出下边界
                    i, j = m - 1, j + 2
                elif j < 0:  # 超出左边界
                    j = 0

        ans.append(matrix[i][j])
        return ans


if __name__ == "__main__":
    solu = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solu.findDiagonalOrder(matrix))

    matrix = [[1, 2, 3]]
    print(solu.findDiagonalOrder(matrix))
