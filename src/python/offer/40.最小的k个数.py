#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   40.最小的k个数.py
@Time    :   2020/09/03 23:23:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
# import heapq

from typing import List


# 快速选择
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k <= 0:
            return []

        def partition(left: int, right: int) -> int:
            j = left - 1
            for i in range(left, right):
                if arr[i] < arr[right]:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]

            j += 1
            arr[j], arr[right] = arr[right], arr[j]
            return j

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = partition(left, right)
            if mid == k - 1:
                return arr[:k]
            elif mid < k - 1:
                left = mid + 1
            else:
                right = mid - 1

        return []


# 大顶堆
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         if not arr or k <= 0:
#             return []

#         pq = [-e for e in arr[:k]]
#         heapq.heapify(pq)
#         for i in range(k, len(arr)):
#             heapq.heappush(pq, -arr[i])
#             heapq.heappop(pq)

#         return [-e for e in pq]

if __name__ == '__main__':
    solu = Solution()
    print(solu.getLeastNumbers([3, 2, 1], 2))
    print(solu.getLeastNumbers([0, 1, 2, 1], 1))
