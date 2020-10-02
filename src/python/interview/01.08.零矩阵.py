#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   01.08.零矩阵.py
@Time    :   2020/10/02 11:31:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = cols[j] = True

        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
