#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5776.判断矩阵经轮转后是否一致.py
@Time    :   2021/06/06 10:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]],
                     target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate():
            nonlocal mat
            tmp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    tmp[j][n - i - 1] = mat[i][j]
            mat = tmp

        for i in range(4):
            if mat == target:
                return True
            rotate()

        return False
