#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5622.平均等待时间.py
@Time    :   2020/12/26 22:44:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        tot, cur = 0, customers[0][0]
        for arrival, cost in customers:
            cur = max(cur, arrival)
            tot += cur - arrival + cost
            cur += cost
        return tot / len(customers)


if __name__ == "__main__":
    solu = Solution()
    print(solu.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
    print(solu.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
    customers = [[2, 3], [6, 3], [7, 5], [11, 3], [15, 2], [18, 1]]
    print(solu.averageWaitingTime(customers))
