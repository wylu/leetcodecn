#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6022.将数组和减半的最少操作次数.py
@Time    :   2022/03/19 22:51:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:

    def halveArray(self, nums: List[int]) -> int:
        pq = [-num for num in nums]
        heapq.heapify(pq)

        precision = 10**8
        ans, cur, half = 0, 0, sum(nums) / 2
        while int(cur * precision) < int(half * precision):
            num = -heapq.heappop(pq)
            num /= 2
            cur += num
            heapq.heappush(pq, -num)
            ans += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.halveArray(nums=[5, 19, 8, 1]))
    print(solu.halveArray(nums=[3, 8, 20]))
