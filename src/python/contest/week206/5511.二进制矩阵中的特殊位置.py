#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5511.二进制矩阵中的特殊位置.py
@Time    :   2020/09/13 10:30:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        def ok(x: int, y: int) -> bool:
            if sum(mat[x]) > 1:
                return False
            if sum(mat[i][y] for i in range(n)) > 1:
                return False
            return True

        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and ok(i, j):
                    ans += 1
        return ans
