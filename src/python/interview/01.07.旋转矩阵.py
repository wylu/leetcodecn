#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   01.07.旋转矩阵.py
@Time    :   2020/10/01 23:49:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 转置
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 反转
        for i in range(n):
            lt, rt = 0, n - 1
            while lt < rt:
                matrix[i][lt], matrix[i][rt] = matrix[i][rt], matrix[i][lt]
                lt += 1
                rt -= 1


if __name__ == "__main__":
    solu = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solu.rotate(matrix)
    print(matrix)
