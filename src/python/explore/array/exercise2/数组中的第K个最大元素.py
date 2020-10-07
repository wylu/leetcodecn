#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   数组中的第K个最大元素.py
@Time    :   2020/10/07 22:59:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   O(nlogk)
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]


if __name__ == "__main__":
    solu = Solution()
    print(solu.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(solu.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
