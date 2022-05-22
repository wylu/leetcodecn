#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6076.表示一个折线图的最少线段数.py
@Time    :   2022/05/22 10:38:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

(x1, y1), (x2, y2), (x3, y3)

k1 = (y2 - y1) / (x2 - x1)
k2 = (y3 - y1) / (x3 - x1)

k1 = k2  ->  (y2 - y1) / (x2 - x1) = (y3 - y1) / (x3 - x1)
         ->  (y2 - y1) * (x3 - x1) = (y3 - y1) * (x2 - x1)
"""
from typing import List


class Solution:

    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n < 3:
            return n - 1

        stockPrices.sort()
        ans = 1
        p, q = stockPrices[0], stockPrices[1]
        for i in range(2, n):
            r = stockPrices[i]

            k1 = (q[1] - p[1]) * (r[0] - p[0])
            k2 = (r[1] - p[1]) * (q[0] - p[0])
            if k1 != k2:
                ans += 1

            p, q = q, r

        return ans


if __name__ == '__main__':
    solu = Solution()
    stockPrices = [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2],
                   [8, 1]]
    print(solu.minimumLines(stockPrices))

    stockPrices = [[3, 4], [1, 2], [7, 8], [2, 3]]
    print(solu.minimumLines(stockPrices))

    stockPrices = [[72, 98], [62, 27], [32, 7], [71, 4], [25, 19], [91, 30],
                   [52, 73], [10, 9], [99, 71], [47, 22], [19, 30], [80, 63],
                   [18, 15], [48, 17], [77, 16], [46, 27], [66, 87], [55, 84],
                   [65, 38], [30, 9], [50, 42], [100, 60], [75, 73], [98, 53],
                   [22, 80], [41, 61], [37, 47], [95, 8], [51, 81], [78, 79],
                   [57, 95]]
    print(solu.minimumLines(stockPrices))  # 29
