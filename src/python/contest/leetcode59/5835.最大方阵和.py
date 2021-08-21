#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5835.最大方阵和.py
@Time    :   2021/08/21 22:43:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        negative = [0] * n
        ans, minimum = 0, 100010
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negative[i] += 1
                    matrix[i][j] *= -1

                ans += matrix[i][j]
                minimum = min(minimum, matrix[i][j])

        cnt = 0
        for neg in negative:
            if neg % 2:
                cnt += 1

        if cnt % 2:
            ans -= minimum * 2

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxMatrixSum(matrix=[[1, -1], [-1, 1]]))
    print(solu.maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
