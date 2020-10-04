#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5518.给定行和列的和求可行矩阵.py
@Time    :   2020/10/03 22:54:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int],
                      colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= ans[i][j]
                colSum[j] -= ans[i][j]
        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.restoreMatrix([3, 8], [4, 7]))
