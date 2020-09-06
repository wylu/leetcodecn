#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5491.矩阵对角线元素的和.py
@Time    :   2020/09/05 22:30:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans, n = 0, len(mat)
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n - i - 1]

        if n % 2 == 1:
            mid = n // 2
            ans -= mat[mid][mid]

        return ans
