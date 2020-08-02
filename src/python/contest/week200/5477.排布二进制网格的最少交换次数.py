#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5477.排布二进制网格的最少交换次数.py
@Time    :   2020/08/02 11:06:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        a = [0 for _ in range(n)]
        for i in range(n):
            j = n - 1
            while j > 0:
                if grid[i][j] == 1:
                    break
                j -= 1
            a[i] = j

        ans = 0
        for i in range(n):
            j = i
            while j < n:
                if a[j] <= i:
                    break
                j += 1

            if j == n:
                return -1

            while j > i:
                a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1
                ans += 1

        return ans
