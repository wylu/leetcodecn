#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5269.从栈中取出K个硬币的最大面值和.py
@Time    :   2022/03/27 11:09:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        pss = []
        for pile in piles:
            cur = [0] * (len(pile) + 1)
            for i, p in enumerate(pile):
                cur[i + 1] = cur[i] + p
            pss.append(cur)

        # f[n][k]: 前 n 个栈中操作了 k 次后可以得到最大面值和

        n = len(piles)
        f = [[0] * (k + 1) for _ in range(n)]

        for i, ps in enumerate(pss[0]):
            if i > k:
                break
            f[0][i] = ps

        for i in range(1, n):
            for j in range(1, k + 1):
                for z in range(min(j + 1, len(pss[i]))):
                    f[i][j] = max(f[i][j], f[i - 1][j - z] + pss[i][z])

        return f[n - 1][k]


if __name__ == '__main__':
    solu = Solution()
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 2
    print(solu.maxValueOfCoins(piles, k))

    piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
    k = 7
    print(solu.maxValueOfCoins(piles, k))

    piles = [[37, 88], [51, 64, 65, 20, 95, 30, 26], [9, 62, 20], [44]]
    k = 9
    print(solu.maxValueOfCoins(piles, k))  # 494
