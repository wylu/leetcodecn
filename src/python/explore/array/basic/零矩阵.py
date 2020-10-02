#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   零矩阵.py
@Time    :   2020/10/02 10:53:12
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


# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m, n = len(matrix), len(matrix[0])
#         rowFlag, colFlag = False, False

#         for i in range(m):
#             if matrix[i][0] == 0:
#                 colFlag = True

#         for j in range(n):
#             if matrix[0][j] == 0:
#                 rowFlag = True

#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = matrix[0][j] = 0

#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0

#         if colFlag:
#             for i in range(m):
#                 matrix[i][0] = 0

#         if rowFlag:
#             for j in range(n):
#                 matrix[0][j] = 0
