#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5839.移除石子使总数最小.py
@Time    :   2021/08/08 10:36:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-pile for pile in piles]
        heapq.heapify(pq)

        while k:
            if pq[0] == 1:
                break

            pile = -(heapq.heappop(pq))
            pile = pile - (pile // 2)
            heapq.heappush(pq, -pile)
            k -= 1

        return -sum(pq)


if __name__ == '__main__':
    solu = Solution()
    print(solu.minStoneSum(piles=[5, 4, 9], k=2))
    print(solu.minStoneSum(piles=[4, 3, 6, 7], k=3))
    print(solu.minStoneSum(piles=[1], k=10000))
