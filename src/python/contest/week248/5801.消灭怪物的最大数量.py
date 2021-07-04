#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5801.消灭怪物的最大数量.py
@Time    :   2021/07/04 10:32:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        pq = []
        for i in range(n):
            heapq.heappush(pq, math.ceil(dist[i] / speed[i]))

        for i in range(n):
            cur = heapq.heappop(pq)
            if cur <= i:
                return i

        return n


if __name__ == '__main__':
    solu = Solution()
    print(solu.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]))
    print(solu.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]))
    print(solu.eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]))
