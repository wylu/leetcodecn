#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   091.粉刷房子.py
@Time    :   2022/06/25 10:32:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        f = costs[0]
        for i in range(1, n):
            r, g, b = f
            f[0] = min(g, b) + costs[i][0]
            f[1] = min(r, b) + costs[i][1]
            f[2] = min(r, g) + costs[i][2]
        return min(f)


if __name__ == '__main__':
    solu = Solution()
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    print(solu.minCost(costs))

    costs = [[7, 6, 2]]
    print(solu.minCost(costs))
