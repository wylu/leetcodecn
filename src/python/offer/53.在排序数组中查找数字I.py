#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   53.在排序数组中查找数字I.py
@Time    :   2021/07/16 10:51:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
# import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def my_search(x: int) -> int:
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left

        left = my_search(target)
        if left == n:
            return 0

        right = my_search(target + 1)
        return right - left


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         left = bisect.bisect_left(nums, target)
#         if left == n:
#             return 0

#         right = bisect.bisect_left(nums, target + 1)
#         return right - left

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         cnt = 0
#         for num in nums:
#             if num == target:
#                 cnt += 1
#         return cnt

if __name__ == '__main__':
    solu = Solution()
    print(solu.search(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(solu.search(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(solu.search(nums=[1, 2], target=2))
