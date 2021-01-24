#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5663.找出第K大的异或坐标值.py
@Time    :   2021/01/24 11:19:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = [matrix[0][0]]

        xor = [[0] * n for _ in range(m)]
        xor[0][0] = matrix[0][0]
        for i in range(1, m):
            xor[i][0] = xor[i - 1][0] ^ matrix[i][0]
            ans.append(xor[i][0])
        for j in range(1, n):
            xor[0][j] = xor[0][j - 1] ^ matrix[0][j]
            ans.append(xor[0][j])

        for i in range(1, m):
            tmp = [matrix[i][0]]
            for j in range(1, n):
                tmp.append(tmp[j - 1] ^ matrix[i][j])
                xor[i][j] = xor[i - 1][j] ^ tmp[j]
                ans.append(xor[i][j])

        ans.sort()
        return ans[-k]


if __name__ == "__main__":
    solu = Solution()
    print(solu.kthLargestValue(matrix=[[5, 2], [1, 6]], k=4))
